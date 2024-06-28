# kills a process named killmenow

exec { 'pkill -f killmenow':
  onlyif => 'pgrep -x killmenow',
  path   => '/usr/bin:'
}
