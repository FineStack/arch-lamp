with open("/etc/httpd/conf/httpd.conf") as file:
    text = file.read()

email = input("Enter your email address: - ")
text = text.replace("ServerAdmin you@example.com", "ServerAdmin " + email)
with open("/etc/httpd/conf/httpd.conf", "w") as file:
    file.write(text)
