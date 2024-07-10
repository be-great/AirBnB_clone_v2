#!/usr/bin/env bash
#0. Prepare your web servers
if ! command -v nginx &> /dev/null
then
        apt-get -y update
        apt-get install -y nginx
fi
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/
echo "Hello, World!" > /data/web_static/releases/test/index.html
if [ -L "/data/web_static/current" ]
then
        rm -f "/data/web_static/current"
fi
ln -s "/data/web_static/releases/test" "/data/web_static/current"
chown -R ubuntu:ubuntu /data
printf %s "
server {
    listen 80;
    location /hbnb_static/ {
        alias /data/web_static/current/;
        autoindex off;
    }


}
" > /etc/nginx/sites-available/default

sudo service nginx restart

