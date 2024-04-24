def bank_Account_SignUp_Inputs():
    print("------------------------------")
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    iban = input("Enter IBAN: ")
    money_amount = 0

    return name, surname, iban, money_amount


def check_Account_SignUp_Inputs(bank_Accounts,iban):
    status = True

    if iban.startswith("TB") and iban[2:].isdigit() and len(iban) == 5:
        for ibans in bank_Accounts:
            if ibans["iban"] == iban:
                status = False
                break
        if status == False:
            print()
            print("Iban Already Exists, Try again")
        else:
            return True
    else:
        print()
        print("Invalid User Input, Try again")
        return False
    

def add_Inputs(bank_Accounts,name,surname,iban,money_amount):
    new_account = {"name": name, "surname": surname, "iban": iban, "moneyamount": money_amount}
    bank_Accounts.append(new_account)
