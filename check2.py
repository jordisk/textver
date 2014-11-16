import commands
import time
from twilio.rest import TwilioRestClient

#output = commands.getoutput('ps -A')
failservice = ""

#Twilio credentials
account_sid = "ACb92ed9bb2f74c72ac3dc1cff81215aee"
auth_token = "5ead811627e32fd0cb5221e9358041d2"
client = TwilioRestClient(account_sid, auth_token)
twilio_number = "+441133203095"
auth_number = "+447763501564"

services = ["apache2", "sshd"]
status = 1
def status1():
        global status
        global failedservice
        global client
        while status == 1:
                time.sleep(2)
                for service in services:
                        output = commands.getoutput('ps -A')
                        if service in output:
                                print(service + " is up an running!")
                        else:
                                print(service + " is NOT running")
                                status = 0
                                failedservice = service
                                smsbody = "Hi Jordi, I'm your server! Sorry to bother you but " + failedservice + " has been stopped unexpectedly -- Reply 'service " + failedservice + " start' if you want to restart the service" 
                                message = client.messages.create(to=auth_number, from_=twilio_number, body=smsbody)
                                break


def status0():
        global status
        global failedservice
        while status == 0:
                print ("Waiting")
                time.sleep(3)
                output = commands.getoutput('ps -A')
                if failedservice not in output:
                        pass
                else:
                        smsbody = failedservice + " is working again."
                        message = client.messages.create(to=auth_number, from_=twilio_number, body=smsbody)
                        status = 1
                        status1()

status1()
status0()

