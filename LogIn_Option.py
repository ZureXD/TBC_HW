def print_Login_Options():
    print("------------------------------")
    print("1.Log In")
    print("2.Sign Up")
    print("3.Exit")


def check_Login_Operation():
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