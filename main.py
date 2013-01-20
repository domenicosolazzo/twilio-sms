import os
account = os.environ.get('TWILIO_ACCOUNT')
token = os.environ.get('TWILIO_TOKEN')


if __name__ == "__main__":
    if not os.environ.get('TWILIO_ACCOUNT') or not os.environ.get('TWILIO_TOKEN'):
        raise Exception("Account and Token are needed for accessing to the Twilio API")