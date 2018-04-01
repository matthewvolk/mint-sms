import mintapi
import subprocess
import json
import getpass

mint_user = input('Please enter your Mint login email: ')
mint_pass = getpass.getpass('Please enter your Mint password: ')

cmd = "mintapi '{}' '{}' --accounts".format(mint_user, mint_pass)
output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

jsonS = output.communicate()
account_json = json.loads(jsonS[0].decode('utf-8'))

for i in range(0, len(account_json)):
  if (account_json[i]['currentBalance'] != 0):
    print(account_json[i]['accountName'], end=' - ')
    print(account_json[i]['fiLoginDisplayName'])
    print('${:,.2f}'.format((account_json[i]['currentBalance'])))
    print('-----------------------')