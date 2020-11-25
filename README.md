# dollar_tweet
Tweet about the price MXN/USD with AWS Lambda (serverless)

UPDATED to use python3

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

`pip3 install tweepy requests`

`pip3 freeze > requirements.txt`

`npm init `

`npm install --save serverless-python-requirements`

5. `sls deploy`

