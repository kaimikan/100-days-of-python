import smtplib
import datetime as dt
import random


# send mail
def send_mail(quote):
    my_email = "secret@gmail.com"
    # this is from the gmail special account setup
    password = "secret"

    # connection = smtplib.SMTP("smtp.gmail.com")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # encrypt connection
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="anothersecret@gmail.com",
                            msg=f"Subject: Quote\n\n{quote}")


# read quotes
with open("quotes.txt") as file:
    quotes = file.read().splitlines()
    # print(quotes)

# check time
now = dt.datetime.now()
DAY_TO_SEND = 4
if now.weekday() == DAY_TO_SEND:
    send_mail(quotes[random.randint(0, len(quotes) - 1)])
