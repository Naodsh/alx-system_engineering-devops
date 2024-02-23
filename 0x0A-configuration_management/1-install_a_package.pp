# This manifest ensures that Flask version 2.1.0 is installed using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  install_options => ['--no-ri', '--no-rdoc'], # Optional: Additional options for pip3
}
