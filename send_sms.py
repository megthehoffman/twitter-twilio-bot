from twilio.rest import Client
import os

ACCOUNT_SID = os.environ['TWILIO_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_NUM = os.environ['TWILIO_NUM']
MY_NUM = os.environ['MY_NUM']
TEST_NUM = os.environ['TEST_NUM']
MATT_NUM = os.environ['MATT_NUM']

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# message = client.messages \
#     .create(
#          body='This is the ship that made the Kessel Run in fourteen parsecs?',
#          from_=TWLIO_NUM,
#          to=MY_NUM
#      )

# print(message.sid)


numbers_to_message = [MY_NUM, TEST_NUM]

for number in numbers_to_message:

    message = client.messages. \
        create(
            body='hi this is Megan thank you for letting me use your phone as a guinea pig',
            from_=TWILIO_NUM,
            to = number
        )

    print(message.sid)


# message = client.messages \
#     .create(
#          body='MMS test text message',
#          from_=TWILIO_NUM,
#          media_url='https://i.pinimg.com/originals/1c/b0/0b/1cb00b3823865b55619ab8c92aac9504.jpg',
#          to=MY_NUM
#      )

# print(message.sid)