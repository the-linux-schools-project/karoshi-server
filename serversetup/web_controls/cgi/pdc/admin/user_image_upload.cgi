#!/usr/bin/perl
#
# File Upload Script        Version 6.00
# Created by Jeff Carnahan  jeffc@terminalp.com
# Created on: 4/8/95        Last Modified on: 01/23/98 23:06
# Scripts Archive:          http://www.terminalp.com/scripts/
#
# ---------------------------------------------------------------------
#
# Copyright (C) 1996 Jeffrey D. Carnahan
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# A full copy of the GNU General Public License can be retrieved from
# http://www.terminalp.com/scripts/license.shtml
#
# - Jeff Carnahan <jeffc@terminalp.com
#
# ---------------------------------------------------------------------
# Program Specific Quickie Notes:
#   * Make Sure The First Line Is Pointing To The Correct Location Of Perl 5.
#   * Make Sure This Program is chmodded with the permissions '755'.
#
#  Version:  Time Stamp:        History:
#  ____________________________________________________________________
#
#     1.00  04/08/96 00:00     The script was created.
#     1.10  04/23/96 00:00     Added User and Group ID to allow file
#                              changing by the actual user, also updated
#                              a security hole which allowed any user with
#                              the UID of 1376 to own the uploaded files.
#                              Also Updated the INSTALL program and README
#                              files.
#     3.00  05/07/96 00:00     New release with group and user id fixes, it
#                              updates a previously unreleased version (2.0)
#     3.10  05/10/96 00:00     Stupid Typo in script fixed, it was
#                              causing problems for some users.
#     4.00  08/04/96 23:16     Security hole regarding '../' paths
#                              fixed.  Thanks to: Rus Berrett.  Mime
#                              type error fixed.  Thanks to: Bob Stewart.
#     4.01  08/07/96 11:20     Typo fixed in &NoOpen.  Thanks to Marco
#                              Dings.
#     5.00  10/06/96 21:42     Fully rewrote script around CGI.pm library.
#                              As soon as I get the time, I'll write more
#                              features into it, but for now, this version
#                              is stable (to the best of my knowledge).
#     5.01  02/09/97 12:41     Fixed some typo's, and added support for
#                              Netscape Communicator.
#     5.02  05/07/97 15:37     Fixed a possible binary file uploading,
#                              added easier support for NT, and fixed
#                              documentation problems. Added the FAQ.
#     5.03  06/19/97 17:30     Fixed a bug which resulted in all files
#                              appearing to be less than one byte in
#                              size, thus uploads weren't saved.
#     6.00  01/23/98 23:06     Added multiple-file uploading.  You can
#                              now upload more than one file at a time.
#                              Also added $MAXIMUM_UPLOAD variable to
#                              restrict file upload sizes.  Script 
#                              completely re-written.  Removed buggy
#                              NT support, and simplified variables.
#                              CGI.pm is no longer bundled with this 
#                              script.  If you need it, download it 
#                              from:
#       http://www.genome.wi.mit.edu/ftp/pub/software/WWW/cgi_docs.html
#                             
# ---------------------------------------------------------------------
# Configurable Options Follow:
#
system "[ -d /var/www/karoshi/user_image_upload ] && rm -f -R /var/www/karoshi/user_image_upload";
system "mkdir -p /var/www/karoshi/user_image_upload";
system "chmod 0700 /var/www/karoshi/";
system "chmod 0700 /var/www/karoshi/user_image_upload";
BEGIN {

	$SAVE_DIRECTORY = "/var/www/karoshi/user_image_upload";
                              #
                              # --> Variable:
                              #         $SAVE_DIRECTORY
                              # --> Function:
                              #         Defines the path to the directory
                              #         on the server that should be used
                              #         as the folder to save files into.
                              # --> Directory Permissions:
                              #         a+rwx
                              # --> Additional Notes:
                              #         This path should not have a
							  #         trailing forward slash.  Also
							  #         remember that this is a path, not
							  #         a URL.  Use something similar to:
							  #
							  #         /home/myself/www/uploads
							  #

	$MAXIMUM_UPLOAD = 0;
                              #
                              # --> Variable:
                              #         $MAXIMUM_UPLOAD
                              # --> Function:
                              #         Defines the number of bytes that
                              #         can be uploaded.  Files that exceed
                              #         this limit will not be saved on the
							  #         server.
                              # --> Additional Notes:
							  #         Set this to zero in order to 
							  #         disable size checking.
							  #
							  
	$ALLOW_INDEX = 0;
                              #
                              # --> Variable:
                              #         $ALLOW_INDEX
                              # --> Function:
                              #         If set to zero, files whose
							  #         names begin with the word 
							  #         index will not be saved.
                              # 
							  #         Set to one to allow files
							  #         named index* to be uploaded.
                              # --> Additional Notes:
                              #
							  
	$SUCCESS_LOCATION = ""
                              #
                              # --> Variable:
                              #         $SUCCESS_LOCATION
                              # --> Function:
                              #         Defines the URL that users
                              #         should be redirected to if 
							  #         the script works properly.  If
							  #         this is left blank, a default
							  #         page will be returned to the
							  #         user.
                              # --> Additional Notes:
                              #         This is a COMPLETE URL, not
                              #         a path.
}
#
# End of Configurable Options.
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# -->           Do Not Change Anything Below This Line.           <-- #
# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

	$| = 1;
	chop $SAVE_DIRECTORY if ($SAVE_DIRECTORY =~ /\/$/);
	use CGI qw(:standard);
	$query = new CGI;

	if ( (!(-e $SAVE_DIRECTORY)) ||
		 (!(-W $SAVE_DIRECTORY)) ||
		 (!(-d $SAVE_DIRECTORY)) ) {
		print header;
		print <<__END_OF_HTML_CODE__;
		
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
			<TITLE>Error: Bad Directory</TITLE>
		</HEAD>
		<BODY BGCOLOR="#FFFFFF">
		<H1>Bad Directory</H1>
		<P>
		The directory you specified:
		<BR>
		<BLOCKQUOTE>
			<TT>\$SAVE_DIRECTORY = "<B>$SAVE_DIRECTORY</B>";</TT>
		</BLOCKQUOTE>
		<BR>
		is invalid.  This problem is caused by one of the three following reasons:
		<OL>
			<LI>The directory doesn't exist.  Make sure that this directory is a complete path name, not
			    a URL or something similar.  It should look similar to <TT>/home/username/public_html/uploads</TT>
			<P>
			<LI>The directory isn't writable.  Make sure that this directory is writable by all users.  At
				your UNIX command prompt, type <TT>chmod 777 $SAVE_DIRECTORY</TT>
			<P>
			<LI>The directory you specified isn't really a directory.  Make sure that this is indeed a directory
				and not a file.
		</OL>
		<HR SIZE=1>
		<CENTER><A HREF="http://www.terminalp.com/scripts/">Jeff's Scripts</A></CENTER>
		</BODY>
		</HTML>
		
__END_OF_HTML_CODE__
		exit;
	}
	
	foreach $key (sort {$a <=> $b} $query->param()) {
		next if ($key =~ /^\s*$/);
		next if ($query->param($key) =~ /^\s*$/);
		next if ($key !~ /^file-to-upload-(\d+)$/);
		$Number = $1;
		
		if ($query->param($key) =~ /([^\/\\]+)$/) {
			$Filename = $1;
			$Filename =~ s/^\.+//;
			$File_Handle = $query->param($key);
			
			if (!$ALLOW_INDEX && $Filename =~ /^index/i) {
				print header;
				print <<__END_OF_HTML_CODE__;
				
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
					<TITLE>Error: Filename Problem</TITLE>
				</HEAD>
				<BODY BGCOLOR="#FFFFFF">
				<H1>Filename Problem</H1>
				<P>
				You attempted to upload a file that isn't properly formatted.  The system administrator
				has decided that you can't upload files that begin with the word '<B>index</B>'. Please
				rename the file on your computer, and try uploading it again.
				<P>
				<HR SIZE=1>
				<CENTER><A HREF="http://www.terminalp.com/scripts/">Jeff's Scripts</A></CENTER>
				</BODY>
				</HTML>
	
__END_OF_HTML_CODE__
				exit;
			}
		} else {
			$FILENAME_IN_QUESTION = $query->param($key);
			
			print header;
			print <<__END_OF_HTML_CODE__;
			
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
				<TITLE>Error: Filename Problem</TITLE>
			</HEAD>
			<BODY BGCOLOR="#FFFFFF">
			<H1>Filename Problem</H1>
			<P>
			You attempted to upload a file that isn't properly formatted.  The file in question 
			is <TT><B>$FILENAME_IN_QUESTION</B></TT>  Please rename the file on your computer, and
			attempt to upload it again.  Files may not have forward or backward slashes in their 
			names.  Also, they may not be prefixed with one (or more) periods.
			<P>
			<HR SIZE=1>
			<CENTER><A HREF="http://www.terminalp.com/scripts/">Jeff's Scripts</A></CENTER>
			</BODY>
			</HTML>

__END_OF_HTML_CODE__
			exit;
		}

        if (!open(OUTFILE, ">$SAVE_DIRECTORY\/$Filename")) {
            print "Content-type: text/plain\n\n";
            print "-------------------------\n";
            print "Error:\n";
            print "-------------------------\n";
            print "File: $SAVE_DIRECTORY\/$Filename\n";
            print "-------------------------\n";
	        print "There was an error opening the Output File\n";
    	    print "for Writing.\n\n";
        	print "Make sure that the directory:\n";
	        print "$SAVE_DIRECTORY\n";
    	    print "has been chmodded with the permissions '777'.\n\n";
        	print "Also, make sure that if your attempting\n";
	        print "to overwrite an existing file, that the\n";
    	    print "existing file is chmodded '666' or better.\n\n";
	        print "The Error message below should help you diagnose\n";
    	    print "the problem.\n\n";
        	print "Error: $!\n";
            exit;
        }

		undef $BytesRead;
		undef $Buffer;
		
        while ($Bytes = read($File_Handle,$Buffer,1024)) {
			$BytesRead += $Bytes;
            print OUTFILE $Buffer;
        }
		
		push(@Files_Written, "$SAVE_DIRECTORY\/$Filename");
		$TOTAL_BYTES += $BytesRead;
		$Confirmation{$File_Handle} = $BytesRead;

        close($File_Handle);
		close(OUTFILE);

        chmod (0600, "$SAVE_DIRECTORY\/$Filename");
    }

	$FILES_UPLOADED = scalar(keys(%Confirmation));

	
	if ($TOTAL_BYTES > $MAXIMUM_UPLOAD && $MAXIMUM_UPLOAD > 0) {
		foreach $File (@Files_Written) {
			unlink $File;
		}
		
		print header;
		print <<__END_OF_HTML_CODE__;
		
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
			<TITLE>Error: Limit Reached</TITLE>
		</HEAD>
		<BODY BGCOLOR="#FFFFFF">
		<H1>Limit Reached</H1>
		<P>
		You have reached your upload limit.  You attempted to upload <B>$FILES_UPLOADED</B> files, totalling 
		<B>$TOTAL_BYTES</B>.  This exceeds the maximum limit of <B>$MAXIMUM_UPLOAD</B> bytes, set by the system 
		administrator.  <B>None</B> of your files were successfully saved.  Please try again.
		<P>
		<HR SIZE=1>
		<CENTER><A HREF="http://www.terminalp.com/scripts/">Jeff's Scripts</A></CENTER>
		</BODY>
		</HTML>
				
__END_OF_HTML_CODE__
		exit;
	}
	
	if ($SUCCESS_LOCATION !~ /^\s*$/) {
		print $query->redirect($SUCCESS_LOCATION);
	} else {

		print header;
		print <<__END_OF_HTML_CODE__;
		
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
			<TITLE>Upload Completed</TITLE><meta http-equiv="REFRESH" content="0; URL=user_image_process.cgi">
		</HEAD>
		<BODY <body style="color: rgb(0, 0, 0); background-color: rgb(0, 0, 0);"
 alink="#000099" link="#000099" vlink="#990099">
		</BODY>
		</HTML>
	
__END_OF_HTML_CODE__

		foreach $key (keys (%Confirmation)) {
			print "$key - $Confirmation{$key} bytes\n";
		}
		
		print <<__END_OF_HTML_CODE__;
		
		</PRE>
		<P>
</div>
		</BODY>
		</HTML>

__END_OF_HTML_CODE__
		exit;	
	}
	
# ---------------------------------------------------------------------
# EOF

