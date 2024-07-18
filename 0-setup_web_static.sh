#!/usr/bin/env bash
# Bash script setting up server

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

echo '
<!DOCTYPE html>
<html>
  <head> Releases Test File </head>

  <body background-color="grey">
    <p> Test-Test, One-Two, One-Two </p>
  </body>

  </html> ' > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

chown -R ubuntu /data
chgrp -R ubuntu /data

printf %s "server {
    listen 80;
    listen [::]:80 default_server;

    add_header X-Served-By '$HOSTNAME';

    root   /var/www/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 https://www.github.com/kal-kyokya;
    }

    location /entertain_me {
        return 301 http://www.cuberule.com/;
    }

    location /hbnb_static {
    	alias /data/web_static/current/;
	index index.html;
    }

    error_page 404 /404.html;

    location /404 {
      root /etc/nginx/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

sudo service nginx restart

exit 0
