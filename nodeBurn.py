import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()
NODE_IP = os.getenv("NODE_IP_BURN")
API_KEY = os.getenv("API_KEY_BURN")
PW = os.getenv("PW_BURN")


def burnNft(tokenId, amount): # burns NFT using node API methods
    unlockWallet()
    headers = {
        'accept': 'application/json',
        'api_key': API_KEY,
        'Content-Type': 'application/json'
    }

    out = {
        "requests": [
            {
                "assetsToBurn": [
                    {
                        "tokenId": tokenId,
                        "amount": amount
                    }
                ]
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

