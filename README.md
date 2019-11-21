# mooclet-email
Emailing System to link with MOOClet framework


## Setup

1. Set up venv for this project
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

2. Run server
```
python manage.py runserver
```

## API Endpoints

1. POST `/email/send` sends an email out to a group of users. In the body, the requester can currently send the following params:
  * `id` which is the mooclet id
  * `emails` which is the emails you want to send to and one thing to note is that these are assumed to be associated to the specified mooclet

2. POST `/email/callback` is the endpoint that needs to be called from Mailgun's webhooks. Whenever a click event or open event for the emails is triggered, this endpoint would get hit once it's configured on Mailgun.

## Setting up Mailgun
This repository was tested thus far on a sandbox account using Amish's personal account

1. Create an account on Mailgun: https://www.mailgun.com/
  * Make sure to submit the credit card information to get full availability - the first 10,000 emails are still free so don't worry!
2. Verify your own sender domain (probably would be josephwilliams.com?):
https://help.mailgun.com/hc/en-us/articles/360026833053-Domain-Verification-Walkthrough
3. Grab the API keys from Mailgun's dashboard
4. Create a .env file under the `src` folder:
```
cd /src
vim .env
```
5. Add the following to the `.env` file
```
MAILGUN_API_KEY=<YOUR_API_KEY>
MAILGUN_SENDER_DOMAIN=<YOUR_SENDER_DOMAIN>
```
6. Test it out by sending a sample email!! (POST `/email/send`)

## TODO
This is just a prototype which has hooked up MOOClet to this service for sending emails. It makes an API call to MOOClet and get's the email contents. After this, it sends out an email using Mailgun. 

* Setup your own Mailgun account following the information above
* Once mailgun account is setup and verfied, enable email tracking on mailgun for you domain by following these instructions:
https://documentation.mailgun.com/en/latest/user_manual.html#tracking-messages
* Add some authentication (Ex. Basic Auth) to the `/email/send` endpoint
* Deploy this system so that webhook can be integrated once this is hosted on a server and there is an valid callback endpoint that mailgun can use.
* Add the callback endpoint to Mailgun's webhooks so that this endpoint gets called when there is an open or click event. More on this is available here:
https://documentation.mailgun.com/en/latest/user_manual.html#webhooks
* Hook the email metric endpoint to MOOClet by making an API call to MOOClet so that it's seamless even for metrics such as opens and click rates.
