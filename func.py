import requests


def load_executed_transactions_list():
    transactions_list = requests.get('https://www.jsonkeeper.com/b/DHRX').json()
    executed_transactions_list = []
    for transaction in transactions_list:
        if transaction.get("state") == "EXECUTED":
            executed_transactions_list.append(transaction)

    return executed_transactions_list
