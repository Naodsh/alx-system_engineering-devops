# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Define Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "\
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        return 301 http://$host/redirect_me;
    }

    location /redirect_me {
        return 200 'Hello World!\n';
    }
}
",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Remove default Nginx site
file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
}
