<?php

// DB config
define('SS_DATABASE_CLASS', 'PostgreSQLDatabase');
define('SS_DATABASE_SERVER', 'localhost');
define('SS_DATABASE_USERNAME', 'admin');
define('SS_DATABASE_PASSWORD', 'admin');
define('SS_DATABASE_NAME', 'silverstripe');

define('SS_DEFAULT_ADMIN_USERNAME', 'admin');
define('SS_DEFAULT_ADMIN_PASSWORD', 'admin');

// Environment config
define('SS_ENVIRONMENT_TYPE', 'dev');


// CLI config
global $_FILE_TO_URL_MAPPING;
$_FILE_TO_URL_MAPPING['/silverstripe'] = 'http://localhost:8888';
