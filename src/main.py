from transaction import Transaction
from course_work_3.src.func import *

if __name__ == "__main__":
    # creating the desired number of class"Transaction" instances
    counter = 1
    transactions = {}
    for date in get_last_executed_transactions_dates(5):
        transactions[counter] = Transaction(date)
        counter += 1

    # vidget output
    for transaction in transactions.values():
        print(f'{transaction.date_format_correction()} {transaction.get_transaction_description()}')
        print(f'{transaction.get_from_account_info()} -> {transaction.get_to_account_info()}')
        print(f'{transaction.get_transaction_amount_and_currency()}\n')
