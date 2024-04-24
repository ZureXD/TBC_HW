def print_Options():
    print("------------------------------")
    print("1.Add Funds to Current Account")
    print("2.Transfer Funds From Current Account to Another Existing Account")
    print("3.Logout From Current Account")


def check_Operation():
    while True:
        print()
        operation_Num = input("Enter Operation Number: ")
        if operation_Num.isdigit():
            if int(operation_Num) == 1:
                option = 1
                return option
            elif int(operation_Num) == 2:
                option = 2
                return option
            elif int(operation_Num) == 3:
                option = 3
                return option
            else:
                print()
                print("invalid option Number")
                continue
        else:
            print()
            print("Invalid Datatype, Enter Number")
            continue 