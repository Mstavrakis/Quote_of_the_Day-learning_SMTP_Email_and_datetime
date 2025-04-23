#pythonmarko0@gmail.com

# smtplib.SMTP("smtp.gmail.com", port=587)
#
# gwkj bdfz ghsu andw
#
#
#  pythonmarko@yahoo.com
#
#
#
# import smtplib
# my_email = "pythonmarko0@gmail.com"
# password="gwkjbdfzghsuandw "
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:# creat my connections.
#     connection.starttls()#Secure connections
#     connection.login(user=my_email,password=password)#logged in
#     connection.sendmail(from_addr=my_email,to_addrs="pythonmarko@yahoo.com",msg="Subject:Hello email\n\n "
#                                                                                 "This is the song that never ends")
#
# import datetime as dt
# now=dt.datetime.now()
# year = now.year
#
# date_of_birth = dt.datetime(year=1975, month=4,day=19) # how to create a date time
import random
import datetime as dt
import smtplib

my_email = "pythonmarko0@gmail.com"
password = "gwkjbdfzghsuandw"
now = dt.datetime.now()
today=now.weekday()



with open("quotes.txt") as quotes:
    list_of_quotes=quotes.readlines()
    quote=random.choice(list_of_quotes)

if today ==2:

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:# create my connections.
        connection.starttls()#Secure connections
        connection.login(user=my_email,password=password)#logged in
        connection.sendmail(from_addr=my_email,to_addrs="pythonmarko@yahoo.com",msg=f"Subject:Quote of the day\n\n "
                                                                               f"{quote}")