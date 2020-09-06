with open("/etc/httpd/conf/httpd.conf") as file:
    text = file.read()

text = text.replace("#LoadModule proxy_module modules/mod_proxy.so",
                    "LoadModule proxy_module modules/mod_proxy.so")
text = text.replace("#LoadModule proxy_fcgi_module modules/mod_proxy_fcgi.so",
                    "LoadModule proxy_fcgi_module modules/mod_proxy_fcgi.so")

with open("/etc/httpd/conf/httpd.conf", "w") as file:
    file.write(text)

text = """DirectoryIndex index.php index.html
<FilesMatch \.php$>
    SetHandler "proxy:unix:/run/php-fpm/php-fpm.sock|fcgi://localhost/"
</FilesMatch>"""

with open("/etc/httpd/conf/extra/php-fpm.conf", "w") as file:
    file.write(text)

with open("/etc/httpd/conf/httpd.conf", "a") as file:
    file.write("\nInclude conf/extra/php-fpm.conf")
