import os
import json
from web3 import Web3
from dotenv import load_dotenv


load_dotenv()
node_provider = os.environ['NODE_PROVIDER']
web3_connection = Web3(Web3.HTTPProvider(node_provider))

def test_connection():
    return web3_connection.isConnected()

def build_contract(contract_address, abi_path):
    with open(abi_path) as f:
        abiJson = json.load(f)
    contract = web3_connection.eth.contract(address=contract_address, abi=abiJson['abi'])
    return contract

def get_address(private_key):
    return web3_connection.eth.account.from_key(private_key).address

def transfer(_contract, _to, _amount, _signature):
    # We need the public key of whoever is signing this transaction
    nonce = web3_connection.eth.get_transaction_count(get_address(_signature))
    function_call = _contract.functions.transfer(_to, _amount).buildTransaction({'nonce':nonce})
    signed_transaction = web3_connection.sign_transaction(function_call, _signature)
    result = web3_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return result

def inc_allowance(_contract, _to, _amount, _signature):
    # We need the public key of whoever is signing this transaction
    nonce = web3_connection.eth.get_transaction_count(get_address(_signature))
    function_call = _contract.functions.increaseAllowance(_to, _amount).buildTransaction({'nonce':nonce})
    signed_transaction = web3_connection.sign_transaction(function_call, _signature)
    result = web3_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return result

def dec_allowance(_contract, _to, _amount, _signature):
    # We need the public key of whoever is signing this transaction
    nonce = web3_connection.eth.get_transaction_count(get_address(_signature))
    function_call = _contract.functions.decreaseAllowance(_to, _amount).buildTransaction({'nonce':nonce})
    signed_transaction = web3_connection.sign_transaction(function_call, _signature)
    result = web3_connection.eth.send_raw_transaction(signed_transaction.rawTransaction)
    return result