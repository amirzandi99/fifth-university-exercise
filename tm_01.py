import os
Inventory = float(input("Enter Inventory : "))
Account = []
count = 0
while(1):
    os.system("cls")
    print("0. Buy")
    print("1. Number of user purchases")
    print("2. Amount deducted")
    print("3. Card balance")
    print("4. Quit\n")
    x = int(input("Enter the choice : "))
    if(x == 0):
        buy = float(input("Enter Purchase amount : "))
        if(buy > Inventory):
            print("Inventory is low !\n\n")
        else:
            Inventory -= buy
            Account.append(buy)
            count += 1
    elif(x == 1):
        print(f"\tNumber of purchase : {count}\n\n")
    elif(x == 2):
        if(count == 0):
            print("Not bought")
        else:
            for i in range(len(Account)):
                print(f"\t1 : {Account[i]}")
        print("\n\n")
    elif(x == 3):
        print(f"\tInventory : {Inventory}\n\n")
    elif(x == 4):
        break
    else:
        print("\tEnter number between 0 .. 4 !\n\n")
    z = str(input("press enter to continue "))