import os
from  twilio.rest import TwilioRestClient

account = os.environ.get('TWILIO_ACCOUNT')
token = os.environ.get('TWILIO_TOKEN')

if not account or not token:
    raise Exception("Account and Token are need for accessing Twilio API")
client = TwilioRestClient(account, token)

if __name__ == "__main__":
    if not os.environ.get('TWILIO_ACCOUNT') or not os.environ.get('TWILIO_TOKEN'):
        print "Account and Token are needed for accessing Twilio API"