from brownie import network, config, accounts, MockV3Aggregator


DECIMALS = 8
STARTING_PRICE = 2000
TEST_NETWORKS = ['development', 'Private']


def get_account():
    if(network.show_active() == 'development' or 'Private'):
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])

def deploy_mocks():
    print(f'Active network is: {network.show_active()}')
    print('Deploying mocks...')
    mock_aggregator = MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {'from': get_account()})
    print('Mock successfully deployed!')
    price_feed_address = mock_aggregator.address
    print(f'Contract deployed to: {price_feed_address}')