# Daily Mint SMS Message

## Description:
#### THE PROBLEM: 
I love receiving a text message every morning from Chase Bank containing the balance of my checking account. I dove into my personal account settings to see if I could schedule a message to be sent to me with the other account balances on my account, only to realize that checking was the only account this was possible with. 

#### THE GOAL: 
Using a library called mintapi, I was able to scrape the account data living in my Mint account. The goal is to send a text message through Twillio with the balance of every single account in my Mint account every single morning.

#### CURRENT PROGRESS:

#### TO DO:
* Bypass 2-Factor-Auth ...legally
* Test to see if my account balances are refreshed automatically so that in the morning, I am provided with the most up to date balances. If this is not the case, I will need to use the built in class method mint.initiate_account_refresh() before the script runs every day. 
* Figure out how to run this from an AWS serverless instance. Then test the same functionality on Google Cloud Platform and Microsoft Azure to measure cost and performance benefits. 
* Figure out how to run Python cron jobs from the cloud server
* Figure out how to run web-scraping jobs from a cloud server. I guarantee there are going to be huge issues with the package dependencies being moved from running on my local to running on a cloud. 


## Usage:

```
1. $ git clone
```

Running the script from the terminal will initiate the following sequence of events:

