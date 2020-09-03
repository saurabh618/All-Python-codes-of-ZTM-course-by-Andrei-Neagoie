# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 10:01:55 2020

@author: saura
"""
from twilio.rest import Client

account_sid = 'AC35a43368114f115baac776029167317c'
auth_token = '8cfe654e7fa576d7961f8698f0b015fd'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+19284823038',
    body='Hello Saurabh, this is your bot JARVIS! Good Morning!',
    to='+919652723113'
    )

print(message.sid)
