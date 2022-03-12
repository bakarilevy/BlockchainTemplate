from brownie import FundMe, network, config
from scripts.helpful_scripts import *

def deploy_fund_me():
    
    account = get_account()
    # If we are on a persistent network like rinkeby
    # Pass the price feed address to fundme contract
    if network.show_active() != network in TEST_NETWORKS:
        price_feed_address = config['networks'][network.show_active()]['eth_usd_price_feed']
        fund_me = FundMe.deploy(price_feed_address, {'from':account}, publish_source=True)
        print(f'Contract deployed to {fund_me.address}')

    else:
        deploy_mocks()

def main():
    deploy_fund_me()