from twilio.rest import Client 
import os

account_sid = 'AC2a292bdf20f43814a186b924ab52f8c1' 
auth_token = 'ecec35588b4ca8344145627c8e85d631' 
client = Client(account_sid, auth_token) 
def func():
    f1=open("students.csv","r")
    x=f1.read()
    f1.close()
    message = client.messages.create(         
    messaging_service_sid='MGc8a512e9e6d8b5e5f49ab24ca848f45c', 
    body=x,      
    to='+917997642581'
    ) 
    print(message.sid)
