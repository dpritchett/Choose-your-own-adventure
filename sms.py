#!/usr/bin/env python

"""
REQUIREMENTS:
    * A Twilio account
    * Python with the twilio library (`pip install twilio`)
    * A purchased phone number on twilio to serve as your "from" number ($1/mo)
    * Some twilio credits to pay for the $.01/msg SMS fees

The python-twilio library uses OS-level environment variables
to store SID/Token info:
    * $TWILIO_ACCOUNT_SID
    * $TWILIO_AUTH_TOKEN
"""

from os import environ
from twilio.rest    import TwilioRestClient

def send_text(body, recipient):
    sms_sender      = environ['TWILIO_PHONE_NUMBER']

    client          = TwilioRestClient()

    message         = client.sms.messages.create(
            to      = recipient,
            from_   = sms_sender,
            body    = body)

    return message
