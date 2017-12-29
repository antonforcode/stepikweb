sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql start
mysql -uroot -e "create database ask"
