from flask import Flask

from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
    r = MessagingResponse()
    r.message('Hi there! Use code ATHENAHACKS to get $25 in Twilio credit for your hack and check out quest.twilio.com to start hacking.')
    return str(r)

@app.route('/voice', methods=['POST'])
def voice():
    r = VoiceResponse()
    r.say('Happy Hacking Athenas!')
    return str(r)

if __name__ == "__main__":
    app.run(debug=True)
