# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:20:38 2020

@author: saura
"""
from twilio.rest import Client

account_sid = 'ACd14286b3a8d093f71f4ec72eb9143e1f'
auth_token = 'ad3a486ed06500c654d82028e56d34df'

client = Client(account_sid, auth_token)

message = client.messages.create(
         # media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80'],
         from_='whatsapp:+14155238886',
         body="Hello Saurabh. This is your bot: JARVIS, reporting on duty!",
         to='whatsapp:+919652723113'
         )

print(message.sid)
