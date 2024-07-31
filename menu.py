def menu():
    opt=0
    print("WELCOME TO FUNDINVESTING \n")
    while(opt < 1 or opt > 3):
        print("CHOOSE OPTION: ")
        print("1. Start analysis")
        print("2. Read me")
        print("3. Close \n")
        try:
            opt=int(input("OPTION: "))
        except:
            print("Type a number\n")
    return opt