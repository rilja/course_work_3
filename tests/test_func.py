from course_work_3.src.func import *
import time

def test_load_executed_transactions_list():
    for transaction in load_executed_transactions_list():
        assert transaction.get("state") == "EXECUTED"


def test_last_executed_transactions_dates():
    last_date = get_last_executed_transactions_dates(1)
    new_last_date = time.strptime(last_date[0], "%Y-%m-%dT%H:%M:%S.%f")
    for transaction in load_executed_transactions_list():
        transaction_date = transaction.get('date')
        new_transaction_date = time.strptime(transaction_date, "%Y-%m-%dT%H:%M:%S.%f")
        if new_transaction_date > new_last_date:
            newest_date = new_transaction_date
            break
        else:
            newest_date = new_last_date

    assert newest_date == new_last_date


def test_full_transactions_from_date():
    assert get_full_transactions_from_date("2019-08-26T10:50:58.294041") == load_executed_transactions_list()[0]
    assert get_full_transactions_from_date("2019-07-03T18:35:29.512364") == load_executed_transactions_list()[1]
    assert get_full_transactions_from_date("2018-06-30T02:08:58.425572") == load_executed_transactions_list()[2]
