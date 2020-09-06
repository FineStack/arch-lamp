with open("/etc/php/php.ini") as file:
    text = file.read()

text = text.replace(";extension=pdo_mysql", "extension=pdo_mysql")
text = text.replace(";extension=mysqli", "extension=mysqli")
text = text.replace(";extension=bz2", "extension=bz2")

with open("/etc/php/php.ini", "w") as file:
    file.write(text)

text = """Alias /phpmyadmin "/usr/share/webapps/phpMyAdmin"
<Directory "/usr/share/webapps/phpMyAdmin">
    DirectoryIndex index.php
    AllowOverride All
    Options FollowSymlinks
    Require all granted
</Directory>"""

with open("/etc/httpd/conf/extra/phpmyadmin.conf", "w") as file:
    file.write(text)

with open("/etc/httpd/conf/httpd.conf", "a") as file:
    file.write("\nInclude conf/extra/phpmyadmin.conf")
