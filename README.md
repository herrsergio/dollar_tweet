# dollar_tweet
Post the MXN/USD, Ethereum and Bitcoin prices to Bluesky with AWS Lambda (serverless)

UPDATED to use python3 and Bluesky (atproto)

Configure your credentials by copying `.env.skel` to `.env` and filling in your
Bluesky `BLUESKY_HANDLE` and `BLUESKY_APP_PASSWORD` (create the app password in
Bluesky **Settings → App Passwords**, not your account password).

Pre-steps:

 1. Create an AWS account.

Steps to install:

 1. Clone this repo.
 2. Install the `serverless` tool.
 
`sudo npm install -g serverless`
    
 3. `cd dollar_tweet`

 4. Execute the following commands:

`virtualenv env`

`source env/bin/activate`

`pip3 install atproto grapheme requests python-dotenv`

`pip3 freeze > requirements.txt`

`npm init `

5. `serverless deploy`

