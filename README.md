TextVer
=======

Receive SMS from your server when any service is down. Start, stop reload or restart your services by sending and SMS to your server


Check2.py
 - Run it in your server
 - Modify the values for account_sid, auth_token, auth_number, twilio_number and services


ssh_connector.py
- Run it in anonther server (e.g: Heroku)
- Change the values for host, username, password, auth_number, auth_token and url
- Configure your twilio number to send the messages to the heroku URL

That's it!



Jordi Vazquez @ WarwickHack 2014
