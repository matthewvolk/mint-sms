import mintapi
import subprocess
import json
import config

print("""
   ____ ___  (_)___  / /_      _________ ___  _____
  / __ `__ \/ / __ \/ __/_____/ ___/ __ `__ \/ ___/
 / / / / / / / / / / /_/_____(__  ) / / / / (__  ) 
/_/ /_/ /_/_/_/ /_/\__/     /____/_/ /_/ /_/____/

Opening browser window...
""")

# Format cmd string to inject into Python subprocess
cmd = "mintapi '{}' '{}' --accounts --headless".format(config.mint_email, config.mint_pass)

# Store command in a variable "output"
# TODO make this a try/catch
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
