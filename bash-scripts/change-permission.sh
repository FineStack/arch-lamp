printf "Enter the username of this computer: - "
read uname
chown -R $uname "/srv/http/"
