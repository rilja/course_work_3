from transaction import Transaction
from func import *

if __name__ == "__main__":
    # creating the desired number of class"Transaction" instances
    counter = 1
    transactions = {}
    for date in last_executed_transactions_dates(5):
        transactions[counter] = Transaction(date)
        counter += 1

    # vidget output
    for transaction in transactions.values():
        print(f'{transaction.correct_date_format()} {transaction.transaction_description()}')
        print(f'{transaction.from_account_info()} -> {transaction.to_account_info()}')
        print(f'{transaction.transaction_amount_and_currency()}\n')


