import datetime as dt
import smtplib
from calendar import weekday

now = dt.datetime.now()
weekday =now.weekday()
if weekday == 1:
    with open("quotes.txt") as file:
        quotes = file.readlines()













