from brownie import SimpleStorage, accounts, config

def read_contract():
    # Contract[-1] always returns the most recently deployed contract
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())

def main():
    read_contract()