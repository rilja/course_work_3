import requests


def load_executed_transactions_list():
    '''returns a list of only completed(executed) transactions'''
    transactions_list = requests.get('https://www.jsonkeeper.com/b/DHRX').json()
    executed_transactions_list = []
    for transaction in transactions_list:
        if transaction.get("state") == "EXECUTED":
            executed_transactions_list.append(transaction)

    return executed_transactions_list


def get_last_executed_transactions_dates(transactions_count=5):
    '''returns the desired number of dates(5 as default) of the last completed transactions'''
    last_transactions_dates = []
    for transaction in load_executed_transactions_list():
        date = transaction.get("date")
        last_transactions_dates.append(date)
    last_transactions_dates.sort(reverse=True)

    return last_transactions_dates[0:transactions_count]


def get_full_transactions_from_date(date_and_time):
    '''returns full info about transaction by date'''
    for transaction in load_executed_transactions_list():
        if transaction.get("date") == date_and_time:
            full_transaction_info = transaction

    return full_transaction_info
