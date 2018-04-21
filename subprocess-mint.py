import mintapi
import subprocess
import json
import config

# Format cmd string to inject into Python subprocess
cmd = "mintapi '{}' '{}' --accounts".format(config.mint_email, config.mint_pass)

# Store class method value in output variable
output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

# Read output value and convert to bytestring
jsonS = output.communicate()

# Decode bytestring into JSON data Array object
account_json = json.loads(jsonS[0].decode('utf-8'))

for i in range(0, len(account_json)):
  if (account_json[i]['currentBalance'] != 0):
    print(account_json[i]['accountName'], end=' - ')
    print(account_json[i]['fiLoginDisplayName'])
    print('${:,.2f}'.format((account_json[i]['currentBalance'])))
    print('-----------------------')