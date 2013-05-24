#
#$Id: Makefile.PL,v 1.5 2003/06/06 11:35:41 edelrio Exp $
#
use ExtUtils::MakeMaker;
# See lib/ExtUtils/MakeMaker.pm for details of how to influence
# the contents of the Makefile that is written.
WriteMakefile(
    'NAME'	=> 'Net::DHCP::Watch',
      'PREREQ_PM' => {
		'Test::More' => 0.47
  	},
    'VERSION_FROM' => 'Watch.pm', # finds $VERSION
);
