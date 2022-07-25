from brownie import SimpleStorage, accounts


def test_deploy():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected_value = 0
    assert starting_value == expected_value

def test_updating():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    tx = simple_storage.store(31, {"from": account})
    tx.wait(1)
    stored_value = simple_storage.retrieve()
    expected_value = 31
    assert stored_value == expected_value