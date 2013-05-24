<?php
/** NOTE **
 ** Make sure that <?php is the FIRST line of this file!
 ** IE: There should NOT be any blank lines or spaces BEFORE <?php
 **/

/**
 * The phpLDAPadmin config file
 * See: http://phpldapadmin.sourceforge.net/wiki/index.php/Config.php
 *
 * This is where you can customise some of the phpLDAPadmin defaults
 * that are defined in config_default.php.
 *
 * To override a default, use the $config->custom variable to do so.
 * For example, the default for defining the language in config_default.php
 *
 * $this->default->appearance['language'] = array(
 *  'desc'=>'Language',
 *  'default'=>'auto');
 *
 * to override this, use $config->custom->appearance['language'] = 'en_EN';
 *
 * This file is also used to configure your LDAP server connections.
 *
 * You must specify at least one LDAP server there. You may add
 * as many as you like. You can also specify your language, and
 * many other options.
 *
 * NOTE: Commented out values in this file prefixed by //, represent the
 * defaults that have been defined in config_default.php.
 * Commented out values prefixed by #, dont reflect their default value, you can
 * check config_default.php if you want to see what the default is.
 *
 * DONT change config_default.php, you changes will be lost by the next release
 * of PLA. Instead change this file - as it will NOT be replaced by a new
 * version of phpLDAPadmin.
 */

/*********************************************/
/* Useful important configuration overrides  */
/*********************************************/

/* If you are asked to put PLA in debug mode, this is how you do it: */
#  $config->custom->debug['level'] = 255;
#  $config->custom->debug['syslog'] = true;
#  $config->custom->debug['file'] = '/tmp/pla_debug.log';

/* phpLDAPadmin can encrypt the content of sensitive cookies if you set this
   to a big random string. */
// $config->custom->session['blowfish'] = null;

/* The language setting. If you set this to 'auto', phpLDAPadmin will attempt
   to determine your language automatically. Otherwise, available lanaguages
   are: 'ct', 'de', 'en', 'es', 'fr', 'it', 'nl', and 'ru'
   Localization is not complete yet, but most strings have been translated.
   Please help by writing language files. See lang/en.php for an example. */
// $config->custom->appearance['language'] = 'auto';

/* The temporary storage directory where we will put jpegPhoto data
   This directory must be readable and writable by your web server. */
// $config->custom->jpeg['tmpdir'] = '/tmp';     // Example for Unix systems
#  $config->custom->jpeg['tmpdir'] = 'c:\\temp'; // Example for Windows systems

/* Set this to (bool)true if you do NOT want a random salt used when
   calling crypt().  Instead, use the first two letters of the user's
   password.  This is insecure but unfortunately needed for some older
   environments. */
#  $config->custom->password['no_random_crypt_salt'] = true;

/* PHP script timeout control. If php runs longer than this many seconds then
   PHP will stop with an Maximum Execution time error. Increase this value from
   the default if queries to your LDAP server are slow. The default is either
   30 seconds or the setting of max_exection_time if this is null. */
// $config->custom->session['timelimit'] = 30;

/* Our local timezone
   This is to make sure that when we ask the system for the current time, we
   get the right local time. If this is not set, all time() calculations will
   assume UTC if you have not set PHP date.timezone. */
// $config->custom->appearance['timezone'] = null;
#  $config->custom->appearance['timezone'] = 'Australia/Melbourne';

/*********************************************/
/* Commands                                  */
/*********************************************/

/* Command availability ; if you don't authorize a command the command
   links will not be shown and the command action will not be permitted.
   For better security, set also ACL in your ldap directory. */
/*
$config->custom->commands['cmd'] = array(
	'entry_internal_attributes_show' => true,
	'entry_refresh' => true,
	'oslinks' => true,
	'switch_template' => true
);

$config->custom->commands['script'] = array(
	'add_attr_form' => true,
	'add_oclass_form' => true,
	'add_value_form' => true,
	'collapse' => true,
	'compare' => true,
	'compare_form' => true,
	'copy' => true,
	'copy_form' => true,
	'create' => true,
	'create_confirm' => true,
	'delete' => true,
	'delete_attr' => true,
	'delete_form' => true,
	'draw_tree_node' => true,
	'expand' => true,
	'export' => true,
	'export_form' => true,
	'import' => true,
	'import_form' => true,
	'login' => true,
	'logout' => true,
	'login_form' => true,
	'mass_delete' => true,
	'mass_edit' => true,
	'mass_update' => true,
	'modify_member_form' => true,
	'monitor' => true,
	'purge_cache' => true,
	'query_engine' => true,
	'rename' => true,
	'rename_form' => true,
	'rdelete' => true,
	'refresh' => true,
	'schema' => true,
	'server_info' => true,
	'show_cache' => true,
	'template_engine' => true,
	'update_confirm' => true,
	'update' => true
);
*/

/*********************************************/
/* Appearance                                */
/*********************************************/

/* If you want to choose the appearance of the tree, specify a class name which
   inherits from the Tree class. */
// $config->custom->appearance['tree'] = 'AJAXTree';
#  $config->custom->appearance['tree'] = 'HTMLTree';

/* Just show your custom templates. */
$config->custom->appearance['custom_templates_only'] = true;

/* Disable the default template. */
// $config->custom->appearance['disable_default_template'] = false;

/* Hide the warnings for invalid objectClasses/attributes in templates. */
$config->custom->appearance['hide_template_warning'] = true;

/* Configure what objects are shown in left hand tree */
// $config->custom->appearance['tree_filter'] = '(objectclass=*)';

/* The height and width of the tree. If these values are not set, then
   no tree scroll bars are provided. */
// $config->custom->appearance['tree_height'] = null;
#  $config->custom->appearance['tree_height'] = 600;
// $config->custom->appearance['tree_width'] = null;
#  $config->custom->appearance['tree_width'] = 250;

/*********************************************/
/* User-friendly attribute translation       */
/*********************************************/

/* Use this array to map attribute names to user friendly names. For example, if
   you don't want to see "facsimileTelephoneNumber" but rather "Fax". */
// $config->custom->appearance['friendly_attrs'] = array();
$config->custom->appearance['friendly_attrs'] = array(
	'facsimileTelephoneNumber' => 'Fax',
	'gid'                      => 'Group',
	'mail'                     => 'Email',
	'telephoneNumber'          => 'Telephone',
	'uid'                      => 'User Name',
	'userPassword'             => 'Password'
);

/*********************************************/
/* Hidden attributes                         */
/*********************************************/

/* You may want to hide certain attributes from being edited. If you want to
   hide attributes from the user, you should use your LDAP servers ACLs.
   NOTE: The user must be able to read the hide_attrs_exempt entry to be
   excluded. */
// $config->custom->appearance['hide_attrs'] = array();
#  $config->custom->appearance['hide_attrs'] = array('objectClass');

/* Members of this list will be exempt from the hidden attributes.*/
// $config->custom->appearance['hide_attrs_exempt'] = null;
#  $config->custom->appearance['hide_attrs_exempt'] = 'cn=PLA UnHide,ou=Groups,c=AU';

/*********************************************/
/* Read-only attributes                      */
/*********************************************/

/* You may want to phpLDAPadmin to display certain attributes as read only,
   meaning that users will not be presented a form for modifying those
   attributes, and they will not be allowed to be modified on the "back-end"
   either. You may configure this list here:
   NOTE: The user must be able to read the readonly_attrs_exempt entry to be
   excluded. */
// $config->custom->appearance['readonly_attrs'] = array();

/* Members of this list will be exempt from the readonly attributes.*/
// $config->custom->appearance['readonly_attrs_exempt'] = null;
#  $config->custom->appearance['readonly_attrs_exempt'] = 'cn=PLA ReadWrite,ou=Groups,c=AU';

/*********************************************/
/* Group attributes                          */
/*********************************************/

/* Add "modify group members" link to the attribute. */
// $config->custom->modify_member['groupattr'] = array('member','uniqueMember','memberUid');

/* Configure filter for member search. This only applies to "modify group members" feature */
// $config->custom->modify_member['filter'] = '(objectclass=Person)';

/* Attribute that is added to the group member attribute. */
// $config->custom->modify_member['attr'] = 'dn';

/* For Posix attributes */
// $config->custom->modify_member['posixattr'] = 'uid';
// $config->custom->modify_member['posixfilter'] = '(uid=*)';
// $config->custom->modify_member['posixgroupattr'] = 'memberUid';

/*********************************************/
/* Support for attrs display order           */
/*********************************************/

/* Use this array if you want to have your attributes displayed in a specific
   order. You can use default attribute names or their fridenly names.
   For example, "sn" will be displayed right after "givenName". All the other
   attributes that are not specified in this array will be displayed after in
   alphabetical order. */
// $config->custom->appearance['attr_display_order'] = array();
#  $config->custom->appearance['attr_display_order'] = array(
#   'givenName',
#   'sn',
#   'cn',
#   'displayName',
#   'uid',
#   'uidNumber',
#   'gidNumber',
#   'homeDirectory',
#   'mail',
#   'userPassword'
#  );

/*********************************************/
/* Define your LDAP servers in this section  */
/*********************************************/

$servers = new Datastore();

/* $servers->NewServer('ldap_pla') must be called before each new LDAP server
   declaration. */

$servers->newServer('ldap_pla');
$servers->setValue('server','name','Samba4 AD Server');
$servers->setValue('server','host','ldapi://%2Fvar%2Flib%2Fsamba%2Fprivate%2Fldapi');
$servers->setValue('login','auth_type','session');
$servers->setValue('login','attr','dn');
$servers->SetValue('login','bind_id','cn=Administrator,cn=Users,CHANGETHISBASE');

?>
