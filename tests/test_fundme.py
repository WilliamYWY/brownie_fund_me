from brownie import network, accounts, exceptions
from scripts.helpful import get_account, LOCAL_BLOCKCHAIN
from scripts.deploy import deploy_fundme
import pytest


def test_can_fund_withfraw():
    account = get_account()
    fundme = deploy_fundme()
    entrance_fee = fundme.getEntranceFee() + 100
    tx = fundme.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fundme.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fundme.withdraw({"from": account})
    tx2.wait(1)
    assert fundme.addressToAmountFunded(account.address) == 0


def test_only_owner():
    if network.show_active() not in LOCAL_BLOCKCHAIN:
        pytest.skip("only for local")
    fundme = deploy_fundme()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fundme.withdraw({"from": bad_actor})
