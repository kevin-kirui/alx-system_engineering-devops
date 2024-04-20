#!/usr/bin/puppet

# Install a specific version of Flask (2.1.0) using Puppet

package { 'flask':
    ensure   => '2.1.0',
    provider => 'pip'
}

