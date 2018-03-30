import mintapi

mint_username = input('Please enter your Mint username: ')
mint_password = input('Please enter your Mint password: ')

mint = mintapi.Mint(mint_username, mint_password)