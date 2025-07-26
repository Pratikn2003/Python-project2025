def add(x,y):
  return x+y
def sub(x,y):
  return x-y
def mul(x,y):
  return x*y
def div(x,y):
  if y == 0:
    return "error.. not the division"
  return x/y
num1=float(input("enter the number: "))
num2=float(input("enter the number: "))
choice=input("enter the choice add,sub,mul,div: ")
if choice in['add','sub','mul','div']:
 if(choice == 'add'):
     print(add(num1,num2))

 elif(choice == 'sub'):
     print(sub(num1,num2))

 elif(choice == 'mul'):
     print(mul(num1,num2))

 elif(choice == 'div'):
     print(div(num1,num2))

 else:
     print("invalid operation")
