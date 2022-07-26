from brownie import SimpleStorage, accounts, config, network


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    tx1 = simple_storage.store(31, {"from": account})
    tx1.wait(1)
    print(tx1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)
    
    tx2 = simple_storage.addPerson("yavuz", 7, {"from": account})
    tx2.wait(1)
    
    print(simple_storage.retrieveNumberOfPerson("yavuz"))
    
def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()