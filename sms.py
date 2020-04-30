from twilio.rest import Client
import sys

accsid = Insert Twilio SID
token = Insert Twilio Token


client = Client(accsid, token)

phone = Inset Twilio Phone
myphone = Insert phone to receive the sms



try:
    numbers = sys.argv
except:
    print('Input é (Número de casos confirmados) e (Número de óbitos)')
    print(numbers)
    sys.exit(-1)


text = f'O número atual de casos confirmados é {numbers[1]} e o número de óbitos é {numbers[2]}'

message = client.messages.create(body = text, from_ = phone, to = myphone)

