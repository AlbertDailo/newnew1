num1 = int(input("Enter a NumOne:"))
num2 = int(input("Enter a NumTwo:"))
choose = input("CHOOSE AN OPERATIONS: +, -, *, /: ")

if choose == '+':
    result = lambda a,b : a+b
    print(f"{num1}+{num2} ={result(num1,num2)}")
elif choose == '-':
    result = lambda a,b : a-b
    print(f"{num1}+{num2} ={result(num1,num2)}")
elif choose == '*':
    result = lambda a,b : a*b
    print(f"{num1}+{num2} ={result(num1,num2)}")
elif choose == '/':
    result = lambda a,b : a/b
    print(f"{num1}+{num2} ={result(num1,num2)}")
else:
    print("error")