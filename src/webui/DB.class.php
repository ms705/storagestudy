<?php

class DB extends PDO
{
   public function __construct($file = 'db_settings.ini') {
      if (!$settings = parse_ini_file($file, TRUE)) throw new Exception('Unable to open ' . $file . '.');

      $dsn = $settings['database']['driver'] . 
               ':host=' . $settings['database']['host'] .
               ((!empty($settings['database']['port'])) ? (';port=' . $settings['database']['port']) : '') .
               ';dbname=' . $settings['database']['dbname'];
      
      parent::__construct($dsn, $settings['database']['username'], $settings['database']['password']);
   }
}

?>

