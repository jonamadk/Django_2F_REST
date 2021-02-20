
from twilio.rest import Client

account_sid = 'AC53f8c0928470a317bb1f4570c18ff2b5'
auth_token = 'f8c323c6e9eab5881c65248997434be9'
client = Client(account_sid, auth_token)

def send_sms(user_code , phone_number):
    print(user_code)
    
    message = client.messages.create(
        body= f'Hi your verification code is {user_code}',
        from_ = '+18139405683',
        to = f'{phone_number}'
    )





