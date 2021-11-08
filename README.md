# Challenge-19

## Block Chain Wallets   

We are Fintech Engineers at a start up. We are building a disruptive new technology that allows firms to find tech talent and pay them through the ethereum blockchain 

To accomplish this we need to do the following:

Step 1: Generate a new Ethereum account instance by using your mnemonic seed phrase.

Step 2: Fetch and display the account balance associated with your Ethereum account address.

Step 3: Calculate the total value of an Ethereum transaction, including the gas estimate, that pays a Fintech Finder candidate for their work.

Step 4: Digitally sign a transaction that pays a Fintech Finder candidate, and send this transaction to the Kovan testnet.

Step 4: Review the transaction hash code associated with the validated blockchain transaction.



## Creating a Mnemonic and Getting Kovan Eth

***mnemonic_gen.py should be run first if cloning the repository 

I created another file called mnemonic_gen.py to create a nmemonic phrase to generate a key from. 

This was done earlier in the lessions for Module 19, but I added this file to the challenge to make everything easier and have Challenge 19 be standalone from the repository.

After a hash has been created from the mnemonic we need some Ethereum. To accomplish this we used the Kovan Testnet in Infura, and got some Kovan Eth from the KETH faucet. 



## Creating Ethereum Transaction Functions 

We created a python file called crypto_wallet.py, which contains some functions for interacting with the blockchain. 

There are functions for creating a wallet based on a mnemonic seed phrase.

There are also functions to check the current balance in ether, and to send transactions to hire our fintech professionals. 

These functions also include provisions to calculate gas fees to get the transactions moving. 



## Importing crypto_wallet.py and modifying fintech_finder.py 

Please see the following screenshots of adding some code snippets and modifying some code to work with the functions laid out in crypto_wallet.py


Importing the crypto_wallet.py functions

![crypto_wallet](https://github.com/seanpatel19/Challenge-19/blob/8ad3c96453d687a7f2252e33de8a133e56052dc0/Images/wallet%20import.png)

Adding information to complete the functions 

![account](https://github.com/seanpatel19/Challenge-19/blob/8ad3c96453d687a7f2252e33de8a133e56052dc0/Images/create%20account.png)

Creating the transaction hash 

![trans hash](https://github.com/seanpatel19/Challenge-19/blob/8ad3c96453d687a7f2252e33de8a133e56052dc0/Images/rans%20hash.png)



## Running our Application via Streamlit 

To deploy these files we decided to use Streamlit and here are some screenshots of the results.

The main page showing our candidates for employment

![main](https://github.com/seanpatel19/Challenge-19/blob/8ad3c96453d687a7f2252e33de8a133e56052dc0/Images/main%20page.png)

Our transactional sidebar

![sidebar](https://github.com/seanpatel19/Challenge-19/blob/8ad3c96453d687a7f2252e33de8a133e56052dc0/Images/transaction%20sidebar.png)

A successful hire

![successful](https://github.com/seanpatel19/Challenge-19/blob/8ad3c96453d687a7f2252e33de8a133e56052dc0/Images/successfull%20transaction.png)

We tried to hire another professional but quickly ran out of money. We should do another round of funding 

![poverty](https://github.com/seanpatel19/Challenge-19/blob/8ad3c96453d687a7f2252e33de8a133e56052dc0/Images/too%20much%20money.png)


## Checking our work on Etherscan and Infura 

Please see the following to show that this is working on the Blockchain 

![etherscan](https://github.com/seanpatel19/Challenge-19/blob/8ad3c96453d687a7f2252e33de8a133e56052dc0/Images/etherscan.png)


And as a Bonus we can see the statistics of the transactions on Infura

![infura](https://github.com/seanpatel19/Challenge-19/blob/4c569adb7e5d7a3b9e8f36eb3d088b6e8bb5dfa1/Images/infura%20stats.png)



---

## Technologies
This application is written in Python 3.7  

This application uses a lot of different functions and libaries

### We will start with the technologies used for mnemonic_gen.py:

OS https://docs.python.org/3/library/os.html

Dotenv https://www.npmjs.com/package/dotenv

mnemonic https://pypi.org/project/mnemonic/

BIP (44 specifically) https://pypi.org/project/bip-utils/ 

Web 3 https://pypi.org/project/web3/

### crypto_wallet.py: 

OS https://docs.python.org/3/library/os.html

Dotenv https://www.npmjs.com/package/dotenv

Requests https://pypi.org/project/requests/

BIP (44 specifically) https://pypi.org/project/bip-utils/ 

Web 3 https://pypi.org/project/web3/


### And finally fintech_finder.py: 

dataclasses https://docs.python.org/3/library/dataclasses.html

typing https://pypi.org/project/typing/

streamlit https://streamlit.io

***Kovan Links

https://faucet.kovan.network/

https://gitter.im/kovan-testnet/faucet  ***back up, put in wallet address to be filled by in KETH

---

## Installation Guide

Before running various dependancies need to be installed. As there are 3 main files please see the attached screenshots for all 3 

mnemonic_gen.py imports 

![mnemo_imports](https://github.com/seanpatel19/Challenge-19/blob/8ad3c96453d687a7f2252e33de8a133e56052dc0/Images/nmemo%20imports.png)

crypto_wallet.py imports

![cw_import](https://github.com/seanpatel19/Challenge-19/blob/8ad3c96453d687a7f2252e33de8a133e56052dc0/Images/crypto%20wallet%20imports.png)

fintech_finder.py imports 

![ff_import](https://github.com/seanpatel19/Challenge-19/blob/8ad3c96453d687a7f2252e33de8a133e56052dc0/Images/fintech%20finder%20import.png)






---

## Usage

To use the data simply clone the repository. All code written in VSCode, and streamlit run from the command line  

```
---

## Contributors

Sean Patel (myself) seanpatel076@gmail.com
---

## License

License is public anyone can use or make changes to this application
