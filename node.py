import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()
NODE_IP = os.getenv("NODE_IP")
API_KEY = os.getenv("API_KEY")
PW = os.getenv("PW")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")


def mintNft(name, description, encodedHash, encodedLink): # mints NFT through node API requests
    unlockWallet()
    headers = {
        'accept': 'application/json',
        'api_key': API_KEY,
        'Content-Type': 'application/json'
    }

    out = {
        "requests": [
            {
                "address": WALLET_ADDRESS,
                "amount": 1,
                "name": name,
                "description": description,
                "decimals": 0,
                "registers": {
                    "R7": "0e020101",
                    "R8": encodedHash,
                    "R9": encodedLink
                }
            }
        ],
        "fee": 1000000
    }

    tx_id = requests.post('http://{}/wallet/transaction/send'.format(NODE_IP), headers=headers,
                          data=json.dumps(out)).json()
    return tx_id


def unlockWallet(): # unlocks node wallet
    headers = {
        'accept': 'application/json',
        'api_key': API_KEY,
        'Content-Type': 'application/json'
    }
    out = {
        "pass": PW
    }
    resp = requests.post('http://{}/wallet/unlock'.format(NODE_IP), headers=headers, data=json.dumps(out)).json()
    return resp


