from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful import get_account, deploy_mock, LOCAL_BLOCKCHAIN
from web3 import Web3


def deploy_fundme():
    account = get_account()

    if network.show_active() not in LOCAL_BLOCKCHAIN:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1]

    fundme = FundMe.deploy(price_feed_address, {"from": account})
    return fundme


def main():
    deploy_fundme()
