import smtplib

my_email = "shreyadesh01032004@gmail.com"
password="apkl scgt qoxl ofxk"

with  smtplib.SMTP("smtp.gmail.com") as connection  :
    connection.starttls()
    connection.login (user=my_email , password =password )
    connection.sendmail(from_addr=my_email , to_addrs="manthansankpal745@gmail.com" , msg = "Subject : Hello\n\n and Muah")
#connection.close()

#manthansankpal745@gmail.com

# import datetime as dt
#
# now = dt.datetime(year=2004,month=3,day=1)
# print(now)
