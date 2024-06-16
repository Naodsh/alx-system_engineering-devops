# to increase the file descriptor limits for the user

file { '/etc/security/limits.d/holberton.conf':
  ensure  => file,
  content => "holberton soft nofile 4096\nholberton hard nofile 4096\n",
  mode    => '0644',
}

exec { 'increase-system-file-limits':
  command => 'sysctl -w fs.file-max=100000',
  unless  => 'sysctl -n fs.file-max | grep -q 100000',
}

exec { 'increase-pam-limits':
  command => 'echo "session required pam_limits.so" >> /etc/pam.d/common-session',
  unless  => 'grep -q "session required pam_limits.so" /etc/pam.d/common-session',
}
