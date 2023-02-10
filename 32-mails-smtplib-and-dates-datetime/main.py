import smtplib
import datetime as dt
import pandas
import random

TOTAL_NUMBER_OF_LETTER_TEMPLATES = 3

# ==================== Extra Hard Starting Project ====================

# 1. Read the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = birthdays.to_dict(orient='list')
print(birthdays_dict)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
this_month = now.month
# get the day of the month
this_day = int(now.strftime("%d"))

birthday_people_names_and_email = []
total_entries = len(birthdays_dict["name"])
# get all keys
for birthday_index in range(0, total_entries):
    # check if the month and day of this birthday match today's
    if birthdays_dict["month"][birthday_index] == this_month and \
            birthdays_dict["day"][birthday_index] == this_day:
        print(f"Today is {birthdays_dict['name'][birthday_index]}'s birthday!")
        birthday_people_names_and_email.append(
            (birthdays_dict["name"][birthday_index], birthdays_dict["email"][birthday_index]))

# 3. If step 2 is true, pick a random letter from letter templates
# and replace the [NAME] with the person's actual name from birthdays.csv
if len(birthday_people_names_and_email) > 0:
    for (name, email) in birthday_people_names_and_email:
        print(f"...generating and sending a letter to {name}...")

        # get a random letter template
        with open(f"./letter_templates/letter_{random.randint(1, TOTAL_NUMBER_OF_LETTER_TEMPLATES)}.txt") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", name)
            print(letter)

        # 4. Send the letter generated in step 3 to that person's email address.
        my_email = "secret@gmail.com"
        # this is from the gmail special account setup
        password = "secret"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            # encrypt connection
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=f"{email}",
                                msg=f"Subject: Happy Birthday!\n\n{letter}")


else:
    print("No birthdays found for today, try again tomorrow!")
