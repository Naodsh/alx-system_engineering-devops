# webstuck deb
class nginx_optimization {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure     => running,
    enable     => true,
    subscribe  => File['/etc/nginx/nginx.conf'],
  }

  file { '/etc/nginx/nginx.conf':
    ensure  => file,
    content => template('nginx_optimization/nginx.conf.erb'),
    notify  => Service['nginx'],
  }
}

include nginx_optimization
