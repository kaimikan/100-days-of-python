import smtplib

my_email = "secret-email@gmail.com"
# this is from the gmail special account setup
password = "secret"

# connection = smtplib.SMTP("smtp.gmail.com")
with smtplib.SMTP("smtp.gmail.com") as connection:
    # encrypt connection
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="anothersecret@gmail.com",
                        msg="Subject: Testing Mails\n\nThis is the body, yo!")
# obsolete when we use with
# connection.close()
