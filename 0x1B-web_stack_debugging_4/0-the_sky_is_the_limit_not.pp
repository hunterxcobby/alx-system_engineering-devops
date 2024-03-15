# Puppet manifest to optimize Nginx configuration for handling load

class nginx_config {
    file { '/etc/nginx/nginx.conf':
        ensure  => file,
        owner   => 'root',
        group   => 'root',
        mode    => '0644',
        content => template('nginx/nginx.conf.erb'),
        notify  => Service['nginx'],
    }
}

service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Class['nginx_config'],
}
