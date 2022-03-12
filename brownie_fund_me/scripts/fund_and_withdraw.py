from brownie import FundMe
from scripts.helpful_scripts import *


def fund():
    fund_me = FundMe[-1]
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)


def main():
    fund()