from eth_account import Account
import secrets


priv = secrets.token_hex(32)

private_key = '0x'+ priv

acct = Account.from_key(private_key)

my_ethaddress = acct.address
print("This is your private key don't share with anyone:  ", private_key)
print("This is your Address, share to recieve token: ", my_ethaddress)