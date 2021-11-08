## mnemonic.py created to make a seed phrase for the other part of the exercise

# Imports
import os
from dotenv import load_dotenv
load_dotenv()
from mnemonic import Mnemonic
from bip44 import Wallet
from web3 import Account 
from web3.auto.infura.kovan import w3

# Load the value of the MNEMONIC variable from the .env file
mnemonic = os.getenv("MNEMONIC")

# Evaluate the contents of the mnemonic variable
# Create a new mnemonic seed phrase if the value of mnemonic equals None
if mnemonic is None:
  mnemo = Mnemonic("english")
  mnemonic = mnemo.generate(strength=128)

wallet = Wallet(mnemonic)
wallet
private, public = wallet.derive_account("eth")
public
account = Account.privateKeyToAccount(private)
account_address = account.address
print(account_address)



# Access the balance of funds for the Ethereum account
wei_balance = w3.eth.getBalance(account_address)

# Convert the balance from a denomination in wei to ether
ether = w3.fromWei(wei_balance, "ether")

# Print the number of ether
print( ether)