from brownie import accounts, network, config, MockV3Aggregator
import os
from web3 import Web3

DECIMALS = 8
START_PRICE = 200000000000
LOCAL_BLOCKCHAIN = ["development", "ganache-local"]
FORKED_LOCAL_ENV = ["mainnet-fork-dev"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN
        or network.show_active() in FORKED_LOCAL_ENV
    ):
        return accounts[0]
    else:
        return accounts.add(os.getenv("PRIVATE_KEY"))


def deploy_mock():
    print("Deploying Mock...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, START_PRICE, {"from": get_account()})
