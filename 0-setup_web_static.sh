#!/usr/bin/env bash
# Install a nginx web server listening on port 80.
#
# Setting server ups
#

new_conf="http {\n\tserver {\n\t\tlisten 80;\n\t\tserver_name 54.80.218.139;\n\t\tlocation /hbnb_static {\n\t\t\talias /data/web_static/current/;\n\t\t\t}\n\t}"

apt update
apt install -y nginx
ufw allow 'Nginx HTTP'
service nginx restart

mkdir -p /data/web_static/releases/test/
mkdir /data/web_static/shared/
echo " " > /data/web_static/releases/test/index.html
sed -i "s| |<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>\n|" /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "s|http {|$new_conf|" /etc/nginx/nginx.conf
service nginx restart
