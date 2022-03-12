from brownie import Lottery, accounts, config, network
from web3 import Web3

def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(config['networks'][network.show_active()]['eth_usd_price_feed'],{'from':account})
    # You get the following numbers by dividing price you want to charge ($50) against current USD/ETH Price
    assert lottery.getEntranceFee() > Web3.toWei(0.009, 'ether')
    assert lottery.getEntranceFee() < Web3.toWei(0.011, 'ether')