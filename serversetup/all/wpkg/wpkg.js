/*******************************************************************************
 *
 * WPKG 0.9.10 - Windows Packager
 * Copyright 2003 Jerry Haltom
 * Copyright 2005-2006 Tomasz Chmielewski <tch (at) wpkg . org>
 * Copyright 2005 Aleksander Wysocki <papopypu (at) op . pl>
 *
 * Please report your issues to the list on http://wpkg.org/
 *
 *
 * Command Line Switches
 *
 * /profile:<profile>
 *     Forces the name of the current profile. If not specified, the profile is
 *     looked up using hosts.xml.
 *
 * /base:<path>
 *     Sets the local or remote path to find the settings files.
 *
 * /query:<option>
 *     Displays a list of packages matching the specified criteria. Valid
 *     options are:
 *
 *     a - all packages
 *     i - packages that are currently installed on the system
 *     x - packages that are not currently installed on the system
 *     u - packages that can be upgraded
 *
 * /show:<package>
 *     Displays a summary of the specified package, including it's state.
 *
 * /install:<package>
 *     Installs the specified package on the system.
 *
 * /remove:<package>
 *     Removes the specified package from the system.
 *
 * /upgrade:<package>
 *     Upgrades the already installed package on the system.
 *
 * /synchronize
 *     Synchronizes the current program state with the suggested program state
 *     of the specified profile. This is the action that should be called at
 *     system boot time for this program to be useful.
 *
 * /quiet
 *     Uses the event log to record all error/status output. Use this when
 *     running unattended.
 *
 * /nonotify
 *     Logged on users are not notified about impending updates.
 *
 * /noreboot
 *     System does not reboot regardless of need.
 *
 * /rebootcmd:<option>
 *     Use the specified boot command, either with full path or
 *     relative to location of wpkg.js
 *     Specifying "special" as option uses tools\psshutdown.exe
 *     from www.sysinternals.com - if it exists - and a notification loop
 *
 * /force
 *     Uses force when performing actions (does not honour wpkg.xml).
 *
 * /forceinstall
 *     Forces installation over existing packages.
 *
 * /norunningstate
 *     Do not export the running state to the registry.
 *
 * /quitonerror
 *     Quits execution if installation of any package was unsuccessful
 *     (default: install next package and show the error summary).
 *
 * /debug
 * /verbose
 *     Prints some debugging info.
 *
 * /dryrun
 *     Does not execute any action. Assumes /debug on.
 *
 * /help
 *     Shows this message.
 *
 ******************************************************************************/

/*******************************************************************************
 *
 * Global variables
 *
 ******************************************************************************/

// script wide properties
var force = false;        // when true: doesn't consider wpkg.xml but checks existence of packages.
var forceInstall = false; // forces instalation over existing packages

var quitonerror = false;

var err_summary = "";
var debug = false;
var dryrun = false;

var quiet = false;
var profile;
var host;
var base;

var packages_file;
var profiles_file;
var settings_file;
var hosts_file;

var packages;
var profiles;
var settings;
var hosts;

var nonotify = false;
var noreboot = false;
var exportRunningState = true;	
var rebootCmd = "standard";

var packagesDocument;
var profilesDocument;
var settingsDocument;
var hostsDocument;


var was_notified = false;

// environment variables to apply to all packages
var global_env_vars;

// names of remote configuration files
// these must be located in the directory specified by the /base switch, or by
// default, the current directory

var packages_file_name = "packages.xml";
var profiles_file_name = "profiles.xml";
var hosts_file_name    = "hosts.xml";

// name of the local settings file, which is located in the System32 folder of
// the current system

var settings_file_name = "wpkg.xml";

var sRegPath = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall";
// here we indicate our running state
var sRegWPKG_Running = "HKLM\\Software\\WPKG\\running";


/*******************************************************************************
 *
 * Program execution
 *
 ******************************************************************************/

// call the main function with arguments.
try {
    main(WScript.Arguments);
} catch (e) {
    error(e.description);
    notifyUserFail();
    exit(2);
}

/**
 * Processes command lines and decides what to do.
 */
function main(argv) {

    // get special purpose argument lists
    var argn = argv.Named;
    var argu = argv.Unnamed;

    // process property named arguments that set values
    if (isArgSet(argv, "/debug") || isArgSet(argv, "/verbose")) {
        debug = true;
    }
    
    // process property named arguments that set values
    if (isArgSet(argv, "/dryrun")) {
        dryrun = true;
        debug = true;
    }
    
    // if the user is wanting command help, give it to him
    if (isArgSet(argv, "/help")) {
        showUsage();
        exit(0);
    }

    // process property named arguments that set values
    if (isArgSet(argv, "/quiet")) {
        quiet = true;
    }

    // if the user passes /nonotify, we don't want to notify the user
    if (isArgSet(argv, "/nonotify")) {
        nonotify = true;
    }

    // if the user passes /noreboot, we don't want to reboot
    if (isArgSet(argv, "/noreboot")) {
        noreboot = true;
    }

    // process property named arguments that set values
    if (isArgSet(argv, "/force")) {
        force = true;
    }

    // process property named arguments that set values
    if (isArgSet(argv, "/quitonerror")) {
        quitonerror = true;
    }
    
    // process property named arguments that set values
    if (isArgSet(argv, "/forceinstall")) {
        forceInstall = true;
    }
    
    if (argn("rebootcmd") != null) {
        rebootCmd=(argn("rebootcmd"));
    }
    dinfo("Reboot-Cmd is " + rebootCmd +".");
    
    // want to export the state of WPKG to registry?
    if (isArgSet(argv, "/norunningstate")) {
    	exportRunningState = false;
    } else {
	// indicate that we are running
	setRunningState("true");
    }
    // will use the fso a bit
    var fso = new ActiveXObject("Scripting.FileSystemObject");
    
    // set host name
    var WshNetwork = WScript.CreateObject("WScript.Network");
    host = WshNetwork.ComputerName.toLowerCase();

    if (argn("base") != null) {
        var base = argn("base");
        base = fso.GetAbsolutePathName(base);
    } else {
        // use the executing location of the script as the default base path
        var path = WScript.ScriptFullName;
        base = fso.GetParentFolderName(path);
    }
    dinfo("base directory " + base + ".");
    

    // append the settingsfile names to the end of the base path
    packages_file = fso.BuildPath(base, packages_file_name);
    profiles_file = fso.BuildPath(base, profiles_file_name);
    hosts_file = fso.BuildPath(base, hosts_file_name);

    // our settings file is located in System32
    var SystemFolder = 1;
    var settings_folder = fso.GetSpecialFolder(SystemFolder);
    settings_file = fso.BuildPath(settings_folder, settings_file_name);


    // load packages and profiles
	hosts = loadXml( hosts_file, createXsl( base, "hosts" ) );
	profiles = loadXml( profiles_file, createXsl( base, "profiles" ) );
	packages = loadXml( packages_file, createXsl( base, "packages" ) );


    if (force  &&  isArgSet(argv, "/synchronize")) {
        dinfo("Skipping current settings. Checking for actually installed packages.");

        settings = createXml("wpkg");

        fillSettingsWithInstalled(settings, packages);
        saveXml(settings, settings_file);
    } else {
        // load or create settings file
        if (!fso.fileExists(settings_file)) {
            dinfo("Settings file does not exist. Creating a new file.");

            settings = createXml("wpkg");
            saveXml(settings, settings_file);
        } else {
            settings = loadXml(settings_file);
        }
    }

	if( debug ) {
		var hst = hosts.selectNodes( "host" );
		info( "Hosts file contains " + hst.length + " hosts:" );
		var dsds = 0;
		for( dsds = 0; dsds < hst.length; ++dsds ) {
			info( hst[dsds].getAttribute( "name" ) );
		}
		info( "" );
	}
	
    if (debug) {
        var packs = settings.selectNodes("package");
        info("settings file contains " + packs.length + " packages:");
        var dsds=0;
        for (dsds=0; dsds<packs.length; ++dsds) {
            if (null != packs[dsds]) {
               info(packs[dsds].getAttribute("id"));
            }
        }
        info("");
    }

    if (debug) {
        var packs = packages.selectNodes("package");
        info("packages file contains " + packs.length + " packages:");
        var dsds=0;
        for (dsds=0; dsds<packs.length; ++dsds) {
            if (null != packs[dsds]) {
               info(packs[dsds].getAttribute("id"));
            }
        }
        info("");
    }

	if( debug ) {
		var profs = profiles.selectNodes( "profile" );
		info( "profiles file contains " + profs.length + " profiles:" );
        var dsds=0;
        for (dsds=0; dsds<profs.length; ++dsds) {
            if (null != profs[dsds]) {
               info(profs[dsds].getAttribute("id"));
            }
        }
        info("");
	}
	

    // set the profile from either the command line or the hosts file
    if (argn("profile") != null) {
        profile = argn("profile");
    } else {
        profile = retrieveProfile(hosts, host);

        if (null == profile) {
            throw new Error("Could not find profile for host " + host + ".");
        }
    }

    dinfo("Using profile: " + profile);

    
    // check for existance of the current profile
    if (profiles.selectSingleNode("profile[@id='" + profile + "']") == null) {
        throw new Error("Could not locate the selected profile " + profile +
            ".");
    }
    
    // process command line arguments to determine course of action
    
    if (argn("query") != null) {
        var arg = argn("query").slice(0,1);
        if (arg == "a") {
            queryAllPackages();
        } else if (arg == "i") {
            queryInstalledPackages();
        } else if (arg == "x") {
            queryUninstalledPackages();
        } else if (arg == "u") {
            queryUpgradablePackages();
        }
        exit(0);
    } else if (argn("show") != null) {
        queryPackage(argn("show"));
    } else if (argn("install") != null) {
        installPackageName(argn("install"));
        exit(0);
    } else if (argn("remove") != null) {
        removePackageName(argn("remove"));
        exit(0);
    } else if (argn("upgrade") != null) {
        upgradePackageName(argn("upgrade"));
        exit(0);
    } else if (isArgSet(argv, "/synchronize")) {
        synchronizeProfile();
        exit(0);
    } else {
        throw new Error("No action specified.");
    }
}

/**
 * Displays command usage.
 */
function showUsage() {
    var message = "";
    message += "WPKG 0.9.10 - Windows Packager\n";
    message += "Copyright 2004 Jerry Haltom\n";
    message += "Copyright 2005-2006 Tomasz Chmielewski <tch (at) wpkg . org>\n";
    message += "Copyright 2005 Aleksander Wysocki <papopypu (at) op . pl>\n";
    message += "\n";
    message += "Please report your issues to the list on http://wpkg.org/\n";
    message += "\n";
    message += "\n";
    message += "/profile:<profile>\n";
    message += "    Forces the name of the current profile. If not specified, the profile is\n";
    message += "    looked up using hosts.xml.\n";
    message += "\n";
    message += "/base:<path>\n";
    message += "    Sets the local or remote path to find the settings files.\n";
    message += "\n";
    message += "/query:<option>\n";
    message += "    Displays a list of packages matching the specified criteria. Valid\n";
    message += "    options are:\n";
    message += "\n";
    message += "    a - all packages\n";
    message += "    i - packages that are currently installed on the system\n";
    message += "    x - packages that are not currently installed on the system\n";
    message += "    u - packages that can be upgraded\n";
    message += "\n";
    message += "/show:<package>\n";
    message += "    Displays a summary of the specified package, including it's state.\n";
    message += "\n";
    message += "/install:<package>\n";
    message += "    Installs the specified package on the system.\n";
    message += "\n";
    message += "/remove:<package>\n";
    message += "    Removes the specified package from the system.\n";
    message += "\n";
    message += "/upgrade:<package>\n";
    message += "    Upgrades the already installed package on the system.\n";
    message += "\n";
    message += "/synchronize\n";
    message += "    Synchronizes the current program state with the suggested program state\n";
    message += "    of the specified profile.\n";
    message += "\n";
    message += "/quiet\n";
    message += "    Uses the event log to record all error/status output. Use this when\n";
    message += "    running unattended.\n";
    message += "\n";    
    message += "/nonotify\n";
    message += "   Logged on users are not notified about impending updates.\n";
    message += "\n";
    message += "/noreboot\n";
    message += "   System does not reboot regardless of need.\n";
    message += "\n";
    message += "/rebootcmd:<filename>\n";
    message += "   Use the specified reboot command\n"
    message += "\n";
    message += "/force\n";
    message += "    Uses force when performing actions.\n";
    message += "\n";
    message += "/forceinstall\n";
    message += "    Forces installation over existing packages.\n";
    message += "\n";
    message += "/norunningstate\n";
    message += "   Do not export the running state to the registry.\n";
    message += "\n";
    message += "/quitonerror\n";
    message += "   Quits execution if installation of any package was unsuccessful\n";
    message += "   (default: installs next package and shows the error summary).\n";
    message += "\n";
    message += "/debug\n";
    message += "/verbose\n";
    message += "    Prints some debugging info.\n";
    message += "\n";
    message += "/dryrun\n";
    message += "    Does not execute any action. Assumes /debug on.\n";
    message += "\n";
    message += "/help\n";
    message += "    Shows this message.\n";
    alert(message);
}

/**
 * Scans an argument vector for an argument "arg". Returns true if found, else
 * false
 */
function isArgSet(argv, arg) {
    // loop over argument vector and return true if we hit it
    for (var i = 0; i < argv.length; i++) {
        if (argv(i) == arg) {
            return true;
        }
    }
    // otherwise, return false
    return false;
}

/**
 * Sends a message to the system console notifying of impending action.
 */
function notifyUserStart() {
    if (!was_notified) {
        var msg = "";
        msg += "The automated software installation utility has or is ";
        msg += "currently applying software updates to your system. Please ";
        msg += "check the time shown at the beginning of this message to ";
        msg += "determine if it is out of date. If not, please save all your ";
        msg += "open documents, as the system might require a reboot. If so, ";
        msg += "the system will be rebooted with no warning when installation ";
        msg += "is complete. Thank you.";
        
        was_notified = true;
        
        try {
            notify(msg);
        } catch (e) {
            throw new Error(0, "Unable to notify user that the system was " +
                "about to begin updating. " + e.description);
        }
    }
}

/**
 * Sends a message to the system console notifying them that all action is
 * complete.
 */
function notifyUserStop() {
    var msg = "";
    msg += "The automated software installation utility has completing ";
    msg += "installing or updating software on your system. No reboot was ";
    msg += "necessary. All updates are complete.";
    
    try {
        notify(msg);
    } catch (e) {
        error("Unable to notify the user that all action has been completed.");
    }
}


/**
 * Sends a message to the system console notifying the user that installation
 * failed.
 */
function notifyUserFail() {
    var msg = "";
    msg += "The software installation has failed.";

    try {
	notify(msg);
    } catch (e) {
	error("Unable to notify the user that all action has been completed.");
    }
}

/**
 * Synchronizes the current package state to that of the specified profile,
 * adding, removing or upgrading packages.
 */
function synchronizeProfile() {
    // accquire packages that should be present
    var packageArray = getAvailablePackages();

    dinfo("number of available packages: " + packageArray.length);

    
    // grab currently installed package nodes
    var installedPackages = settings.selectNodes("package");
    var removablesArray = new Array();
    
    // loop over each installed package and check whether it still applies
    for (var i = 0; i < installedPackages.length; i++) {
        var installedPackageNode = installedPackages(i);
        dinfo("found installed package: " + installedPackageNode.getAttribute("id"));
        
        // search for the installed package in available packages
        var found = false;
        for (j in packageArray) {
            dinfo("testing available package: " + packageArray[j].getAttribute("id"));


            if (packageArray[j].getAttribute("id") ==
                installedPackageNode.getAttribute("id")) {
                dinfo("package: " + installedPackageNode.getAttribute("id") + " found in available packages.");

                found = true;
                break;
            }
        }
        
        // if package is no longer present, mark for remove
        if (!found) {
            dinfo("marking package: " + installedPackageNode.getAttribute("id") + " for remove");
	    removablesArray.push(installedPackageNode);
        }
    }

    var allPackagesArray = getAllPackages();
    dinfo("number of packages to remove: " + removablesArray.length); 
    // check for zombies, then really remove trashed packages
    for (i in removablesArray) {
	var packageName = removablesArray[i].getAttribute("id");
	var found = false;
        dinfo("Checking " + packageName + " to remove.");
        for (j in allPackagesArray) {
            if (allPackagesArray[j].getAttribute("id") == packageName)       found = true;
	}
	if (found) {
            dinfo("Checked removal of package: " + packageName);
            notifyUserStart();
            removePackage(removablesArray[i]);
	} else {
	      if (quitonerror) {
                throw new Error("Installation error while synchronizing " +
                    "package " + packageName + ", synchronization aborting." +
                    "\n\n" + "Zombie found: package installed but not in packages database.");
	      } else {
err_summary += "\n\nPackage name: " + packageName +  
                    "\n\n" + "Zombie found: package installed but not in packages database.";
}
	    
        }
    }
    
    // create a native jscript array to do the sorting on
    var sortedPackages = new Array(packageArray.length);
    for (var i = 0; i < packageArray.length; i++) {
        sortedPackages[i] = packageArray[i];
    }
    
    // classic bubble-sort algorithm on the "priority" attribute
    var len = packageArray.length;
    for (var i = 0; i < len - 1; i++) {
        for (var j = 0; j < len - 1 - i; j++) {
            var pri1;
            var pri2;
            var szpri1 = sortedPackages[j].getAttribute("priority");
            var szpri2 = sortedPackages[j + 1].getAttribute("priority");
            
            // if a priority is not set, we assume 0
            
            if (szpri1 == null) {
                pri1 = 0;
            } else {
                pri1 = parseInt(szpri1);
            }
            
            if (szpri2 == null) {
                pri2 = 0;
            } else {
                pri2 = parseInt(szpri2);
            }
            
            // if the priority of the first one in the list exceeds the second,
            // swap the packages
            if (pri1 < pri2) {
                var tmp = sortedPackages[j];
                sortedPackages[j] = sortedPackages[j + 1];
                sortedPackages[j + 1] = tmp;
            }
        }
    }
    
    // sorting complete
    packageArray = sortedPackages;
    
    // loop over each available package and determine whether to install or
    // upgrade
    for (var i = 0; i < packageArray.length; i++) {
        var packageNode = packageArray[i];
        var packageId   = packageNode.getAttribute("id");
        var packageName = packageNode.getAttribute("name");
        var packageRev  = parseInt(packageNode.getAttribute("revision"));

        var executeAttr = packageNode.getAttribute("execute");
        var notifyAttr  = packageNode.getAttribute("notify");    
	
        // search for the package in the local settings
        var installedPackage = settings.selectSingleNode("package[@id='" +
            packageId + "']");
            
        if (executeAttr == "once") {
            if ((null == installedPackage) |
               ((null != installedPackage) &&
	       (parseInt(installedPackage.getAttribute("revision")) < packageRev )) ) {
                try {
                    if (notifyAttr != "false") {
                        notifyUserStart();
                    }

                    executeOnce(packageNode);
                } catch (e) {
		  if (quitonerror) {
                    throw new Error("Installation error while synchronizing " +
                        "package " + packageName + ", synchronization aborting." +
                        "\n\n" + e.description);
		  } else {
err_summary += "\n\nPackage name: " + packageName + "\n\n" + e.description; 
}

                }
            }
        } else if (executeAttr == "always") {
           // do not look if package is installed
            try {
                if (notifyAttr != "false") {
                    notifyUserStart();
                }
                executeOnce(packageNode);
            } catch (e) {
	      if (quitonerror) {
                throw new Error("Installation error while synchronizing " +
                    "package " + packageName + ", synchronization aborting." +
                    "\n\n" + e.description);
	      } else {
err_summary += "\n\nPackage name: " + packageName + "\n\n" + e.description; 
}

            }
	    
        } else {
            // if the package is not installed, install it
            if (installedPackage == null) {
                try {
                    if (notifyAttr != "false") {
                        notifyUserStart();
                    }
                    installPackage(packageNode);
                } catch (e) {
		  if (quitonerror) {
                    throw new Error("Installation error while synchronizing " +
                        "package " + packageName + ", synchronization aborting." +
                        "\n\n" + e.description);
		  } else {
err_summary += "\n\nPackage name: " + packageName + "\n\n" + e.description;
}

                }
            } else if (parseInt(installedPackage.getAttribute("revision")) <
                packageRev) {
                try {
                    if (notifyAttr != "false") {
                        notifyUserStart();
                    }
                    upgradePackage(installedPackage, packageNode);
                } catch (e) {
		  if(quitonerror) {
                    throw new Error("Upgrade error while synchronizing " +
                        "package " + packageName + ", synchronization aborting." +
                        "\n\n" + e.description);
		  } else {
err_summary += "\n\nPackage name: " + packageName + "\n\n" + e.description;
}

                }
            }
        }
    }
    
    // if we had previously warned the user about an impending installation, let
    // them know that all action is complete
    if (was_notified) {
        notifyUserStop();
    }
}

function queryAllPackages() {
    // retrieve packages
    var settingsNodes = settings.selectNodes("package");
    var packagesNodes = packages.selectNodes("package");
    
    // concatenate both lists
    var packageNodes = concatenateList(settingsNodes, packagesNodes);
    var packageNodes = uniqueAttributeNodes(packageNodes, "id");
    
    // create a string to append package descriptions to
    var message = new String();
    
    for (var i = 0; i < packageNodes.length; i++) {
        var packageNode     = packageNodes[i];
        var packageName     = packageNode.getAttribute("name");
        var packageId       = packageNode.getAttribute("id");
        var packageRevision = packageNode.getAttribute("revision");
        var packageReboot   = packageNode.getAttribute("reboot");
        
        if (packageReboot != "true") {
            packageReboot = "false";
        }
        
        message += packageName + "\n";
        message += "    ID:         " + packageId + "\n";
        message += "    Revision:   " + packageRevision + "\n";
        message += "    Reboot:     " + packageReboot + "\n";
        if (searchList(settingsNodes, packageNode)) {
            message += "    Status:     Installed\n";
        } else {
            message += "    Status:     Not Installed\n";
        }
        message += "\n";
    }
    
    info(message);
}

/**
 * Show the user a list of packages that are currently installed.
 */
function queryInstalledPackages() {
    // retrieve currently installed nodes
    var packageNodes = settings.selectNodes("package");
    
    // create a string to append package descriptions to
    var message = new String();
    
    for (var i = 0; i < packageNodes.length; i++) {
        var packageNode     = packageNodes(i);
        var packageName     = packageNode.getAttribute("name");
        var packageId       = packageNode.getAttribute("id");
        var packageRevision = packageNode.getAttribute("revision");
        var packageReboot   = packageNode.getAttribute("reboot");
        
        if (packageReboot != "true") {
            packageReboot = "false";
        }
        
        message += packageName + "\n";
        message += "    ID:         " + packageId + "\n";
        message += "    Revision:   " + packageRevision + "\n";
        message += "    Reboot:     " + packageReboot + "\n";
        message += "    Status:     Installed\n";
        message += "\n";
    }
    
    info(message);
}

/**
 * Shows the user a list of packages that are currently not installed.
 */
function queryUninstalledPackages() {
    // create a string to append package descriptions to
    var message = new String();
    
    // retrieve currently installed nodes
    var packageNodes = packages.selectNodes("package");
    
    // loop over each package
    for (var i = 0; i < packageNodes.length; i++) {
        var packageNode     = packageNodes(i);
        var packageId       = packageNode.getAttribute("id");
        var packageName     = packageNode.getAttribute("name");
        var packageRevision = packageNode.getAttribute("revision");
        var packageReboot   = packageNode.getAttribute("reboot");
        
        if (packageReboot != "true") {
            packageReboot = "false";
        }
        
        // search for the package in the local settings
        var installedPackage = settings.selectSingleNode("package[@id='" +
            packageId + "']");
            
        // if the package is not installed, install it
        if (installedPackage == null) {
            message += packageName + "\n";
            message += "    ID:         " + packageId + "\n";
            message += "    Revision:   " + packageRevision + "\n";
            message += "    Reboot:     " + packageReboot + "\n";
            message += "    Status:     Not Installed\n";
            message += "\n";
        }
    }
    
    info(message);
}

/**
 * Installs a package by name.
 */
function installPackageName(name) {
    // query the package node
    var node = packages.selectSingleNode("package[@id='" + name + "']");
    
    if (node == null) {
        info("Package " + name + " not found!");
        return;
    }

    var executeAttr = node.getAttribute("execute");
    if (executeAttr == "once") {
        executeOnce(node);
    } else {
        installPackage(node);
    }
}

/**
 * Upgrades a package by name.
 */
function upgradePackageName(name) {
    // query the package node
    var nodeNew = packages.selectSingleNode("package[@id='" + name + "']");
    var nodeOld = settings.selectSingleNode("package[@id='" + name + "']");
    
    if (nodeOld == null) {
        info("Package " + name + " not installed!");
        return;
    }
    
    if (nodeNew == null) {
        info("New package " + name + " not found!");
        return;
    }

    var executeAttr = nodeNew.getAttribute("execute");
    if (executeAttr != "once") {
        upgradePackage(nodeOld, nodeNew);
    }
}

/**
 * Removes a package by name.
 */
function removePackageName(name) {
    // query the package node
    var node = settings.selectSingleNode("package[@id='" + name + "']");
    
    if (node == null) {
        info("Package " + name + " not currently installed.");
        return;
    }
    
    removePackage(node);
}


/**
 * Builds settings document tree containing actually installed packages.
 * Tests all packages from given doc tree for "check" conditions.
 * If given conitions are positive, package is considered as installed.
 */
function fillSettingsWithInstalled(settingsDoc, packagesDoc) {

    var packagesNodes = packagesDoc.selectNodes("package");

    for (var i = 0; i < packagesNodes.length; i++) {
        var packNode = packagesNodes[i];

        if (checkInstalled(packNode)) {
            var clone = packNode.cloneNode(true);

            settingsDoc.appendChild(clone);
        }
    }
}



/**
 * Returns value of given key in registry.
 */
function getRegistryValue(keyName) {
    var WshShell = new ActiveXObject("WScript.Shell");
    var val;
    try {
        val = WshShell.RegRead(keyName);
    } catch (e) {
        val = null;
    }

    return val;
}

function setRunningState(statename) {
    var WshShell = new ActiveXObject("WScript.Shell");
    var val;
    
    try {
    	val = WshShell.RegWrite(sRegWPKG_Running, statename);
    } catch (e) {
    	val = null;
    }

    return val;
}
    	

/**
 * Scans uninstall list for given name.
 * Uninstall list is placed in registry under 
 *    HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall
 * Every subkey represents package that can be uninstalled.
 * Function checks each subkey for containing value named DisplayName.
 * If this value exists, function returns true if nameSearched matches it.
 */

function scanUninstallKeys(nameSearched) {
    var HKLM = 0x80000002;
    var dName;
    try
    {
        oLoc = new ActiveXObject("WbemScripting.SWbemLocator");
        oSvc = oLoc.ConnectServer(null, "root\\default");
        oReg = oSvc.Get("StdRegProv");
        //-------------------------------------------------------------

        oMethod = oReg.Methods_.Item("EnumKey");
        oInParam = oMethod.InParameters.SpawnInstance_();
        oInParam.hDefKey = HKLM;
        oInParam.sSubKeyName = sRegPath;
        oOutParam = oReg.ExecMethod_(oMethod.Name, oInParam);

        aNames = oOutParam.sNames.toArray();

        for (i = 0; i < aNames.length; i++) {
            dName = getRegistryValue("HKLM\\" + sRegPath + "\\" + aNames[i] + "\\DisplayName");

            if (null != dName) {
                if (dName == nameSearched) {
                    return true;
                }
            }
        }
    }
    catch(err)
    {
        WScript.Echo("Error occurred when searching registry for " +
                                nameSearched +
                                "\nCode: " + 
                                hex(err.number) + 
                                "; Descriptions: " + 
                                err.description);
    }

    return false;
}


//User-defined function to format error codes.
//VBScript has a Hex() function but JScript does not.
function hex(nmb)
{
    if (nmb > 0)
        return nmb.toString(16);
    else
        return (nmb + 0x100000000).toString(16);
}

/** 
 * Presents some debug output if debugging is enabled
 */
function dinfo(stringInfo) {
    if (debug) {
        info(stringInfo)
    }
}

/**
 * Checks for the success of a check condition for a package.
 */
function checkCondition(checkNode) {

    var checkType = checkNode.getAttribute("type");
    var checkCond = checkNode.getAttribute("condition");
    var checkPath = checkNode.getAttribute("path");
    var checkValue = checkNode.getAttribute("value");

    // sanity check: must have Type set here
    if (checkType == null) {
         throw new Error("Check Type is null - this is not permitted. Perhaps a typo? " +
                         "To help find it, here are the other pieces of information: " +
                         "condition='"+checkCond+"', path='"+checkPath+"', value='"+checkValue+"'");
    } // if checkType == null

    if (checkType == "registry") {

        // sanity check: must have Cond and Path set for all registry checks
       if ((checkCond == null) ||
           (checkPath == null)) {
           throw new Error("condition and / or path is null for a registry check. Perhaps " +
                           "a typo? To help find it, here are the other pieces of information: " +
                           "condition='"+checkCond+"', path='"+checkPath+"', value='"+checkValue+"'");
        } // if checkCond == null || checkPath == null

        if (checkCond == "exists") {
            var val = getRegistryValue(checkPath);

            if (val != null) {
                // Some debugging information
                dinfo("The registry path '"+checkPath+"' exists: the check was successful");
                return true;
            } else {
                // Some debugging information
                dinfo("The registry path '"+checkPath+"' does not exist: the check failed");
                return false;
            }
        } else if (checkCond == "equals") {
            var val = getRegistryValue(checkPath);

            if (val == checkValue) {
                // Some debugging information
                dinfo("The registry path '"+checkPath+"' contained the correct value: '"+
                      checkValue+"': the check was successful");
                return true;
            } else {
                info("The registry path '"+checkPath+"' did not contain the value: '"+
                         checkValue+"' : the check failed");
// change: use a return false:
                return false;
// endChange
            }
        } else {
            throw new Error("Check condition " + checkCond + " unknown " +
                "for type registry.");
        }
    } else if (checkType == "file") {
        // sanity check: must have Cond and Path set for all file checks
        if ((checkCond == null) ||
            (checkPath == null)) {
            throw new Error("condition and / or path is null for a file check. Perhaps " +
                            "a typo? To help find it, here are the other pieces of information: " +
                            "condition='"+checkCond+"', path='"+checkPath+"', value='"+checkValue+"'");
        } // if checkCond == null || checkPath == null

        var shell = new ActiveXObject("WScript.Shell");
        checkPath=shell.ExpandEnvironmentStrings(checkPath);
        if (checkCond == "exists") {
            var fso = new ActiveXObject("Scripting.FileSystemObject");
            if (fso.FileExists(checkPath)) {
                // Some debugging information
                dinfo("The path '"+checkPath+"' exists: the test was successful");
                return true;
            } else {
                // Some debugging information
                dinfo("The path '"+checkPath+"' does not exist: the test failed");
                return false;
            }
        } else if (checkCond == "sizeequals") {
            // sanity check: must have Value set for a size check
            if (checkValue == null) {
                throw new Error("Value is null for a file sizeequals check. Perhaps " +
                                "a type? To help find it, here are the other pieces of information: " +
                                "condition='"+checkCond+"', path='"+checkPath+"', value='"+checkValue+"'");
            } // if checkValue == null

            filesize=GetFileSize(checkPath);
            if (filesize == checkValue) {
                dinfo("The file '"+checkPath+"' has size "+filesize+": the test was successful");
                return true;
            } else {
                dinfo("The file '"+checkPath+"' has size "+filesize+" - wanted "+
                      checkValue+": the test fails")
            }
        } else if (checkCond.substring(0,7) == "version") {
            // sanity check: Must have a value set for version check
            if (checkValue == null) {
                throw new Error("Value is null for a file version check. Perhaps " +
                                "a type? To help find it, here are the other pieces of information: " +
                                "condition='"+checkCond+"', path='"+checkPath+"', value='"+checkValue+"'");
            } // if checkValue == null

            CheckValFromFileSystem = GetFileVersion(checkPath);
            CheckValFromWpkg       = checkValue;
            if (CheckValFromFileSystem != "UNKNOWN") {
                var versionresult = VersionCompare(CheckValFromFileSystem,
                                                   CheckValFromWpkg);
                dinfo ("Checking file version " + CheckValFromFileSystem + " is " + checkCond + 
                       " (than) " + CheckValFromWpkg + " - got result "+versionresult);
                switch (checkCond) {
                   case "versionsmallerthan":
                       retval=(versionresult == -1);
                       dinfo("Checking version of '"+checkPath+"' : Is "+CheckValFromFileSystem+
                             " < "+checkValue+" ? "+retval);
                       return retval;
                       break;
                   case "versionlessorequal":
                       retval=(   (versionresult == -1)
                               || (versionresult == 0) );
                       dinfo("Checking version of '"+checkPath+"' : Is "+CheckValFromFileSystem+
                             " <= "+checkValue+" ? "+retval);
                       return retval;
                       break;
                   case "versionequalto":
                       retval=(versionresult == 0);
                       dinfo("Checking version of '"+checkPath+"' : Is "+CheckValFromFileSystem+
                             " = "+checkValue+" ? "+retval);
                       return retval;
                       break;
                   case "versiongreaterorequal":
                       retval=(   (versionresult == 1)
                               || (versionresult == 0) );
                       dinfo("Checking version of '"+checkPath+"' : Is "+CheckValFromFileSystem+
                             " >= "+checkValue+" ? "+retval);
                       return retval;
                       break;
                   case "versiongreaterthan":
                       retval=(versionresult == 1);
                       dinfo("Checking version of '"+checkPath+"' : Is "+CheckValFromFileSystem+
                             " >= "+checkValue+" ? "+retval);
                       return retval;
                       break;
                   default:
                       throw new Error("Unknown operation on file versions : " + checkCond);
                       break;
               }
           } else {
               // Didn't get a sensible version number from GetFileVersion
               dinfo("Unable to find the file version for " + checkPath);
               return (false);
           }

        } else {
            throw new Error("Check condition " + checkCond + " unknown for " +
                "type file.");
        }

    } else if (checkType == "uninstall") {
        // sanity check: must have Cond and Path set for all uninstall checks
        if ((checkCond == null) ||
            (checkPath == null)) {
             throw new Error("condition and / or path is null for an uninstall check. Perhaps " +
                             "a typo? To help find it, here are the other pieces of information: " +
                             "condition='"+checkCond+"', path='"+checkPath+"', value='"+checkValue+"'");
        } // if checkCond == null || checkPath == null

        if (checkCond == "exists") {
            if (scanUninstallKeys(checkPath)) {
                dinfo("Uninstall entry for "+checkPath+" was found: test successful");
                return true;
            } else {
                dinfo("Uninstall entry for "+checkPath+" missing: test failed");
                return false;
            }
        } else {
            throw new Error("Check condition " + checkCond + " unknown for " +
                "type uninstall.");
        }
    } else if (checkType == "logical") {
    
        // sanity check: must have Cond set for logical checks
        if (checkCond == null) {
            throw new Error("condition is null for a logical check." );
        } // if checkCond == null
    
        var subcheckNodes = checkNode.selectNodes("check");
   
        switch (checkCond) {
        case "not":
            if (subcheckNodes.length == 1) {
                retval=! checkCondition(subcheckNodes[0]);
                dinfo("Result of logical 'NOT' check therefore "+retval);
                return retval;
            } else {
                throw new Error("Check condition 'not' requires one and only " +
                    "one child check condition. I found " + checkNodes.length);
            }
            break;
        case "and":
            for (var i = 0; i < subcheckNodes.length; i++) {
                if (! checkCondition(subcheckNodes[i])) {
                    // lazy execution here.
                    dinfo("Result of logical 'AND' check is false");
                    return false;
                }
            }
            dinfo("Result of logical 'AND' check is true");
            return true;
            break;
        case "or":
            for (var i = 0; i < subcheckNodes.length; i++) {
                if (checkCondition(subcheckNodes[i])) {
                    dinfo("Result of logical 'OR' check is true");
                    return true;
                }
            }
            dinfo("Result of logical 'OR' check is false");
            return false;
            break;
        case "atleast":
            if (checkValue == null) {
                throw new Error("Check condition logical 'atleast' requires a value ");
            }
            var count=0;
            for (var i = 0; i < subcheckNodes.length; i++) {
                if (checkCondition(subcheckNodes[i])) count++;
                // lazy execution
                if (count >= checkValue) {
                    dinfo("Result of logical 'AT LEAST' check is true");
                    return true;
                }
            } // for loop over subcheckNodes
            dinfo("Result of logical 'AT LEAST' check is false");
            return false;
            break;
        case "atmost":
            var count=0;
            for (var i = 0; i < subcheckNodes.length; i++) {
                if (checkCondition(subcheckNodes[i])) count++;
                // lazy execution
                if (count > checkValue) {
                    dinfo("Result of logical 'AT MOST' check is false");
                    return false;
                }
            }
            // result will be true now
            dinfo("Result of logical 'AT MOST' check is true");
            return true;
            break;
        default:
            throw new Error("Check condition " + checkCond + " unknown for " +
            "type logical.");
            break;
        }
    } else {
        throw new Error("Check condition type " + checkType + " unknown.");
    }
    
    return false;
}

/**
 *   VersionCompare - compare two executable versions
 */
function VersionCompare(a,b) {
    // Return 0 if equal
    // Return -1 if a < b
    // Return +1 if a > b
    var as = a.split(".");
    var bs = b.split(".");
    var length=as.length;
    var ret=0;
    for (var i = 0; i < length; i++) {
        var av = as[i]*1;
        var bv = bs[i]*1;
        if (av<bv) {
            ret=-1;
            i=length; // Hack to exit loop
        } else if (av>bv) {
            ret=1;
            i=length;
        }
    }
    return ret;
}

/**
 *  Gets the version of a file
 */
function GetFileVersion (file) {
    var version="UNKNOWN";
    try {
        dinfo ("Finding version of "+file+"\n");
        var FSO = new ActiveXObject("Scripting.FileSystemObject");
        version = FSO.GetFileVersion(file);
        dinfo ("Obtained version \""+version+"\".");
    } catch (e) {
        version="UNKNOWN";
        dinfo ("Unable to find file version for "+file+" : "+
                e.description);
    }
    dinfo ("Leaving GetFileVersion with version "+version);
    return version;
}

/**
 *  Gets the size of a file
 */

function GetFileSize (file) {
    var size="UNKNOWN";
    try {
        dinfo ("Finding size of "+file+"\n");
        var FSO = new ActiveXObject("Scripting.FileSystemObject");
        var fsof = FSO.GetFile(file);
        size = fsof.Size;
    } catch (e) {
        size="UNKNOWN";
        dinfo("Unable to get file size for "+file+" : "+
               e.description);
    }
    dinfo ("Leaving GetFileSize with size "+size);
    return size;
}

/**
 *  Check if package is installed.
 */
function checkInstalled(packageNode) {
    var packageName = packageNode.getAttribute("name");

    dinfo ("checking existence of package:" + packageName);
    
    // get a list of checks to perform before installation.
    var checkNodes = packageNode.selectNodes("check");
    
    // when there are no check conditions, say "not installed"
    if (checkNodes.length == 0) {
        return false;
    }

    // loop over every condition check
    // if all are successful, we consider package as installed
    for (var i = 0; i < checkNodes.length; i++) {
        if (! checkCondition(checkNodes[i])) {
            return false;
        } 
    }

    return true;
}

/**
 * Executes command of the package and registers this fact.
 */
function executeOnce(packageNode) {
    var packageName = packageNode.getAttribute("name");
    var packageId = packageNode.getAttribute("id");
    
    info("Executing commands for " + packageName + "...");
        
    // select command lines to install
    var cmds = packageNode.selectNodes("install");
        
    // execute each command line
    for (var i = 0; i < cmds.length; i++) {
        var cmdNode = cmds(i);
        var cmd = cmdNode.getAttribute("cmd");
        var timeout = cmdNode.getAttribute("timeout");
            
        if (timeout == null) {
            timeout = 0;
        } else {
            timeout = parseInt(timeout);
        }
            
        try {

            dinfo("executing command : " + cmd);
            var result = 0;
            result = exec(cmd, timeout);
            dinfo("command returned result: " + result);

            // if exit code is 0, return successfully
            if (result == 0) {
                continue;
            }

            // search for exit code
            var exitNode = cmdNode.selectSingleNode("exit[@code='" +
                result + "']");

            // check for special exit codes
            if (exitNode != null) {
                if (exitNode.getAttribute("reboot") == "true") {
                    // this exit code forces a reboot
                    info("Command of " + packageName +
                        " returned non-zero exit code [" + result + "]. This " +
                        "exit code requires an immediate reboot.");
                    reboot();
                } else {
                    // this exit code is successful
                    info("Command of " + packageName +
                        " returned non-zero exit code [" + result + "]. This " +
                        "exit code is not an error.");
                    continue;
                }
            }

            // command did not succeed, throw error
            throw new Error(0, "Exit code returned non-successful value: " +
                result + ".\n\n" + cmd);
        } catch (e) {
            throw new Error("Could not execute " + packageName + ". " +
                e.description);       
        }
    }
    
    // check for old node and remove it if there, to avoid duplicate settings
    // file entries when execution=always
    var nodeOld = settings.selectSingleNode("package[@id='" + packageId + "']");
    if (nodeOld != null) {
       info("Replacing settings entry " + packageName);
       settings.removeChild(nodeOld);
    }
    
    // append new node to local xml
    settings.appendChild(packageNode);
    saveXml(settings, settings_file);
    
    // reboot the system if this package is suppose to
    if (packageNode.getAttribute("reboot") == "true") {
        info("Execution of commands of " + packageName + " successful, system " +
            "rebooting.");
        reboot();
    } else {
        info("Execution of " + packageName + " successful.");
    }
}


/**
 * Removes leading / trailing spaces
 */
function trim(string)
{
    return(string.replace(new RegExp("(^\\s+)|(\\s+$)"),""));
}

/**
 * Installs the specified package node to the system.
 */
function installPackage(packageNode) {
    var packageName = packageNode.getAttribute("name");
    
    // get a list of checks to perform before installation.
    var checkNodes = packageNode.selectNodes("check");
    var bypass = false;


    // when "/forceinstall" say "not installed"
    if (!forceInstall) {
        bypass = checkInstalled(packageNode);
        if (bypass) {
                info("Bypassing installation of package " + packageName);

		// yes the packages is installed, but is it in wpkg.xml?
		var packageID = packageNode.getAttribute("id");
		var nodeInst = settings.selectSingleNode("package[@id='" + packageID + "']");

		if (nodeInst == null) {
		  
		  dinfo("Package " + packageName +
			 " missing from settings file, adding it now.");
		  
		  settings.appendChild(packageNode);
		  saveXml(settings, settings_file);
		}
        }
    }
    

    
    if (!bypass) {
        info("Installing " + packageName + "...");
        
        // select command lines to install
        var cmds = packageNode.selectNodes("install");
        
        // execute each command line
        for (var i = 0; i < cmds.length; i++) {
            var cmdNode = cmds(i);
            var cmd = cmdNode.getAttribute("cmd");
            var timeout = cmdNode.getAttribute("timeout");
            
            if (timeout == null) {
                timeout = 0;
            } else {
                timeout = parseInt(timeout);
            }
            
            try {


                dinfo("executing command : " + cmd);

                var result = 0;
                result = exec(cmd, timeout);
                dinfo("command returned result: " + result);

                // if exit code is 0, return successfully
                if (result == 0) {
                    continue;
                }

                // search for exit code
                var exitNode = cmdNode.selectSingleNode("exit[@code='" +
                    result + "']");

                // check for special exit codes
                if (exitNode != null) {
                    if (exitNode.getAttribute("reboot") == "true") {
                        // this exit code forces a reboot
                        info("Command in installation of " + packageName +
                            " returned non-zero exit code [" + result + "]. This " +
                            "exit code requires an immediate reboot.");
                        reboot();
                    } else {
                        // this exit code is successful
                        info("Command in installation of " + packageName +
                            " returned non-zero exit code [" + result + "]. This " +
                            "exit code is not an error.");
                        continue;
                    }
                }

                // command did not succeed, throw error
                throw new Error(0, "Exit code returned non-successful value: " +
                    result + ".\n\n" + cmd);
            } catch (e) {
                throw new Error("Could not install " + packageName + ".\n" +
                    e.description);
            }
        }

        if (!checkInstalled(packageNode)) {
            throw new Error("Could not install " + packageName + ".\n" +
                            "Failed checking after installation.");
        }

    
	// append new node to local xml
	settings.appendChild(packageNode);
	saveXml(settings, settings_file);
    
	// reboot the system if this package is suppose to
	if (packageNode.getAttribute("reboot") == "true") {
	  info("Installation of " + packageName + " successful, system " +
	       "rebooting.");
	  reboot();
	} else {
	  info("Installation of " + packageName + " successful.");
	}
    }
}

/**
 * Upgrades the old package node to the new package node.
 */
function upgradePackage(oldPackageNode, newPackageNode) {
    info("Upgrading " + newPackageNode.getAttribute("name") + "...");
    var packageName = newPackageNode.getAttribute("name");
    
    // select command lines to install
    var cmds = newPackageNode.selectNodes("upgrade");
    
    // execute each command line
    for (var i = 0; i < cmds.length; i++) {
        var cmdNode = cmds(i);
        var cmd = cmdNode.getAttribute("cmd");
        var timeout = cmdNode.getAttribute("timeout");
        
        if (timeout == null) {
            timeout = 0;
        } else {
            timeout = parseInt(timeout);
        }
        
        try {
            dinfo("executing command : " + cmd);
            var result = 0;
            result = exec(cmd, timeout);
            dinfo("command returned result: " + result);


            // if exit code is 0, return successfully
            if (result == 0) {
                continue;
            }
            
            // search for exit code
            var exitNode = cmdNode.selectSingleNode("exit[@code='" + result +
                "']");
                
            // if found, command was successful
            if (exitNode != null) {
                info("Command in upgrade of " + packageName + " returned " +
                    "non-zero exit code [" + result + "]. This exit code " +
                    "is not an error.");
                continue;
            }

            // check for special exit codes
            if (exitNode != null) {
                if (exitNode.getAttribute("reboot") = "true") {
                    // this exit code forces a reboot
                    info("Command in upgrade of " + packageName + " returned " +
                        "non-zero exit code [" + result + "]. This exit code " +
                        "requires an immediate reboot.");
                    reboot();
                } else {
                    // this exit code is successful
                    info("Command in upgrade of " + packageName + " returned " +
                        "non-zero exit code [" + result + "]. This exit code " +
                        "is not an error.");
                    continue;
                }
            }
            
            // command did not succeed, throw error
            throw new Error(0, "Exit code returned non-successful value: " +
                result + ".\n\n" + cmd);
        } catch (e) {
            throw new Error("Could not upgrade " + packageName + ".\n" +
                e.description);
        }
    }


    if (!checkInstalled(newPackageNode)) {

        if (!checkInstalled(oldPackageNode)) {
            //remove old node
            settings.removeChild(oldPackageNode);
            saveXml(settings, settings_file);
        }

        throw new Error("Could not upgrade " + packageName + ". " +
                        "Failed checking after installation.");

    } else {
        // replace local node with new node
        settings.removeChild(oldPackageNode);
        settings.appendChild(newPackageNode);
        saveXml(settings, settings_file);
    }


    info("Upgrade of " + newPackageNode.getAttribute("name") + " to Rev. "+ newPackageNode.getAttribute("revision") + " successful.");
    
    // reboot the system if this package is suppose to
    if (newPackageNode.getAttribute("reboot") == "true") {
        reboot();
    }
}

/**
 * Removes the specified package node from the system.
 */
function removePackage(packageNode) {
    var  failure = false;

    var packageName = packageNode.getAttribute("name");
    info("Removing " + packageName + "...");
    
    // select command lines to remove
    var cmds = packageNode.selectNodes("remove");
    
    // execute each command line
    for (i = 0; i < cmds.length; i++) {
        var cmdNode = cmds(i);
        var cmd = cmdNode.getAttribute("cmd");
        var timeout = cmdNode.getAttribute("timeout");
        
        if (timeout == null) {
            timeout = 0;
        } else {
            timeout = parseInt(timeout);
        }
        
        try {
            dinfo("executing command : " + cmd);

            var result = exec(cmd, timeout);
            dinfo("command returned result: " + result);
            
            // if exit code is 0, return successfully
            if (result == 0) {
                continue;
            }
            
            // search for exit code
            var exitNode = cmdNode.selectSingleNode("exit[@code='" + result +
                "']");
                
            // if found, command was successful
            if (exitNode != null) {
                info("Command in removal of " + packageName + " returned " +
                    "non-zero exit code [" + result + "]. This exit code " +
                    "is not an error.");
                continue;
            }

            // check for special exit codes
            if (exitNode != null) {
                if (exitNode.getAttribute("reboot") = "true") {
                    // this exit code forces a reboot
                    info("Command in removal of " + packageName + " returned " +
                        "non-zero exit code [" + result + "]. This exit code " +
                        "requires an immediate reboot.");
                    reboot();
                } else {
                    // this exit code is successful
                    info("Command in removal of " + packageName + " returned " +
                        "non-zero exit code [" + result + "]. This exit code " +
                        "is not an error.");
                    continue;
                }
            }
            
            // command did not succeed, throw error
            throw new Error(0, "Exit code returned non-successful value: " +
                result + ".\n\n" + cmd);
        } catch (e) {
            failure = true;
            break;

//            throw new Error("Could not remove " + packageName + ". " +
//                e.description);
        }
    }
    

    if (!checkInstalled(packageNode)) {
        // remove package node from local xml
        settings.removeChild(packageNode);
        saveXml(settings, settings_file);
    } else {
        failure = true;

//        throw new Error("Could not remove " + packageName + ". " +
//                        "Check after removing failed.");
    }
        
    
    // log a nice informational message
    if (!failure) {
        info("Removal of " + packageNode.getAttribute("name") + " successful.");
    } else {
        info("Errors occurred while removing " + packageName + ". ");
        return;
    }
    
    // reboot the system if this package is suppose to
    if (packageNode.getAttribute("reboot") == "true") {
        reboot();
    }
}

/**
 * Returns an array of all package nodes that can be installed
 */
function getAllPackages() {
    // retrieve packages
    var settingsNodes = settings.selectNodes("package");
    var packagesNodes = packages.selectNodes("package");
    
    // concatenate both lists
    var packageNodes = uniqueAttributeNodes(packagesNodes, "id");
    
    var packageArray = new Array();

    for (var i = 0; i < packageNodes.length; i++) {
        var packageNode     = packageNodes[i];
            if (packageNode != null) {
		if (!searchArray(packageArray, packageNode)) {
                   // add the new node to the array 
                   packageArray.push(packageNode);
		}
            }
    }
    return packageArray;
}

/**
 * Returns an array of package nodes that should be applied to the current
 * profile.
 */
function getAvailablePackages() {
    // get array of all profiles that apply to the base profile
    var profileArray = getAvailableProfiles();


    // create new empty package array
    var packageArray = new Array();
    
    // add each profile's packages to the array
    for (var i in profileArray) {
        profileNode = profileArray[i];

        // search for package tags in each profile
        var packageNodes = profileNode.selectNodes("package");

        // append all the resulting profiles identified by profile-id
        for (var j = 0; j < packageNodes.length; j++) {
            var packageId = packageNodes(j).getAttribute("package-id");

            // grab the package node
            var packageNode = packages.selectSingleNode("package[@id='" +
                packageId + "']");

            // search array for pre-existing package, we don't want duplicates
            if (searchArray(packageArray, packageNode)) {
                continue;
            }

            // sometimes nodes can be null
            if (packageNode != null) {
		// add package-id dependencies 
		appendPackageDependencies(packageArray, packageNode);
		if (!searchArray(packageArray, packageNode)) {
                // add the new node to the array _after_ adding dependencies
                packageArray.push(packageNode);
            }
        }
            }
    }

    return packageArray;
}

/* nearly the same as appendProfileDependencies() but more relaxed on unknown
 * or invalid dependencies */
function appendPackageDependencies(packageArray, packageNode) {
    appendDependencies(packageArray, packageNode, packages, "package");
}

function appendDependencies(appendArray, appendNode, sourceArray, sourceName) {
    // search for package tags in each profile
    var dependsNodes = appendNode.selectNodes("depends");
    if (dependsNodes != null) {
	for (var i = 0; i < dependsNodes.length; i++) {
	    var dependsId = dependsNodes(i).getAttribute(sourceName + "-id");
	    // skip unknown entries 
	    if (dependsId == null) continue;

	    dinfo("Checking " + sourceName + " dependency: " + dependsId);
	    var dependsNode = sourceArray.selectSingleNode(sourceName + "[@id='" +
		dependsId + "']");

	    if (dependsNode == null) {
		throw new Error(0, "Invalid dependency \"" + dependsId +
			"\" from " + sourceName +  " \"" + appendNode.getAttribute("id") 
			+ "\".");
	    }
	    // duplicate check 
	    if (searchArray(appendArray, dependsNode)) {
                        continue;
                    } else {
		dinfo("Add " + sourceName + " dependecy: " + dependsId);
		appendArray.push(dependsNode);
		appendDependencies(appendArray, dependsNode, sourceArray, sourceName);
                }
        }
    }
}

/**
 * Returns an array of profile nodes that should be applied to the current
 * profile.
 */
function getAvailableProfiles() {
    // create array to hold available package nodes
    var profileArray = new Array();
    
    // acquire the node of the current profile
    var profileNode = profiles.selectSingleNode("profile[@id='" + profile +
        "']");

    dinfo("profile: " + profile + " profileNode: " + profileNode);
        
    // add the current profile's node as the first element in the array
    profileArray.push(profileNode);
    
    // append dependencies of the current profile to the list (recursive)
    appendProfileDependencies(profileArray, profileNode);
    
    return profileArray;
}

/**
 * Appends dependent profile nodes of the specified profile to the specifed
 * array. Recurses into self to get an entire dependency tree.
 */
function appendProfileDependencies(profileArray, profileNode) {
    appendDependencies(profileArray, profileNode, profiles, "profile");
}

/**
 * Scans the specified array for the specified element and returns true if
 * found.
 */
function searchArray(array, element) {
    for (var i in array) {
        var e = array[i];
        if (element == e) {
            return true;
        }
    }
    
    return false;
}

/**
 * Scans the specified list for the specified element and returns true if
 * found.
 */
function searchList(list, element) {
    for (var i = 0; i < list.length; i++) {
        var e = list(i);
        if (element == e) {
            return true;
        }
    }
    
    return false;
}

/**
 * Returns a new array of nodes unique by the specified attribute.
 */
function uniqueAttributeNodes(nodes, attribute) {
    // hold unique nodes in a new array
    var newNodes = new Array();
    
    // loop over nodes
    for (var i = 0; i < nodes.length; i++) {
        var node = nodes[i];
        var val = node.getAttribute(attribute);
        
        // determine if node with attribute already exists
        var found = false;
        for (var j = 0; j < newNodes.length; j++) {
            var newVal = newNodes[j].getAttribute(attribute);
            if (val == newVal) {
                found = true;
                break;
            }
        }
        
        // if it doesn't exist, add it
        if (!found) {
            newNodes.push(node);
        }
    }
    
    return newNodes;
}

/**
 * Combines one list and another list into a single array.
 */
function concatenateList(list1, list2) {
    // create a new array the size of the sum of both original lists
    var list = new Array();
    
    for (var i = 0; i < list1.length; i++) {
        list.push(list1(i));
    }
    
    for (var i = 0; i < list2.length; i++) {
        list.push(list2(i));
    }
    
    return list;
}

/**
 * Remove duplicate items from an array.
 */
function uniqueArray(array) {
    // hold unique elements in a new array
    var newArray = new Array();
    
    // loop over elements
    for (var i = 0; i < array.length; i++) {
        var found = false;
        for (var j = 0; j < newArray.length; j++) {
            if (array[i] == newArray[j]) {
                found = true;
                break;
            }
        }
        
        if (!found) {
            newArray.push(array[i]);
        }
    }
    
    return newArray;
}


/**
 * Retrieves profile from given "hosts" XML document.
 * Searches for node having attribute "name" matching
 * given hostName. Returns it's attribute "profile-id".
 *
 * Check is performed using regular expression object:
 * "name" attribute value as the pattern and 
 * hostName as matched string.
 * First matching profile is returned.
 */

function retrieveProfile(hosts, hostName) {

    if (null == hostName) {
        //error! lack of attribute "profile-id"
        throw new Error("Error! Lack of host name: " + hostName + ".");
    }


    var hostNodes = hosts.selectNodes("host");
    var i;
    var node;

    var attrName;
    var attrProfile;

    for (i=0; i<hostNodes.length; ++i) {
        node = hostNodes[i];
        if (null != node) {
            attrName = node.getAttribute("name");
            if (null != attrName) {
                if (hostName.toUpperCase() == attrName.toUpperCase()) {

                    attrProfile = node.getAttribute("profile-id");

                    if (null == attrProfile) {
                        //error! lack of attribute "profile-id"
                        throw new Error("Error! Lack of attribute \"profile-id\" for host description " + 
                            attrName + ".");
                    }

                    return attrProfile;
                }
            } else {
                //error! lack of attribute "name"
            }
        }
    }



    for (i=0; i<hostNodes.length; ++i) {
        node = hostNodes[i];

        if (null != node) {
            attrName = node.getAttribute("name");

            if (null != attrName) {
                var reg = new RegExp("^" + attrName + "$", "i");

                if (reg.test(hostName)) {
                    attrProfile = node.getAttribute("profile-id");

                    if (null == attrProfile) {
                        //error! lack of attribute "profile-id"
                        throw new Error("Error! Lack of attribute \"profile-id\" for host description " + 
                            attrName + ".");
                    }

                    return attrProfile;
                }
            } else {
                //error! lack of attribute "name"
            }
        }
    }

    throw new Error("Could not find profile for host " + hostName + ".");
}
/**
 * Loads an XML file and returns the root element.
 */
function loadXml( xmlPath, xslPath ) {
	var source = new ActiveXObject("Msxml2.DOMDocument.3.0");
	source.async = false;
	source.validateOnParse = false;
	source.load( xmlPath );
	
	if (source.parseError.errorCode != 0) {
	   var myErr = source.parseError;
	   info("Error parsing xml: " + myErr.reason );
           info("File      " + xmlPath);
           info("Line      " + myErr.line);
           info("Linepos   " + myErr.linepos);
           info("Filepos   " + myErr.filepos);
           info("srcText   " + myErr.srcText);
	   
	   exit(2);
	}
	else {
		if( xslPath != null ) {
		  try {
			var xmlDoc = new ActiveXObject("Msxml2.DOMDocument.3.0")
			xmlDoc.async="false"
			xmlDoc.validateOnParse = false;
			xmlDoc.loadXML( source.transformNode( xslPath ) );
			return xmlDoc.documentElement;
		  } catch (e) {
		  	if (quitonerror) {
                  	  throw new Error("Error reading file: " + xmlPath +
                          "\n\n" + e.description);
		  	} else {
err_summary += "\n\nError reading file: " + xmlPath + "\n\n" + e.description;
				return source.documentElement;
			}
		   }
		}
		else {
			return source.documentElement;
		}
	}
}

/**
 * Creates xsl document object and returns it.
 */
function createXsl( base, folder ) {
	var fso = new ActiveXObject("Scripting.FileSystemObject");
	var file;
	if( !fso.folderExists( base + "\\" + folder ) ) {
		return null;
	}
	var e = new Enumerator(fso.GetFolder( base + "\\" + folder ).files);
	var str = "";
	var root = "";
	if( folder == "hosts" ) {
		root = "wpkg";
	}
	else {
		root = folder;
	}

	str = "<?xml version=\"1.0\"?>\r\n";
	str += "<xsl:stylesheet xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\" version=\"1.0\">\r\n";
	str += "	<xsl:output encoding=\"ISO-8859-1\" indent=\"yes\" method=\"xml\" version=\"1.0\"/>\r\n";
	str += "	<xsl:template match=\"/\">\r\n";
	str += "		<" + root + ">\r\n";
	str += "			<xsl:copy-of select=\""+ root + "/child::*\"/>\r\n";
	for( e.moveFirst(); ! e.atEnd(); e.moveNext() ) {
		file = e.item();
		var DotSpot = file.name.toString().lastIndexOf('.');
		var extension = file.name.toString().substr(DotSpot + 1,file.name.toString().length);

		if(extension == "xml") {
				str = str + "			<xsl:copy-of select=\"document('" + 
					base.replace( /\\/g, "/" ) + "/" + folder + "/" + file.name + 
					"')/" + root + "/child::*\"/>\r\n";
		}
	}
	str += "		</" + root + ">\r\n";
	str += "	</xsl:template>\r\n";
	str += "</xsl:stylesheet>\r\n";
	var xsl = new ActiveXObject( "Msxml2.DOMDocument.3.0" );
	xsl.async = false;
	xsl.loadXML( str );
	return xsl.documentElement;
}

/**
 * Saves the root element to the specified XML file.
 */
function saveXml(root, path) {
    if (dryrun) {
        path += ".dryrun";
    }
    dinfo("saving XML : " + path);
    var xmlDoc = new ActiveXObject("Msxml2.DOMDocument.3.0");
    xmlDoc.appendChild(root);
    if (xmlDoc.save(path)) {
        throw new Error(0, "Could not save XML document to " + path);
    }
}

/**
 * Creates a new root element of the specified name.
 */
function createXml(root) {
    var xmlDoc = new ActiveXObject("Msxml2.DOMDocument.3.0");

//    xmlDoc.createNode(1, root, "");
//    return xmlDoc;

    return xmlDoc.createNode(1, root, "");
}

/*******************************************************************************
 *
 * Miscellaneous functions
 *
 ******************************************************************************/

/**
 * Echos text to the command line or a prompt depending on how the program is
 * run.
 */
function alert(msg) {
    WScript.Echo(msg);
}

/**
 * Logs the specified event type and description in the Windows event log.
 */
function log(type, description) {
    WshShell = WScript.CreateObject("WScript.Shell");
    WshShell.logEvent(type, description);
}

/**
 * Logs or presents an error message depending on interactivity.
 */
function error(message) {
    if (quiet) {
        log(1, message);
    } else {
        alert(message);
    }
}

/**
 * Logs or presents an info message depending on interactivity.
 */
function info(message) {
    if (quiet) {
        log(4, message);
    } else {
        alert(message);
    }
}

/**
 * Executes a shell command and blocks until it is completed, returns the
 * program's exit code. Command times out and is terminated after the
 * specified number of seconds.
 */
function exec(cmd, timeout) {

    if (dryrun) {
        return 0;
    }

    try {
        var shell = new ActiveXObject("WScript.Shell");
        
        // timeout after an hour by default
        if (timeout == 0) {
            timeout = 3600;
        }
        
        var shellExec = shell.exec(cmd);
        
        var count = 0;
        while (shellExec.status == 0) {
            WScript.sleep(1000);
            count++;
            
            if (count >= timeout) {
                return -1;
            }
        }
        
        WScript.sleep(1000);
        
        return shellExec.exitCode;
    } catch (e) {
        throw new Error(0, "Command \"" + cmd
            + "\" was not successful.\n" + e.description);
    }
}

/**
 * Notifies the user/computer with a pop up message.
 */
function notify(message) {
    if (!nonotify) {
	var cmd = "";
        cmd += "%SystemRoot%\\System32\\NET.EXE SEND ";
        cmd += host;
        cmd += " \"" + message + "\"";
        try {
    	    exec(cmd, 0);
        } catch (e) {
    	    throw new Error(0, "Notification failed. " + e.description);
        }
    } else {
	info("User notification suppressed.");
    }
}

/**
 * Notifies the user/computer with a pop up message.

function notify(message) {
    var cmd = "";
    cmd += "%SystemRoot%\\System32\\NET.EXE SEND ";
    cmd += host;
    cmd += " \"" + message + "\"";
    try {
        exec(cmd, 0);
    } catch (e) {
        throw new Error(0, "Notification failed. " + e.description);
    }
}
 */
/**
 * Reboots the system.
  */
function reboot() {
    if (!noreboot ) {
      switch (rebootCmd) {
        case "standard":
		{	       
		  var wmi = GetObject("winmgmts:{(Shutdown)}//./root/cimv2");
		  var win = wmi.ExecQuery("select * from Win32_OperatingSystem where Primary=true");
		  var e = new Enumerator(win);
	
		  info("System reboot in progress!");
	
		  for (; !e.atEnd(); e.moveNext()) {
		    var x = e.item();
		    x.win32Shutdown(6);
		  }
	        }
		break;
        case "special":
                       psreboot();
                       break;
	default:
      var fso = new ActiveXObject("Scripting.FileSystemObject");
          	if (!fso.fileExists(rebootCmd)) {
                    var path = WScript.ScriptFullName;
                    base = fso.GetParentFolderName(path);
        	    rebootCmd = fso.BuildPath(base, rebootCmd);
        	    if (!fso.fileExists(rebootCmd)) {
        	      throw new Error("Could not locate rebootCmd " + rebootCmd + ".");
		    } 
		} 
          	info("Running a shutdown command: "+rebootCmd);
          	exec(rebootCmd,0); 
	  	break;
	}
/**    } else if (pretend) {
	info("REBOOT");
*/
    } else {
	info("System reboot was initiated but overridden.");
    }

    exit(0);
}

/**
 * Reboots the system.
 */
function psreboot() {
    if (!noreboot ) {

    // RFL prefers shutdown tool to this method: allows user to cancel
    // if required, but we loop for ever until they give in!
    var i;
    var cmd;
    var msg="Rebooting to complete software installation. Please note that "+
            "some software might not work until the machine is rebooted."
    // overwrites global variable rebootcmd !   
    var rebootCmd="tools\\psshutdown.exe"
    var fso = new ActiveXObject("Scripting.FileSystemObject");
    	if (!fso.fileExists(rebootCmd)) {
            var path = WScript.ScriptFullName;
            base = fso.GetParentFolderName(path);
            rebootCmd = fso.BuildPath(base, rebootCmd);
            if (!fso.fileExists(rebootCmd)) {
              throw new Error("Could not locate rebootCmd " + rebootCmd + ".");
	    } 
	} 
    var shutdown=rebootCmd + " -r ";

    for (i=60; i!=0; i=i-1) {
        // This could be cancelled
        cmd=shutdown+" -c -m \"" +msg+ "\" -t "+i;
        info("Running a shutdown command: "+cmd);
        exec(cmd,0);
        WScript.Sleep(i*1000);
    }
    // Hmm. We're still alive. Let's get more annoying.
    for (i=60; i!=0; i=i-3) {
        cmd=shutdown+" -m \"" + msg + "\" -t "+i;
        info("Running a shutdown command: "+cmd);
        exec(cmd,0);
        WScript.Sleep(i*1000);
    }
    // And if we're here, there's problem.
    notify("This machine needs to reboot.");

/** } else if (pretend) {
    info("REBOOT");
 */
    } else {
        info("System reboot was initiated but overridden.");
    }

    exit(0);
}

/**
 * Ends program execution with the specified exit code.
 */
function exit(exitCode) {
    if (exportRunningState) {
	// reset running state 
	setRunningState("false");
    }

if (err_summary != "") {
info( "\n\nThere were the following errors:\n" + err_summary );
exitCode = 1;
}
    WScript.Quit(exitCode);
}
/**
 * Show the user a list of packages that can be updated.
 */
function queryUpgradablePackages() {
    // retrieve currently installed and installable nodes
    var installedNodes = settings.selectNodes("package");
    var availableNodes = packages.selectNodes("package");

    // create a string to append package descriptions to
    var message = new String();

    for (var i = 0; i < installedNodes.length; i++) {
        var installedNode       = installedNodes(i);
        var instPackageId       = installedNode.getAttribute("id");
        var instPackageRevision = installedNode.getAttribute("revision");
	var instPackageExecAttr = installedNode.getAttribute("execute");
	if (instPackageExecAttr == "") {
	    instPackageExecAttr = "none";
	}
        for (var j = 0; j < availableNodes.length; j++) {
            var availableNode        = availableNodes(j);
            var availPackageId       = availableNode.getAttribute("id");
            var availPackageRevision = availableNode.getAttribute("revision");
            if (instPackageId == availPackageId) {
                if (instPackageRevision < availPackageRevision) {
                    message += availableNode.getAttribute("name") + "\n";
                    message += "    ID:           " + instPackageId + "\n";
                    message += "    Old Revision: " + instPackageRevision + "\n";
                    message += "    New Revision: " + availableNode.getAttribute("revision") + "\n";
			  message += "    ExecAttribs:  " + instPackageExecAttr + "\n";
                    message += "    Status:       updatable\n";
                    message += "\n";
                }
            }
        }
    }
    info(message);
}

/**
 * Show the user information about a specific package.
 */
function queryPackage(pack) {
    // retrieve packages
    var settingsNodes = settings.selectNodes("package");
    var packagesNodes = packages.selectNodes("package");

    // concatenate both lists
    var packageNodes = concatenateList(settingsNodes, packagesNodes);
    var packageNodes = uniqueAttributeNodes(packageNodes, "id");

    // create a string to append package descriptions to
    var message = new String();

    for (var i = 0; i < packageNodes.length; i++) {
        var packageNode     = packageNodes[i];
        var packageReboot   = packageNode.getAttribute("reboot");
        var packageName     = packageNode.getAttribute("name");
        var packageId       = packageNode.getAttribute("id");
	var packageExecAttr = packageNode.getAttribute("execute");
        if (packageReboot != "true") {
            packageReboot = "false";
        }
	if (packageExecAttr == "") {
	    packageExecAttr = "none";
	}
        if (packageName == pack || packageId == pack) {
            message += packageName + "\n";
            message += "    ID:         " + packageId + "\n";
            message += "    Revision:   " + packageNode.getAttribute("revision") + "\n";
            message += "    Reboot:     " + packageReboot + "\n";
	    message += "    ExecAttribs:" + packageExecAttr + "\n";
            if (searchList(settingsNodes, packageNode)) {
                message += "    Status:     Installed\n";
            } else {
                message += "    Status:     Not Installed\n";
            }
            message += "\n";
        }
    }
    info(message);
}

