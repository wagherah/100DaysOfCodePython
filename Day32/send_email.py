import smtplib

my_email = 'passawa420@gmail.com'
password = 'Shadi420'

# SMTP object
# we use smtlp object to connect to location of email provider SMTP server 
connection = smtplib.SMTP('smtp.gmail.com', 587)

# TLS encryption
# TLS -> Transport layer security
connection.starttls()

# login
connection.login(user=my_email, password=password)

# sending email
connection.sendmail(from_addr=my_email, to_addrs='yasirasmat4545@gmail.com', msg='Hello') 
connection.quit()