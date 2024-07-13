# Install and configure an Nginx server

exec { 'update':
  path    => '/usr/bin/:',
  command => 'apt update && apt -y upgrade',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

exec { 'configure_firewall':
  command => 'ufw allow "Nginx HTTP"',
  onlyif  => 'ufw --version',
  path    => '/usr/bin/:',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [Exec['configure_firewall'], Package['nginx']],
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
  require => Package['nginx'],
}

file_line { 'nginx_custom_header':
  path    => '/etc/nginx/sites-available/default',
  line    => 'add_header X-Served-By $hostname always;',
  after   => 'listen 80 default_server;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file_line { 'nginx_redirect':
  path    => '/etc/nginx/sites-available/default',
  line    => 'location /redirect_me { return 301 https://www.alxafrica.com; }',
  after   => 'server_name _;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file_line { 'nginx_error_page':
  path    => '/etc/nginx/sites-available/default',
  line    => 'error_page 404 /404.html;',
  after   => 'server_name _;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file_line { 'nginx_404_location':
  path    => '/etc/nginx/sites-available/default',
  line    => 'location = /404.html { internal; }',
  after   => 'error_page 404 /404.html;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

exec { 'reload_nginx':
  command     => 'nginx -s reload',
  refreshonly => true,
  subscribe   => File_line['nginx_custom_header'],
}

exec { 'check_nginx_status':
  command => 'curl -I http://localhost 2>/dev/null | grep -q "200 OK"',
  unless  => 'curl -I http://localhost 2>/dev/null | grep -q "200 OK"',
  path    => '/usr/bin/:',
  require => Service['nginx'],
}

