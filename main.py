import smtplib
import random
import datetime as dt

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open('quotes.txt') as data:
        all_quotes = data.readlines()
        quote = random.choice(all_quotes)

    my_email = "nadirtest7@gmail.com"
    password = "Nadir@123"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(
            user=my_email,
            password=password
        )
        connection.sendmail(
            from_addr=my_email,
            to_addrs="nadiraziziyah@gmail.com",
            msg="Subject: Monday quotes\n\n"
                f"{quote}")
