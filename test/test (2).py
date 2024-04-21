# from web3 import Web3,HTTPProvider
# import json


# def connect_with_blockchain(account):
#     blockchain_server = "http://127.0.0.1:8545"
#     web3 = Web3(HTTPProvider(blockchain_server))

#     if account == 0:
#         web3.eth.default_account = web3.eth.accounts[0]
#     else:
#         web3.eth.default_account = account

#     with open('c:/Users/vikra/OneDrive/Desktop/ContactDapp/build/contracts/mycontract.json') as f:
#         artifact_json = json.load(f)
#         contract_abi = artifact_json['abi']
#         contract_address = artifact_json['networks']['5777']['address']

#     contract =  web3.eth.contract(address=contract_address,abi=contract_abi)

#     return(contract,web3)


# contract,web3 = connect_with_blockchain(0)
# trans_hash = contract.functions.insertContact("Vikrant","vikrantrathi79@gmail.com","8182526876","Bit Mesra").transact()
# web3.eth.wait_for_transaction_receipt(trans_hash)

# result = contract.functions.viewContacts().call()

# print(result)

