def add(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y


def calculate (*args,**kwargs):
    res = 0
    op=None
    for key,value in kwargs.items():
        if key == "operation" or "Operation":
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
    return res
    

res = calculate(10,20,operation = 'div')
print(res)