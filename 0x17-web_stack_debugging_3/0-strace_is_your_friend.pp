# Fixes a wordpress bug

file_line { 'Fix-wordpress':
  path    => '/home/vagrant/ALX/alx-system_engineering-devops/0x17-web_stack_debugging_3/wp-settings.php',
  line    => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
  match   => '^require_once\( ABSPATH \. WPINC \. \'/class-wp-locale\.phpp\' \);$',
}
