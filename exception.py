a = int(input("enter your number"))

try:
    a = int(input("enter a number: "))
    print(a + 3)
 
except Exception as e:
    print("some error occurred", e)