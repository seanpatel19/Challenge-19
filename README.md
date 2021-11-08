# Challenge-19

## Block Chain Wallets   

We are Fintech Engineers at a start up. We are building a disruptive new technology that allows firms to find tech talent and pay them through the ethereum blockchain 

To accomplish this we need to do the following:

Step 1: Generate a new Ethereum account instance by using your mnemonic seed phrase.

Step 2: Fetch and display the account balance associated with your Ethereum account address.

Step 3: Calculate the total value of an Ethereum transaction, including the gas estimate, that pays a Fintech Finder candidate for their work.

Step 4: Digitally sign a transaction that pays a Fintech Finder candidate, and send this transaction to the Kovan testnet.

Step 4: Review the transaction hash code associated with the validated blockchain transaction.

---

## Creating a Mnemonic 

### mnemonic_gen.py should be run first if cloning the repository ###

I created another file called mnemonic_gen.py to create a nmemonic phrase to generate a key from. 

This was done earlier in the lessions for Module 19, but I added this file to the challenge to make everything easier and have Challenge 19 be standalone from the repository.

---

## Creating Ethereum Transaction Functions 

We created a python file called crypto_wallet.py, which contains some functions for interacting with the blockchain. 

There are functions for creating a wallet based on a mnemonic seed phrase.

There are also functions to check the current balance in ether, and to send transactions to hire our fintech professionals. 

These functions also include provisions to calculate gas fees to get the transactions moving. 

---

## Importing crypto_wallet.py and modifying fintech_finder.py 

Please see the following screenshots of adding some code snippets and modifying some code to work with the functions laid out in crypto_wallet.py


Importing the crypto_wallet.py functions

![crypto_wallet](https://github.com/seanpatel19/Challenge-18/blob/bc543fb11ec798be8aaaa07b042917861458499b/images/installs.png)

Adding information to complete the functions 

![account](https://github.com/seanpatel19/Challenge-18/blob/bc543fb11ec798be8aaaa07b042917861458499b/images/installs.png)

Creating the transaction hash 

![trans hash](https://github.com/seanpatel19/Challenge-18/blob/bc543fb11ec798be8aaaa07b042917861458499b/images/installs.png)

---

## Running our Application via Streamlit 

To deploy these files we decided to use Streamlit and here are some screenshots of the results.

The main page showing our candidates for employment

![main](https://github.com/seanpatel19/Challenge-18/blob/bc543fb11ec798be8aaaa07b042917861458499b/images/installs.png)

Our transactional sidebar

![sidebar](https://github.com/seanpatel19/Challenge-18/blob/bc543fb11ec798be8aaaa07b042917861458499b/images/installs.png)

A successful hire

![successful](https://github.com/seanpatel19/Challenge-18/blob/bc543fb11ec798be8aaaa07b042917861458499b/images/installs.png)

We tried to hire another professional but quickly ran out of money. We should do another round of funding 

![poverty](https://github.com/seanpatel19/Challenge-18/blob/bc543fb11ec798be8aaaa07b042917861458499b/images/installs.png)





---

## Technologies
This application is written in Python 3.7  

This application uses a lot of different functions and libaries :

Pandas  https://pandas.pydata.org

dataclasses https://docs.python.org/3/library/dataclasses.html

typing https://pypi.org/project/typing/

hashlib https://docs.python.org/3/library/hashlib.html

streamlit https://streamlit.io



---

## Installation Guide

Before running various dependancies need to be installed. As there are 3 main files please see the attached screenshots for all 3 

mnemonic_gen.py imports 

![imports](https://github.com/seanpatel19/Challenge-18/blob/bc543fb11ec798be8aaaa07b042917861458499b/images/installs.png)

crypto_wallet.py imports

![imports](https://github.com/seanpatel19/Challenge-18/blob/bc543fb11ec798be8aaaa07b042917861458499b/images/installs.png)

fintech_finder.py imports 

![imports](https://github.com/seanpatel19/Challenge-18/blob/bc543fb11ec798be8aaaa07b042917861458499b/images/installs.png)






---

## Usage

To use the data simply clone the repository. This can also be used via Google Collab but I chose jupyter notebook 

Different layers could be added as well ad different values of the layers 
```
---

## Contributors

Sean Patel (myself) seanpatel076@gmail.com
---

## License

License is public anyone can use or make changes to this application
