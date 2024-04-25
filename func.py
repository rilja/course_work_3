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

    return last_transactions_dates[0:transactions_count]


def full_transactions_from_date(date_and_time):
    for transaction in load_executed_transactions_list():
        if transaction.get("date") == date_and_time:
            full_transaction_info = transaction

    return full_transaction_info


print(full_transactions_from_date('2019-11-19T09:22:25.899614'))