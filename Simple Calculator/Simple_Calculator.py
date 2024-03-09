def add(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    try :
        res = x/y
    except :
        print("Divison by zero is not possible ")
    return res
        

def calculate (*args,**kwargs):
    res = 0
    op=None
    for key,value in kwargs.items():
        if key == "Operation" or "operation":
            op = value
    if op == "add":
        res = add(*args)
    elif op == "sub":
        res = subtraction(*args)
    elif op == "mul":
        res = multiplication(*args)
    elif op == "div":
        res = division(*args)
    else:
        print("Enter correct operation\n Select from\n 1. add\n 2. sub\n 3. mul\n 4. div\n")
        res = call()
    print()
    return res
    
def call():
    x = int(input("Enter value of x: "))
    y = int(input("Enter value of y: "))
    print("Select from\n 1. add\n 2. sub\n 3. mul\n 4. div\n Eg: Type 'add' and press Enter for addition\n")
    op = input("Operation : ")
    res = calculate(x,y,operation = op)
    return res

res = call()
print('Result : ', res)
