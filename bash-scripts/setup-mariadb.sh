mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
systemctl start mariadb.service
clear
printf "Enter new username for MariaDB: - "
read username
printf "Enter new password for MariaDB: - "
read password
Q1="CREATE USER '$username'@'localhost' IDENTIFIED BY '$password';"
Q2="GRANT ALL PRIVILEGES ON *.* TO '$username'@'localhost' WITH GRANT OPTION;"
Q3="FLUSH PRIVILEGES;"
SQL="${Q1}${Q2}${Q3}"
mysql -e "$SQL"
clear
mysql_secure_installation
