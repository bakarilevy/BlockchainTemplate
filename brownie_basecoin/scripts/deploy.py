import os
from brownie import accounts, network, config, basecoin

#Using account Wallaby - frisky

def deploy_basecoin_contract():
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
    basecoin_contract = basecoin.deploy({'from': account})
    print(basecoin_contract)


def get_account():
    if(network.show_active()=='development'):
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def main():
    deploy_basecoin_contract()