# @Machines_Notifications_bot

import requests
from manipulate import date, hour


# BOT_TOKEN
token = "BOT_TOKEN" # set bot token

# ALLOCATION USER
user = "ALLOCATION_USER" # set allocation user

# URL WEBHOOK
webhook_url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}".format(token,user)

# Message which will be send to user
machine = "MACHINE -->" # set machine name
message_date = date()
message_hour = hour()

content = input(str())

mesagge = str("""{} Notificación de su dispositivo el {} a las {}
{}""".format(machine,
                message_date,
                message_hour,
                content))

# JSON file
data = {"text":mesagge}


# Request POST to webhook
response = requests.post(webhook_url,json=data)


