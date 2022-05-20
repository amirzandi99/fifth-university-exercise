cost = 0
cvnCountInt = 0
cvnTimeInt = 0
cvnCountExt = 0
cvnTimeExt = 0
# 
number = str(input("Enter the number : "))
# 
cvnCountInt = int(input("Enter number of Internal conversation : "))
cvnTimeInt = int(input("Enter Call time : "))
cost += (cvnTimeInt * 150) * cvnCountInt
# 
cvnCountExt = int(input("Enter number of External conversation : "))
cvnTimeExt = int(input("Enter Call time : "))
cost += (cvnTimeExt * 4000) * cvnCountExt
# 
int_internet = int(input("Enter internal internet connection time : "))
cost += int_internet * 800
ext_internet = int(input("Enter external internet connection time : "))
cost += ext_internet * 1300
# 
# 
print(f"\n\n---------- number ----------- : {number}")
print(f"Internal call time -------------- : {cvnTimeInt}")
print(f"external call time -------------- : {cvnTimeExt}")
print(f"number of Internal call time ---- : {cvnCountInt}")
print(f"number of external call time ---- : {cvnCountExt}")
print(f"internal internet connection time : {int_internet}")
print(f"external internet connection time : {ext_internet}")
print(f"---------- total cost ----------- : {cost}\n\n")