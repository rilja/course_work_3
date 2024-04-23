import requests


def load_executed_transactions_list():
    transactions_list = requests.get('https://www.jsonkeeper.com/b/DHRX').json()
    executed_transactions_list = []
    for transaction in transactions_list:
        if transaction.get("state") == "EXECUTED":
            executed_transactions_list.append(transaction)

    return executed_transactions_list


def last_executed_transactions_dates(transactions_count=5):
    last_transactions_dates = []
    for transaction in load_executed_transactions_list():
        date = transaction.get("date")
        last_transactions_dates.append(date)
    last_transactions_dates.sort(reverse=True)

    return last_transactions_dates[0:transactions_count+1]


