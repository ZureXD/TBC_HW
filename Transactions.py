def add_Funds(Bank_Accounts,iban):
    print("------------------------------")
    money = int(input("Enter Money Amount: "))

    # Add money to Already existing Account
    for account in Bank_Accounts:
        if account["iban"] == iban:
            account["moneyamount"] += money
            print(f"Added {money} to account with IBAN: {iban}, Current Fund:{account["moneyamount"]}")
            return
    print("Account not found")


def move_Funds(bank_Accounts,source_iban, destination_iban, amount):
    destination_account = None
    
    # Find source and destination accounts
    for account in bank_Accounts:
        if account["iban"] == source_iban:
            source_account = account
        if account["iban"] == destination_iban:
            destination_account = account
    
    # Check if destination account is found
    if destination_account is None:
        print("Destination accounts not found")
        return
    
    # Check if source account has enough funds
    if source_account["moneyamount"] < amount:
        print(f"Insufficient funds in source account, Your fund is : {source_account["moneyamount"]}")
        return
    
    # Move funds
    source_account["moneyamount"] -= amount
    destination_account["moneyamount"] += amount
    print(f"Transferred {amount} from account with IBAN: {source_iban} to account with IBAN: {destination_iban}")
    print(f"{source_iban} Funds: {source_account["moneyamount"]}")
    print(f"{destination_iban} Funds: {destination_account["moneyamount"]}")

def destination_inputs():
    iban = input("Enter IBAN: ")
    money_amount = int(input("Enter Money: "))

    return iban,money_amount