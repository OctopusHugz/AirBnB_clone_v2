#!/usr/bin/env bash
# This script sets up web static on a web server
string='\\t'\\t'alias /data/web_static/current/;'
apt-get install -y nginx
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
cd /etc/nginx/sites-available
sed -i '37a \\tlocation /hbnb_static/ {' default
sed -i '38a '"${string}"'' default
sed -i '39a \\t}' default
sed -i '40a \\n' default
service nginx restart
