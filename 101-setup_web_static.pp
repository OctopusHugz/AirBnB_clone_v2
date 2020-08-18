# This manifest configures a server specifically
$update = '/usr/bin/env apt-get -y update'
$string='\\t\\talias /data/web_static/current/;'
$command1 = "/usr/bin/env sed -i '37a \\tlocation /hbnb_static/ {' /etc/nginx/sites-available/default"
$command2 = "/usr/bin/env sed -i '38a ${string}' /etc/nginx/sites-available/default"
$command3 = "/usr/bin/env sed -i '39a \\t}' /etc/nginx/sites-available/default"
$command4 = "/usr/bin/env sed -i '40a \\n' /etc/nginx/sites-available/default"

exec { 'apt-get update':
  command => $update
}

-> package { 'nginx':
  ensure   => 'installed',
  provider => 'apt'
}

-> exec { 'mkdir1':
  command => '/bin mkdir -p /data/web_static/releases/test'
}

-> exec { 'mkdir2':
  command => '/bin mkdir -p /data/web_static/shared'
}

-> exec { 'index.html content':
  command => '/bin echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html'
}

-> exec { 'symlink':
  command => '/bin ln -sfn /data/web_static/releases/test/ /data/web_static/current'
}

-> exec { 'chown':
  command => '/bin chown -R ubuntu:ubuntu /data'
}

-> exec { 'sed1':
  command => $command1
}

-> exec { 'sed2':
  command => $command2
}

-> exec { 'sed3':
  command => $command3
}

-> exec { 'sed4':
  command => $command4
}

-> service { 'nginx':
  ensure  => 'running',
  restart => 'sudo service nginx restart'
}
