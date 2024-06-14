# sky_is_the_limit_not.pp
# This Puppet manifest configures Nginx to handle a high number of connections and requests more efficiently

exec { 'increase-worker-connections':
  command => 'sed -i "s/worker_connections .*/worker_connections 1024;/" /etc/nginx/nginx.conf',
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
  onlyif  => 'grep -q "worker_connections 768;" /etc/nginx/nginx.conf',
  notify  => Exec['restart-nginx'],
}

exec { 'increase-worker-processes':
  command => 'sed -i "s/worker_processes .*/worker_processes auto;/" /etc/nginx/nginx.conf',
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
  onlyif  => 'grep -q "^worker_processes" /etc/nginx/nginx.conf',
  notify  => Exec['restart-nginx'],
}

exec { 'increase-keepalive-timeout':
  command => 'sed -i "s/keepalive_timeout .*/keepalive_timeout 65;/" /etc/nginx/nginx.conf',
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
  onlyif  => 'grep -q "^keepalive_timeout" /etc/nginx/nginx.conf',
  notify  => Exec['restart-nginx'],
}

exec { 'increase-server-names-hash-bucket-size':
  command => 'sed -i "s/server_names_hash_bucket_size .*/server_names_hash_bucket_size 64;/" /etc/nginx/nginx.conf',
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
  onlyif  => 'grep -q "^server_names_hash_bucket_size" /etc/nginx/nginx.conf',
  notify  => Exec['restart-nginx'],
}

exec { 'restart-nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
}

# Ensure puppet-lint compliance
exec { 'ensure-puppet-lint-compliance':
  command => 'puppet-lint 0-the_sky_is_the_limit_not.pp --fix',
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
}
