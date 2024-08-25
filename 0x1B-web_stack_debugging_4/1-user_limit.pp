# Fix holberton user open file limit

exec { 'Fix-holberton-user-limit':
  command => 'sed -i \'/^holberton/ s/^/# /\' /etc/security/limits.conf',
  path    => ['/bin', '/sbin'],
}
