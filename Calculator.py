def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def avg(num1,num2):
    return (num1+num2)/2

print("please select a operation: \n" \
    "1.Addition\n"\
        "2.Substraction\n"\
            "3.Multiplication\n" \
                "4.Divition\n"\
                    "5.Average\n")

select=int(input("select a operation from 1/2/3/4/5:  "))

number1=int(input("enter the first num: "))
number2=int(input("enter the second num: "))

if select==1:
  print("Sum of two number is;", add(number1,number2)) 
elif select==2:
   print("Subsraction of two number is;", sub(number1,number2)) 
elif select==3:
   print("Multiplication of two number is;", multiply(number1,number2))
elif select==4:
   print("Divition of two number is;", divide(number1,number2))
elif select==5:
   print("Avrage of two number is\2;", avg(number1,number2))
else:
    print("please selcet valid number again:\nthank you!")
