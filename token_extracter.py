import requests
import fileOperations
from dotenv import load_dotenv
import os

load_dotenv()
address = os.getenv("WALLET_ADDRESS_BURN")


def tokenAPI(z):  # Function that grabs api and parses data. It returns the name of the specified (based on index)
    # token/NFT and returns the corresponding token id

    response = \
        requests.get(
            f'https://api.ergoplatform.com/api/v1/addresses/{address}/balance/confirmed'
        )  # gets the data from the url
    data = response.json()  # organizes the data
    name = data["tokens"][z]["name"]  # gets the name based on index
    tokenId = data["tokens"][z]["tokenId"]  # gets the token id based on index

    return name, tokenId, data  # returns the name, token id, and the all the data from the link


def length():  # function that gets the length of all the tokens/NFTs there are in the wallet
    response = \
        requests.get(
            f'https://api.ergoplatform.com/api/v1/addresses/{address}/balance/confirmed'
        )
    data = response.json()

    return len(data["tokens"])


def extract():
    for x in range(length()):  # this runs as many times as there are tokens in the wallet
        name = tokenAPI(x)[0]  # calls the function and tells to return the name which is in the 0th index
        tokenId = tokenAPI(x)[1]  # calls the function and tells to return the token id which is in the 1st index
        y = {"NFT": name, "TokenId": tokenId, }  # format of what to print
        fileOperations.write(y, 'tokenid.json')  # writes the name and id to tokenid.json


extract()
