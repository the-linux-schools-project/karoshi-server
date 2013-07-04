<?php defined('MOODLE_INTERNAL') || die();
 $configuration = array (
  'siteidentifier' => 'cc9d5997aedb714d84941591638b0186',
  'stores' => 
  array (
    'default_application' => 
    array (
      'name' => 'default_application',
      'plugin' => 'file',
      'configuration' => 
      array (
      ),
      'features' => 14,
      'modes' => 3,
      'default' => true,
      'class' => 'cachestore_file',
      'lock' => 'cachelock_file_default',
    ),
    'default_session' => 
    array (
      'name' => 'default_session',
      'plugin' => 'session',
      'configuration' => 
      array (
      ),
      'features' => 14,
      'modes' => 2,
      'default' => true,
      'class' => 'cachestore_session',
      'lock' => 'cachelock_file_default',
    ),
    'default_request' => 
    array (
      'name' => 'default_request',
      'plugin' => 'static',
      'configuration' => 
      array (
      ),
      'features' => 6,
      'modes' => 4,
      'default' => true,
      'class' => 'cachestore_static',
      'lock' => 'cachelock_file_default',
    ),
  ),
  'modemappings' => 
  array (
    0 => 
    array (
      'mode' => 1,
      'store' => 'default_application',
      'sort' => -1,
    ),
    1 => 
    array (
      'mode' => 2,
      'store' => 'default_session',
      'sort' => -1,
    ),
    2 => 
    array (
      'mode' => 4,
      'store' => 'default_request',
      'sort' => -1,
    ),
  ),
  'definitions' => 
  array (
    'core/string' => 
    array (
      'mode' => 1,
      'simplekeys' => true,
      'simpledata' => true,
      'persistent' => true,
      'persistentmaxsize' => 3,
      'component' => 'core',
      'area' => 'string',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/databasemeta' => 
    array (
      'mode' => 1,
      'requireidentifiers' => 
      array (
        0 => 'dbfamily',
      ),
      'persistent' => true,
      'persistentmaxsize' => 2,
      'component' => 'core',
      'area' => 'databasemeta',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/eventinvalidation' => 
    array (
      'mode' => 1,
      'persistent' => true,
      'requiredataguarantee' => true,
      'simpledata' => true,
      'component' => 'core',
      'area' => 'eventinvalidation',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/questiondata' => 
    array (
      'mode' => 1,
      'simplekeys' => true,
      'requiredataguarantee' => false,
      'datasource' => 'question_finder',
      'datasourcefile' => 'question/engine/bank.php',
      'component' => 'core',
      'area' => 'questiondata',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/htmlpurifier' => 
    array (
      'mode' => 1,
      'component' => 'core',
      'area' => 'htmlpurifier',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/config' => 
    array (
      'mode' => 1,
      'persistent' => true,
      'simpledata' => true,
      'component' => 'core',
      'area' => 'config',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/groupdata' => 
    array (
      'mode' => 1,
      'simplekeys' => true,
      'simpledata' => true,
      'persistent' => true,
      'persistmaxsize' => 2,
      'component' => 'core',
      'area' => 'groupdata',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/calendar_subscriptions' => 
    array (
      'mode' => 1,
      'simplekeys' => true,
      'simpledata' => true,
      'persistent' => true,
      'component' => 'core',
      'area' => 'calendar_subscriptions',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/yuimodules' => 
    array (
      'mode' => 1,
      'component' => 'core',
      'area' => 'yuimodules',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/plugintypes' => 
    array (
      'mode' => 1,
      'simplekeys' => true,
      'simpledata' => true,
      'persistent' => true,
      'persistmaxsize' => 2,
      'component' => 'core',
      'area' => 'plugintypes',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/pluginlist' => 
    array (
      'mode' => 1,
      'simplekeys' => true,
      'simpledata' => true,
      'persistent' => true,
      'persistentmaxsize' => 2,
      'component' => 'core',
      'area' => 'pluginlist',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/plugininfo_base' => 
    array (
      'mode' => 1,
      'simplekeys' => true,
      'simpledata' => true,
      'persistent' => true,
      'persistentmaxsize' => 2,
      'component' => 'core',
      'area' => 'plugininfo_base',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/plugininfo_mod' => 
    array (
      'mode' => 1,
      'simplekeys' => true,
      'simpledata' => true,
      'persistent' => true,
      'persistentmaxsize' => 1,
      'component' => 'core',
      'area' => 'plugininfo_mod',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/plugininfo_block' => 
    array (
      'mode' => 1,
      'simplekeys' => true,
      'simpledata' => true,
      'persistent' => true,
      'persistentmaxsize' => 1,
      'component' => 'core',
      'area' => 'plugininfo_block',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/plugininfo_filter' => 
    array (
      'mode' => 1,
      'simplekeys' => true,
      'simpledata' => true,
      'persistent' => true,
      'persistentmaxsize' => 1,
      'component' => 'core',
      'area' => 'plugininfo_filter',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/plugininfo_repository' => 
    array (
      'mode' => 1,
      'simplekeys' => true,
      'simpledata' => true,
      'persistent' => true,
      'persistentmaxsize' => 1,
      'component' => 'core',
      'area' => 'plugininfo_repository',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/plugininfo_portfolio' => 
    array (
      'mode' => 1,
      'simplekeys' => true,
      'simpledata' => true,
      'persistent' => true,
      'persistentmaxsize' => 1,
      'component' => 'core',
      'area' => 'plugininfo_portfolio',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/coursecattree' => 
    array (
      'mode' => 1,
      'persistent' => true,
      'invalidationevents' => 
      array (
        0 => 'changesincoursecat',
      ),
      'component' => 'core',
      'area' => 'coursecattree',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/coursecat' => 
    array (
      'mode' => 2,
      'persistent' => true,
      'invalidationevents' => 
      array (
        0 => 'changesincoursecat',
        1 => 'changesincourse',
      ),
      'ttl' => 600,
      'component' => 'core',
      'area' => 'coursecat',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/coursecatrecords' => 
    array (
      'mode' => 4,
      'simplekeys' => true,
      'persistent' => true,
      'invalidationevents' => 
      array (
        0 => 'changesincoursecat',
      ),
      'component' => 'core',
      'area' => 'coursecatrecords',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/coursecontacts' => 
    array (
      'mode' => 1,
      'persistent' => true,
      'simplekeys' => true,
      'component' => 'core',
      'area' => 'coursecontacts',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
    'core/repositories' => 
    array (
      'mode' => 4,
      'persistent' => true,
      'component' => 'core',
      'area' => 'repositories',
      'selectedsharingoption' => 2,
      'userinputsharingkey' => '',
    ),
  ),
  'definitionmappings' => 
  array (
  ),
  'locks' => 
  array (
    'cachelock_file_default' => 
    array (
      'name' => 'cachelock_file_default',
      'type' => 'cachelock_file',
      'dir' => 'filelocks',
      'default' => true,
    ),
  ),
);