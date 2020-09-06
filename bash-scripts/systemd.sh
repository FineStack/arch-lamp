systemctl restart mariadb.service
systemctl start php-fpm.service
systemctl start httpd.service
systemctl enable httpd.service
systemctl enable mariadb.service
systemctl enable php-fpm.service
