from algosdk import mnemonic
from algosdk.v2client import algod
from algosdk.future.transaction import AssetConfigTxn, wait_for_confirmation


# Troque algod_token e algod_address para conectar a um cliente diferente - PT/BR
# Change algod_token and algod_address to connecto to a different client - EN
algod_token = ""
algod_address = "https://testnet-algorand.api.purestake.io/ps2"
headers = {
"X-API-Key": "SUA-CHAVE-API-DA-PURESTAKE-----YOUR-API-KEY",
}

# Inicializar um Cliente Algod - PT/BR
# Initialize an Algod Client - EN
algod_client = algod.AlgodClient(algod_token, algod_address, headers)

defaultAlc = ""
def_privateKey = "SUA CHAVE PRIVADA ALGORAND/YOUR ALGORAND 25 WORDS MNEMONIC"

def create_fungible_token(_def_privateKey):

  print("--------------------------------------------")
  print("Criando Ativo/CREATING ASSET...")

  params = algod_client.suggested_params()

  txn = AssetConfigTxn(
      sender='SEU ENDEREÇO/YOUR ADDRESS',
      sp=params,
      total=1000,
      default_frozen=False,
      unit_name="",
      asset_name="",
      manager='SEU ENDEREÇO/YOUR ADDRESS',
      reserve=None,
      freeze=None,
      clawback=None,
      strict_empty_address_check=False,
      url="https://path/to/my/asset/details", 
      decimals=0)

  # Assinar com a chave secreta do criador - PT/BR
  # Sign with creators secret ket - EN
  privatekey = mnemonic.to_private_key(_def_privateKey)
  stxn = txn.sign(privatekey)

  # Enviar a transação para a rede e receber o txid - PT/BR
  # Send transaction to network and receive txid - EN

  txid = algod_client.send_transaction(stxn)
  print("Asset Creation Transaction ID: {}".format(txid))

  # Aguardar pela confirmação da transação - PT/BR
  # Wait for transaction confirmation - EN
  confirmed_txn = wait_for_confirmation(algod_client, txid, 4)  
  print("TXID: ", txid)
  try:
      # Pegar informação de conta para o criador
      # Obter asset_id do tx
      # Obter informação do novo ativo do conta do criador
      ptx = algod_client.pending_transaction_info(txid)
      asset_id = ptx["asset-index"]
  except Exception as e:
      print(e)

  print("--------------------------------------------")
  print("Você criou seu próprio token com sucesso! YOU CREATED YOUR OWN TOKEN SUCCESSFULLY")

create_fungible_token(def_privateKey)
