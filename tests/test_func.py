from course_work_3.src.func import *


def test_load_executed_transactions_list():
    for transaction in load_executed_transactions_list():
        assert transaction.get("state") == "EXECUTED"
