# Daily Mint SMS Message

![mint-sms](https://i.imgur.com/E45crgL.png "mint-sms")

## Project Background/TODO:
#### THE PROBLEM: 
I love receiving a text message every morning from Chase Bank containing the balance of my checking account. I dove into my personal account settings to see if I could schedule a message to be sent to me with the other account balances on my account, only to realize that checking was the only account this was possible with. 

#### THE GOAL: 
Using a library called mintapi, I was able to scrape the account data living in my Mint account. The goal is to send a text message through Twillio with the balance of every single account in my Mint account every single morning.

#### CURRENT PROGRESS:
* Script prompts user for username and password
* Script returns value of account names and account balances
* Script only runs on local

#### TO DO:
* Migrate project to Scrapy

* Utilize mint.initiate_account_refresh() before the script runs every day to refresh account balances. Cron this, so that it runs at 1:00 AM daily.  
* Figure out how to run this from an AWS serverless instance. Then test the same functionality on Google Cloud Platform and Microsoft Azure to measure cost and performance benefits. [Currently WIP: AWS]
* Figure out how to run Python cron jobs from the cloud server.
* Figure out how to run web-scraping jobs from a cloud server. I guarantee there are going to be huge issues with the package dependencies being moved from running on my local to running on a cloud. Trying to solve this by localizing the mintapi package

#### Issues/Security Concerns:
* 2-Factor-Auth prevents a reliable login after cookie expires.
* Chrome is not run in headless mode. Takes a huge amount of CPU resources.

## Usage:

Retrieve Mint Account Balances via Terminal:
```
1. $ git clone
2. $ cd mint-sms/
3. $ python3 main.py
```

Force Mint Account Balances refresh:
```
1. $ python3 mint-force-refresh.py
```

Running the script from the terminal will initiate the following sequence of events:

1. Script will prompt user for username and password
2. Script will use Selenium to login to Mint account from Chrome GUI
3. Script will return the value of account_json to terminal screen
