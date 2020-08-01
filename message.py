from twilio.rest import Client 

msg = input("Enter the Message :\n") 

account_sid = 'ACef59534c7ea1b6ab4f3fdf64bb60c692' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=msg,      
                              to='whatsapp:+919108496304' 
                          ) 
 
print(message.sid)