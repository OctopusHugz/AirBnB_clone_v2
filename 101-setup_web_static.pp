# This manifest configures a server specifically
$update = '/usr/bin/env apt-get -y update'
$string='alias /data/web_static/current/;'
$command1 = "/usr/bin/env sed -i '37a location /hbnb_static/ {' /etc/nginx/sites-available/default"
$command2 = "/usr/bin/env sed -i '38a ${string}' /etc/nginx/sites-available/default"
$command3 = "/usr/bin/env sed -i '39a }' /etc/nginx/sites-available/default"

exec { 'apt-get update':
  command => $update
}

-> package { 'nginx':
  ensure   => 'installed',
  provider => 'apt'
}

-> exec { 'mkdir1':
  command => '/usr/bin/env mkdir -p /data/web_static/releases/test'
}

-> exec { 'mkdir2':
  command => '/usr/bin/env mkdir -p /data/web_static/shared'
}

-> exec { 'index.html content':
  command => '/usr/bin/env echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html'
}

-> exec { 'symlink':
  command => '/usr/bin/env ln -sfn /data/web_static/releases/test/ /data/web_static/current'
}

-> exec { 'chown':
  command => '/usr/bin/env chown -R ubuntu:ubuntu /data'
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

-> service { 'nginx':
  ensure  => 'running',
  restart => 'sudo service nginx restart'
}
