def bank_Account_Login_Inputs():
    print("------------------------------")
    iban = input("Enter IBAN: ")

    return iban


def check_Account_Login_Inputs(bank_Accounts,iban):
    status = True

    if iban.startswith("TB") and iban[2:].isdigit() and len(iban) == 5:
        for ibans in bank_Accounts:
            if ibans["iban"] == iban:
                status = True
                break
        if status == True:
            return True
        else:
            print()
            print("Iban Doesn't Exist")
            return False
    else:
        print()
        print("Invalid User Input, Try again")
        return False