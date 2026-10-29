print("hellow would")



def add(a , b):
    return a + b

def sub(a, b):
    return a - b

def multi(a , b):
    return(a * b)

def divide(a, b):
    return "Error : cannot divide by zero!" if b == 0 else a / b

operations = {
    "+":add,
    "-":sub,
    "*":multi,
    "/":divide
}


num1 = int(input("Enter Your Value : "))
operator = input("Enter Your Operator : ")
num2 = int(input("Enter Your Second Value : "))


if operator in operations:
    result = operations[operator](num1 , num2)
    print(f"Result {result}")

else:
    print("Invaild Operator")



# except ValueError:
#      print("Error : Please Enter Valid Number Only .")