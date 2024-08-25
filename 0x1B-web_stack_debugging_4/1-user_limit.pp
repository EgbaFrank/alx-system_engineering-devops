# Fix holberton user open file limit

exec { 'Fix-holberton-user-limit':
  command => 'sed -i \'s/^holberton=/# holberton=/g\' /etc/security/limits.conf',
  path    => ['/bin', '/sbin'],
}
