from brownie import FundMe
from scripts.helpful import get_account


def fund():
    fundme = FundMe[-1]
    account = get_account()
    entrance_fee = fundme.getEntranceFee()
    print(f"the current fee is {entrance_fee}")
    print("Funding...")
    fundme.fund({"from": account, "value": entrance_fee})


def getprice():
    fundme = FundMe[-1]
    price = fundme.getPrice()
    print(price)


def withdraw():
    fundme = FundMe[-1]
    account = get_account()
    fundme.withdraw({"from": account})


def main():
    withdraw()
