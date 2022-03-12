import os
import json
from web3 import Web3
from solcx import compile_standard
from dotenv import load_dotenv

load_dotenv()

with open('./SimpleStorage.sol', 'r') as file:
    simple_storage_file  = file.read()
    print('Original Contract')
    print(simple_storage_file)

# First we need to compile the smart contract
compiled_sol = compile_standard(
    {
        'language': 'Solidity',
        'sources': {'SimpleStorage.sol': {'content': simple_storage_file}},
        'settings': {
            'outputSelection': {
                '*': {
                    '*': ['abi', 'metadata', 'evm.bytecode', 'evm.sourceMap']
                }
            },
        },
    },
    solc_version='0.6.0'
)
print('Deploying to chain...')
with open('compiled_code.json', 'w') as file:
    json.dump(compiled_sol, file)

# We need the bytecode of the contract in order to deploy it
bytecode = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['evm']['bytecode']['object']
# We also need our ABI
abi = compiled_sol['contracts']['SimpleStorage.sol']['SimpleStorage']['abi']
# Deploy in a simulated environment using Ganache
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
# We need the chain or network id (Ganache uses 1337 as default chain id)
chain_id = 1337
# Address to deploy from
my_address = '0xD83e19962DE91F20062b5DAA4d2146c1CdfB8054'
# Need corresponding address' private key (You need to add an 0x to the front of all private keys in Python)
private_key = os.getenv('PRIVATE_KEY')

SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# The deployment consists of the following steps
# Build the contract deploy transaction
# Sign the contract
# Send the transaction

# We can get our nonce for this transaction by getting our latest transaction count
nonce = w3.eth.getTransactionCount(my_address)
transaction = SimpleStorage.constructor().buildTransaction({'chainId':chain_id, 'from':my_address, 'nonce': nonce})
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print('Contract successfully deployed to the chain')

# To work with a contract we always need the contract address and the contract abi

# Interacting with deployed contract
print('Attempting to call the contract functions store and retrieve')
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
# When interacting with contracts on chain we have two options
# Call -> Simulates making the call and getting a return value without making a state change to the chain
# Transact -> Actually makes a state change to the chain
# Example calling deployed contract's retrieve function
#print(simple_storage.functions.retrieve().call())

# We have to repeat the same steps to create a transaction since we are storing data to the chain
# It would be smart to create a high level function for this task
store_transaction = simple_storage.functions.store(15).buildTransaction({
    'chainId': chain_id,
    'from': my_address,
    'nonce': nonce + 1
})
signed_stored_txn = w3.eth.account.sign_transaction(store_transaction, private_key=private_key)
store_transaction_hash = w3.eth.send_raw_transaction(signed_stored_txn.rawTransaction)
store_transaction_receipt = w3.eth.wait_for_transaction_receipt(store_transaction_hash)
retrieve_value = simple_storage.functions.retrieve().call()
print(f'Successfully called store function, result of retrieve is: {retrieve_value}')