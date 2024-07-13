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

file_line { 'custom_header':
  path    => '/etc/nginx/sites-available/default',
  line    => "\n\tadd_header X-Served-By $hostname always;",
  after   => 'server_name _;',
  require => Package['nginx'],
}

exec { 'restart_nginx':
  command => 'service nginx restart',
  path    => ['/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  require => File_line['custom_header'],
}
