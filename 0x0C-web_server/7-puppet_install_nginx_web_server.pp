# Install and configure an Nginx server

exec { 'update':
  path    => '/usr/bin/:',
  command => 'apt update && apt -y upgrade',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file  { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

file_line { 'nginx_redirect':
  path    => '/etc/nginx/sites-available/default',
  line    => 'location /redirect_me { return 301 https://www.alxafrica.com; }',
  after   => 'server_name _;',
  require => Package['nginx'],
  notify  => Service['nginx'],
}
