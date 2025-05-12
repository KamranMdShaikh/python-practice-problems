def find_elder_brother(a,b):
    if a > b:
        print("Brother 1 is older")
    if b > a:
        print("Brother 2 is older")
    else:
        print("Both brother are equal")

a = int(input("Enter age of Brother 1: "))
b = int(input("Enter age of Brother 2: "))


find_elder_brother(a,b)

