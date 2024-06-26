from course_work_3.src.func import get_full_transactions_from_date
import datetime


class Transaction:

    def __init__(self, transaction_date):
        ''''creating instance using date in format "%Y-%m-%dT%H:%M:%S.%f" '''
        self.transaction_date = transaction_date
        self.full_transaction_info = get_full_transactions_from_date(transaction_date)

    def date_format_correction(self):
        '''returns date in format "%d.%m.%Y" '''
        correct_date = datetime.datetime.strptime(self.transaction_date, "%Y-%m-%dT%H:%M:%S.%f")
        return correct_date.strftime('%d.%m.%Y')

    def get_transaction_description(self):
        ''''returns transaction description'''
        transaction_description = self.full_transaction_info.get("description")
        return transaction_description

    def get_from_account_info(self):
        ''''returns "Opening a deposit" if no info about
        retruns card name and secret card number
        '''
        from_account_info = self.full_transaction_info.get("from")
        if from_account_info is None:
            return f'Opening a deposit'      # if no from information

        # split txt from card/account numbers
        txt_in_info = from_account_info.split()
        card_name = []
        for txt in txt_in_info:
            if txt.isdigit():
                card_number = txt
            else:
                card_name.append(txt)

        # if transaction is from account to account
        if card_name[0] == "Счет":
            short_card_number = []
            for i in range(-1, -5, -1):
                short_card_number.insert(0, card_number[i])
            secret_card_number = "**" + ''.join(short_card_number)
        else:
            # numbers secreting un spliting by 4 digits
            secret_card_number = list(card_number)
            for num in range(6, 12):
                secret_card_number[num] = "*"
            for num in range(4, 20, 5):
                secret_card_number.insert(num, " ")

        secret_card_number = ''.join(secret_card_number)
        full_card_name = ' '.join(card_name)
        new_from_account_info = full_card_name + " " + secret_card_number

        return new_from_account_info

    def get_to_account_info(self):
        ''''retruns card name and secret card number'''
        to_account_info = self.full_transaction_info.get("to")

        # split txt from card/account numbers
        txt_in_info = to_account_info.split()
        card_name = []
        for txt in txt_in_info:
            if txt.isdigit():
                card_number = txt
            else:
                card_name.append(txt)

        # numbers secreting un shortening
        short_card_number = []
        for i in range(-1, -5, -1):
            short_card_number.insert(0, card_number[i])
        secret_card_number = "**" + ''.join(short_card_number)
        full_card_name = ' '.join(card_name)
        new_to_account_info = full_card_name + " " + secret_card_number

        return new_to_account_info

    def get_transaction_amount_and_currency(self):
        ''''returns transaction amount and currency'''
        transaction_amount = self.full_transaction_info.get("operationAmount").get('amount')
        transaction_currency = self.full_transaction_info.get("operationAmount").get('currency').get('name')
        transaction_amount_and_currency = transaction_amount + " " + transaction_currency

        return transaction_amount_and_currency

    def __repr__(self):
        return f"Transation ('{self.full_transaction_info}')"

    def __str__(self):
        return f"Transation on date: {self.transaction_date}"
