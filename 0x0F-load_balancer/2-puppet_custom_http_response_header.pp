# Install and configure an Nginx server

exec { 'update':
  path    => '/usr/bin/:',
  command => 'apt update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update'],
}

file_line { 'custom_header':
  path    => '/etc/nginx/nginx.conf',
  line    => "\n\tadd_header X-Served-By ${hostname} always;",
  after   => 'http {',
  require => Package['nginx'],
}

exec { 'restart_nginx':
  command => 'service nginx restart',
  path    => ['/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  require => File_line['custom_header'],
}
