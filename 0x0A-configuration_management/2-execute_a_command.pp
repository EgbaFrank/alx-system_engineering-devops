exec { 'pkill -f killmenow':
  onlyif  => 'pgrep -x killmenow',
  path    => '/usr/bin:'
}
