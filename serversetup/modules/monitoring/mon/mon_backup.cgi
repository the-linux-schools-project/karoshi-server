#!/usr/bin/perl -T
#!/usr/bin/perl -Tw broke when I made changes to list_dtlog that involved
# submitting three commas ",,," in a row into the value of $args :(
#
# NAME
#  mon.cgi
#
#
# DESCRIPTION
#  Web interface for the Mon resource monitoring system. mon.cgi
#  implements a significant subset of the Perl interface to Mon, which
#  allows administrators to quickly view the status of their network
#  and perform many common Mon tasks with a simple web client.
#
# Requires mon 0.38-21 and Mon::Client 0.11 for proper operation.
#
#
# AUTHORS
#  Originally by:
#   Arthur K. Chan <artchan@althem.com>
#  Based on the Mon program by Jim Trocki <trockij@transmeta.com>. 
#   http://www.kernel.org/software/mon/
#  Rewritten to support Mon::Client, mod_perl, taint mode,
#  authentication, the strict pragma, and other visual/functional 
#  enhancements by Andrew Ryan <andrewr@nam-shub.com>.
#  Downtime logging contributed by Martha H Greenberg <marthag@mit.edu>
#  Site-specific customization routines contributed by Ed Ravin <eravin@panix.com>
#
# ----------------------------------------------------------------------
# $Id: mon.cgi,v 1.52 2001/05/22 21:27:23 andrewr Exp $
# ----------------------------------------------------------------------
#
#
# INSTRUCTIONS
# Install this cgi script to wherever your cgi-bin directory sits
# on your mon server. If you don't have a web server installed, try
# http://www.apache.org. This script hasn't been tested with any
# web server, although there is no reason it wouldn't work under
# any other web server as a CGI script.
#
# This script now runs cleanly under mod_perl (tested under apache 1.3.9,
# mod_perl 1.21), if you're running that. Global variables have not
# been eliminated but at least we're being careful now.
#
# This script also runs cleanly under taint mode, which is activated
# by using the -T switch for CGI scripts, and by using the directive
# "PerlTaintCheck On" in your httpd.conf file if you are running
# under mod_perl.
#
# Modify the "Configurable Parameters" section below to customize it
# to your site's settings. mon.cgi also supports an optional config
# file which allows you to set all the same parameters. Please
# see the file README.site-customization for more details.
#
# If you want to easily customize the look and feel of mon.cgi, 
# as well as various other configuration options, copy the sample 
# mon.cgi.cf file (in the /config directory of this distribution) 
# into a location where your webserver can read it, and edit the 
# line beginning '$moncgi_config_file = ""' to reflect the path 
# to your config file. You can then change the look and feel of 
# mon.cgi, as well as implement access controls, directly from this 
# file.
#
# If you want to do a lot of the things that this script lets you do,
# and you don't want any authorization to be necessary, then
# you need to open up your auth.cf file to allow anyone to perform
# actions that you would like mon.cgi to perform. 
#
# No authentication might work in an environment where there are very
# few Mon users and they can all be trusted equally, or if you want
# to use mon.cgi in a sort of "read-only" capacity, where all users
# can list, for example, but no web users can enable/disable 
# monitoring and/or control the server in any way.
#
# Alternatively, if you want to use authentication, you need to have
# a working authentication setup with Mon from the command line
# before attempting to make authentication work with mon.cgi.
#
# Authentication is very flexible, and is trivial to implement in 
# mon.cgi, assuming you already have authentication working from 
# the command line. Just un-comment out the "$must_login line, change
# $app_secret to be something unique (VERY IMPORTANT!) and 
# mon will start requiring authentication for ALL commands.
#
# Authentication users should change their app secret on a regular
# basis if security is a concern. Actually, if security is a concern,
# don't run mon.cgi, because unless you use SSL, AND your monhost is
# on the same server as your web server, AND you use a short timeout
# on cookies, AND you change your app secret often and keep it
# VERY secure, you don't have a secure web system. But this simple 
# authentication mechanism is enough to keep most people happy.
#
#
# This script will require the CGI perl module. Available at any
# perl CPAN site. See http://www.perl.org for details. Oh, and don't
# forget Mon::Client, but the assumption is you are already running
# mon in some fashion and so you know this already.
#
# In addition, if you want to use the authentication piece of mon.cgi,
# you need to install the Crypt::TripleDES module, also available
# (tested w/ Crypt::TripleDES v0.24), and your browser needs to allow
# cookies (or else you need to be prepared to type in your username
# and password an awful lot!).
#
#
# BUGS
#  Probably many.
#  Send bugs/comments about this software to 
#  Andrew Ryan <andrewr@nam-shub.com>
#  Please include any output from your web server's error log that the
#  script might have output, this will help immensely in solving problems.
#  Also please include the versions of mon.cgi, Mon and Mon::Client you 
#  are using.
#


BEGIN {
    # Auto-detect if we are running under mod_perl or CGI.
    $USE_MOD_PERL = exists $ENV{'MOD_PERL'}
    ? 1 : 0;
    if ($USE_MOD_PERL) {
	# Use the cgi module and compile all methods at 
	# the beginning but only once
	use CGI qw (-compile :standard) ;				       
    } else {
	# Use the cgi module and compile all methods only 
	# when they are invoked via the autoloader.
	#use CGI qw (-debug) ; #DEBUG
	use CGI qw (:standard) ;
    }
    $CGI::POST_MAX=1024 * 100;  # max 100K posts
    $CGI::DISABLE_UPLOADS = 1;  # no uploads
}


# Configurable Parameters ----------------------------------------------
# Basic global vars
use Mon::Client;			       # mon client interface
use strict;			               # because strict is GOOD
use vars qw($RCSID $RCSVERSION $VERSION $AUTHOR $organization $monadmin 
	    $logo $logo_link $reload_time  $monhost $monport $url 
	    $login_expire_time $cookie_name $cookie_path %cgiparams
	    $monhost_and_port_args $monhost_and_port_args_meta
	    $has_read_config $moncgi_config_file $cf_file_mtime
	    $untaint_ack_msgs @show_watch $show_watch_strict
	    $required_mon_client_version);
# Formatting-related global vars
use vars qw($BGCOLOR $TEXTCOLOR $LINKCOLOR $VLINKCOLOR 
	    $greenlight_color $redlight_color $unchecked_color 
	    $yellowlight_color $disabled_color 
	    $fixed_font_face $sans_serif_font_face 
	    $dtlog_max_failures_per_page);
# Security-related global vars
use vars qw($must_login $app_secret %loginhash $des $has_prompted_for_auth $destroy_auth_cookie $default_username $default_password);
$has_prompted_for_auth = "";        #this must always be cleared for mod_perl
undef $destroy_auth_cookie;        #this must always be undef'd for mod_perl
undef %cgiparams;        # this must always be undef'd for mod_perl
undef $monhost_and_port_args;      # This is defined if the user overrided monhost or monport
undef $monhost_and_port_args_meta;      # This is defined if the user overrided monhost or monport
undef @show_watch;
undef $show_watch_strict;

$RCSID = '$Id: mon.cgi,v 1.52 2001/05/22 21:27:23 andrewr Exp $';
$RCSVERSION = '$Revision: 1.52 $';
$VERSION = $RCSVERSION;
$VERSION =~ s/\Revision: //i; $VERSION =~ s/\$//g ; $VERSION =~ s/\s+//g;
$AUTHOR = 'andrewr@nam-shub.com';
$required_mon_client_version = "0.11";  #Version of Mon::Client which we require for successful operation

#
# If you want to use a config file to specify mon.cgi parameters, put
# the full path to the file in this variable. 
#
# If you do not wish to use a config file, leave this variable empty.
#
$moncgi_config_file = "";


#
# This subroutine initializes the configuration variables which
# can be set here, but also overridden with the optional mon.cgi 
# config file.
#
# We put this subroutine at the top of the code so that users
# can get to it more easily.
#
sub initialize_config_globals ;
sub initialize_config_globals {
    undef $has_read_config ;   #undef this for mod_perl
    $must_login = "";                    #this must always be undef'd for mod_perl

    $organization = "";	   # Organization name.
    $monadmin = "BOFH\@your.domain";		   # Your e-mail address.
                                                   # note: must escape @ signs!
    $logo = "/mon/logo.png";      # Company or mon logo.
    $reload_time = 60;				      # Seconds for page reload.

    $monhost = "localhost";				# Mon server hostname.
    $monport = "2583";				# Mon port number.

    #$must_login = "yes";                 # Uncomment this out if you want 
    # authentication to be mandatory
                                     # for all connections to the mon server.
    #!!! WARNING!!!!! You must change $app_secret to something unique to your site!
    $app_secret = '1.90LK=R==36jlel492jl><><oiOIUIGWgIgiiGYrrEGb9c<udY^dz{z9Vg57(aYt#RLaw4:)y?j0h.!()()1&jjJJJHGIp^YS'; # something unguessable
    $default_username = "readonly" ;       # default username to try when
                                       # authenticating (should be a
                                       # low-privilege account)
    $default_password = "public" ;         # default password to try when
                                       # authenticating (should be a
                                       # low-privilege account)
    $login_expire_time = 900 ;            # Idle time, in seconds, until login
                                     # cookie is invalidated. Note that if
                                     # $login_expire_time < $reload_time,
                                     # you will not be able to "idle" and
                                     # authentication will be required much
                                     # more often.
    $cookie_name = "mon-cookie";           #name of cookie given to browser for auth
    $cookie_path = "/";                  # path for auth cookie
                                     # Set this to "" for auto-path set
    $untaint_ack_msgs = "yes";           # Use HTML::Entities to scrub user-supplied ack messages (recommended!)
    # Define optional regexes in the @show_watch variable,
    # and only hostgroups which match one of these regexes
    # will be shown.
    #@show_watch = ("hostgroup1", "hostgroup2", "www.*");
    $show_watch_strict = "no";     #set this to "yes" to enforce show_watches strictly

    $fixed_font_face = "courier";        #default 'fixed' font-face to use
    $sans_serif_font_face = "Helvetica, Arial";  #default 'sans-serif' font-face to use

    $BGCOLOR = "#054a63";				# Background color
    $TEXTCOLOR = "#D8D8BF";			        # Text color (default is gray)
    $LINKCOLOR = "yellow";			        # Link color
    $VLINKCOLOR = "#00FFFF";			# Visited link color (default is teal)

    $greenlight_color = "#00ab5d";                # color of "good" status events
    $redlight_color = "#bd0101";                      # color of "bad" status events
    $unchecked_color = "#000033";                   # color of "unknown" status events
    $disabled_color="#5f5f5f";                  # color of "disabled" items
    $yellowlight_color = "#FF9933";             # color of "going bad" status events

    # Maximum dtlog entries to show per page
    $dtlog_max_failures_per_page = "100";
}

###############################################################
# You shouldn't need to change anything below this !!!!!!!!
###############################################################
$url = CGI::script_name();			# URL of this script.


# General Declarations -------------------------------------------------
use vars qw($c $connect_failed $webpage $time $localtime @year_months @days_of_week );
@year_months = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');
@days_of_week = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday');

$connect_failed = 0;     #we assume the connection will succeed until proven otherwise

%loginhash = ("username","", "password","");

$webpage = new CGI;			       # Initialize web page CGI object

$time = time;				       # This will be used for 
$localtime = localtime(time);		       # the time on the page.
                                               # (should perhaps use servertime?)

use vars  qw($command $args $rt $rtargs $ackcomment %alert_vars @time_based_alert_vars @pp_sec_alert_vars %auth_commands $auth_commands_checked );
# These global vars all need to be zeroed out at the beginning of each
# instance so that they don't confuse mod_perl. If you're running under CGI,
# you don't need to do this, but it won't hurt either.
$command = "";
$ackcomment = "";
$args = "";
$rt = "";
$rtargs = "";


#
# Initialize global variables, by source and/or an optional config file
# Read the mon.cgi configuration file if one was specified
#
if ($moncgi_config_file) { #config file specified
    # First read the configuration global variables, if we
    # haven't yet. But only read in config globals once from the
    # source code, after a config file has been read in, the 
    # config file is the authoritative source of configuration
    # information.
    &initialize_config_globals unless $has_read_config;
    # Then override these with settings from the config file.
    # Note that monhost and monport can later be overridden 
    # CGI params.
    &moncgi_read_cf($moncgi_config_file) if $moncgi_config_file;
} else { #no config file specified
    # initialize config globals unconditionally
    # Note that monhost and monport can later be overridden 
    # CGI params.
    &initialize_config_globals;
}



#
# Check for a proper version of Mon::Client. If the user has a
# version that's too old, tell them so and exit.
#
if ($Mon::Client::VERSION < $required_mon_client_version) {
    print $webpage->header();
    print $webpage->start_html(-title=>"mon.cgi error: insufficient Mon::Client version",
			       -BGCOLOR=>$BGCOLOR,
			       -TEXT=>$TEXTCOLOR,
			       -LINK=>$LINKCOLOR,
			       -VLINK=>$VLINKCOLOR,
			       -META=>{
				   'generator'=>"mon.cgi $VERSION ($AUTHOR)",
			       },
			       );    
    print $webpage->h3("Insufficient version ($Mon::Client::VERSION) of the Mon::Client perl module installed. Please upgrade your Mon::Client to at least version $required_mon_client_version before running mon.cgi.");
    print $webpage->h3("Also note, if you're running mon.cgi under Apache+mod_perl, you'll need to restart Apache after upgrading the Mon::Client library.");
    print $webpage->end_html;
    exit;
}


#
# Read CGI params -- these overwrite anything in a config file 
# or hard-coded.
# This can change the value of the $monhost and $monport 
# global variables defined in initialize_config_globals and
# moncgi_read_cf.
#
# This can cause a problem if $monhost or $monport are defined here and we are running mod_perl...
#
&moncgi_get_params;


#
# Used to escape HTML in ack's
#
if ($untaint_ack_msgs =~ /^y(es)?$/i) {
    eval "use HTML::Entities" ;
} else {
    undef $untaint_ack_msgs;
}


# Initialize a TripleDES global if login is required, 
#  otherwise undef $must_login
if ($must_login =~ /^y(es)?$/i) {
    eval "use Crypt::TripleDES";
    $des = new Crypt::TripleDES;
} else {
    $must_login = "";
}

#
# Set (or unset) $show_watch_strict according to its value
#
if ($must_login =~ /^y(es)?$/i) {
    $show_watch_strict = 1;
} else {
    $show_watch_strict = "";
}

#
#Initialize the wordy descriptions of alert variables
#
%alert_vars = (
	       'depend' => "Dependencies, if any",
	       'service' => "Service being monitored",
	       'last_check' => "The last time this service was checked",
	       'timer' => "Time remaining until this service is next checked",
	       'last_summary' => "Summary output from most recent failure of this service",
	       'opstatus' => "Current status of this service (0=error, 1=OK, 7=unchecked)",
	       'alerts_sent' => "Number of alerts sent",
	       'interval' => "Test interval, in seconds",
	       'last_detail' => "Detail output from the most recent failure of this service",
	       'monitor' => "Monitor used to test this service",
	       'last_trap' => "Last time a trap was received on this service",
	       'last_alert' => "Last time an alert was sent for this service",
	       'last_success' => "Last time this service returned an OK result",
	       'group' => "Hostgroup",
	       'failure_duration' => "Length of failure",
	       'ack' => "Acknowledgement status (1=failed service was ack'ed)",
	       'ackcomment' => "Comment issued by the acknowledger",
	       'first_failure' => "First failure time of this service",
	       'last_failure' => "Last failure time of this service",
	       'depend' => "Hostgroups/Services on which this service depends",
	       'last_check' => "Time this service was last checked",
	       'service' => "Service being checked",
	       'last_opstatus' => "Previous opstatus for this service (0=error, 1=OK, 7=unchecked)",
	       'exitval' => "Last exit value of monitor for this service (0=OK, anything else indicates failure)",
	       'depstatus' => "Dependency status (1 = dependencies OK, 0=dependencies not OK or no dependencies)",
	       'last_summary' => "Summary output from most recent failure of this service",
	       'last_detail' => "Detail output from the most recent failure of this service",
	       );


# These are variables from svc_details which should be represented as
# pretty-printed time strings. Mon gives them to us as UNIX time(2), so we
# have to convert. They used to be hardcoded deep into the code, this
# is an attempt at a readability improvement.
# Example representation: '(31 days, 17 hours, 53 minutes, 25 seconds ago)'
@time_based_alert_vars = (
			  "last_check",
			  "last_failure",
			  "last_trap",
			  "last_alert",
			  "last_success",
			  "last_failure",
			  "first_failure",
			  );

# These are variables from svc_details which should be represented as
# "pretty printed" seconds/minutes/hours/days.
# Example representation: '4 minutes, 19 seconds'
@pp_sec_alert_vars = (
			  "timer",
			  "interval",
			  "failure_duration",
		      );


%auth_commands = (                 # This global tracks the authorization
                                   # status of all commands mon.cgi can 
                                   # issue for a user. It is a candidate for
                                   # inclusion in a cookie someday.
		  list =>      { auth=>0, bgcolor=>""},
		  reset =>     { auth=>0, bgcolor=>""},
		  stop =>      { auth=>0, bgcolor=>""},
		  start =>     { auth=>0, bgcolor=>""},
		  savestate => { auth=>0, bgcolor=>""},
		  loadstate => { auth=>0, bgcolor=>""},
		  disable =>   { auth=>0, bgcolor=>""},
		  enable =>    { auth=>0, bgcolor=>""},
		  test =>      { auth=>0, bgcolor=>""},
		  ack =>       { auth=>0, bgcolor=>""},
		  reload =>    { auth=>0, bgcolor=>""},
		  );

$auth_commands_checked = 0;        # This global tracks whether authorization
                                   # for all commands has been checked.


###############################################################
# Function definitions begin below
###############################################################
#
# Forward declare all functions, for our sanity.
#
#
# General functions
#
sub pp_sec ;
sub pp_sec_brief ;
sub arithmetic_mean ;
sub median ;
sub std_dev ;
sub validate_name ;
sub gen_ciphertext ;
sub gen_cleartext ;
#
# Base mon.cgi pages
#
sub setup_page ;
sub print_bar ;
sub query_opstatus ;
sub can_show_group ;
sub list_status ;
sub query_group ;
sub end_page ;
sub list_alerthist ;
sub svc_details ;
sub list_disabled ;
sub list_dtlog ;
sub list_pids ;
#
# mon functions
#
sub mon_connect ;
sub mon_list_group ;
sub mon_list_watch ;
sub mon_list_failures ;
sub mon_list_successes ;
sub mon_list_opstatus ;
sub mon_list_disabled ;
sub mon_reload ;
sub mon_loadstate ;
sub mon_savestate ;
sub mon_loadstate_savestate ;
sub mon_schedctl ;
sub mon_list_pids ;
sub mon_list_descriptions ;
sub mon_enable ;
sub mon_disable ;
sub mon_test_service ;
sub mon_test_config ;
sub mon_reset ;
sub mon_list_alerthist ;
sub mon_list_sched_state ;
sub mon_list_dtlog ;
sub mon_ack ;
sub mon_servertime ;
sub mon_checkauth ;
sub mon_state_change_enable_only ;
sub mon_state_change ;
#
# mon.cgi functions
#
sub moncgi_get_params ;
sub moncgi_logout ;
sub moncgi_authform ;
sub moncgi_generic_button ;
sub moncgi_switch_user ;
sub moncgi_print_service_table_legend ;
sub moncgi_list_dtlog_navtable ;
sub moncgi_test_all ;
sub moncgi_reset ;
sub moncgi_read_cf ;
sub moncgi_login ;
sub moncgi_custom_print_bar ;
sub moncgi_custom_commands;

###############################################################
# General functions, not specific to Mon or mon.cgi
###############################################################
sub pp_sec {
    # This routine converts a number of seconds into a text string
    # suitable for (pretty) printing. The dtlog from Mon reports downtime
    # in seconds, and we want to present the user with more meaningful
    # data than "the service has been down for 13638 seconds"
    #
    # By Martha Greenberg <marthag@mit.edu> w/ pedantic plural 
    # modifications by Andrew.
    use integer;
    my $n = $_[0];
    my ($days, $hrs, $min, $sec) = ($n / 86400, $n % 86400 / 3600,
				    $n % 3600 / 60, $n % 60);
    my $s = $sec . " second";
    $s .= "s" if $sec != 1;   #because 0 is plural too :)
    if ($min > 0) {
	if ($min == 1) {
	    $s = $min . " minute, " . $s;
	} else {
	    $s = $min . " minutes, " . $s;
	}
    }
    if ($hrs > 0) {
	if ($hrs == 1) {
	    $s = $hrs . " hour, " . $s;
	} else {
	    $s = $hrs . " hours, " . $s;
	}
    }
    if ($days > 0) {
	if ($days == 1) {
	    $s = $days . " day, " . $s;
	} else {
	    $s = $days . " days, " . $s;
	}
    }
    return $s;
}


sub pp_sec_brief {
    # This routine converts a number of seconds into a text string
    # suitable for brief (yet pretty) printing.
    #
    # We use this on the opstatus page to display deltas of times (for
    # last check, next check).
    use integer;
    my $n = $_[0];
    my $s;
    if ($n >= 0) {
	$s .= "+" ;
    } else {
	$s .= "-" ;
	$n = abs($n);
    }
    my ($days, $hrs, $min, $sec) = ($n / 86400, $n % 86400 / 3600,
				    $n % 3600 / 60, $n % 60);
    if ($days > 0) {
	$s .= $days . "d";
    }
    if ($hrs > 0) {
	$s .= $hrs . "h";
    }
    if ($min > 0) {
	$s .= $min . "m";
    }
    $s .= "${sec}s" ;
    return $s;
}


sub arithmetic_mean {
    # Given an array of numbers, this function returns the arithmetic mean
    return 0 if scalar(@_) == 0 ;      #don't waste our time
    my $sum = 0;
    foreach (@_) {
	$sum += $_;
    }
    return $sum/scalar(@_);
}

sub median {
    # Given an array of numbers, this function returns the median
    return 0 if scalar(@_) == 0 ;      #don't waste our time
    my $middle_element_index = int(scalar(@_)/2);
    @_ = sort {$a <=> $b} @_;
    if (scalar(@_)%2 == 1) {  #odd num of elements, take the middle
        return $_[$middle_element_index];
    } else {  # even # of elements, take the avg of the 2 middle elements
        return &arithmetic_mean($_[$middle_element_index],$_[($middle_element_index-1)]);
    }
}


sub std_dev {
    # Given an array of numbers, this function returns their 
    # standard deviation.
    return 0 if scalar(@_) < 2 ;      #don't waste our time
    my $sum = 0;
    my $mean = &arithmetic_mean(@_);
    foreach (@_) {
	$sum += ( $_ - $mean )**2 ;
    }
   return ( $sum/(scalar(@_) - 1) )**0.5 ;
}


sub validate_name {
    # Return untainted host or group name if safe, undef otherwise.
    # Because you can never scrub your input too well.
    return $_[0] =~ /^([\w.\-_]+)$/ ? $1 : undef;
}


sub gen_ciphertext {
    # This function takes as its input a piece of plaintext and
    # returns a piece of ASCII, 3DES-encoded ciphertext, or undef if 3DES fails
    # for some reason. The key used is the global value "$app_secret".
    my ($plaintext) = (@_);
    my $ciphertext ;

    if ($ciphertext = $des->encrypt3 ("$plaintext", "$app_secret" )) {
	# convert key to hex
	$ciphertext = unpack("H*", $ciphertext) ;
#	print "ciphertext is $ciphertext<br>\n";   #DEBUG
	return $ciphertext;
    } else {
	return undef;
    }
}


sub gen_cleartext {
    # This function takes as its input a piece of ASCII, 3DES-encoded 
    # ciphertext and returns a piece of  plaintext, 
    # or undef if 3DES fails for some reason. The key used is the 
    # global value "$app_secret".
    my ($ciphertext) = (@_);
    my $plaintext ;

    return undef if ! $ciphertext;

    #convert key to format decrypt3() will understand
    $ciphertext = pack("H*", $ciphertext) ;    

    if ($plaintext = $des->decrypt3 ("$ciphertext", "$app_secret" )) {
#	print "plaintext is $plaintext<br>\n";   #DEBUG
	return $plaintext;
    } else {
	return undef;
    }
}



###############################################################
# Presentation functions. These all have the common feature
# that they format a bunch of information and present it in 
# a nice(?) way to the user.
###############################################################
sub setup_page {
    # Setup the html doc headers and such
    # Also, get/set username/password cookie if $must_login is in effect

    my ($title) = (@_);
    my (@time, $ttime);
    my $title_color = "$TEXTCOLOR"; 
    my $page_title = "$organization : " if $organization ne "";
    $page_title = "${page_title}MON - $title ($monhost:$monport)";
    my $time_now = time;
    my @expires_time = gmtime($time_now + $login_expire_time);
    # Put the cookie date format in the standard cookie format
    my $expires = sprintf ("%s, %.2d-%s-%d %.2d:%.2d:%.2d GMT", @days_of_week[$expires_time[6]], $expires_time[3], @year_months[$expires_time[4]], $expires_time[5] + 1900, @expires_time[2,1,0]);
    my ($encrypted_password, $cookie, $cookie_value);
    my $refresh_url;

    #
    # Define $args as null if it is not currently defined
    #
    $args = "" if ! defined($args);

    # Set the refresh page to always be the summary page, unless 
    # certain commands are selected.
    if ( $command eq "query_opstatus_full" ) {
	$refresh_url = "$url?${monhost_and_port_args_meta}command=query_opstatus_full";
    } elsif ( ($command eq "mon_test_service") || ($command eq "svc_details") ) {
	$refresh_url = "$url?${monhost_and_port_args_meta}command=svc_details&args=$args";
    } elsif ($command eq "query_group") {
	$refresh_url = "$url?${monhost_and_port_args_meta}command=query_group&args=$args";
    } elsif ($command eq "list_dtlog") {
	$refresh_url = "$url?${monhost_and_port_args_meta}command=list_dtlog&args=$args";
    } else {
	$refresh_url = "$url?${monhost_and_port_args_meta}command=query_opstatus";
    }

    if ($must_login) {
	if ( ( defined($loginhash{'username'}) ) &&
	     ( $loginhash{'username'} ne "" )
	     ) {
	    # Don't get the username and password from the cookie 
	    # if the user just submitted it via the login form.
	    # Encrypt the password for cookie storage.
	    $encrypted_password = &gen_ciphertext($loginhash{'password'}) ;
	} else {
	    # Get the existing cookie and parse it
	    $cookie_value = $webpage->cookie(-name=>"$cookie_name",
						);
	    ($loginhash{'username'},$loginhash{'password'}) = split(':', $cookie_value) if $cookie_value;
	    $encrypted_password = $loginhash{'password'} ;
	    # Decrypt the password string (if any) for use by the app,
	    # unless the user just submitted it in cleartext.
	    $loginhash{'password'} = &gen_cleartext($loginhash{'password'}) ;
	    # for some reason (bug?) I get a space at the end of the password
	    # that is returned here, so for now let's take it out, since
	    # spaces are illegal in passwords anyway.
	    $loginhash{'password'} =~ s/\s+//g if defined($loginhash{'password'}) ;
	}

	# Set up the new cookie (re-issue a new cookie with every access)
	if ($destroy_auth_cookie) {
	    $cookie_value = "" ;
	} elsif ( defined($loginhash{'password'}) ) {
	    $cookie_value = "$loginhash{'username'}:$encrypted_password" ;
	} else { # no username was supplied
	    $cookie_value = "" ;
	}
	$cookie = $webpage->cookie(-name=>"$cookie_name",
				   -value=>"$cookie_value",
				   -expires=>"$expires",
				   -path=>"$cookie_path",
				   );
	print $webpage->header(
			       -cookie=>$cookie,
			       -refresh=>"$reload_time; URL=$refresh_url",
			       );
    } else {
	# Plain & simple, no cookie, no passsword
	$encrypted_password = "" ;
	print $webpage->header(
			       -refresh=>"$reload_time; URL=$refresh_url",
			       );
    }


    print $webpage->start_html(-title=>"$page_title",
			       -BGCOLOR=>$BGCOLOR,
			       -TEXT=>$TEXTCOLOR,
			       -LINK=>$LINKCOLOR,
			       -VLINK=>$VLINKCOLOR,
			       -META=>{
				       'generator'=>"mon.cgi $VERSION ($AUTHOR)",
				   },
			       );

# Useful for debugging username/password/cookie issues  #DEBUG
#    print "cookie value is $cookie_value<br>\n";  #DEBUG
#    print "encrypt passwd is $encrypted_password<br>\n";  #DEBUG
#    print "username is &quot;$loginhash{'username'}&quot;<br>\n";  #DEBUG
#    print "decrypt passwd is &quot;$loginhash{'password'}&quot;<br>\n";  #DEBUG

    #
    # Print the logo image, if it was defined by the user.
    #
    if ($logo) {
	$webpage->print("<table border=0><tr><td>\n");
	#
	# If the user has given a logo_link link, then insert an
	# anchor tag to it here, if logo_link was defined by the 
	# user.
	#
	if ($logo_link) {
	    $webpage->print("<a href=\"$logo_link\"><img src=\"$logo\" alt=\"[$organization logo]\"></a></td><td><h1><font color=$title_color>MON: $title</font></h1></td>\n");
	} else {
	    $webpage->print("<img src=\"$logo\" alt=\"[$organization logo]\"></td><td><h1><font color=$title_color>MON: $title</font></h1></td>\n");
	}
	$webpage->print("</tr></table>\n");
	$webpage->print("<hr>\n");
    } else {
	#just print the generic page with no logo and no link
	$webpage->print("<h1><font color=$title_color>MON: $title</font></h1>\n");     
    }
    &print_bar;


    @time = localtime($time);
    $ttime = sprintf ("%.2d:%.2d:%.2d on %s, %.2d-%s-%d", @time[2,1,0], @days_of_week[$time[6]], $time[3], @year_months[$time[4]], $time[5] + 1900 );

    $webpage->print("<center>");
    $webpage->print
	("\nThis information was presented at $ttime");

    #
    # If the user is currently logged in, tell the user who 
    # they are logged in as.
    # If the user is NOT currently logged in, offer to log
    # them in.
    #
    if ( 
	 ($loginhash{'username'}) && 
	 ($loginhash{'username'} ne $default_username) 
	 ) {
	$webpage->print
	    (" to user <i>$loginhash{'username'}</i> (<a href=\"$url?${monhost_and_port_args}command=moncgi_logout\">log off user <i>$loginhash{'username'}</i></a>)")  ;
    } else {
	$webpage->print
	    (" (<a href=\"$url?${monhost_and_port_args}command=moncgi_login\">log in</a>)");
    }
    $webpage->print(".</center>");

} 



sub print_bar {
    # Print the command bar. Called at both the beginning and the end
    # of each page.
    #
    my $button = "INPUT TYPE=\"submit\" NAME=\"command\"";
    my $table_width = "100%";
    my $face = $sans_serif_font_face;
    my ($cmd, $command, $desc);
    my $all_commands_unauthorized = 1;
    my $i;

    foreach $cmd (keys %auth_commands) {
	$auth_commands{$cmd}{'auth'} = &mon_checkauth($cmd);
	#last if $auth_commands{$cmd}{'auth'} == -1; # stop checking if we can't
                       	        	     	# contact the server
	$auth_commands{$cmd}{'bgcolor'} = $auth_commands{$cmd}{'auth'} == 0 ?  "bgcolor=\"$disabled_color\"" : "";
	$all_commands_unauthorized = 0 if $auth_commands{$cmd}{'auth'} == 1 ;
    }
    # Check to see if authentication is required and the selected user has
    # no permissions to do anything. This can only happen if your mon admin
    # is very cruel and gives you an account with no permissions (should
    # be very rare), or if a user enters the wrong password for a valid
    # account name (the usual case).
    # The main thing I don't like about this solution is that it embeds
    # the default l/p into the URL, but this isn't a secure password
    # anyway, right?
    $cmd = "list";   #set $cmd to the most basic of commands
    if ($auth_commands{$cmd}{'auth'} == 0) {
	$webpage->print("<h2>Cannot connect to the mon server. Check the mon process to see if it is running.</a></h2><br>\n");
    } elsif ( ($must_login) && ($all_commands_unauthorized == 1) ) {
	$webpage->print("<h2>You are attempting to log in with the username &quot;$loginhash{'username'}&quot; but your password is incorrect.<br><br>Either enter in the correct username/password above or <a href=\"$url?${monhost_and_port_args}command=query_opstatus&amp;username=$default_username&amp;password=$default_password\">click here to clear your authentication credentials and log back in as the default user.</a></h2><br>\n");
    }
    $auth_commands_checked = 1;

    # We have to lay the tables out by hand bec. of the colspanning :(
    $webpage->print("<table width=\"$table_width\" border=1 align=center>\n");

    #
    # Print the first row of the command table
    #
    $webpage->print("<tr>\n");
    $webpage->print("\t<td $auth_commands{'list'}{'bgcolor'} align=center><font FACE=\"$face\"><a href=\"$url?${monhost_and_port_args}command=query_opstatus\">Show Operational Status (summary)</a></font></td>\n");
    $webpage->print("\t<td $auth_commands{'list'}{'bgcolor'} align=center><font FACE=\"$face\"><a href=\"$url?${monhost_and_port_args}command=list_alerthist\">Show Alert History</a></font></td>\n");
    $webpage->print("\t<td $auth_commands{'loadstate'}{'bgcolor'} align=center><font FACE=\"$face\"><a href=\"$url?${monhost_and_port_args}command=mon_loadstate&amp;args=\">Load scheduler state</a></font></td>\n");
    $webpage->print("\t<td $auth_commands{'start'}{'bgcolor'} align=center><font FACE=\"$face\"><a href=\"$url?${monhost_and_port_args}command=mon_schedctl&amp;args=start\">Start scheduler</a></font></td>\n");

   $webpage->print("\t<td $auth_commands{'list'}{'bgcolor'} colspan=2 align=center><font FACE=\"$face\"><a href=\"$url?${monhost_and_port_args}command=list_disabled\">List Disabled Hosts/ Watches/ Svcs</a></font></td>\n");
   $webpage->print("\t<td $auth_commands{'test'}{'bgcolor'} align=center><font FACE=\"$face\"><a href=\"$url?${monhost_and_port_args}command=mon_test_config\">Test Mon Config File</a></font></td>\n");
    $webpage->print("</tr>\n");

    #
    # Print the second row of the menu table
    #
    $webpage->print("<tr>\n"); 
    $webpage->print("\t<td $auth_commands{'list'}{'bgcolor'} align=center><font FACE=\"$face\"><a href=\"$url?${monhost_and_port_args}command=query_opstatus_full\">Show Operational Status &nbsp;&nbsp;(full)</a></font></td>\n");
    $webpage->print("\t<td $auth_commands{'list'}{'bgcolor'} align=center><font FACE=\"$face\"><a
href=\"$url?command=list_dtlog\">Show Downtime Log</a></font></td>\n") ;
    $webpage->print("\t<td $auth_commands{'savestate'}{'bgcolor'} align=center><font FACE=\"$face\"><a href=\"$url?${monhost_and_port_args}command=mon_savestate&amp;args=\">Save scheduler state</a></font></td>\n");
    $webpage->print("\t<td $auth_commands{'stop'}{'bgcolor'} align=center><font FACE=\"$face\"><a href=\"$url?${monhost_and_port_args}command=mon_schedctl&amp;args=stop\">Stop scheduler</a></font></td>\n");
    $webpage->print("\t<td $auth_commands{'reload'}{'bgcolor'} align=center><font FACE=\"$face\"><a href=\"$url?${monhost_and_port_args}command=mon_reload&amp;args=auth\">Reload auth file</a></font></td>\n");
    $webpage->print("\t<td $auth_commands{'list'}{'bgcolor'} align=center><font FACE=\"$face\"><a href=\"$url?command=list_pids\">List Mon PIDs</a></font></td>\n");
    $webpage->print("\t<td $auth_commands{'reset'}{'bgcolor'} align=center><font FACE=\"$face\"><a href=\"$url?${monhost_and_port_args}command=moncgi_reset\">Reset Mon</a></font></td>\n");
    $webpage->print("</tr>\n");

    #
    # Print the optional third row of the command table
    # This row can be defined at individual sites and contain commands
    # of your choice. Thanks to Ed Ravin (eravin@panix.com) for this.
    #
    &moncgi_custom_print_bar($face);   # row 3, if any, for the local site

    $webpage->print("</table>");
}


# query the server operational status ----------------------------------
sub query_opstatus {
    my ($detail_level) = (@_);
    my ($retval);            # some variables for failures
    my (%op_success, %op_failure);
    my @scheduler_status = &mon_list_sched_state ;
    my $opstatus_table_width = "100%";  # the width of the whole opstatus tbl
    my $service_column_width = "40%";  # the width of the Service column
    my $service_legend_table_width = "70%";  # the width of the service legend table
    
    $webpage->print("<center>\n");
    if ($scheduler_status[0] != 0) {
	$webpage->print
	    ("The scheduler on <b>$monhost:$monport</b> is currently <font color=$greenlight_color>running</font>. ");
    } else {
	my @sched_down_time = localtime ($scheduler_status[1]);
	my $pretty_sched_down_time = sprintf ("%.2d:%.2d:%.2d, %s-%s-%s\n", @sched_down_time[2, 1, 0, 3], @year_months[$sched_down_time[4]], $sched_down_time[5]+1900);
	if ($scheduler_status[1] != 0) {
	    $webpage->print
		("<br>The scheduler has been <font color=$redlight_color>stopped</font> since $pretty_sched_down_time.<br>\n");
	} else {    #value is undef, scheduler cannot be contacted (or auth failure)
	    $webpage->print
		("<br><font color=$redlight_color>The scheduler cannot be contacted at this time.</font><br>\n");
	}
    }

    $webpage->print
	("This page will reload every $reload_time seconds.<br>");
    $webpage->print("</center><br>\n");

    %op_success = &mon_list_successes;
    %op_failure = &mon_list_failures ;


    $webpage->print("<a name=\"$url#opstat_tbl\"></a>");
    $webpage->print
	("<table align=center width=\"$opstatus_table_width\" border=1>\n");
    $webpage->print
	("<tr><th><font size=+2>Host Group</font></th><th width=\"$service_column_width\"><font size=+2>Service</font>&nbsp;<sup><font size=-1><a href=\"$url#legend\">(legend)</a></font></sup></th>\n");
    $webpage->print
	("<th><font size=+2>Last Checked</font></th><th><font size=+2>Est. Next Check</font></th></tr>\n");

    # Give extra notification if the scheduler is down (this is a big deal!)
    unless ($scheduler_status[0] != 0) {
	if ($scheduler_status[1] != 0) {
	    $webpage->print
		("<tr><td colspan=4><center><font size=+2 color=$redlight_color>! SCHEDULER IS NOT RUNNING. RESULTS SHOWN BELOW MAY NOT BE CORRECT !</font></center></td></tr>\n");
	} else {
	    $webpage->print
		("<tr><td colspan=4><center><font size=+2 color=$redlight_color>! SCHEDULER CANNOT BE CONTACTED. RESULTS SHOWN BELOW MAY NOT BE CORRECT !</font></center></td></tr>\n");	    
	}
    }

    &list_status($detail_level, %op_failure) if defined(%op_failure);
    &list_status($detail_level, %op_success) if defined(%op_success);

    $webpage->print("</table>\n");    

    # Print the legend below the table
    &moncgi_print_service_table_legend ($service_legend_table_width);
}

#
# This subroutine tests whether a given group is allowed to be
# shown to the user.
# Inputs:      Name of group to check
# Outputs:  1  Group is allowed to be shown
#           0  Group is not allowed to be shown
#
sub can_show_group {
    my ($group) = (@_);
    my $watch;
    # Do not print out the status for this group
    # unless it is on the "allowed" list
    if (@show_watch) {  #user defined one or more watch keywords
	#
	# Loop through each access control and look for a match
	#
	foreach $watch (@show_watch) {
	    if ( $group =~ m/^$watch$/ )  { #we found a match
		#print STDERR "Group $group matched '$watch'\n"; #DEBUG
		return 1;
	    }
	}
    } else { #user didn't define any watch keywords, so show everything
	return 1;
    }

    return 0;
}

sub list_status {
    # This function lists the status of all hosts and services. It is 
    # kind of a mess, but this is the function that 90% of the time
    # you will be viewing, and it has to do a lot. It could still be
    # cleaned up considerably though.
    #
    my ($detail_level, %op) = (@_);
    my (%group_list, $group, $service, $s, $g, $h);
    my (@time);
    my $bg_fail = $redlight_color ; 
    my $bg_fail_noalerts = $yellowlight_color ; 
    my $bg_ok = $greenlight_color;
    my $td_bg_color;
    my $face = $sans_serif_font_face;
    
    my %d = &mon_list_disabled ;
    my %desc = &mon_list_descriptions if $detail_level eq "full";
    my $servertime = &mon_servertime;
    my (%ONDS, %ONDS_lastcheck, %ONDS_nextcheck) ;    #special hashes of arrays for "OK, Non-Disabled Services"
    my %OPSTAT = %Mon::Client::OPSTAT;

    my $service_disabled_string ;
    my ($service_acked_string, $ackcomment) ;
    my $host_disabled_string ;
    my $watch_disabled_string ;
    my $failure_string;
    my $desc_string ;
    my %saw ;      #used for sorting
    my @disabled_hosts;

    foreach $group (sort keys %op) {    #begin group loop
	# Only show this group if we are allowed to see it
	next unless &can_show_group($group) ;

	if ($detail_level eq "full") {
	    # get a list of members of the group if we haven't already
	    # we need the defined() to deal with certain empty groups
	    $group_list{$group} = [ &mon_list_group($group) ] unless defined(@{$group_list{$group}});
	}
	foreach $service (sort keys %{$op{$group}}) {     #begin service loop
	    $s = \%{$op{$group}->{$service}};
	    $service_disabled_string = "";
	    $service_acked_string = "";
	    $host_disabled_string = "";
	    $watch_disabled_string = "";
	    $desc_string = "";
	    undef %saw;
	    undef @disabled_hosts;
	    $service_disabled_string = "(DISABLED)" if ${ d{"services"}{$group}{$service} };
	    # assemble the ACK message, if any.
	    # Escape the HTML to avoid any potential nastiness if the
	    # user requested it, otherwise, just pass it on through 
            # as is.
	    if ( $op{$group}{$service}{'ack'} == 1 ) {
		if ($untaint_ack_msgs) {
		    #
		    # We untaint
		    #
		    $ackcomment = $op{$group}{$service}{'ackcomment'} eq "" ? "(no ack msg)" : HTML::Entities::encode_entities($op{$group}{$service}{'ackcomment'}) ;
		} else {
		    #
		    # We don't untaint
		    #
		    $ackcomment = $op{$group}{$service}{'ackcomment'} eq "" ? "(no ack msg)" : $op{$group}{$service}{'ackcomment'} ;
		}
		$service_acked_string = " (ACKED: $ackcomment)" ;
	    }
	    foreach $g (keys %{$d{"hosts"}}) {
		foreach $h (keys %{$d{"hosts"}{$group}}) {
		    push(@disabled_hosts , $h);
		}

	    }
	    # uniq and sort the returned array of disabled hosts
	    @saw{@disabled_hosts} = ();
	    @disabled_hosts = sort keys %saw;
	    $host_disabled_string = join(" " , @disabled_hosts) if scalar(@disabled_hosts) > 0 ;
	    $host_disabled_string = "<br>($host_disabled_string DISABLED)\n" if ($host_disabled_string ne "");
	    $watch_disabled_string = "(DISABLED)" if (${d{"watches"}{$group}});
            $td_bg_color = ( ($watch_disabled_string ne "") || ($host_disabled_string ne "") ) ? $disabled_color : $BGCOLOR ;

            # Don't print the service individually if we are in brief mode
            # mode and the service is an ONDS.
	    next if ( ($s->{"opstatus"} == $OPSTAT{"ok"}) && ($service_disabled_string eq "") && ($detail_level ne "full") );

            # Now print the first column (the group and its status)
            $webpage->print("<tr><td align=left bgcolor=\"$td_bg_color\">\n");
            # check to see if full display was requested
	    if ($detail_level eq "full") {
		$desc_string = ($desc{$group}{$service} ne "") ? " &quot;$desc{$group}{$service}&quot;" : " &lt;no description specified&gt;" ;
		$webpage->print("$watch_disabled_string<a href=\"$url?${monhost_and_port_args}command=query_group&amp;args=$group\">");
		$webpage->print("<font FACE=\"$face\" size=+1>$group</font></a><br>\n(");
		$webpage->print(join(", ",@{$group_list{$group}}));
		$webpage->print(")$host_disabled_string</td>\n");
	    } else {
		$webpage->print("<font FACE=\"$face\" size=+1>\n");
		$webpage->print("$watch_disabled_string<a href=\"$url?${monhost_and_port_args}command=query_group&amp;args=$group\">");
		$webpage->print("$group</a></font>$host_disabled_string</td>\n");
	    }


            # Now print the second column (the service and its status)
	    if ($s->{"opstatus"} == $OPSTAT{"untested"})  {
		# for untested, don't use a bg in table cell and change
		# font color instead.
		$td_bg_color = ($service_disabled_string eq "") ?  $unchecked_color : $disabled_color ;
		$webpage->print("<td align=left bgcolor=\"$td_bg_color\">\n");
		$webpage->print("$service_disabled_string<a href=\"$url?${monhost_and_port_args}command=svc_details&amp;args=$group,$service\">");
		$webpage->print("<b>${service}</b>");
		$webpage->print("<br><font>(UNCHECKED)</font></a>${desc_string}\n");
		$webpage->print("</td>\n");

	    } elsif ($s->{"opstatus"} == $OPSTAT{"fail"}) {
		# Check to see if the service has issued any alerts.
		# If not, then we call this service "failing" instead
		# of failed, on the assumption that if it hasn't
		# generated an alert yet, it isn't "really" important,
		# although you'd still like to know about it.
		if ( $s->{"alerts_sent"} == 0 ) {
		    $td_bg_color = $bg_fail_noalerts ;
		    $failure_string = "FAILED,NOALERTS" ;
		} else {
		    $td_bg_color = $bg_fail ;
		    $failure_string = "FAILED" ;
		    # Also give the # of alerts if "full" view was selected
		    $failure_string .= ",alerts_sent=" . $s->{"alerts_sent"} if $detail_level eq "full";
		}
		$td_bg_color = ($service_disabled_string eq "") ? $td_bg_color : $disabled_color ;
		$webpage->print("<td align=left bgcolor=\"$td_bg_color\">");
		$webpage->print("$service_disabled_string<a href=\"$url?${monhost_and_port_args}command=svc_details&amp;args=$group,$service\">");
		$webpage->print("<font size=+1><b>${service}</b></font></a>${desc_string} : \n");
		$webpage->print("<font size=+1>$s->{last_summary}</font>\n");
		$webpage->print("<br>($failure_string)");
		$webpage->print(" ${service_acked_string}") if $service_acked_string ne "";
		$webpage->print("</td>\n");
	    
	    } elsif ($s->{"opstatus"} == $OPSTAT{"ok"}) {
		$td_bg_color = ($service_disabled_string eq "") ?  $bg_ok : $disabled_color ;
		$webpage->print("<td bgcolor=\"$td_bg_color\"><font size=+0>");
		$webpage->print("$service_disabled_string<a href=\"$url?${monhost_and_port_args}command=svc_details&amp;args=$group,$service\">");
		$webpage->print("${service}</a></font>${desc_string}</td>\n");
		
	    } else {
		my $txt = "";
		for (keys %OPSTAT) {
		    $txt = $_ if ($s->{"opstatus"} == $OPSTAT{$_});
		}
		$webpage->print("<td><font>");
		$webpage->print("${service_disabled_string}${service} (details: $txt)</font></td>\n");
	    }
    
            if ($s->{"opstatus"} == $OPSTAT{"untested"}) {
		$webpage->print("<font COLOR=$unchecked_color>");
		$webpage->print("<td>--</td>");
		$webpage->print("</font>\n");
		
	    } else {
		$webpage->print("<td><font size=+1>");
		if ($s->{"last_check"}) {   #traps have a null value for last_check
		    # Service IS NOT a trap
		    if ($s->{"opstatus"} == $OPSTAT{"fail"}) { #check svc status
			# If service is failing, print last checked time
			#  and also print out last_OK time
			print &pp_sec_brief($s->{"last_check"} - $servertime);
                        # We need to check if the var is defined, since traps
	                # can throw us off.
			$webpage->print("<br>(Last OK: ");
			if ( (!defined($s->{"last_success"})) || ($s->{"last_success"} == 0) ) {   #service is currently failed and does not have a last_success time defined
			    # The event has never occurred
			    $webpage->print ("Never") ;
			} else {  #service is currently failed and has a last_success time defined
			    # Pretty-print the time that the service was last OK
			    @time = localtime ($s->{"last_success"});
			    $_ = $s->{"last_success"};
			    # Also calculate the delta and pretty-print that
			    $s->{"last_success"} .= "(" . &pp_sec($time - $_) . " ago)";
			    print &pp_sec_brief($s->{"last_success"} - $servertime);
			}
			$webpage->print(")");
		    } else {
			# If service is not failing, just print last checked time
			print &pp_sec_brief($s->{"last_check"} - $servertime);
		    }
		} else {
		    # Service IS a trap, or has never been checked
		    $webpage->print("--");
		}
		$webpage->print("</font></td>\n");
	    }
	    
	    	    
            $webpage->print("<td><font size=+1>");
            # Handle case where service is a trap and hence last_check=undef
            if ( ( $s->{"timer"} == 0 ) && (!($s->{"last_check"})) ) { 
                $webpage->print("--");
	    } else {
		$webpage->print ("<a href=\"$url?${monhost_and_port_args}command=mon_test_service&amp;args=$group,$service\">");
                $webpage->print (&pp_sec_brief($s->{"timer"}));
		$webpage->print ("</a>");
		$webpage->print ("&nbsp;&nbsp;<font size=-1><a href=\"$url?${monhost_and_port_args}command=moncgi_test_all&amp;args=$group\">(test all on $group)</a></font>") ;

	    }
            $webpage->print("</font></td>\n");
            # The next 4 lines are the old way of printing (absolute time)
            #@time = localtime ($qtime + $s->{"timer"});
	    #$webpage->print("<td><font size=+1>");
	    #printf("%.2d:%.2d:%.2d\n", @time[2, 1, 0] );
            #$webpage->print("</font></td>\n");
            $webpage->print("</tr>");
	    
        } # end $service loop
#
# NEW: print a "compressed" version of OK, Non-Disabled Services (ONDS)
# (the assumption being that ONDS's are not all that interesting,
# let's not use up a lot of screen real estate discussing them)
#
#  The whole thing is contingent upon us being in "brief" mode
        if ($detail_level ne "full") {
	    # Build the array of ONDS's
            foreach $service (sort keys %{ $op{$group} }) {
	        $s = \%{ $op{$group}->{$service} };
	        next if ( ${d{"services"}{$group}{$service}} ) ;
        	if ($s->{"opstatus"} == $OPSTAT{"ok"}) {
	            push (@{ $ONDS{$group} }, "<a href=\"$url?${monhost_and_port_args}command=svc_details&amp;args=$group,$service\">$service</a>");
		    if ($s->{"last_check"}) {   #check to see if service is a trap
			# Service IS NOT a trap
			push (@{ $ONDS_lastcheck{$group} }, &pp_sec_brief($s->{"last_check"} - $servertime) );
		    } else {
			# Service IS a trap
			push (@{ $ONDS_lastcheck{$group} }, "--");
		    }
  	            if ( ( $s->{"timer"} == 0 ) && (!($s->{"last_check"})) ) {
			# Service IS a trap
			push (@{ $ONDS_nextcheck{$group} }, "--");
		    } else {
			# Service IS NOT a trap
			#push (@{ $ONDS_nextcheck{$group} }, &pp_sec_brief($s->{"timer"}) );
			push (@{ $ONDS_nextcheck{$group} }, "<a href=\"$url?${monhost_and_port_args}command=mon_test_service&amp;args=$group,$service\">" . &pp_sec_brief($s->{"timer"}) ."</a>"); 
		    }
		}
            }
            # print the OK, no disabled services for this host if any exist
            if ( defined(@{ $ONDS{$group} }) ) {
		$td_bg_color = ( ($watch_disabled_string ne "") || ($host_disabled_string ne "") ) ? $disabled_color : $BGCOLOR ;
		$webpage->print("<tr>\n");
		$webpage->print("<td align=left bgcolor=\"$td_bg_color\">");
		$webpage->print("$watch_disabled_string<font FACE=\"$face\" size=+1><a href=\"$url?${monhost_and_port_args}command=query_group&amp;args=$group\">$group</a></font>$host_disabled_string");
		$webpage->print("</td>\n");
		$webpage->print("<td align=left bgcolor=\"$bg_ok\"><font size=-0>");
		print join(", ", @{$ONDS{$group}});
		$webpage->print("</font></td>\n");
		#Now print out the time(s)
		$webpage->print("<td align=left><font size=-1>");
		print join(", ", @{$ONDS_lastcheck{$group}});
		$webpage->print("</font></td>\n");
		$webpage->print("<td align=left><font size=-1>");
		# Add the "test all" command if there is more than
		# one service in the group.
		push (@{ $ONDS_nextcheck{$group} }, "<a href=\"$url?${monhost_and_port_args}command=moncgi_test_all&amp;args=$group\">(test all on $group)</a>") if scalar(@{ $ONDS_nextcheck{$group} }) > 1 ;
		print join(", ", @{$ONDS_nextcheck{$group}});
		$webpage->print("</font></td>\n");
		$webpage->print("</tr>\n");
	    }
	}  # end of ONDS printing
    }   # end of $group loop
}


sub query_group {
    #
    # Print out info about the hosts in a particular hostgroup
    #
    my ($args) = (@_);
    my $group = &validate_name ($args);
    my (%hosts, $host, $retval, $c, $e, $s, $service, $status, %op, $bgcolor, $msg, $ena_checked, $dis_checked) ;
    my %OPSTAT = %Mon::Client::OPSTAT;
    my $table_width = "90%";
    # Color to shade the cells depending on whether a user is allowed to
    # execute the disable/enable commands.
    my $disable_command_bgcolor = $auth_commands{'disable'}{'auth'} == 0 ? "bgcolor=\"$disabled_color\"" : "" ;
    my $enable_command_bgcolor = $auth_commands{'enable'}{'auth'} == 0 ? "bgcolor=\"$disabled_color\"" : "" ;

    my %d = &mon_list_disabled ;

    if (!defined $group) {
	$webpage->print("Invalid host group \"$group\"\n");
	return undef;
    }

    @_ = &mon_list_group($group) ;
    # turn the array into a hash, which is what we really want
    foreach (@_) {
	$hosts{$_} = "";
    }
    $webpage->print("<center>This page will reload every $reload_time seconds.<br></center>");

    # Only show the rest of this page if we are allowed to see 
    # information about this group.
    if ($show_watch_strict) {
	unless ( &can_show_group($group) ) {
	    print $webpage->h3("You are not authorized to see detailed information for hostgroup '$group'.");
	    print $webpage->h4("Please contact your system administrator for access.");
	    return 0;
	}
    }


    $webpage->print("<br><center><a href=\"$url?${monhost_and_port_args}command=query_group&amp;args=$group\"><font size=+1>Reload this page immediately.</font></a></center>\n");
    #############################################################
    # The table is divided into 3 sections: hostgroup, hosts, 
    # and services
    #############################################################
    # Start the form and set up our defaults
    print $webpage->startform(-action=>"$url");
    $webpage->param('command','mon_state_change');
    print $webpage->hidden(-name=>'command',
			   );
    $webpage->param('group',"$group");
    print $webpage->hidden(-name=>'group',
			   );
    $webpage->param('h',"$monhost");
    print $webpage->hidden(-name=>'h',
			   );
    $webpage->param('monport',"$monport");
    print $webpage->hidden(-name=>'p',
			   );
    # Start the table
    $webpage->print("<br><table align=center width=\"$table_width\" border=1>");
    #############################################################
    # Print the hostgroup portion of the table
    #############################################################
    $webpage->print("<tr>");
    $webpage->print("<th>Hostgroup &quot;<em>$group</em>&quot;</th>");
    $webpage->print("<th>Enabled</th>");
    $webpage->print("<th>Disabled</th>");
    $webpage->print("</tr>\n");
    $webpage->print("<tr>");
    $bgcolor = ( ${d{"watches"}{$group}} ) ? $disabled_color : $BGCOLOR;
    $webpage->print("<td bgcolor=\"$bgcolor\">$group <a href=\"$url?${monhost_and_port_args}command=list_dtlog&amp;args=$group\">(list downtime log for hostgroup $group)</a></td>") ;
    $dis_checked = ( ${d{"watches"}{$group}} ) ? "checked" : "";
    $ena_checked = (!${d{"watches"}{$group}} ) ? "checked" : "";
    $webpage->print("<td $enable_command_bgcolor><input type=radio name=group_$group value=ena $ena_checked></td>");
    $webpage->print("<td $disable_command_bgcolor><input type=radio name=group_$group value=dis $dis_checked></td>");
    $webpage->print("</tr>\n");

    #############################################################
    # Print the hosts portion of the table
    #############################################################
    $webpage->print("<tr>");
    $webpage->print("<th>Members of hostgroup \"<em>$group</em>\"</th>");
    $webpage->print("<th>Enabled</th>");
    $webpage->print("<th>Disabled</th>");
    $webpage->print("</tr>");

    foreach $host (keys %hosts) {
	if ($host =~ /^\*/) {
	    $host =~ s/^\*// ;    #strip the * or else mon dies
	    $hosts{$host} = "disabled";
	} else {
	    $hosts{$host} = "enabled";
	}		
    }
    foreach $host (sort keys %hosts) {
	next if ($host =~ /^\*/);      #ignore disabled hosts
	$webpage->print("<tr>");
	if ($hosts{$host} eq "disabled") {    #check to see if the host is disabled
	    # the host is currently disabled
	    $host =~ s/^\*// ;    #strip the * or else mon dies (should already be gone but just in case, this is a bad thing to happen)
	    $webpage->print("<td bgcolor=\"$disabled_color\">$host (DISABLED)</td>");
	    $webpage->print("<td $enable_command_bgcolor><input type=radio name=host_$host value=ena></td>");
	    $webpage->print("<td $disable_command_bgcolor><input type=radio name=host_$host value=dis checked></td>");
	} else {    #host is not currently disabled
	    $webpage->print("<td>$host</td>");
	    $webpage->print("<td $enable_command_bgcolor><input type=radio name=host_$host value=ena checked></td>");
	    $webpage->print("<td $disable_command_bgcolor><input type=radio name=host_$host value=dis></td>");
	}
	$webpage->print( "</tr>\n") ;
    }

    #############################################################
    # Print the services portion of the table
    #############################################################
    $webpage->print("<tr>");
    $webpage->print("<th>Services monitored on hostgroup \"<em>$group</em>\"<br><a href=\"$url?${monhost_and_port_args}command=moncgi_test_all&amp;args=$group\">(test all services on hostgroup <em>$group</em>)</a></th>");
    $webpage->print("<th>Enabled</th>");
    $webpage->print("<th>Disabled</th>");
    $webpage->print("</tr>\n");
    %op = &mon_list_opstatus;

    foreach $service (sort keys %{$op{$group}}) {     #begin service loop
	$s = \%{$op{$group}->{$service}};
	undef $bgcolor;
	if (${d{"services"}{$group}{$service}}) {    #service is disabled
	    $bgcolor = "$disabled_color";
	}
        $dis_checked = ( ${d{"services"}{$group}{$service}} ) ? "checked" : "";
        $ena_checked = (!${d{"services"}{$group}{$service}} ) ? "checked" : "";
        if ($s->{"opstatus"} == $OPSTAT{"ok"}) { #OK
	    $bgcolor = "$greenlight_color" unless $bgcolor;
	    $msg="(status: OK)";
	} elsif ($s->{"opstatus"} == $OPSTAT{"fail"}) {
	    unless ($bgcolor) {
		if ( $s->{"alerts_sent"} == 0 ) {
		    $bgcolor = "$yellowlight_color";
		    $msg=": $s->{'last_summary'}<br>(status: FAILED,NOALERTS)";
		} else {
		    $bgcolor = "$redlight_color";
		    $msg=": $s->{'last_summary'}<br>(status: FAILED)";
		}
		if ( $s->{'ackcomment'} ne "" ) {
                    $msg .= "(ACKED: $s->{'ackcomment'})";
                } else {
                    $msg .= "(no ack msg)";
                }
	    }
	} elsif ($s->{"opstatus"} == $OPSTAT{"untested"}) {
	    $bgcolor = "$unchecked_color" unless $bgcolor;
	    $msg="(status: UNTESTED)";
	}

	$webpage->print("<tr><td bgcolor=\"$bgcolor\"><a href=\"$url?${monhost_and_port_args}command=svc_details&amp;args=$group,$service\">$service</a> $msg <a href=\"$url?${monhost_and_port_args}command=list_dtlog&amp;args=$group,$service\"><br>&nbsp;&nbsp;&nbsp;&nbsp;(list downtime log for <em>$group:$service</em>)</a>") ;
	$webpage->print("<a href=\"$url?${monhost_and_port_args}command=mon_test_service&amp;args=$group,$service\"><br>&nbsp;&nbsp;&nbsp;&nbsp;(test service <em>$service</em> on group <em>$group</em> immediately)</a></td>") ;

	# Check whether the service is disabled or enabled
        $webpage->print("<td $enable_command_bgcolor><input type=radio name=svc_$service value=ena $ena_checked></td>");
	$webpage->print("<td $disable_command_bgcolor><input type=radio name=svc_$service value=dis $dis_checked></td>");
	$webpage->print("</tr>\n");
    }
    $webpage->print("<tr><td colspan=1 valign=top><center>");
    print $webpage->reset(-name=>'Cancel Changes');
    $webpage->print("</center></td>");
    $webpage->print("<td colspan=2><center>");
    print $webpage->submit(-name=>'Apply Changes');
    $webpage->print("</center></td></tr>");
    $webpage->print("</table>");
    print $webpage->end_form();
}


sub end_page {
    # End the document with a footer and contact info
    &print_bar;
    if ($monadmin ne "") {
	$webpage->print("<table width=100% border=0><tr><td align=left>For questions about this server,<br>contact <a href=\"mailto:$monadmin\">$monadmin</a></td><td align=right><i>mon.cgi v$VERSION</i></td></tr></table>");
    }
    print $webpage->end_html;
}


sub list_alerthist {
    # This function lists the alert history formatted in a table    
    my @l = &mon_list_alerthist ;
    my ($line, $localtime);
    my $table_width = "80%";

    $webpage->print("<table border=1 width=\"$table_width\" align=center>\n");

    $webpage->print("<tr><th>Group</th><th>Service</th>\n");
    $webpage->print("<th>Type</th><th>Time</th><th>Alert</th>\n");
    $webpage->print("<th>Args</th><th>Summary</th>\n");
    $webpage->print("</tr>\n");	

    foreach $line (reverse sort {$a->{"time"} <=> $b->{"time"}} (@l)) {
	# Only show the alert if we are allowed to see information
	# about this group.
	if ($show_watch_strict) {
	    next unless &can_show_group($line->{group});
	}

	$localtime = localtime ($line->{"time"});

	$webpage->print("<tr><td><a href=\"$url?${monhost_and_port_args}command=query_group&amp;");
	$webpage->print("args=$line->{group}\">$line->{group}</a></td>");

        $webpage->print("<td>$line->{service}</td>\n");
	$webpage->print("<td>$line->{type}</td>\n");
	$webpage->print("<td>$localtime</td>\n");

	$line->{"alert"} =~ s{^.*\/([^/]*)$}{$1};

	$webpage->print("<td>$line->{alert}</td>\n");

	my $args = "-";
	if ($line->{"args"} !~ /^\s*$/) {
	    $args = $line->{"args"};
	}

	$webpage->print("<td>$args</td>\n");
	$webpage->print("<td>$line->{summary}</td>");

	$webpage->print("</tr>\n");
    }

    $webpage->print("</table>\n");	
    print $webpage->hr;    
}



sub svc_details {
    # Lists details about a particular alert's status, regardless of
    # whether the alert is successful or not.
    # As of 1.40, this function has been expanded considerably, and
    # has also been given the benefit of additional verbiage from the
    # global variables %alert_vars, @time_based_alert_vars, and 
    # @pp_sec_alert_vars
    #
    my ($arg) = (@_);
    my ($group, $service) = split (/\,/, $arg);

    # Only show the rest of this page if we are allowed to see
    # information about this group.
    if ($show_watch_strict) {
        unless ( &can_show_group($group) ) {
            print $webpage->h3("You are not authorized to see detailed information for hostgroup '$group'.");
            print $webpage->h4("Please contact your system administrator for access.");
            return 0;
        }
    }

    my $status;
    my $retval;
    my (@pids, $server, $acknowledge_string, $name_string, $ackcomment_default);
    my (%op, $s, $g, $var, @time);
    my $table_width = "90%";            #let's give both tables the same width
    my $font_color;

    my %d = &mon_list_disabled;
    my %desc = &mon_list_descriptions;
    my $servertime = &mon_servertime;
    my @group_members = &mon_list_group($group) ;
    my $time_now = $servertime;
    my $enable_command_bgcolor = $auth_commands{'enable'}{'auth'} == 0 ? "bgcolor=\"$disabled_color\"" : "" ;
    my $disable_command_bgcolor = $auth_commands{'disable'}{'auth'} == 0 ? "bgcolor=\"$disabled_color\"" : "" ;
    my $test_command_bgcolor = $auth_commands{'test'}{'auth'} == 0 ? "bgcolor=\"$disabled_color\"" : "" ;
    my $ack_command_bgcolor = $auth_commands{'ack'}{'auth'} == 0 ? "bgcolor=\"$disabled_color\"" : "" ;
    my $disabled_hosts_string ;

    # Determine whether the service is failing or not
    # We'll be optimistic and assume it's NOT failing :)
    # Actually, unchecked services also show up as "ok".
    %op = &mon_list_successes;
    if ($op{$group}{$service}) {
	$status = "ok";
    } else {
	$status = "fail";
	%op = &mon_list_failures;
    }

    $webpage->print("<center>This page will reload every $reload_time seconds.<br></center>");
    print $webpage->hr;
    $webpage->print("<center>");
    if (${d{"services"}{$group}{$service}}) {    #service is disabled
	$webpage->print
	    ("<font size=+2 color=$disabled_color>Test detail for disabled service <i>$service</i> in group $group</font>&nbsp;\n");
    } elsif ($op{$group}{$service}{'opstatus'} == 1) { #OK
	$webpage->print
	    ("<font size=+2>Success detail for group <font color=$greenlight_color>$group</font>\n");
	$webpage->print
	    ("and service test <font size=+2 color=$greenlight_color><i>$service</i></font></font>&nbsp;");

    } elsif ($op{$group}{$service}{'opstatus'} == 7) {   # service is Untested
	$webpage->print
	    ("<font size=+2>Test detail for group <font color=$unchecked_color>$group</font> and service test <font color=$unchecked_color><i>$service</i></font></font>");
	$webpage->print
	    ("<br>(service is <font color=$unchecked_color>UNCHECKED!</font>)");
    } else {  # service is Failed (or some other opstatus code I don't know about)
	# If a service fails, print the detail and summary information
	# at the top. Yes, it's buried down in the middle of the page, but
	# it's important enough to take up screen real estate with and 
	# bring it to the top.
	$font_color = ($op{$group}{$service}{'alerts_sent'} == 0) ? $yellowlight_color : $redlight_color ;
	$webpage->print("<table width=\"$table_width\" border=0 align=center cellpadding=2 cellspacing=2>\n");
	$webpage->print("<tr><td colspan=2>");
    $webpage->print("<center>");
	$webpage->print
	    ("<font size=+2>Failure detail for group <font color=$font_color>$group</font> ");
	$webpage->print
	    ("and service test <font color=$font_color><i>$service</i></font></font><font size=+2>:</font> \n");
    $webpage->print("</center>");
	$webpage->print("</td></tr>");

	# Now print the detail and summary information for the failed service
	$op{$group}->{$service}->{'last_summary'} = "&lt;not specified&gt;" if $op{$group}->{$service}->{'last_summary'} eq "" ;
	$op{$group}->{$service}->{'last_detail'} = "&lt;not specified&gt;" if $op{$group}->{$service}->{'last_detail'} eq "" ;
	$op{$group}->{$service}->{'last_detail'} =~ s/\n/<BR>/g;
	$webpage->print("<tr><td width=25%><font size=+1 color=\"$font_color\">Failure summary</font>:</td><td>$op{$group}->{$service}->{'last_summary'}</td></tr>\n");
	$webpage->print("<tr><td width=25%><font size=+1 color=\"$font_color\">Failure detail</font>:</td><td>$op{$group}->{$service}->{'last_detail'}</td></tr>\n");
	$webpage->print("</table>");
    }

    # Issue warning if the whole group has been disabled. 
    if ( ${d{"watches"}{$group}} ) {
        $webpage->print ("<br><font size=+1>(NOTE: group </font> <font size=+1 color=$disabled_color>$group</font> <font size=+1> is disabled.)</font>");
    }

    # Issue warning if any hosts in the group are currently disabled.
    foreach (@group_members) {
        if ($_ =~ s/^\*//) {
	    $disabled_hosts_string = " <font size=+1 color=$disabled_color>$_</font>" . $disabled_hosts_string ;
	}
    }
    $disabled_hosts_string = "<br><font size=+1>(NOTE: The following host(s) in group <i>$group</i> are disabled: $disabled_hosts_string)" if $disabled_hosts_string ne "";
    $webpage->print ($disabled_hosts_string);

    # Check to see if a test for this service is currently running
    # and report back if it is (because the status might not have updated
    # yet...)
    @pids = &mon_list_pids;
    if (!defined(@pids)) {
	$webpage->print("<font size=+1>Unable to to determine whether this service is currently being tested (list_pids failed)!</font>\n");
    } else {
	shift @pids;   #discard server PID, we don't need it
	for (@pids) {
	    if ( ($_->{"watch"} eq $group) && ($_->{"service"} eq $service) ) {
		# we have a match, a monitor is currently running for 
		# this group and this service.
		$webpage->print("<br><font size=+1>NOTE: A monitor for this service is currently running as PID $_->{'pid'}. Results/opstatus codes might change when this test finishes!</font>\n");
	    }
	}
    }
    $webpage->print("<br><font size=+1><a href=\"$url?${monhost_and_port_args}command=svc_details&amp;args=$args\">Reload this page immediately.</a><br></font>");

    $webpage->print("</center>");
    print $webpage->br;
    $webpage->print("<table width=\"$table_width\" align=center border=1><tr>");
    $webpage->print
	("<td $test_command_bgcolor><font size=+1><a href=\"$url?${monhost_and_port_args}command=mon_test_service&amp;args=$group,$service\">Test service <em>$service</em> on group <em>$group</em> immediately</a></font></td>\n");

    if (${d{"services"}{$group}{$service}}) {
        #service is disabled, offer to enable
        $webpage->print("<td $enable_command_bgcolor><font size=+1><a href=\"$url?${monhost_and_port_args}command=mon_enable&amp;args=service,$group,$service&amp;rt=svc_details\">(ENABLE service <em>$service</em> in group <em>$group</em>)</a></font></td>\n");
    } else {
        #service is enabled, offer to disable
        $webpage->print("<td $disable_command_bgcolor><font size=+1><a href=\"$url?${monhost_and_port_args}command=mon_disable&amp;args=service,$group,$service&amp;rt=svc_details\">(DISABLE service <em>$service</em> in group <em>$group</em>)</a></font></td>\n");
    }
    $webpage->print
	("<td><font size=+1><a href=\"$url?${monhost_and_port_args}command=list_dtlog&amp;args=$group,$service\">List downtime log for service <em>$service</em> and group <em>$group</em></a></font></td>");

    $webpage->print("</tr>\n");
    $webpage->print("</table>\n");

    # If the service is in a failure state, offer to ack it.
    if ($status eq "fail") {
	$webpage->print("<table width=\"$table_width\" align=center border=0>");
	$webpage->print("<tr>");
	$webpage->print("<td $ack_command_bgcolor colspan=1 width=50%>");
	
	if ($op{$group}{$service}{'ack'} == 1) {
	    # Service has already been acked, offer to re-ack
	    $acknowledge_string = "<font size=+1><b>Re-acknowledge this failure:</b></font><br>(changes the acknowledgement message)<br>";
	    $ackcomment_default = "Was:\"$op{$group}{$service}{'ackcomment'}\"";
	} else {
	    # Service has not yet been acked, offer to ack
	    $acknowledge_string = "<font size=+1><b>Acknowledge this failure:</b></font><br>(disables all subsequent alerts for this failure period)<br>";
	    $ackcomment_default = "${name_string}";
	}
	$webpage->print("$acknowledge_string ");
	$webpage->print("</td>");
	$webpage->print("<td align=top>");
	# It is crucial that we reset the param value, otherwise the
	# value of the default will be ignored.
	print $webpage->startform(-action=>"$url");
	$webpage->param('ackcomment', $ackcomment_default);
        $webpage->param('h',"$monhost");
        print $webpage->hidden(-name=>'h');
        $webpage->param('p',"$monport");
        print $webpage->hidden(-name=>'p');

	print $webpage->textfield(-name=>'ackcomment',
				  -value=>"$ackcomment_default",
				  -size=>40,
				  );
# The textarea is nice, but you lose the ability to hit ENTER to
# submit your ack, which I really really like.
#	print $webpage->textarea(-name=>'ackcomment',
#				  -value=>"$ackcomment_default",
#				  -rows=>2,
#				  -wrap=>'soft',
#				  -columns=>40,
#				  );
	$webpage->print("&nbsp;&nbsp;");
	# We also have to reset this param value
	$webpage->param('command','mon_ack');
	print $webpage->hidden(-name=>'command',
			       );
	$webpage->param('args',"$group,$service");
	# We also have to reset this param value
	print $webpage->hidden(-name=>'args',
			       );
	print $webpage->submit(-name=>'ack');
	print $webpage->end_form();
	$webpage->print("</td></tr>\n");
	$webpage->print("</table>\n");
    }

    $webpage->print("<table width=\"$table_width\" border=1 align=center cellpadding=2 cellspacing=2>\n");
    $webpage->print("<tr><td align=left><font size=+2><b>Variable Description</b> (name)</font></td>\n");
    $webpage->print("<td align=left><font size=+2><b>Value</b></font></td></tr>\n");
    my $desc_string = ($desc{$group}{$service} ne "") ? "&quot;$desc{$group}{$service}&quot;" : "&lt;no description specified&gt;" ;
    $webpage->print("<tr><td align=left><font size=+1><b>Service Description</b></font></td><td>$desc_string</td></tr>\n");

    foreach $var (sort {$b cmp $a } (keys %{$op{$group}{$service}}) ) {
		# Special cases where we have a time formatted in secs 
		# since 1970, we'll make it look purty
		if (grep /^${var}$/, @time_based_alert_vars) {
	             # We need to check if the var is defined, since traps
	             # can throw us off.
	             if ( (!defined($op{$group}->{$service}->{$var})) || ($op{$group}->{$service}->{$var} == 0) ) {
			# The event has never occurred
	   	        $op{$group}->{$service}->{$var} = "Never" ;
		     } else {
			# Pretty-print the time
			@time = localtime ($op{$group}->{$service}->{$var});
			$_ = $op{$group}->{$service}->{$var};
			$op{$group}->{$service}->{$var} = sprintf ("%.2d:%.2d:%.2d, %s-%s-%s\n", @time[2, 1, 0, 3], @year_months[$time[4]], $time[5]+1900);
			# Also calculate the delta and pretty-print that
		        $op{$group}->{$service}->{$var} .= "(" . &pp_sec($time_now - $_) . " ago)";
		     }
		} elsif ($op{$group}->{$service}->{$var} eq "") {
		     # special case where value of $var is empty 
		     #(i.e. mon has never seen the service fail)
		     $op{$group}->{$service}->{$var} = "-";
		} elsif (grep /^${var}$/, @pp_sec_alert_vars) {
	             if ( (!defined($op{$group}->{$service}->{$var})) || ($op{$group}->{$service}->{$var} == 0) ) {
			# The event has never occurred
	   	        $op{$group}->{$service}->{$var} = "Never" ;
		     } else {
	                # Special case where time is a duration and 
	                # should be pretty printed.
	                $op{$group}->{$service}->{$var} = &pp_sec($op{$group}->{$service}->{$var});
                     }
                }
		$op{$group}->{$service}->{$var} =~ s/\n/<BR>/g;
		$webpage->print("<tr><td><font size=+1><b>$alert_vars{$var}</b> ($var)</font></td><td><font size=+1>$op{$group}->{$service}->{$var}</font></td></tr>\n");
    }

    $webpage->print("</table>\n");
    print $webpage->hr;
}



sub list_disabled {
    # This function lists all the disabled watches, services, and hosts
    # and returns the result as pretty(?) HTML
    my (%d, $group, $service, $host, $watch);
    my (@disabled_hosts, @disabled_svcs);
    my $enable_command_bgcolor = $auth_commands{'enable'}{'auth'} == 0 ? "bgcolor=\"$disabled_color\"" : $BGCOLOR ;

    %d = &mon_list_disabled;

    print $webpage->hr;

    $webpage->print("<center>\n");
    # Start the form and set up our defaults
    print $webpage->startform(-action=>"$url");
    $webpage->param('command','mon_state_change_enable_only');
    print $webpage->hidden(-name=>'command',
			   );
    $webpage->param('h',"$monhost");
    print $webpage->hidden(-name=>'h');
    $webpage->param('p',"$monport");
    print $webpage->hidden(-name=>'p');

    $webpage->print("<table border=1>\n");
    $webpage->print( "<tr>");
    $webpage->print("<td colspan=1><h2>Disabled Watches</h2></td>");
    $webpage->print("<td><h3>Enable?</h3></td>");
    $webpage->print( "</tr>\n");
    $webpage->print( "<tr>");
    if ( scalar(keys %{$d{"watches"}}) > 0 ) {
	for (keys %{$d{"watches"}}) {
	    $webpage->print("<td colspan=1><font size=+1>$_</font></td>");
	    $webpage->print("<td $enable_command_bgcolor><input TYPE=\"checkbox\" VALUE=\"$_\" NAME=enagroup_$_></td></tr>\n");
	}
    } else {
	$webpage->print("<td colspan=2><center><font size=+1><b>&lt;NONE&gt;</b></font></center></td></tr>\n");
    }

    #
    # Disabled hosts portion of table
    #
    $webpage->print("<tr>");
    $webpage->print("<td colspan=1><h2>Disabled Hosts</h2></td>");
    $webpage->print("<td><h3>Enable?</h3></td>");
    $webpage->print( "</tr>\n");
    foreach $group (keys %{$d{"hosts"}}) {
	foreach $host (keys %{$d{"hosts"}{$group}}) {
	    push(@disabled_hosts,"<tr><td><font size=+1>$group:$host</font></td>");
	    push(@disabled_hosts,"<td $enable_command_bgcolor><input TYPE=\"checkbox\" VALUE=\"$host\" NAME=enahost_$host></td></tr>");
	}
    }
    if (scalar(@disabled_hosts) > 0 ) {
	print join("\n", @disabled_hosts);
    } else {
	$webpage->print("<tr>");
	$webpage->print("<td colspan=2><center><font size=+1><b>&lt;NONE&gt;</b></font></center></td>");
	$webpage->print("</tr>\n");
    }


    #
    # Disabled services portion of table
    #
    $webpage->print("<tr>");
    $webpage->print("<td><h2>Disabled Services</h2></td>");
    $webpage->print("<td><h3>Enable?</h3></td>");
    $webpage->print("</tr>\n");
    foreach $watch (keys %{$d{"services"}}) {
	foreach $service (keys %{$d{"services"}{$watch}}) {
	    push(@disabled_svcs, "<tr><td><font size=+1>$watch:$service</font></td>");
	    push(@disabled_svcs,"<td $enable_command_bgcolor><input TYPE=\"checkbox\" VALUE=\"$watch,$service\" NAME=enasvc_${watch}_$service></td></tr>");
	}
    }
    if (scalar(@disabled_svcs) > 0 ) {
	print join("\n", @disabled_svcs);
    } else {
	$webpage->print("<tr><td colspan=2><center><font size=+1><b>&lt;NONE&gt;</b></font></center></td></tr>\n");
    }

    $webpage->print("<tr><td colspan=1 valign=top><center>");
    print $webpage->reset(-name=>'Cancel Changes');
    $webpage->print("</center></td>");
    $webpage->print("<td colspan=1><center>");
    print $webpage->submit(-name=>'Apply Changes');
    $webpage->print("</center></td></tr>\n");

    $webpage->print("</table>\n");
    print $webpage->end_form();
    $webpage->print("</center>\n");
}



sub list_dtlog {
    # Accepts the following arguments, all of which are optional:
    # (group,service,sortby,first log entry to show, last log entry to show)
    # to sort by.
    #
    # Default sort key is failtime. 
    #
    # If {service,group} is null, shows detail about all failures 
    # for the given {group,service}.
    #
    # Default first log entry to show is 1.
    #
    # Default last log entry to show is 1+$dtlog_max_failures_per_page.
    #
    # No arguments means show all service failures for all groups, 
    # sorted by failtime.
    #
    # Someday it would be nice to take args like time ranges, etc., but
    # that capability should really be built into Mon itself since it
    # is such a useful feature and something which could leverage a lot
    # of mon's timeperiod work as well.
    #
    # Original patch by Martha H Greenberg <marthag@mit.edu>
    #
    my ($arg) = (@_);
    my ($group, $service,$sortby,$dtlog_begin,$dtlog_end);
    if ( defined($arg) ) {
	($group, $service,$sortby,$dtlog_begin,$dtlog_end) = split (/\,/, $arg) ;
    } else {
	$group = "";
	$service = "";
	$sortby = "" ;
	$dtlog_begin = "";
	$dtlog_end = "";
    }

    $dtlog_begin = 1 unless ( ($dtlog_begin) && ($dtlog_begin > 0) );
    $dtlog_end = ($dtlog_begin + $dtlog_max_failures_per_page - 1) unless ( ($dtlog_end) && ($dtlog_end > 0) );
    $sortby = "failtime" unless ($sortby);
    my $face = $sans_serif_font_face;
    my $summary_table_width = "80%";
    my $dt_table_width = "100%";
    my $i;
    # This has keeps track of the sortby keys and what 
    # their descriptions map to.
    my %sortby_key = ("group" => "Group",
		      "service" => "Service",
		      "failtime" => "Service Failure Begin Time",
		      "timeup" => "Service Failure End Time",
		      "downtime" => "Total Observed Failure Time",
		      "interval" => "Testing Interval",
		      "summary" => "Summary",
		      );

    print $webpage->hr;
    my ($line, $localtimeup, $localfailtime, $ppdowntime, $ppinterval);

    my ($first_failure_time, $total_failures, $mtbf, $mean_recovery_time, $median_recovery_time, $std_dev_recovery_time, $min_recovery_time, $max_recovery_time, @l) = &mon_list_dtlog($group, $service) ;
    my ($ppfft, $ppmtbf, $ppmean_recovery_time, $ppmedian_recovery_time, $ppmin_recovery_time, $ppmax_recovery_time, $ppstd_dev_recovery_time);

    # Estimated uptime calculation
    my $time_now = time;
    my $approx_uptime_pct = ( ( ($time_now - $first_failure_time + $mtbf ) > 0) && ( ($time_now - $first_failure_time + $mtbf - scalar(@l) * $mean_recovery_time > 0 ) ) ) ? sprintf("%.2f%", ( ( ($time_now - $first_failure_time + $mtbf) - (scalar(@l) * $mean_recovery_time) ) / ($time_now - $first_failure_time + $mtbf) ) * 100 ) : "&lt;not applicable&gt;";

    $webpage->print("<table border=1 align=center width=\"$summary_table_width\">\n");
    $webpage->print("<tr>\n");
    $webpage->print("<td colspan=2 align=center><font size=+1 face=\"$face\">\n");
    $webpage->print("Downtime Summary For Hostgroup ");
    if ($group eq "") {
	$webpage->print("<b>&lt;any&gt;</b>");
    } else {
	$webpage->print("<b>&quot;$group&quot;</b>");
    }
    $webpage->print(" and Service ");
    if ($service eq "") {
	$webpage->print("<b>&lt;any&gt;</b>");
    } else {
	$webpage->print("<b>&quot;$service&quot;</b>");
    }
    $webpage->print("</font></td>\n");
    $webpage->print("</tr>\n");
    $webpage->print("<tr>\n");
    $ppfft = $first_failure_time;
    my @fftime = localtime ($first_failure_time);
    $ppfft = sprintf ("%s, %s %d, %.2d at %.2d:%.2d:%.2d", @days_of_week[$fftime[6]], @year_months[$fftime[4]], $fftime[3], $fftime[5] + 1900 , @fftime[2,1,0] );
    $webpage->print("<td>Log begins at:</td>\n<td>$ppfft</td>\n");
    $webpage->print("</tr>\n");
    $webpage->print("<tr>");
    $webpage->print("<td>Total observed service failures:</td>\n<td>$total_failures</td>\n");
    $webpage->print("</tr>\n");
    $webpage->print("<tr>");
    $webpage->print("<td>Mean time between service failures:</td>\n");
    $ppmtbf = &pp_sec($mtbf);
    $webpage->print("<td>$ppmtbf</td>\n"); 
    $webpage->print("</tr>\n");
    $webpage->print("<tr>");
    $webpage->print("<td>Mean observed service failure time:</td>\n");
    $ppmean_recovery_time = &pp_sec($mean_recovery_time);
    $webpage->print("<td>$ppmean_recovery_time</td>\n");
    $webpage->print("</tr>\n");
    $webpage->print("<tr>");
    $webpage->print("<td>Median observed service failure time:</td>\n");
    $ppmedian_recovery_time = &pp_sec($median_recovery_time);
    $webpage->print("<td>$ppmedian_recovery_time</td>\n");
    $webpage->print("</tr>\n");
    $webpage->print("<tr>");
    $webpage->print("<td>Standard deviation of observed service failure times:</td>\n");
    $ppstd_dev_recovery_time = &pp_sec($std_dev_recovery_time);
    $webpage->print("<td>$ppstd_dev_recovery_time</td>\n");
    $webpage->print("</tr>\n");
    $webpage->print("<tr>");
    $webpage->print("<td>Minimum observed service failure time:</td>\n");
    $ppmin_recovery_time = &pp_sec($min_recovery_time);
    $webpage->print("<td>$ppmin_recovery_time</td>\n");
    $webpage->print("</tr>\n");
    $webpage->print("<tr>");
    $webpage->print("<td>Maximum observed service failure time:</td>\n");
    $ppmax_recovery_time = &pp_sec($max_recovery_time);
    $webpage->print("<td>$ppmax_recovery_time</td>\n");
    $webpage->print("</tr>\n");
    $webpage->print("<tr>");
    $webpage->print("<td><i>Approximate</i> percentage of time in failure-free operation:</td>\n");
    $webpage->print("<td>$approx_uptime_pct</td>\n");
    $webpage->print("</tr>\n");
    $webpage->print("</table>\n");

    return 0 if scalar(@l) == 0;   # stop if we returned no downtime events

    ($dtlog_begin, $dtlog_end) = &moncgi_list_dtlog_navtable ($url, $group, $service, $sortby, $dtlog_begin, $dtlog_end, $total_failures, scalar(@l), %sortby_key) ;

    # Start printing the actual downtime log table.
    # Print the header as a table with a thicker border
    $webpage->print("<table border=1 width=\"$dt_table_width\" align=center>\n");
    $webpage->print("<tr><th><font size=+1>Entry</font></th>\n");
    $webpage->print("<th><font size=+1><a href=\"$url?${monhost_and_port_args}command=list_dtlog&amp;args=$group,$service,group,$dtlog_begin,$dtlog_end\">$sortby_key{\"group\"}</a></font></th>\n");
    $webpage->print("<th><font size=+1><a href=\"$url?${monhost_and_port_args}command=list_dtlog&amp;args=$group,$service,service,$dtlog_begin,$dtlog_end\">$sortby_key{\"service\"}</a></font></th>\n");
    $webpage->print("<th><font size=+1><a href=\"$url?${monhost_and_port_args}command=list_dtlog&amp;args=$group,$service,failtime,$dtlog_begin,$dtlog_end\">$sortby_key{\"failtime\"}</a></font></th>\n");
    $webpage->print("<th><font size=+1><a href=\"$url?${monhost_and_port_args}command=list_dtlog&amp;args=$group,$service,timeup,$dtlog_begin,$dtlog_end\">$sortby_key{\"timeup\"}</a></font></th>\n");

    $webpage->print("<th><font size=+1><a href=\"$url?${monhost_and_port_args}command=list_dtlog&amp;args=$group,$service,downtime,$dtlog_begin,$dtlog_end\">$sortby_key{\"downtime\"}</a></font></th>\n");
    $webpage->print("<th><font size=+1><a href=\"$url?${monhost_and_port_args}command=list_dtlog&amp;args=$group,$service,interval,$dtlog_begin,$dtlog_end\">$sortby_key{\"interval\"}</a></font></th>\n");
    $webpage->print("<th><font size=+1><a href=\"$url?${monhost_and_port_args}command=list_dtlog&amp;args=$group,$service,summary,$dtlog_begin,$dtlog_end\">$sortby_key{\"summary\"}</a></font></th>\n");
    $webpage->print("</tr>\n");

    # default sort order is "failtime", so no need to resort
    if ($sortby ne "failtime") {
	# do a forward-alphanumeric or reverse-numeric sort, 
	# depending on the sortby parameter
	if ( 
	     ($sortby eq "group") || 
	     ($sortby eq "service") || 
	     ($sortby eq "summary") 
	     ) {
	    @l = (sort {$a->{"$sortby"} cmp $b->{"$sortby"}}(@l));
	} else {
	    @l = (reverse sort {$a->{"$sortby"} <=> $b->{"$sortby"}}(@l));
	}
    }

    # Now print the rows of the downtime table
    for ( $i = $dtlog_begin ; $i <= $dtlog_end ; $i++ ) {
	$line = $l[$i-1];
	$webpage->print("<tr><td>$i</td>");
	$webpage->print("<td><a href=\"$url?${monhost_and_port_args}command=list_dtlog&amp;args=$line->{\"group\"}\">");
	$webpage->print("<font face=\"$face\">$line->{\"group\"}</font></a></td>");
        $webpage->print("<td><a href=\"$url?${monhost_and_port_args}command=list_dtlog&amp;args=,$line->{\"group\"},$line->{\"service\"}\">");
	$webpage->print("<font face=\"$face\">$line->{\"service\"}</font></a></td>\n");
	
	$localfailtime = localtime ($line->{"failtime"});

	$webpage->print("<td>$localfailtime</td>\n");

	$localtimeup = localtime ($line->{"timeup"});
	$webpage->print("<td>$localtimeup</td>\n");
	
	$ppdowntime = &pp_sec ($line->{"downtime"});
	$webpage->print("<td>$ppdowntime</td>\n");
        $ppinterval = &pp_sec ($line->{"interval"});
	$webpage->print("<td>$ppinterval</td>\n");
	$webpage->print("<td>$line->{\"summary\"}</td>");
	
	$webpage->print("</tr>\n");
    }

    $webpage->print("</table>\n");
    &moncgi_list_dtlog_navtable ($url, $group, $service, $sortby, $dtlog_begin, $dtlog_end, $total_failures, scalar(@l), %sortby_key) ;

    print $webpage->hr;
    undef @l;
}


sub list_pids {
    my $retval;
    my @pids = &mon_list_pids ;

    print $webpage->hr;
    print $webpage->h2("List of mon PID's:");

    $webpage->print("Unable to list PID's on server!<br>\n") if !defined(@pids);
    my $server = shift @pids;

    $webpage->print ("<font size=+0>Server PID is $server</font><br><br>\n");
    if ( scalar(@pids) > 0 ) {
	$webpage->print("PID's of currently active monitors:<br>\n");
	$webpage->print("<br><table border=1><tr><th>Hostgroup</th><th>Service</th><th>PID</th></tr>\n");
	for (@pids) {
	    $webpage->print (join ("",
			"<tr><td>",
			$_->{"watch"},
			"</td><td>",
			$_->{"service"},
			"</td><td>",
			$_->{"pid"},
			"</td></tr>\n",
			));
	}
	$webpage->print("</table>\n");
    } else {
	$webpage->print("<font size=+1>&lt;No monitors are running at this time&gt;</font><br>\n");
    }
}


###############################################################
# Mon-specific functions. These all have the common feature
# that they connect to a Mon server and retrieve some data.
# Generally these functions are called by the Presentation functions,
# or if they are called directly they do no special output
# formatting.
###############################################################

sub mon_connect {
    # Performs the basic connection, and if necessary, authentication,
    # to a mon server.
    # If successful, returns a 1
    # If unsuccessful because of login failure, returns -1
    # If unsuccessful because of other reasons, returns 0
    my $retval;

    #
    # If we're not connected, we need to connect and possibly authenticate
    #
    if ( (! defined($c->connected()) ) || ( $c->connected() == 0 ) ) {
	$c->connect();
	if ($c->error) {
	    $retval = $c->error;
	    print "<font face=\"$fixed_font_face\">mon_connect: Could not contact mon server &quot;$monhost&quot;: $retval </font>\n" if $connect_failed == 0 ;
	    $connect_failed = 1;    #set the global $connect_failed var
	    return 0;
	}
	
	#
	# Test to see if login is required, and if so,
	# set the username and password.
	#
	if ($must_login) {
	    #print "<pre>Login is &quot;$loginhash{\"username\"}&quot; and passwordis &quot;$loginhash{\"password\"}&quot;\n</pre>";
	    #
	    # Test to see if username and password are blank.
	    # If so, then use the default username/password.
	    #
	    if (
		( ( ! defined($loginhash{"username"}) ) && 
		  ( ! defined($loginhash{"password"}) )
		  ) ||
		( ( $loginhash{"username"} eq "" ) && 
		  ( $loginhash{"password"} eq "" )
		  )
		) {
		# Login is required but no username/password was given, so
		# try the login and password to the default account
		$loginhash{"username"} = $default_username ;
		$loginhash{"password"} = $default_password ;
	    }	
	    $c->login(%loginhash);
	    #print "connected as user $loginhash{'username'}\n";  #DEBUG
	}
    }

    if ( ($must_login) && 
	 ( defined($c->error) ) && 
	 ( 
	   ($c->error =~ /530 login unsuccessful/) ||
	   ($c->error =~ /no password/) || 
	   ($c->error =~ /no username/)
	   )
	 ) {
	# Login was required and unsuccessful, present the authform
	# if it hasn't already been presented. Since some presentation
	# functions call multiple methods you could very easily
	# end up with multiple prompts, which is confusing to the 
	# user.
	&moncgi_authform ($command,"$args") unless $has_prompted_for_auth;
	$has_prompted_for_auth = 1;
	return -1;
    }
    
    return 1;
}


sub mon_list_group {
    # List all the hosts in a given group. Returns an array of hosts
    # if successful, or undef if failure.
    my ($group) = (@_);
    my (@hosts, $retval);

    my $conn = &mon_connect ;
    return 0 if $conn == 0;
    
    @hosts = $c->list_group ($group);
    
    unless ($c->error) {
	return @hosts ;
    } else {
	$retval = $c->error;
	$webpage->print ("<font face=\"$fixed_font_face\">Could not list groups on mon server &quot;$monhost&quot;: $retval</font>");
	return undef;
    }
}


sub mon_list_watch {
    # List all the watches. Returns an array of defined watch groups and
    # services.
    # if successful, or undef if failure.
    my ($group) = (@_);
    my (@hosts, $retval);

    my $conn = &mon_connect ;
    return 0 if $conn == 0;
    
    @hosts = $c->list_watch ($group);
    
    unless ($c->error) {
	return @hosts ;
    } else {
	$retval = $c->error;
	$webpage->print ("<font face=\"$fixed_font_face\">Could not list watches on mon server &quot;$monhost&quot;: $retval</font>");
	return undef;
    }
}


sub mon_list_failures {
    # This function returns a hash of failures.
    my (%op, $retval);

    my $conn = &mon_connect ;
    return 0 if $conn == 0;

    %op = $c->list_failures();

    if ($c->error) {
	$retval = $c->error;
    	print "<font face=\"$fixed_font_face\">Could not execute list failures command mon server on server &quot;$monhost&quot;: $retval (perhaps you don't have permissions in auth.cf?)</font>\n";
	&moncgi_switch_user($retval);
    } else {
	#print "<pre>list_failures command executed successfully</pre>\n";
    }

    return %op;
}


sub mon_list_successes {
    # This function returns a hash of successes
    my (%op, $retval);

    my $conn = &mon_connect ;
    return 0 if $conn == 0;

    %op = $c->list_successes();

    if ($c->error) {
	$retval = $c->error;
    	print "<font face=\"$fixed_font_face\">Could not execute list successes command on server &quot;$monhost&quot;: $retval (perhaps you don't have permissions in auth.cf?)</font>\n";
	&moncgi_switch_user($retval);
    }
    return %op;
}


sub mon_list_opstatus {
    # This function returns a hash of opstatus
    # It should accept an optional anonymous array argument, of
    # [group, service ...] to only return
    # the opstatus of the group/service pairs you are interested in.
    #
    # But it doesn't because I am lazy and don't need this feature 
    # right now :)
    #my ($criteria) = @_;
    my (%op, $retval);

    my $conn = &mon_connect ;
    return 0 if $conn == 0;

    %op = $c->list_opstatus();

    if ($c->error) {
	$retval = $c->error;
    	print "<font face=\"$fixed_font_face\">Could not execute list opstatus command on server &quot;$monhost&quot;:<br> $retval (perhaps you don't have permissions in auth.cf?)</font>\n";
	&moncgi_switch_user($retval);
    }
    return %op;
}


sub mon_list_disabled {
    # This function lists all the disabled watches, services, and hosts
    # and returns the result as a hash
    my (%d, $retval);

    my $conn = &mon_connect ;
    return 0 if $conn == 0;

    %d = $c->list_disabled();

    if ($c->error) {
	$retval = $c->error;
    	print "<font face=\"$fixed_font_face\">Could not execute list disabled command mon server on server &quot;$monhost&quot;:<br> $retval (perhaps you don't have permissions in auth.cf?)</font>\n";
	&moncgi_switch_user($retval);
    } else {
	#print "<pre>list_disabled command executed successfully</pre>\n";
    }
    
    return %d;

}


sub mon_reload {
    # Reload mon config file.
    # Right now the only option supported is to reload the auth.cf file.
    #
    my ($what) = (@_);
    print $webpage->hr;
    print $webpage->h2("Reloading mon...");
    my $retval;

    my $conn = &mon_connect ;
    return 0 if $conn == 0;

    $retval = $c->reload($what);

    if ($c->error) {
	$retval = $c->error;
    	print "<font face=\"$fixed_font_face\">Could not reload &quot;$what&quot; mon server on server &quot;$monhost&quot;:<br> $retval (perhaps you don't have permissions in auth.cf?)</font>\n";
	&moncgi_switch_user($retval);
    } else {
	print "<font face=\"$fixed_font_face\">mon server on &quot;$monhost&quot; successfully reloaded.</font>\n";
    }


}



sub mon_loadstate {
    # A simple wrapper function that calls mon_loadstate_savestate with
    # the proper arguments.
    my ($state) = (@_);
    $state = "disabled" if $state eq "";
    print $webpage->hr;
    print $webpage->h2("Loading saved state for $state...");
    &mon_loadstate_savestate("load",$state);
}


sub mon_savestate {
    # A simple wrapper function that calls mon_loadstate_savestate with
    # the proper arguments.
    my ($state) = (@_);
    $state = "disabled" if $state eq "";
    print $webpage->hr;
    print $webpage->h2("Saving current state for $state...");
    &mon_loadstate_savestate("save",$state);
}


sub mon_loadstate_savestate {
    # Loads or saves state of a mon object specifed by $target. Currently
    # the only object supported by mon for loading/saving state is the
    # state of the scheduler, so using this function with $target="" will
    # load or save the state of the scheduler.
    #
    # The load/save action is specified by the variable $action
    my ($action, $state) = (@_);
    my $retval;

    my $conn = &mon_connect ;
    return 0 if $conn == 0;

    if ($action eq "save") {
	($retval = $c->savestate($state)) || ($retval = $c->error);
    }
    elsif ($action eq "load") {
	($retval = $c->loadstate($state)) || ($retval = $c->error);
    }

    if ($c->error ne "") {
	print "<font face=\"$fixed_font_face\">Could not $action state mon server for state &quot;$state&quot; on server &quot;$monhost&quot;:<br> $retval (perhaps you don't have permissions in auth.cf?)</font>\n";
	&moncgi_switch_user($retval);
    } else {
	print "<font face=\"$fixed_font_face\">$action state succeded on mon server &quot;$monhost&quot;.</font>\n";
    }

}


# Stop or start scheduler  ---------------------------------------------
sub mon_schedctl {
    # Either stops or starts the scheduler, depending on how it was called,
    # either with the "stop" argument or the "start" argument.
    # No return value.
    my ($action) = (@_);
    print $webpage->hr;
    print $webpage->h2("MON: $action scheduler...");
    my $retval;

    my $conn = &mon_connect ;
    return 0 if $conn == 0;

    if ($action eq "stop") {
	$retval = $c->stop();
    } elsif ($action eq "start") {
	$retval = $c->start();
    }
    if ($c->error) {
	$retval = $c->error;
    	print "<font face=\"$fixed_font_face\">Could not $action mon server on server &quot;$monhost&quot;:<br> $retval (perhaps you don't have permissions in auth.cf?)</font>\n";
	&moncgi_switch_user($retval);
    } else {
	print "<font face=\"$fixed_font_face\">$action scheduler on mon server on &quot;$monhost&quot; succeeded.</font>\n";
    }

}


sub mon_list_pids {
    my $retval;
    my @pids;

    my $conn = &mon_connect ; #test
    return 0 if $conn == 0;

    @pids = $c->list_pids;
#    my $server = shift @pids;

    if ($c->error) {
	$retval = $c->error;
    	print "<font face=\"$fixed_font_face\">Could not list pids on mon server &quot;$monhost&quot;: $retval (perhaps you don't have permissions in auth.cf?)</font>\n";
	&moncgi_switch_user($retval);
	return undef;
    } else {
	return @pids;
    }

}


sub mon_list_descriptions {
    # This subroutine executes the list_descriptions() routine and,
    # if successful, returns a hash of service descriptions, indexed
    # by watch and service. Returns undef on failure.
    #
    my $retval;
    my %desc;

    my $conn = &mon_connect ;
    return 0 if $conn == 0;

    %desc = $c->list_descriptions;

    if ($c->error) {
	$retval = $c->error;
    	print "<font face=\"$fixed_font_face\">Could not list descriptions on mon server &quot;$monhost&quot;:<br> $retval (perhaps you don't have permissions in auth.cf?)</font>\n";
	&moncgi_switch_user($retval);
	return undef;
    } else {
	return %desc;
    }
}


# Enable a disabled host/watch/service ----------------------------------
sub mon_enable {
    my ($arg) = (@_);
    my ($type, $arg1, $arg2) = split (/\,/, $arg);
    print $webpage->h2("Enabling service...");
    my $retval;

    # Only show the rest of this page if we are allowed to see
    # information about this group.
    if ( ($show_watch_strict) && ( ! $type eq "host") ) {
        unless ( &can_show_group($arg1) ) {
            print $webpage->h3("You are not authorized to see detailed information for hostgroup '$arg1'.");
            print $webpage->h4("Please contact your system administrator for access.");
            return 0;
        }
    }

    my $conn = &mon_connect ;
    return 0 if $conn == 0;

    if ($type eq "service") {
	$retval = $c->enable_service($arg1, $arg2);
    } elsif ($type eq "host") {
	$retval = $c->enable_host($arg1);
    } elsif ($type eq "watch") {
	$retval = $c->enable_watch($arg1);
    }

    if ($c->error) {
	$retval = $c->error;
    	print "<font face=\"$fixed_font_face\">Could not successfully execute command enable_${type} with arguments &quot;$arg1&quot; and &quot;$arg2&quot; on server &quot;$monhost&quot;:<br> $retval (perhaps you don't have permissions in auth.cf?)</font>\n";
	&moncgi_switch_user($retval);
	return 0;
    } else {
	print "<font face=\"$fixed_font_face\">enable_${type} succeeded for ";
	    if ($type eq "service") {
		print "<br>watch $arg1, service $arg2";
	    } elsif ($type eq "host") {
		print "<br>host $arg1";
	    } elsif ($type eq "watch") {
		print "<br>watch $arg1";
	    }
	print "</font>\n";
    }
    return 1;
}

# Disable an enabled service ----------------------------------------------
sub mon_disable {
    my ($arg) = (@_);
    my ($type, $arg1, $arg2) = split (/\,/, $arg);
    print $webpage->h2("Disabling service...");
    my $retval;

    # Only show the rest of this page if we are allowed to see
    # information about this group.
    if ( ($show_watch_strict) && ( ! $type eq "host") ) {
        unless ( &can_show_group($arg1) ) {
            print $webpage->h3("You are not authorized to see detailed information for hostgroup '$arg1'.");
            print $webpage->h4("Please contact your system administrator for access.");
            return 0;
        }
    }
    
    my $conn = &mon_connect ;
    return 0 if $conn == 0;

    if ($type eq "service") {
	$retval = $c->disable_service($arg1, $arg2);
    } elsif ($type eq "host") {
	$retval = $c->disable_host($arg1);
    } elsif ($type eq "watch") {
	$retval = $c->disable_watch($arg1);
    }

    if ($c->error) {
	$retval = $c->error;
    	print "<font face=\"$fixed_font_face\">Could not successfully execute command disable_${type} with arguments &quot;$arg1&quot; and &quot;$arg2&quot; on server &quot;$monhost&quot;:<br> $retval (perhaps you don't have permissions in auth.cf?)</font>\n";
	&moncgi_switch_user($retval);
    } else {
	print "<font face=\"$fixed_font_face\">disable_${type} succeeded for ";
	    if ($type eq "service") {
		print "<br>watch $arg1, service $arg2";
	    } elsif ($type eq "host") {
		print "<br>host $arg1";
	    } elsif ($type eq "watch") {
		print "<br>watch $arg1";
	    }
	print "</font>\n";
    }

}


sub mon_test_service {
    # Test a service immediately.
    # Accepts as arguments a group and a service, and optionally an
    # test argument, which can be either alert, upalert, or startupalert.
    # Default test is "alert"
    my ($arg) = (@_);
    my ($group, $service,$test) = split (/\,/, $arg);

    # Only show the rest of this page if we are allowed to see
    # information about this group.
    if ($show_watch_strict) {
        unless ( &can_show_group($group) ) {
            print $webpage->h3("You are not authorized to see detailed information for hostgroup '$group'.");
            print $webpage->h4("Please contact your system administrator for access.");
            return 0;
        }
    }

    $test = "monitor" if $test eq "";
    print $webpage->h2("Performing $test test on service $service in hostgroup $group...");
    my $retval;
    
    my $conn = &mon_connect ;
    return 0 if $conn == 0;

    $retval = $c->test($test, $group, $service);

    if ($c->error) {
	$retval = $c->error;
    	print "<font face=\"$fixed_font_face\">Could not successfully execute command &quot;$test&quot; test service &quot;$service&quot; on hostgroup &quot;$group&quot; on server &quot;$monhost&quot;: $retval (perhaps you don't have permissions in auth.cf?)</font>\n";
	&moncgi_switch_user($retval);
    } else {
	print "<font face=\"$fixed_font_face\">test $test completed for service $service and hostgroup $group:<br><br><br>";
	print "&nbsp;$retval</font>\n";
    }

}


sub mon_test_config {
    # Test the mon config file immediately.
    # Takes no argument (there is only one config file after all)
    #
    print $webpage->h2("Testing the syntax of your mon config file...");
    my $retval;

    my $conn = &mon_connect ;
    return 0 if $conn == 0;

    my @s = $c->test_config;

    if ($c->error) {
	$retval = $c->error;
	if ( $retval !~ /^520 test config completed/ ) { # command not authorized
	    print "<font face=\"$fixed_font_face\">Could not successfully execute command &quot;test config&quot; on server &quot;$monhost&quot;:<br>$retval (perhaps you don't have permissions in auth.cf?)</font>\n";
	    &moncgi_switch_user($retval);	    
	} elsif ( (defined ($s[0])) && ($s[0] == 0) ) {  # there are config file errors
	    $webpage->print("Error in config file found:<br><pre>" . $s[1] . "\n\n</pre>");
	    $webpage->print("Please note that you may have other errors in your configuration file, but the checking stops after the first one is found.<br>");
	} else {   # some other error occurred
	    print "<font face=\"$fixed_font_face\">Could not successfully execute command &quot;test config&quot; on server &quot;$monhost&quot;:<br>$retval (perhaps you don't have permissions in auth.cf?)</font>\n";
	    &moncgi_switch_user($retval);
	}
    } else {
	$webpage->print("<font face=\"$fixed_font_face\">Test config completed OK, no errors were found in your config file<br><br>\n");
    }

}


# Reset  mon  ----------------------------------------------------
sub mon_reset {
    ($args) = (@_);
    print $webpage->hr;
    print $webpage->h2("Reset mon...");
    my $retval;

    my $conn = &mon_connect ;
    return 0 if $conn == 0;

    if ( $args eq "keepstate" ) {
	# specify we want to keep the scheduler state
	$retval = $c->reset($args);
    } else {
	# reset scheduler state, don't give reset any arguments
	$retval = $c->reset();
    }

    if ($c->error) {
	$retval = $c->error;
    	$webpage->print 
	    ("<font face=\"$fixed_font_face\">Could not reset mon server on server &quot;$monhost&quot;: $retval (perhaps you don't have permissions in auth.cf?)</font>\n");
	&moncgi_switch_user($retval);
    } else {
	$webpage->print ("<font face=\"$fixed_font_face\">mon server on &quot;$monhost&quot; successfully reset.<br><br>");
	if ( $args eq "keepstate" ) {
	    $webpage->print ("Scheduler state was NOT reset.<br><br>All previously disabled hosts/groups/services are still disabled."); 
	} else {
	    $webpage->print ("Scheduler state was reset.<br><br>All hosts/groups/services are now enabled."); 
	}
	$webpage->print ("</font>\n");
    }
}



# List alert history --------------------------------------------------
sub mon_list_alerthist {
    print $webpage->hr;
    print $webpage->h2("Alert History:");
    my $retval ;

    my $conn = &mon_connect ;
    return 0 if $conn == 0;

    my @l = $c->list_alerthist();

    if ($c->error) {
	$retval = $c->error;
    	print "<font face=\"$fixed_font_face\">Could not list alert history on mon server &quot;$monhost&quot;: $retval (perhaps you don't have permissions in auth.cf?)</font>\n";
	&moncgi_switch_user($retval);
    } else {
	#print "<pre>alert history on on &quot;$monhost&quot; successfully retrieved.</pre>\n";
    }

    return @l;
}


sub mon_list_sched_state {
    # This function returns an array, @scheduler_state, which 
    # contains the state of the scheduler. This  is not exactly 
    # documented, but @scheduler_state[0]==0 seems to indicate 
    # that the scheduler is stopped and @scheduler_state[1]
    # seems to hold the time (in epoch seconds) since the scheduler was
    # stopped.
    my (@scheduler_state, $retval);

    my $conn = &mon_connect ;
    return 0 if $conn == 0;

    @scheduler_state = $c->list_state();

    if ($c->error) {
	$retval = $c->error;
    	print "<font face=\"$fixed_font_face\">Could not execute list state command mon server on server &quot;$monhost&quot;: $retval (perhaps you don't have permissions in auth.cf?)</font>\n";
	&moncgi_switch_user($retval);
    } else {
	#print "<pre>list state command executed successfully</pre>\n";
    }

    return @scheduler_state;

}


sub mon_list_dtlog {
    # Lists the downtime log (all of it) and returns the results as
    # an array of hash references.
    my ($group, $service) = (@_);
    my $retval ;
    my (@ltmp, @l, $line);
    my (@recovery_times);
    my ($first_failure_time, $mtbf, $mean_recovery_time, $median_recovery_time, $std_dev_recovery_time, $max_recovery_time, $min_recovery_time);
    my $max_recovery_time_default = -1;  #some arbitrary number less than 0
    my $min_recovery_time_default = 9999999999999;  #some arbitrary really big number

    my $conn = &mon_connect ;
    return 0 if $conn == 0 ;

    @ltmp = $c->list_dtlog();

    if ($c->error) {
      $retval = $c->error;
      $webpage->print("<font face=\"$fixed_font_face\">Could not list downtime log on mon server &quot;$monhost&quot;: $retval (perhaps you don't have permissions in auth.cf?)</font>\n");
      &moncgi_switch_user($retval);
      return undef;
    }

    my $time_now = time;
    $max_recovery_time = $max_recovery_time_default;                     # initialize this to something really small
    $min_recovery_time = $min_recovery_time_default;          # initialize this to something really big
    $first_failure_time = $time_now;
    #
    # Loop through all downtimes, get first downtime, min and max, 
    # and filter based on criteria/specifications.
    #
    foreach $line (reverse sort {$a->{"failtime"} <=> $b->{"failtime"}}(@ltmp)){
	#
	# Test to see if this is the first failure time.
	#
	if ($line->{"failtime"} < $first_failure_time) {
	    # since this list is already sorted, this will only be true
	    # the very first time we go thru this loop
	    $first_failure_time = $line->{"failtime"} if $line->{"failtime"} < $first_failure_time ;
	}

	#
	# Skip this line if a group and/or service param was
	# specified and the param doesn't match.
	#
	if ( ( defined($group) ) &&
	     ($group ne "") && 
	     ($group ne $line->{"group"})
	     ) {
	    next;
	}
	if ( ( defined($service) ) &&
	     ($service ne "") && 
	     ($service ne $line->{"service"})
	     ) {
	    next;
	}

	#
	# Only show this downtime log entry if we are allowed to see
	# information about this group. This is probably slow but
	# no one said security was efficient!
	#
	if ($show_watch_strict) {
	    unless ( &can_show_group($line->{"group"}) ) {
		# This line should not be shown to the user
		next;
	    }
	}

	#
	# Add this downtime to the list of downtimes 
	# for statistical calculation purposes.
	#
	push(@l, $line);
	push(@recovery_times, $line->{"downtime"});

	#
	# set min and max downtimes
	#
	$min_recovery_time = $line->{"downtime"} if $line->{"downtime"} < $min_recovery_time;
	$max_recovery_time = $line->{"downtime"} if $line->{"downtime"} > $max_recovery_time;
    }

    undef @ltmp; #we don't need @ltmp's memory anymore
    #
    # Calculate mean recovery time
    #
    $mean_recovery_time = &arithmetic_mean(@recovery_times);
    #
    # also calculate median recovery time
    #
    $median_recovery_time = &median(@recovery_times);
    #
    # calculate the mean time between failures as:
    # (total elapsed time since first failure + E(time until first failure))/(total # of failures)
    #
    $mtbf = (scalar(@recovery_times) == 0) ? 0 : ($time_now - $first_failure_time + (($time_now - $first_failure_time) / scalar(@recovery_times))) / scalar(@recovery_times);
    #
    # Calculate std deviation of failure times
    #
    $std_dev_recovery_time = &std_dev(@recovery_times);
    #
    # In case $max_recovery_time and $min_recovery_time are unset 
    # (i.e. there were no failures), set them to sensible defaults.
    #
    $max_recovery_time = 0 if $max_recovery_time == $max_recovery_time_default;
    $min_recovery_time = 0 if $min_recovery_time == $min_recovery_time_default;

    return $first_failure_time, scalar(@recovery_times), $mtbf, $mean_recovery_time, $median_recovery_time, $std_dev_recovery_time, $min_recovery_time, $max_recovery_time,  @l ;
}


sub mon_ack {
    # This subroutine takes a comma separated list of a group and a service
    # as input.
    # It relies on the global "$ackcomment" for its text.
    #
    # If the user is authenticated as anyone other than the default
    # user, mon_ack inserts their name into the ack comment.
    #
    # mon_ack sends an acknowledgement to the mon server for the given 
    # service on the host, the effect of which is to disable any further
    # alerts for the current failure period. 
    # Ack'ing a service that is not in a failure state will produce the
    # following error:
    # "520 service is in a non-failure state"
    #
    # We get around this by only presenting the option to ack for 
    # services that are currently in a failure state.
    #
    # This function does not return any values.
    my ($args)  = @_;
    my ($group, $service) = split (/\,/, $args);

    # Only show the rest of this page if we are allowed to see
    # information about this group.
    if ($show_watch_strict) {
        unless ( &can_show_group($group) ) {
            print $webpage->h3("You are not authorized to see detailed information for hostgroup '$group'.");
            print $webpage->h4("Please contact your system administrator for access.");
            return 0;
        }
    }

    my $retval ;
    my $conn = &mon_connect ;
    return 0 if $conn == 0 ;
    my $name_string = ( ($loginhash{"username"} eq $default_username) || ($loginhash{"username"} eq "") ) ? "" : "[$loginhash{'username'}]: ";


    # Ack the service w/comment
    $retval = $c->ack($group, $service, "${name_string}${ackcomment}");

    if ($c->error) {
	$retval = $c->error;
	$webpage->print("<font face=\"$fixed_font_face\">mon_ack: Could not ack service \"$service\" in group \"$group\" on mon server &quot;$monhost&quot;: $retval (perhaps you don't have permissions in auth.cf?)</font>\n");
	&moncgi_switch_user($retval);
    } else {
	$webpage->print("<font face=\"$fixed_font_face\">Service \"$service\" in group \"$group\" acknowledged successfully.</font>");
    }
}



sub mon_servertime {
    # This subroutine calls the Mon::Client::servertime function and
    # returns the time as a scalar, or undef if there is an error.
    my $retval;
    my $servertime;

    my $conn = &mon_connect ;
    return 0 if $conn == 0;

    $servertime = $c->servertime;

    if ($c->error) {
	$retval = $c->error;
    	print "<font face=\"$fixed_font_face\">Could not get server time on mon server &quot;$monhost&quot;: $retval (perhaps you don't have permissions in auth.cf?)</font>\n";
	&moncgi_switch_user($retval);
	return undef;
    } else {
	return $servertime;
    }
}


sub mon_checkauth {
    # This subroutine checks the authorization for a given command
    # to see if it is authorized by the server.
    # Returns: 
    #  -1 if a connection with the server cannot be made
    #   0 if the command is authorized, 
    #   1 if the command is not
    # authorized, and returns the error string if checkauth fails
    # (which really shouldn't happen unless a Mon server isn't running)
    my ($cmd)  = @_;
    my $retval ;
    my $conn = &mon_connect ;
    return 0 if $conn == 0 ;
    return -1 if $conn == -1 ;

    $retval = $c->checkauth($cmd);
    if ($retval == 0) {
	# command not authorized
	$retval = 0;
    } elsif ($retval == 1) {
	# command authorized
	$retval = 1;
    } else {
	# This command should not fail unless a mon server is not running
	$retval = $c->error;
	$webpage->print("<font face=\"$fixed_font_face\">mon_checkauth: Could not check auth for \"$cmd\" on mon server &quot;$monhost&quot;: $retval</font>\n");
#	&moncgi_switch_user($retval);
    }

    return $retval;
}



sub mon_state_change_enable_only {
    # This is called only by list_disabled, and wraps mon_state_change
    # because mon_state_change assumes only one group and this can 
    # span multiple groups (although the command is enable only, which
    # simplifies things some).
    my ($group, $param);
    my @groups = &mon_list_watch ;
    foreach $param ( keys(%cgiparams) ) {
	# For each matching action, try to enable or else exit
	# in case of an authentication failure (this makes us
	# keep our CGi variables so that when we do authenticate,
	# all of our actions are executed).
	if ($param =~ /^enagroup_/) {
	    &mon_enable("watch,$cgiparams{$param}") || return undef;
	} elsif ($param =~ /^enahost_/) {
	    &mon_enable("host,$cgiparams{$param}") || return undef;
	} elsif ($param =~ /^enasvc_/) {
	    &mon_enable("service,$cgiparams{$param}") || return undef;
	}
    }
    &list_disabled;
}


sub mon_state_change {
    # This function changes one or more of the states of the hostgroup
    # given as an argument. It uses the global value %cgiparam to know
    # what else (hosts and/or services) to modify.
    my ($group, %hosts, $host, %op, $service);
    $group = $cgiparams{'group'};
    my %d = &mon_list_disabled ;

    # List the state of the group

    if (!defined $group) {
	$webpage->print("Invalid host group \"$group\"\n");
	return undef;
    }

    # Disable/enable group, if that was requested
    if ( ( defined ($cgiparams{"group_$group"}) ) &&
	 ( $cgiparams{"group_$group"} eq "ena" )
	 ) {
	# Enable group if the group is already disabled
	if ( ${d{"watches"}{$group}} ) {
	     &mon_enable("watch,$group") || return 0;
	 }
    } elsif  ( ( defined ($cgiparams{"group_$group"}) ) &&
	 ( $cgiparams{"group_$group"} eq "dis" )
	 ) {
	# Disable group if the group is already enabled
	if ( ! ${d{"watches"}{$group}} ) {
	     &mon_disable("watch,$group") || return 0;
	 }
    }


    @_ = &mon_list_group($group) ;

    # List each member of the group, check to see if there is something
    # defined for the group.
    # If so, then change the state if that is required.
    # Don't make a state change if one is not required.
    foreach $host (@_) {
	# Hosts are disabled if they begin with an asterisk
	# (this is mon's convention, not mine)
	#print STDERR "Host is $host\n";  #DEBUG
	if  ($host =~ m/^\*/) {
	    # Host is disabled, check to see if we should try and re-enable
	    $host =~ s/^\*//;
	    if ( 
		 ( defined($cgiparams{"host_$host"}) ) && 
		 ( $cgiparams{"host_$host"} eq "ena") 
		 ) {
		     # Try to enable and stop if we can't.
		     &mon_enable("host,$host") || return 0;
	    }
	} else {
	    # Host is enabled, check to see if we should try and disable
	    if ( 
		 ( defined($cgiparams{"host_$host"}) ) && 
		 ( $cgiparams{"host_$host"} eq "dis") 
		 ) {
		     # Try to disable and stop if we can't.
		     &mon_disable("host,$host") || return 0;
	    }
	}
    }
    
    # Check each service on the host to see if its state 
    # needs to change.
    %op = &mon_list_opstatus;
    foreach $service (sort keys %{ $op{$group} }) {
	if (
	    ( defined($cgiparams{"svc_$service"}) ) &&
	    ( $cgiparams{"svc_$service"} eq "dis")
	    ) {
		if (! ${d{"services"}{$group}{$service}}) {    #service is enabled
		    # Try to enable and stop if we 
		    # can't (i.e. no permissions)
	            &mon_disable("service,$group,$service") || return 0;
		}
	} elsif (
		     ( defined($cgiparams{"svc_$service"}) ) &&
		     ( $cgiparams{"svc_$service"} eq "ena")
		     ) {
		if (${d{"services"}{$group}{$service}}) {    #service is disabled
		    # Try to enable and stop if we 
		    # can't (i.e. no permissions)
		    &mon_enable("service,$group,$service") || return 0;
		}
        }
    }
    &query_group($group);
}



###############################################################
# Mon.cgi-specific functions
# The moncgi_* fuctions generally do not manipulate Mon in any
#  way or present any Mon output to the user.
# The moncgi_* functions will each generally call one or more
#  mon_* functions.
###############################################################

# Get the params from the form -----------------------------------------
sub moncgi_get_params {
    my (@names, $name, $monhost_not_null, $monport_not_null);

    #
    # First get params we know about and expect to get.
    #
    $command = $webpage->param('command');
    $args = $webpage->param('args');
    $rt = $webpage->param('rt');   # return to value for pages 
                                   # which need to keep state info about
                                   # which page called them.
    $rtargs = $webpage->param('rtargs');   #args for $rt
    $ackcomment = $webpage->param('ackcomment');   #ackcomment
    
    #
    # For the login form, grab username and password.
    #
    $loginhash{'username'} = $webpage->param('username');
    $loginhash{'password'} = $webpage->param('password');
    
    #
    # Now get any more parameters which we may have defined.
    #
    @names = $webpage->param;
    foreach $name (@names) {
	$cgiparams{$name} = $webpage->param($name);
    }


    $monhost_not_null = 1 if defined($cgiparams{"h"}) &&  $cgiparams{"h"} ne "";
    $monport_not_null = 1 if defined($cgiparams{"p"}) &&  $cgiparams{"p"} ne "";

    #
    # Allow user to override values of monhost and monport with
    #  CGI params.
    #
    # Untaint monhost and monport, first remove bogus characters,
    # then "officially" untaint them using $1
    #
    if ( defined($monhost_not_null) ) {
#	print STDERR "Monhost is defined as '$cgiparams{'h'}'\n"; #DEBUG
	$monhost = $cgiparams{"h"} ;
	$monhost =~ s/[^\w.-]//g;
	$monhost =~ /(.*)/; 
	$monhost = $1;
    }

    if ( defined($monport_not_null) ) {
#	print STDERR "Monport is defined as '$cgiparams{'p'}'\n"; #DEBUG
	$monport = $cgiparams{"p"} ;
	$monport =~ s/[^\d]//g;
	$monport =~ /(.*)/;
	$monport = $1;
    }

    #
    # If the user gave either a host or port argument that may (or
    # may not) override the hard-coded value, we need to preserve
    # this value and encode it in all future URL's that we 
    # generate, so that the value will be preserved when the 
    # mon.cgi page auto-reloads. We also undef $has_read_config, 
    # for mod_perl namespace purposes (scenario: instance 1
    # of mon.cgi is invoked with a h= parameter, instance 2 is not,
    # the instance 2 will eventually pick up instance 1's h= 
    # parameter.
    #
    #
    if ( ( defined($monhost_not_null) ) || ( defined($monport_not_null) ) ) {
	#print STDERR "Monhost is defined as '$cgiparams{'h'}' (h=$monhost)\n"; #DEBUG
	#print STDERR "Monport is defined as '$cgiparams{'p'}' (p=$monport)\n"; #DEBUG
	#
	# The META tag doesn't respect &amp; for some reason, so
	# we define another variable.
	# At least under Navigator 4.x, this is true.
	#
	$monhost_and_port_args_meta = "h=$monhost&p=$monport&";
	$monhost_and_port_args = "h=$monhost&amp;p=$monport&amp;";
	undef $has_read_config ;
    } else { #user did not enter in either monhost or monport args
	#print STDERR "Monport ('$monport_not_null':'$cgiparams{'p'}') and monhost('$monhost_not_null':'$cgiparams{'h'}') are undefined.\n"; #DEBUG
	#undef $monhost_and_port_args_meta;
	#undef $monhost_and_port_args;
	$monhost_and_port_args_meta = "";
	$monhost_and_port_args = "";
    }
}


sub moncgi_logout {
    # This subroutine provides the written evidence to the user
    # that they have been logged out of the mon server. The actual
    # logging out is done in the setup_page() routine, when the
    # auth cookie is destroyed in accordance to the value of the 
    # global variable $destroy_auth_cookie
    print $webpage->hr;
    print $webpage->h3("User <i>$loginhash{'username'}</i> has been logged off.<br>");
    print $webpage->h3("You will need to re-authenticate to perform further privileged actions.");
}


#
# This subroutine presents the authentication form to the user,
# and then runs the command the user was trying to execute with
# the new, improved level of privilege.
#
# This subroutine is usually called because a user tried to
# do something that they aren't authorized to do.
#
# The special command name "moncgi_login" is given when the user
# wants to log in without actually doing anything that requires
# privs.
#
sub moncgi_authform {
    my ($command, $args) = (@_);
    print $webpage->startform(-method=>'POST',
			      );
    $webpage->print("<center>");
    print $webpage->hr;

    #
    # Test to see if the command was the special command
    # "moncgi_login".
    #
    if ($command eq "moncgi_login") {
	$command = "query_opstatus";
	print $webpage->h3("Please enter your mon username and password below.<br>");
    } else {
	print $webpage->h3("You must authenticate as a user of sufficient privilege to perform this command.<br>");
    }

    #
    # Start the table.
    #
    $webpage->print("<table border=0>\n");
    $webpage->print("<tr>\n");
    $webpage->print("<tr>\n");
    $webpage->print("<td><b>MON username:</b></td>\n");
    $webpage->print("<td>");
    print $webpage->textfield(-name=>'username',
				   -size=>8,
				   -maxlength=>100,
				   );
    $webpage->print("</td>");
    $webpage->print("</tr>\n");
    $webpage->print("<tr>\n");
    $webpage->print("<td><b>MON password:</b></td>\n");
    $webpage->print("<td>");
    # Reset the passwd param so it's always blank before 
    # printing out the password field.
    $webpage->param('password',"");
    print $webpage->password_field(-name=>'password',
				   -size=>8,
				   -value=>"",
				   -maxlength=>100,
				   );
    $webpage->print("</td>");
    $webpage->print("</tr>\n");
    $webpage->print("<tr>");
    $webpage->print("<td colspan=2 align=center>");
    print $webpage->submit(-name=>'Login',
			   );
    $webpage->print("</td>");
    $webpage->print("</tr>");
    $webpage->print("</table>\n");
    $webpage->print("<center>");

    print $webpage->br;
    # if this works correctly, the command will be re-executed with 
    # the credentials the user just entered
    $webpage->param('command', $command);
    $webpage->param('args', $args);
    $webpage->param('ackcomment', $ackcomment);

    # Now pass on the rest of the CGI params as hidden 
    # fields if there are any params passed to the form.
    foreach (keys (%cgiparams) ) {
	print $webpage->hidden(-name=>"$_",
			       -value=>"$cgiparams{$_}",
			       );
    }
    print $webpage->end_form;

}    


# Generic button function ---------------------------------------------
# Not strictly necessary, but could be useful if you wished to disable
# certain features of the client or add new ones in a test capacity.
sub moncgi_generic_button {
    my ($title, $command) = (@_);

    print $webpage->hr;
    print $webpage->h2("$title");
    $webpage->print ("(command $command not implemented in this client)\n");
    print $webpage->hr;
}


sub moncgi_switch_user {
    # This subroutine is called after a command fails because a user
    # is authenticated as a user without sufficient permission to perform
    # the requested command, so we give the user a chance to re-authenticate
    # as someone of sufficient privilege.
    my ($retval) = (@_) ;
    if ( ($must_login) && ($retval =~ /520 command could not be executed/) ) {
        # User doesn't have permission to perform command
        &moncgi_authform ($command,"$args") unless $has_prompted_for_auth;
        $has_prompted_for_auth = 1;
    }
}


#
# This subroutine just prints out the legend table explaining what 
# colors mean what. I broke it out as a separate function so I 
# could experiment with its location (top or bottom of table).
#
# Inputs: Width of table (e.g. "70%")
# Outputs: always returns 1
sub moncgi_print_service_table_legend {
    my ($service_table_width) = (@_);

    # Old way to draw table
    if (1 == 0 ) {
	$webpage->print("<table align=center border=1 width=\"$service_table_width\">");
	$webpage->print
	    ("<tr><td><font color=$TEXTCOLOR>Service color legend:</font></td>\n");
	$webpage->print("<td><font color=$unchecked_color>Unchecked</font></td>\n");
	$webpage->print("<td><font color=$greenlight_color>Good</font></td>\n ");
	$webpage->print("<td><font color=$yellowlight_color>Failed<br>(no alerts sent)</font></td>\n");
	$webpage->print("<td><font color=$redlight_color>Failed<br>(alerts sent)</font></td>\n");
	$webpage->print("<td><font color=$disabled_color>Disabled</font></td>\n");
	$webpage->print("</tr></table>");
    }
    
    # New way to draw table
    $webpage->print("<a name=\"legend\"></a>");
    $webpage->print("<table align=center border=1 width=\"$service_table_width\">");
    $webpage->print
	("<tr><td rowspan=2><font size=+1 color=$TEXTCOLOR>Service color legend:</font><br><a href=\"$url#opstatus_tbl\">(top of table)</a></td>\n");
    $webpage->print("<td><font>Unchecked</font></td>\n");
    $webpage->print("<td><font>Good</font></td>");
    $webpage->print("<td><font>Failed<br>(no alerts sent)</font></td>");
    $webpage->print("<td><font>Failed<br>(alerts sent)</font></td>");
    $webpage->print("<td><font>Disabled</font></td>");
    $webpage->print("</tr>\n");
    $webpage->print("<tr>");
    $webpage->print("<td bgcolor=$unchecked_color><font color=$unchecked_color>$unchecked_color</font></td>");
    $webpage->print("<td bgcolor=$greenlight_color><font color=$greenlight_color>$greenlight_color</font></td>");
    $webpage->print("<td bgcolor=$yellowlight_color><font color=$yellowlight_color>$yellowlight_color</font></td>");
    $webpage->print("<td bgcolor=$redlight_color><font color=$redlight_color>$redlight_color</font></td>");
    $webpage->print("<td bgcolor=$disabled_color><font color=$disabled_color>$disabled_color</font></td>");

    $webpage->print("</tr></table>\n");


    return 1;
}


sub moncgi_list_dtlog_navtable {
    # This function is called by list_dtlog. It takes as arguments 
    # the following: ($url, $group, $service, $sortby, $dtlog_begin, 
    # $dtlog_end, $total_failures, $num_events, %sortby_key).
    #
    # This function doesn't print any downtime log information per 
    # se. It just prints out navigation for the user to browse the 
    # downtime log.
    #
    # This function prints out a table allowing the user to navigate 
    # between the previous N downtime log entries and the next N downtime
    # log entries, where N is a number we derive based on what the range
    # the user asked for, what the maximum entries per page to show is, 
    # and the total number of failures observed.
    #
    # The reason it's a separate function is that we want to have the
    # footer placed at the top and the bottom of the downtime log 
    # table, so we're calling it twice.
    my ($url, $group, $service, $sortby, $dtlog_begin, $dtlog_end, $total_failures, $num_events, %sortby_key) = (@_);
    my ($next_matches_lower, $next_matches_upper, $prev_matches_lower, $prev_matches_upper);

    return ($dtlog_begin, $dtlog_end) if $num_events == 0;   # stop if we returned no downtime events

    # Lower bound on which failures to show as next
    # min($dtlog_end + 1, $total_failures
    $next_matches_lower = ($total_failures < $dtlog_end + 1) ? $total_failures : $dtlog_end + 1;
    # Upper bound on which failures to show as next
    # min($next_matches_lower + $dtlog_max_failures_per_page - 1, $total_failures)
    $next_matches_upper = ( $total_failures < ($next_matches_lower + $dtlog_max_failures_per_page - 1) ) ? $total_failures : ($next_matches_lower + $dtlog_max_failures_per_page - 1) ;
    # now reset $dtlog_end in case we were handed a bogus end point
    $dtlog_end = $next_matches_upper if ($dtlog_end > $num_events);
    # now reset $dtlog_begin in case we were handed a bogus begin point
    $dtlog_begin = $dtlog_end if $dtlog_begin > $num_events;
    # Lower bound on which failures to show as prev
    # max(1, $dtlog_begin  - $dtlog_max_failures_per_page)
    $prev_matches_lower = ($dtlog_begin  -  $dtlog_max_failures_per_page > 0) ? ($dtlog_begin  -  $dtlog_max_failures_per_page ) : 1 ;

    #$webpage->print("total_failures=$total_failures, dtlog_begin=$dtlog_begin, dtlog_end=$dtlog_end, prev_matches_lower=$prev_matches_lower, next_matches_upper = $next_matches_upper, next_matches_lower = $next_matches_lower\n"); #DEBUG


    # Start printing the "show previous, show next" table
    $webpage->print("<br><table border=0 width=100%><tr><td width=17% align=left>\n");
    # Only give the option to show previous entries if there are previous
    # entries to show.
    if ( 
	 ($prev_matches_lower > 0) && 
	 ($dtlog_begin > 1) 
	 )  {
	# in the case where ($dtlog_begin - $dtlog_max_failures_per_page)
	# (e.g. we are currently showing entry 9-23 and want to display 1-8)
	if (
	    ( $dtlog_begin > 1) && 
	    ($dtlog_begin - $dtlog_max_failures_per_page < 0) 
	    ) {
	    $prev_matches_lower = 1;
	}
	# Needs to be min($dtlog_begin -1, $total_failures)
	$prev_matches_upper = ($total_failures < $dtlog_begin - 1) ? $total_failures : $dtlog_begin - 1;
	printf("<a href=\"%s?%scommand=list_dtlog&amp;args=%s,%s,%s,%d,%d\">" , $url, ${monhost_and_port_args}, $group, $service, $sortby, $prev_matches_lower, $prev_matches_upper );
	printf("See events %d-%d</a>\n" , $prev_matches_lower, $prev_matches_upper) ;
    }

    # Print the current entries being shown
    $webpage->print("</td><td width=66% align=center><font size=+1><b>Displaying downtime events $dtlog_begin-$dtlog_end of $total_failures<br>(sorting by $sortby_key{$sortby})</b></font></td><td width=17% align=right>");

    # Only give the option to show subsequent entries if there are subsequent
    # entries to show.
    if (
	 ($next_matches_upper <= $total_failures) && 
	 ($dtlog_end < $total_failures) 
	 ) {
	printf("<a href=\"%s?%scommand=list_dtlog&amp;args=%s,%s,%s,%d,%d\">", $url, ${monhost_and_port_args}, $group, $service, $sortby, $next_matches_lower , $next_matches_upper );
	printf("See events %d-%d</a>\n", $next_matches_lower , $next_matches_upper) ;
    }

    $webpage->print("</td></tr></table><br>\n");
    # It is possible for these values to be changed in this routine,
    # so send back the values to the calling routine.
    return ($dtlog_begin, $dtlog_end);
}


sub moncgi_test_all {
    # Tests all services for a particular hostgroup
    #
    # Inputs: group name
    # Outputs: void
    #
    my ($group) = (@_);

    # Only show the rest of this page if we are allowed to see
    # information about this group.
    if ($show_watch_strict) {
        unless ( &can_show_group($group) ) {
            print $webpage->h3("You are not authorized to see detailed information for hostgroup '$group'.");
            print $webpage->h4("Please contact your system administrator for access.");
            return 0;
        }
    }

    my (%s, $service);

    my $conn = &mon_connect;
    return 0 if $conn == 0;

    %s = &mon_list_opstatus;

    if ( ! &mon_checkauth("test") ) {
	#command is unauthorized
	&moncgi_switch_user("520 command could not be executed");
	return 0;
    } 

    foreach $service (keys %{$s{$group}}) {
	&mon_test_service("$group,$service");
    }

    return 1;
}


#
# This subroutine presents a table for the user to reset keepstate
# or to reset without keepstate. To do nothing is also an option.
#
sub moncgi_reset {
    my $reset_command_bgcolor = $auth_commands{'reset'}{'auth'} == 0 ? "bgcolor=\"$disabled_color\"" : $BGCOLOR ;
    $webpage->print("<br><br><table border=1 cellpadding=5 cellspacing=5>");
    $webpage->print("<tr><td $reset_command_bgcolor><a href=\"$url?${monhost_and_port_args}command=mon_reset&amp;args=keepstate\">Reset mon server, <b>keep scheduler state</b></a></td><td><p>This clears the state of the scheduler, re-reads the config file, and keeps all watches/hosts/services in their current disabled/enabled state.</p><p>You usually want to use this method of resetting the server.</p></td></tr>");
    $webpage->print("<tr><td $reset_command_bgcolor><a href=\"$url?${monhost_and_port_args}command=mon_reset\">Reset mon server, <b>reset scheduler state</b></a></td><td><p>This clears the state of the scheduler, re-reads the config file, and sets all watches/hosts/services to ENABLED.</p><p>You only want to use this option if you're sure you want to re-enable all groups/hosts/services!</p></td></tr>");
    $webpage->print("<tr><td colspan=2 align=center><a href=\"$url?${monhost_and_port_args}command=query_opstatus\">Do nothing and return to the main status screen</a></td></tr>");
    $webpage->print("</table><br><br>");

    return 1;

}


#
# This subroutine reads and parses the optional mon.cgi config file,
# and alters global variable values accordingly.
#
# Inputs: config filename to read
#
# Outputs: 1      if up-to-date config file has been read
#          0      if config file contains errors.
#          undef  if up-to-date config file was not read (file not found)
#
sub moncgi_read_cf {
    my ($cf_file) = (@_) ;
    my ($newcf_file_mtime, $key, $val);
    #
    # Test that config file can be read, and if it can, check to see
    # if we've already read it.
    #
    if(-r $cf_file) {
	# First we check if we have ever read a config file. This
	# is controlled by the global variable $has_read_config
	# If so, then we check to see if the copy we have read is 
	# the latest copy.
	# If not, then we try to read the config file.
	if ($has_read_config) {
	    #
	    # Since we've already read a config file at least once,
	    # we now check to see if we need to read it again.
	    # We re-read the config file if the mtime of the config 
	    # file is different (older OR newer) than the last config
	    # file we read.
	    #
	    $newcf_file_mtime = (stat($cf_file))[9];
	    if ($newcf_file_mtime == $cf_file_mtime) {
		#print STDERR "Skipping config read ($newcf_file_mtime == $cf_file_mtime)\n"; #DEBUG
		return 1;
	    } else {
		#
		# Record the new mtime
		#
		#print STDERR "Re-reading config ($newcf_file_mtime == $cf_file_mtime)\n"; #DEBUG
		$cf_file_mtime = $newcf_file_mtime;
	    }
	} else {
	    #
	    # We've never read the config before, so we get the
	    # initial config file mtime.
	    #
	    $cf_file_mtime = (stat($cf_file))[9];
	}
    } else {
	print STDERR "mon.cgi: moncgi_read_cf: Unable to open config file '$cf_file' for reading: $!\n";
	return undef;
    }

    #
    # Start reading config file
    #
    if ( open (CF , "$cf_file") ) {
	while (<CF>) {
	    chomp;
	    # Skip blank lines and comment lines
	    next if /^\s*\#/;
	    next if /^\s*$/;
	    # Strip off extra blank space at beg. and end of each line
	    s/^\s*//; s/\s*$//;

	    #
	    # Parse config file lines
	    #
	    if (/^(\w+) \s* = \s* (.*) \s*$/ix) {
		$key = $1;
		$val = $2;
		#
		# Trivially untaint $key and $val.
		# We'll do the "real" untainting within the
		# config file parsing, later.
		#
		$key =~ /(.*)/;
		$key = $1;
		$val =~ /(.*)/;
		$val = $1;

		#
		# Look for matching key/value pairs and assign them
		# to the proper variable. Complain if a key/value
		# pair doesn't match.
		#
		if ($key eq "organization") {
		    $organization = $val;
		} elsif ($key eq "monadmin") {
		    $monadmin = $val;
		} elsif ($key eq "logo") {
		    $logo = $val ;
		} elsif ($key eq "logo_link") {
		    $logo_link = $val ;
		} elsif ($key eq "reload_time") {
		    if ($val <= 0) {
			print STDERR "mon.cgi: moncgi_read_cf: $cf_file: dtlog_max_failures_per_page must be a number > 0\n";
			return 0;
		    }
		    $reload_time = $val;
		} elsif ($key eq "monhost") {
		    # strip out all non-valid chars for taint purposes
		    $val =~ s/[^\d\w.-]//g;
		    $monhost = $val;
		} elsif ($key eq "monport") {
		    # strip out all non-digits for taint purposes
		    $val =~ s/[^\d]//g;
		    if ($val <= 0) {
			print STDERR "mon.cgi: moncgi_read_cf: $cf_file: monport must be a number > 0\n";
			return 0;
		    }
		    $monport = $val;
		} elsif ($key eq "must_login") {
		    $must_login = $val;
		} elsif ($key eq "app_secret") {
		    $app_secret = $val;
		} elsif ($key eq "default_username") {
		    $default_username = $val;
		} elsif ($key eq "default_password") {
		    $default_password = $val;
		} elsif ($key eq "login_expire_time") {
		    if ($val <= 0) {
			print STDERR "mon.cgi: moncgi_read_cf: $cf_file: login_expire_time must be a number > 0\n";
			return 0;
		    }
		    $login_expire_time = $val;
		} elsif ($key eq "cookie_name") {
		    $cookie_name = $val;
		} elsif ($key eq "cookie_path") {
		    $cookie_path = $val;
		} elsif ($key eq "fixed_font_face") {
		    $fixed_font_face = $val;
		} elsif ($key eq "sans_serif_font_face") {
		    $sans_serif_font_face = $val;
		} elsif ($key eq "BGCOLOR") {
		    $BGCOLOR = $val;
		} elsif ($key eq "TEXTCOLOR") {
		    $TEXTCOLOR = $val;
		} elsif ($key eq "LINKCOLOR") {
		    $LINKCOLOR = $val;
		} elsif ($key eq "VLINKCOLOR") {
		    $VLINKCOLOR = $val;
		} elsif ($key eq "greenlight_color") {
		    $greenlight_color = $val;
		} elsif ($key eq "redlight_color") {
		    $redlight_color = $val;
		} elsif ($key eq "yellowlight_color") {
		    $yellowlight_color = $val;
		} elsif ($key eq "unchecked_color") {
		    $unchecked_color = $val;
		} elsif ($key eq "dtlog_max_failures_per_page") {
		    if ($val <= 0) {
			print STDERR "mon.cgi: moncgi_read_cf: $cf_file: dtlog_max_failures_per_page must be a number > 0\n";
			return 0;
		    }
		    $dtlog_max_failures_per_page = $val;
		} elsif ($key eq "untaint_ack_msgs") {
		    $untaint_ack_msgs = $val;
		} elsif ($key eq "watch") {
		    push(@show_watch, $val);
		} elsif ($key eq "show_watch_strict") {
		    $show_watch_strict = $val;
		} else {
		    print STDERR "mon.cgi: moncgi_read_cf: Unknown key-value pair in config file $cf_file: '$key = $val'\n";
		    return 0;
		}
	    } else {
		print STDERR "mon.cgi: moncgi_read_cf: Unparseable config file line in config file '$cf_file': $_\n";
		return 0;
	    }
	}
    } else {
	print STDERR "mon.cgi: moncgi_read_cf: Unable to open config file '$cf_file' for reading: $!\n";
	return undef;
    }

    #
    # If we've gotten this far, it means the config file was 
    # successfully parsed.
    #

    #
    # Set the global variable that indicates that we have read the 
    # config file.
    #
    $has_read_config = 1;
    #print STDERR "Read the config file!\n"; #DEBUG

    return 1;
}


#
# This subroutine allows the user to log in without attempting 
# a privileged action. Trivial but useful.
#
sub moncgi_login {
    &moncgi_authform ("moncgi_login","");
}


#
# This subroutine allows site admins to define their own custom 
# rows of the command table, which will appear as a third row to the
# main command table. Take a look at the sample that's here below.
#
# You're on your own here with whatever code you put in this subroutine!
# Go nuts!
#
sub moncgi_custom_print_bar {
    #
    # This is a sample routine, contributed by Ed Ravin (eravin@panix.com).
    #
    # Everything is commented out, and none of the functions are implemented 
    # here, but this should give you the idea of what a custom command 
    # bar would look like.
    #
    my ($face)= (@_);

    #$webpage->print("<tr>\n");
    #$webpage->print("\t<td  align=center><font FACE=\"$face\"><a href=$url?${monhost_and_port_args}command=launch&amp;args=space_shuttle>Launch Space Shuttle</a></font></td>\n");
    #$webpage->print("\t<td  colspan=2 align=center><font FACE=\"$face\"><a href=$url?${monhost_and_port_args}command=coffee&amp;args=offtime,30,nosugar>Take Coffee Break for 30 minutes</a></font></td>\n");
    #$webpage->print("\t<td  colspan=2 align=center><font FACE=\"$face\"><a href=$url?${monhost_and_port_args}command=fizz&amp;args=offtime,0>Reset Soda Machine</font></td>\n");
    #$webpage->print("\t<td  colspan=2 align=center><font FACE=\"$face\"><a href=$url?${monhost_and_port_args}command=ackall&amp;args=>Acknowledge All Alarms</a></font></td>\n");
    #$webpage->print("</tr>\n");
}


#
# This subroutine extends the main command processing loop at the end
# of this script with your own custom commands. Used in conjunction 
# with moncgi_custom_print_bar, and other subroutines that you 
# define in this script, moncgi_custom_commands provides a nice way
# to extend mon.cgi at your site.
# From Ed Ravin (eravin@panix.com)
#
sub moncgi_custom_commands
{
       if ($command eq "replace_this_string_with_a_custom_command")
       {
               &setup_page("Custom Command #1");
               # &call_your_first_custom_code_here;
       }
       elsif ($command eq "replace_this_string_with_another_custom_command")
       {
               &setup_page("Custom Command #2");
               # &call_your_second_custom_code_here;
       }
# as many other custom commands as you care to define go below
       else  # didn't find anything
       {
               return 0;
       }
       1; # did find something, suppress further command processing
}



###############################################################
# Main program
###############################################################
#
# Instantiate the mon client
#
$c = new Mon::Client (
		      host => $monhost,
		      port => $monport,
		      );

if ($command eq "query_opstatus" ){		       # Summary opstatus view
    &setup_page("karoshi Server Status: Summary View");
    &query_opstatus("summary");
}
elsif ($command eq "query_group" ){		       # Expand hostgroup.
    &setup_page("Group Expansion");
    &query_group($args);
}
elsif ($command eq "list_alerthist"){	       # Alert history button.
    &setup_page("List the alert history");
    &list_alerthist;
}
elsif ($command eq "svc_details"){		       # View failure details.
    &setup_page("Service Details");
    &svc_details($args);
}
elsif ($command eq "list_disabled"){		       # List disabled hosts button.
    &setup_page("List disabled hosts");
    &list_disabled;
}
elsif ($command eq "mon_test_service"){		 # Test a service immediately
    &setup_page("Test Service");
    &mon_test_service($args);
    sleep 1;   # if we don't sleep here, svc_details will kick off before
               # the test does and it will look like we aren't running a test.
    &svc_details($args);
}
elsif ($command eq "mon_schedctl"){	       # Stop/start the scheduler
    &setup_page("$args scheduler");
    &mon_schedctl ($args);
    &query_opstatus("summary");
}
elsif ($command eq "list_dtlog"){             # List the downtime log
    &setup_page("List Downtime Log");
    &list_dtlog($args);
}
elsif ($command eq "mon_disable"){		       # Disable a host/group/service
    &setup_page("Disable alert for host, group. or service");
    &mon_disable($args);
    if ($rt eq "query_group") {
	&query_group($rtargs);
    } else {
	&query_opstatus("summary");
    }
}
elsif ($command eq "mon_enable"){		       # Enable a host/group/service
    &setup_page("Enable alert for host, group, or service");
    &mon_enable($args);
    if ($rt eq "query_group") {
	&query_group($rtargs);
    } elsif ($rt eq "svc") {
	&query_opstatus("summary");
    } else {
	&query_opstatus;
    }
}
elsif ($command eq "list_pids"){		       # View pid button.
    &setup_page("List pids of server, alerts and monitors.");
    &list_pids;
}
elsif ($command eq "mon_reset"){		       # Reset mon button.
    &setup_page("Reset mon");
    &mon_reset($args);
}
elsif ($command eq "mon_ack"){		       # Reset mon button.
    &setup_page("Acknowledge service failure");
    &mon_ack($args);   #$ackcomment is a global
    &svc_details($args);
}
elsif ($command eq "mon_reload"){		       # Reload button.
    &setup_page("Reload Mon");
    &mon_reload($args);
}
elsif ($command eq "mon_loadstate"){	       # load mon scheduler state
    &setup_page("Load Scheduler State");
    # right now we expect $args to be empty, since loadstate doesn't take
    # any arguments, but someday it might, so we prepare.
    &mon_loadstate($args);
}
elsif ($command eq "mon_savestate"){	       # save mon scheduler state
    &setup_page("Save Scheduler State");
    # right now we expect $args to be empty, since loadstate doesn't take
    # any arguments, but someday it might, so we prepare.
    &mon_savestate($args);
}
elsif ($command eq "moncgi_logout"){		       # Log out as auth user.
    $destroy_auth_cookie = "yes";
    &setup_page("Logging out");
    &moncgi_logout;
}
elsif ($command eq "query_opstatus_full"){		       # Full operations status
    &setup_page("Operation Status: Full View");
    &query_opstatus("full");
# Selection "mon_opstatus" will fall through to else.
}
elsif ($command eq "mon_state_change") {
    &setup_page("Operation Status: Disable/Enable Groups/Hosts/Services");
    &mon_state_change;
}
elsif ($command eq "mon_state_change_enable_only") {
    &setup_page("Operation Status: Enable Groups/Hosts/Services");
    &mon_state_change_enable_only;
}
elsif ($command eq "moncgi_test_all") {
    &setup_page("Operation Status: Test All Services In Group");
    &moncgi_test_all($args);
}
elsif ($command eq "mon_test_config") {
    &setup_page("Test Mon Config File Syntax");
    &mon_test_config($args);
}
elsif ($command eq "moncgi_reset") {
    &setup_page("Reset mon Server");
    &moncgi_reset($args);
}
elsif ($command eq "moncgi_login") {
    &setup_page("Log In To mon Server");
    &moncgi_login($args);
}
elsif ( &moncgi_custom_commands) # check for user extensions
{
    # The actual custom commands are processed 
    #  inside &moncgi_custom_commands.
    #
    # moncgi_custom_commands returns non-zero if it finds 
    #  a command to execute;
}
else {					       # All else.
    &setup_page("Operation Status: Summary View");
    &query_opstatus("summary");
}

$webpage->print("<hr>");

#
# Some stuff we keep around for debugging
#
#print "commands is $command, args is $args<br>\n";   #DEBUG
#print $webpage->dump;   #DEBUG

&end_page;
$c->disconnect();
