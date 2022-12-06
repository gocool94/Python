import smtplib

my_email = "gocool94@gmail.com"

connection = smtplib.SMTP("smtp.gmail.com")
print(1)
connection.starttls()
print(2)
connection.login(user="gocool94@gmail.com",password="gokulkumar777@")
print(3)
connection.sendmail(from_addr=my_email,to_addrs="gocool94@gmail.com",msg="Hello")
print(4)
connection.close()
