import os
from  twilio.rest import TwilioRestClient

# You can find these tokens at http://www.twilio.com/user/account
account = os.environ.get('TWILIO_ACCOUNT')
token = os.environ.get('TWILIO_TOKEN')

# It has to be a Twilio number. It will fail if you do not insert a valid number
twilio_number = os.environ.get('TWILIO_NUMBER', 'XXXXXXXX')

if not account or not token:
    raise Exception("Account and Token are need for accessing Twilio API")
client = TwilioRestClient(account, token)

if __name__ == "__main__":
    if not os.environ.get('TWILIO_ACCOUNT') or not os.environ.get('TWILIO_TOKEN'):
        print "Account and Token are needed for accessing Twilio API"
    to=raw_input("Which number do you want to send an SMS?")
    sms_text=raw_input("Write the sms now: ")

    message = client.sms.messages.create(to=to, from_=twilio_number, body=sms_text)