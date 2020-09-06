sh bash-scripts/install.sh
clear
sh bash-scripts/change-permission.sh
clear
python3 python-scripts/replace-email.py
clear
python3 python-scripts/enable-proxy.py
sh bash-scripts/setup-mariadb.sh
clear
python3 python-scripts/setup-phpmyadmin.py
python3 python-scripts/fix-phpmyadmin-errors.py
clear
sh bash-scripts/systemd.sh
clear
