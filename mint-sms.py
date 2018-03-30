import mintapi
import getpass

mint_username = input('Please enter your Mint username: ')
mint_password = getpass.getpass('Please enter your Mint password: ')

mint = mintapi.Mint(mint_username, mint_password)
account_json = mint.get_accounts()

for i in range(0, len(account_json)):
  if (account_json[i]['currentBalance'] != 0):
    print(account_json[i]['accountName'], end=' - ')
    print(account_json[i]['fiLoginDisplayName'])
    print('${:,.2f}'.format((account_json[i]['currentBalance'])))
    print('-----------------------')
