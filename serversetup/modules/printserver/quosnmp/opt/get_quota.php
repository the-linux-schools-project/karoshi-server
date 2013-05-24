<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<!--
  get_quota.php
  Version 1.8.0 Final
  A web app for querying the user print quotas enforced by quosnmp

  Released by Marcus Lauer (marcus.lauer at nyu dot edu)
  Available at http://quosnmp.sourceforge.net

  Copyright (C) 2009 by Marcus Lauer (marcus.lauer at nyu dot edu)

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307,
  USA.

  Development supported by the Center for Information Technology at New York
  University (NYU) and the Wilf Department of Politics at NYU.
-->
<HEAD>
	<TITLE>Your print quota</TITLE>
	<STYLE>
		div.ridgebox { border-color: #CFCFCF; border-width: 3px; border-style: outset; margin: 0px; padding: 10px 20px 10px 20px; display: inline-block; }
		p.name { text-align: center; font-size: 16pt; color: black; line-height: 16pt; }
		p.result { text-align: center; font-size: 12pt; color: black; line-height: 16pt; }
		p.noprint { text-align: center; font-size: 12pt; color: red; line-height: 16pt; }
		p.unlimited { text-align: center; font-size: 12pt; color: green; line-height: 16pt; }
		p.tiny { text-align: center; font-size: 9pt; color: black; line-height: 12pt; }
		body.nice { background-color: white; text-align: center; }
	</STYLE>
</HEAD>

<BODY CLASS="nice">

	<?php
		// This code calculates the user's print quota using the same algorithm as quosnmp-util.  
		// User quotas override group quotas (the highest of which is used).  Group quotas 
		// override default quotas.  All adjustments are applied.
		//
		// IMPORTANT NOTE: There must be some authentication system in place for accessing this 
		// script.  The details of that system is your problem. :)  You'll need something which 
		// makes your web server authenticate against whatever your printing system authenticates 
		// against.  For example, if you use SAMBA and serve this web app via Apache then maybe 
		// something which accesses ntlm_auth would do the trick.  I'm using Apache2::AuthenNTLM 
		// with a similar setup.  If you authenticate against an Active Directory and have Apache 
		// then one of the LDAP or winbind modules might work.
		//
		// Note that this script uses the variables below to set the locations of the accounting 
		// and quota directories.  It may eventually be expanded to parse quosnmp.conf to get 
		// these values.

		// SET THESE two variables to values which are appropriate for your system
		$quotaDir = "/var/log/cups/quotas";
		$accountingDir = "/var/log/cups/accounting";

		function quotaExpired ( $quotaString ) {
			if ( !preg_match( "/,/", $quotaString ) ) {
				return(0); // No timestamp == not expired.
			}
			else {
				list( $quotaPart, $timestampPart ) = explode( ",", $quotaString, 2 );
				$timestampPart = rtrim($timestampPart);
				$tsLength = strlen($timestampPart);

				if ( strlen($tsLength) == 0 ) {
					return(0);
				}
				else if ( strlen($timestampPart) != 12 ) {
					return(1); // The safe thing to do, return expired on errors.
				}

				// Convert the timestamp into a nice array.
				$timestampArray = array( (int)(substr($timestampPart,0,4)),
							 (int)(substr($timestampPart,4,2)),
							 (int)(substr($timestampPart,6,2)),
							 (int)(substr($timestampPart,8,2)),
							 (int)(substr($timestampPart,10,2))
							);

				// Convert the localtime into a similar array.
				$currentTime = localtime();
				$currentTimeArray = array( (((int)$currentTime[5]) + 1900),
							   (((int)$currentTime[4]) + 1),
							   (int)$currentTime[3],
							   (int)$currentTime[2],
							   (int)$currentTime[1]
							);

				// Check each of the five values (year, month, day, hour, minute) in the timestamp
				for ( $counter = 0; $counter <= 4; $counter++ ) {
					if ( $timestampArray[$counter] < $currentTimeArray[$counter] ) {
						return(1);
					}
					if ( $timestampArray[$counter] > $currentTimeArray[$counter] ) {
						return(0);
					}
				}

				return(1);
			}
		}

		function validQuota ( $quotaString ) {
			if ( preg_match( "/^[UN](,\d{12})?$/",$quotaString ) ) {
				return(1);
			}

			if ( preg_match( "/^[+-]?\d+(,\d{12})?$/",$quotaString ) ) {
				return(1);
			}

			return(0);
		}

		function processQuotaFile ($quotaFile) {
			// Set some default values
			$quota = "NONE";
			$foundQuota = 0;
			$adjustments = 0;

			$quotaFileContents = file($quotaFile);

			foreach ( $quotaFileContents as $quotaLine ) {
				if ( validQuota($quotaLine) == 1 ) {
					if ( quotaExpired($quotaLine) == 0 ) {
						if ( preg_match( "/,/", $quotaLine ) ) {
							list( $quotaPart, $timestampPart ) = explode( ",", $quotaLine, 2 );
						}
						else {
							$quotaPart = $quotaLine;
						}

						if ( preg_match( "/^[+-]\d+$/", $quotaPart ) ) {
							$adjustments = $adjustments + (int)$quotaPart;
						}
						else {
							$quota = $quotaPart;
						}
					}
				}
			}

			return( array($quota, $adjustments) );
		}

		// Store the username of the person who accessed this page
		if ( !isset($_SERVER['PHP_AUTH_USER']) && !isset($_SERVER['REMOTE_USER'] ) ) {
			echo 'You must enter your Politics username and password to access your print quota';
			exit;
		}

		if ( isset($_SERVER['PHP_AUTH_USER']) ) {
			$username = $_SERVER['PHP_AUTH_USER'];
		}
		else {
			$username = $_SERVER['REMOTE_USER'];
		}

		// Set some variables to default values.
		$finalQuota = "0"; // Should remain a string until the last minute.
		$foundQuota = 0;
		$totalAdjustments = 0;

		// Get the current page count
		$accountingFileName = $accountingDir . "/" . $username;
		if ( file_exists($accountingFileName) ) {
			$currentPages = file_get_contents($accountingFileName);
		}
		else {
			$currentPages = "0"; // Maybe not a safe assumption...
		}

		// Get the user print quota (if any) and adjustments
		$userQuotaFileName = $quotaDir . "/" . $username . "_user_quota";
		if ( file_exists( $userQuotaFileName ) ) {
			list ( $userQuota, $userAdjustments ) = processQuotaFile($userQuotaFileName);

			if ( !preg_match( "/^NONE$/", $userQuota ) ) {
				$finalQuota = $userQuota;
				$foundQuota = 1;
			}

			$totalAdjustments = $totalAdjustments + (int)$userAdjustments;
		}

		// Figure out which groups the user is in
		$groupsFile = file( '/etc/group' );

		foreach ( $groupsFile as $groupsLine ) {
			if ( preg_match( "/[:,]$username,/i", $groupsLine ) || preg_match( "/[:,]$username$/i", $groupsLine ) ) {
				// If they're in the group, add the group to the group list.
				$latestGroup = explode( ":", $groupsLine );
				$groupsList[] = $latestGroup[0];
			}
		}

		// Get the group print quota (if any) and adjustments
		$topGroupQuota = 0;

		foreach ( $groupsList as $group ) {
			$groupQuotaFileName = $quotaDir . "/" . $group . "_group_quota";

			if ( file_exists($groupQuotaFileName) ) {
				list ( $groupQuota, $groupAdjustments ) = processQuotaFile($groupQuotaFileName);

				if ( $foundQuota == 0 && !preg_match( "/^NONE$/", $groupQuota ) ) {
					if ( preg_match( "/^[NU]$/", $groupQuota ) ) {
						$finalQuota = $groupQuota;
						$foundQuota = 1;
					}
					elseif ( (int)$groupQuota > $topGroupQuota ) {
						$topGroupQuota = (int)$groupQuota;
					}
				}

				$totalAdjustments = $totalAdjustments + (int)$groupAdjustments;
			}
		}

		if ( $foundQuota == 0 && $topGroupQuota > 0 ) {
			$finalQuota = $topGroupQuota;
			$foundQuota = 1;
		}

		// Get the default print quota (if any) and adjustments
		$defaultQuotaFileName = $quotaDir . "/print_quota";

		if ( file_exists($defaultQuotaFileName) ) {
			list ( $defaultQuota, $defaultAdjustments ) = processQuotaFile($defaultQuotaFileName);

			if ( $foundQuota == 0 && !preg_match( "/^NONE$/", $defaultQuota ) ) {
				$finalQuota = $defaultQuota;
				$foundQuota = 1;
			}

			$totalAdjustments = $totalAdjustments + (int)$defaultAdjustments;
		}

		// Now (finally!) print out some sort of response based on the user's quota and pagecount
		echo "<DIV CLASS=\"ridgebox\">\n";
		echo "<P CLASS=\"name\">Your username: $username</P>\n";

		if ( $foundQuota == 0 ) {
			echo "<P CLASS=\"noprint\">Apparently you are not allowed to print, but only because no quota files were found. This could be a configuration problem.</P>\n";
		}
		elseif ( preg_match( "/^N$/", $finalQuota ) || preg_match( "/^0$/", $finalQuota ) ) {
			echo "<P CLASS=\"noprint\">Apparently you are not allowed to print.</P>\n";
		}
		elseif ( preg_match( "/^U$/", $finalQuota ) || preg_match( "/^-1$/", $finalQuota ) ) {
			echo "<P CLASS=\"unlimited\">You have an <STRONG>unlimited</STRONG> quota. Enjoy!\n";
		}
		else {
			// Calculate the remaining pages if any
			$finalQuota = (int)$finalQuota + (int)$totalAdjustments;
			$pagesLeft = (int)$finalQuota - (int)$currentPages;

			if ( $pagesLeft > 0 ) {
				echo "<P CLASS=\"result\">You have <STRONG>$pagesLeft</STRONG> pages left in your printing allowance.<BR>Pages printed: $currentPages, quota: $finalQuota</P>\n";
				if ( (int)$currentPages < 0 ) {
					echo "<P CLASS=\"tiny\">\"Pages printed\" can be negative if a periodic (e.g. monthly) quota is in use.<BR>These \"negative\" pages are ones which rolled over from the previous period.<BR>One you use them up, you will be back to zero pages printed.</P>\n";
				}
			}
			else {
				echo "<P CLASS=\"noprint\">You are over quota!<BR>pages printed: $currentPages, quota: $finalQuota</P>\n";
			}
		}

		echo "</DIV>\n";
	?>

</BODY>
