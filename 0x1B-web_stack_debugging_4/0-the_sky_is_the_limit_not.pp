# Puppet manifest configures Nginx to handle a higher number of connections by setting ULIMIT

file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT=\"-n 4096\"\n",
  notify  => Exec['restart-nginx'],
}

exec { 'restart-nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
}
