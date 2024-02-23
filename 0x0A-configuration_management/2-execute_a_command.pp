# This manifest uses 'exec' resource to kill a process named 'killmenow' using 'pkill'
exec { 'kill_killmenow_process':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
}
