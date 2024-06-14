# manifests/init.pp

# Class: nginx_optimization
# This class installs and configures Nginx with optimal settings to handle high loads.
class nginx_optimization {
	# Ensure the Nginx package is installed
	package { 'nginx':
		ensure => installed,
		}

	# Ensure the Nginx service is running and enabled
	service { 'nginx':
		ensure    => running,
		enable    => true,
		subscribe => File['/etc/nginx/nginx.conf'],
		}

	# Apply optimal Nginx configuration from template
	file { '/etc/nginx/nginx.conf':
		ensure  => file,
		content => template('nginx_optimization/nginx.conf.erb'),
		notify  => Service['nginx'],
		}
}

# Apply the nginx_optimization class
include nginx_optimization
