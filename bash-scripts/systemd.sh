systemctl restart mariadb.service
systemctl restart php-fpm.service
systemctl restart httpd.service
systemctl enable httpd.service
systemctl enable mariadb.service
systemctl enable php-fpm.service
