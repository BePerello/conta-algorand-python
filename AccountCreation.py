import json
from algosdk.v2client import algod
from algosdk import account, mnemonic


algod_address = "https://testnet-algorand.api.purestake.io/ps2"
algod_token = ""
headers = {
"X-API-Key": "YOUR-PURESTAKE-API-KEY",
}

# Inicializar um Algod client
algod_client = algod.AlgodClient(algod_token, algod_address, headers)

def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))
    return private_key, address

generate_algorand_keypair()
