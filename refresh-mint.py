import mintapi
import config
import time

mint = mintapi.Mint(config.mint_email, config.mint_pass)
mint.initiate_account_refresh()
