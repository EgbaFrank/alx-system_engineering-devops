# Fixes a wordpress bug

exec { 'Fix-wordpress-phpp':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/usr/bin:/bin',
}
