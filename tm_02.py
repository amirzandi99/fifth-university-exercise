u1, u2, tie = 0, 0, 0
t = 1
a = 1
c = 0
while(t == 1):
    if(c == 3):
        break
    R1, P1, S1 = 0, 0, 0
    R2, P2, S2 = 0, 0, 0
    if(a == 1):
        user1 = input("user 1  ->   Rock = (R)   Paper = (P)   Scissors = (S)   Quit = (Q) : ")
        if(user1 == "R" or user1 == "P" or user1 == "S" or user1 == "Q"):
            if(user1 == "Q"):
                t == 0
                break
        user2 = input("user 2  ->   Rock = (R)   Paper = (P)   Scissors = (S)   Quit = (Q) : ")
        if(user2 == "R" or user2 == "P" or user2 == "S" or user2 == "Q"):
            if(user2 == "Q"):
                t == 0
                break
    else:
        user2 = input("user 2  ->   Rock = (R)   Paper = (P)   Scissors = (S)   Quit = (Q) : ")
        if(user2 == "R" or user2 == "P" or user2 == "S" or user2 == "Q"):
            if(user2 == "Q"):
                t == 0
                break
            user1 = input("user 1  ->   Rock = (R)   Paper = (P)   Scissors = (S)   Quit = (Q) : ")
        if(user1 == "R" or user1 == "P" or user1 == "S" or user1 == "Q"):
            if(user1 == "Q"):
                t == 0
                break
    # 
    # 
    print(user1,end='')
    if (user1 == "R"):
        R1 = 1
        print(" -> Rock")
    elif (user1 == "P"):
        P1 = 1
        print(" -> Paper")
    elif (user1 == "S"):
        S1 = 1
        print(" -> Scissors")
    #
    #
    print(user2,end='')
    if (user2 == "R"):
        R2 = 1
        print(" -> Rock")
    elif (user2 == "P"):
        P2 = 1
        print(" -> Paper")
    elif (user2 == "S"):
        S2 = 1
        print(" -> Scissors")
    #
    #
    if ((R1 and R2 == 1) or (P1 and P2 == 1) or (S1 and S2 == 1)):
        print("thats a tie")
        tie += 1
    elif ((R1 and S2 == 1) or (P1 and R2 == 1) or (S1 and P2 == 1)):
        print("user 1 win")
        u1 += 1
        a = 1
        c += 1
    elif ((S1 and R2 == 1) or (P1 and S2 == 1) or (P2 and R1 == 1)):
        print("user 2 win")
        u2 += 1
        a = 0
        c += 1
    print("\n")
# 
# 
print("\n===================")
print("user1 win :" , u1)
print("user2 win :" , u2)
print("tie       :" , tie)
print("===================")