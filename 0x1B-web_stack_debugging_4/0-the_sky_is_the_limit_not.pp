# Fix nginx config limit error

exec { 'Fix-nginx-limit':
  command => 'sed -i \'s/^ULIMIT=/# ULIMIT=/g\' /etc/default/nginx',
  path    => ['/bin', '/sbin'],
  notify  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => 'service nginx reload',
  path        => ['/usr/bin', '/usr/sbin'],
  refreshonly => true,
}
