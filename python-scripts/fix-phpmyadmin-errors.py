print('https://phpsolved.com/phpmyadmin-blowfish-secret-generator/')
blowfish = input('Enter the blowfish from the website: - ')

with open('/etc/webapps/phpmyadmin/config.inc.php') as file:
    text = file.read()

text = text.replace("$cfg['blowfish_secret'] = ''",
                    "$cfg['blowfish_secret'] = '" + blowfish + "'")

with open('/etc/webapps/phpmyadmin/config.inc.php', 'w') as file:
    file.write(text)

with open('/etc/webapps/phpmyadmin/config.inc.php', 'a') as file:
    file.write("\n$cfg['TempDir'] = '/tmp';")
