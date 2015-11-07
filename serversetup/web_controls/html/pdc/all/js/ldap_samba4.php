<p id="searchresults">
<?php
	// PHP5 Implementation - uses MySQLi & LDAP.
	$enableldap=1;
	// Connect LDAP
	$ldapconnected=0;  
	// Specify the LDAP server to connect to
	if($enableldap == 1){
		if($ldapconnection = ldap_connect("127.0.0.1")){
			$ldapconnected = 1;
		}
	}	 
	// bind to the LDAP server specified above
	if ($ldapconnected == 1){
		@ldap_set_option($ldapconnection, LDAP_OPT_NETWORK_TIMEOUT, 4);
		@ldap_set_option($ldapconnection, LDAP_OPT_PROTOCOL_VERSION, 3);
                @ldap_set_option($ldapconnection, LDAP_OPT_SIZELIMIT, 8);
		if ((ldap_bind($ldapconnection))==false){
			$ldapconnected = 0;       
		}	
	}
	
		// Is there a posted query string?
		if(isset($_POST['queryString'])) {
			$queryString = $_POST['queryString'];
			
			// Is the string length greater than 0?
			if(strlen($queryString) > 1) {
                                
				if($ldapconnected == 1){
	         					$attributes= array("gidNumber","cn","name");
                                                        $lookupString = "userPrincipalName=$queryString*";                               
	         					if($userresults=@ldap_search($ldapconnection, "OU=People,LDAPBASE",$lookupString, $attributes)){
                                                            // While there are results loop through them - fetching an Object.
                                                           $info=@ldap_get_entries($ldapconnection, $userresults);
                                                            // Generate the category id
                                                           echo "<span class=category>Users</span>";
                                                            
                                                           if($info["count"] > 0){
                                                            $entry = ldap_first_entry($ldapconnection, $userresults);
                                
                                                            while($entry) {
                                                                
                                                                $name = (@ldap_get_values($ldapconnection,$entry,'cn'));
                                                                $name = $name[0];
                                                                if(strlen($name) > 35) {
                                                                    $name = substr($name, 0, 35) . "...";
                                                                }
                                                               
                                                                    $userName = (@ldap_get_values($ldapconnection,$entry,'name'));
                                                                    $groupDisplayName = array("Unknown");                              
                                                                    $gidNumber = (@ldap_get_values($ldapconnection,$entry,'gidNumber'));
                                                                    $attributes= array("name");
                                                                    $gidNumber = $gidNumber[0];
                                                                    $primarygroupnameresults=@ldap_search($ldapconnection, "OU=People,LDAPBASE", "(&(objectClass=group)(gidNumber=$gidNumber))", $attributes);
                                                                    if($entry2=@ldap_first_entry($ldapconnection,$primarygroupnameresults)){
                                                                      $groupDisplayName = (@ldap_get_values($ldapconnection,$entry2,'name'));
                                                                    }

								    //Start RTB Code
								    $url = "/var/www/html_karoshi/images/user_images/$groupDisplayName[0]/$userName[0].jpg";		
								    if(file_exists($url)){
                                                                      $photo = "/images/user_images/$groupDisplayName[0]/$userName[0].jpg";
								    } else {
								      $photo = "/images/blank_user_image.jpg";
								    }
								    echo '<a href="javascript:void" onclick="updateForm(\''.$userName[0].'\',\''.$photo.'\')">'; 
								    // End RTB Code		
								    if(file_exists($url)){
                                                                      echo '<img src="/images/user_images/'.$groupDisplayName[0].'/'.$userName[0].'.jpg" alt="" height="50" width="40"/>';
								    } else {
								      echo '<img src="/images/blank_user_image.jpg" alt="" height="50" width="40"/>';
								    }
                                                                    echo '<span class="searchheading">'.$name.'</span>';
                                                                $description = "Username: $userName[0] PrimaryGroup: $groupDisplayName[0]";
                                                                
                                                                if(strlen($description) > 80) {
                                                                    $description = substr($description, 0, 80) . "...";
                                                                }

                                                                echo '<span>'.$description.'</span></a>';
                                                                
                                                                $entry = ldap_next_entry($ldapconnection, $entry );
                                                            }
                                                           }
	         				}else{
					echo 'ERROR: There was a problem with the query.';
				}
	         	
				
					
	         		
				
			} else {
				// Dont do anything.
			} // There is a queryString.
		} else {
			echo 'Enter more than two characters';
		}
	}
	if($ldapconnected){
		ldap_close($ldapconnection);
	}
?>
</p>


