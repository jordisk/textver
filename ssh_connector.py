from flask import Flask, request, redirect
import os
import twilio.twiml
from twilio.util import RequestValidator
from pexpect import pxssh


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def application():
    #Credentials
    host = ""
    username = ""
    password = ""
    auth_number = "+44"
    auth_token = ""
    validator = RequestValidator(auth_token)
    url = ""
    sa = pxssh.pxssh()
    body_message = str(request.values.get('Body', None))
    signature = request.headers.get('X-Twilio-Signature')


    from_number = request.values.get('From', None)
    body1 = body_message.split(' ')[0]
    if (from_number == auth_number and body1 == "service"):
        sa.login(host, username, password)
        sa.sendline(body_message)
        sa.prompt()
        sa.logout()
        sms_content = "Done!"
        message = str(sms_content)
        resp = twilio.twiml.Response()
        resp.message(message)
        return str(resp)
    
    else:
        sms_content = "You are not allowed to send commands to this server"
        message = str(sms_content)
        resp = twilio.twiml.Response()
        resp.message(message)
        return str(resp)
        pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

