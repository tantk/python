from twilio.rest import TwilioRestClient

account_sid = "AC3327c51f9aafb7b8d8eeffc7adfaeb93" # Your Account SID from www.twilio.com/console
auth_token  = "849f6ff51d1af25385a844543d8b92a1"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+12345678901",    # Replace with your phone number
    from_="+12345678901") # Replace with your Twilio number

print(message.sid)
