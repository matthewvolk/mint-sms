import mintapi

mint_username = input('Please enter your Mint username: ')
mint_password = input('Please enter your Mint password: ')

mint = mintapi.Mint(mint_username, mint_password)
account_json = mint.get_accounts()

print(account_json[0]['accountName'], end=' - ')
print(account_json[0]['fiLoginDisplayName'])
print((account_json[0]['currentBalance']))