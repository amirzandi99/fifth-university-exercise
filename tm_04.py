import os
count1 = 0
count2 = 0
count3 = 0
Memory = int(input("Enter size of memory : "))
M = Memory
print()
while(1):
    os.system("cls")
    print("1. Add file")
    print("2. Memory display")
    print("3. Quit\n")
    x = int(input("Enter the choice : "))
    if(x == 1):
        print("\n1. text")
        print("2. audio")
        print("3. video\n")
        print("Enter type of file : ", end='')
        y = int(input())
        if(y == 1):
            if(Memory >= 1):
                Memory -= 1
                count1 += 1
            else:
                print("Memory is full")
        elif(y == 2):
            if(Memory >= 3):
                Memory -= 3
                count2 += 1
            else:
                print("Memory is full")
        elif(y == 3):
            if(Memory >= 1):
                Memory -= 1
                count3 += 1
            else:
                print("Memory is full")
        else:
            print("Enter number between 1 .. 3 !")
        print("\n")
    elif(x == 2):
        print(f"\nsize of Memory  : {M}")
        print(f"Remaining space : {Memory}")
        print(f"number of text  : {count1}")
        print(f"number of audio : {count2}")
        print(f"number of video : {count3}\n\n")
    elif(x == 3):
        break
    else:
        print("Enter number between 1 .. 3 !\n\n")
    z = str(input("press enter to continue "))