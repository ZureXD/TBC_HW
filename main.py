from Login_Inputs import bank_Account_Login_Inputs,check_Account_Login_Inputs
from SignUp_Inputs import bank_Account_SignUp_Inputs,add_Inputs,check_Account_SignUp_Inputs
from Transactions import add_Funds,move_Funds,destination_inputs
from Transaction_Options import print_Options,check_Operation
from LogIn_Option import check_Login_Operation,print_Login_Options

# This is to save some time
bank_Accounts = [
    {"name": "Pete", "surname": "Doe", "iban": "TB123", "moneyamount": 100},
    {"name": "Bob", "surname": "Johnson", "iban": "TB932", "moneyamount": 1500}
]


while True:
    print_Login_Options()
    login_Option = check_Login_Operation()

    if login_Option == 1:        
        iban = bank_Account_Login_Inputs()
        if check_Account_Login_Inputs(bank_Accounts,iban) == True:
            while True:
                print_Options()
                Transaction_Option = check_Operation()
                if Transaction_Option == 1:
                    add_Funds(bank_Accounts,iban)
                elif Transaction_Option == 2:
                    destination_Iban, money_amount = destination_inputs()
                    move_Funds(bank_Accounts,iban,destination_Iban,money_amount)
                elif Transaction_Option == 3:
                    break


            
    elif login_Option == 2:
        name, surname, iban, money_amount = bank_Account_SignUp_Inputs()
        if check_Account_SignUp_Inputs(bank_Accounts,iban) == True:
            add_Inputs(bank_Accounts,name,surname,iban,money_amount)
            while True:
                print_Options()
                Transaction_Option = check_Operation()
                if Transaction_Option == 1:
                    add_Funds(bank_Accounts,iban)
                elif Transaction_Option == 2:
                    destination_Iban, money_amount = destination_inputs()
                    move_Funds(bank_Accounts,iban,destination_Iban,money_amount)
                elif Transaction_Option == 3:
                    break
    elif login_Option == 3:
        break



