import os
from brownie import accounts, network, config, SimpleStorage

#Using account Wallaby - frisky

def deploy_simple_storage():
    ''' 
     To use A created account run
     account = accounts.load('wallaby')
     For using a configured or production better to use the bellow with config
     account = accounts.add(config['wallets']['from_key'])
     print(account) 
    '''
    # For testing on local Ganache instance
    account = get_account()
    # Every time you deploy or make transaction you need a from and sometimes a to
    simple_storage = SimpleStorage.deploy({'from': account})
    stored_value = simple_storage.retrieve()
    transaction = simple_storage.store(15, {'from': account})
    transaction.wait(1)
    updated_value = simple_storage.retrieve()


def get_account():
    if(network.show_active()=='development'):
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def main():
    deploy_simple_storage()