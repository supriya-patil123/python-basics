#check even/odd
num = int(input("Enter the number: "))
if(num % 2 == 0):
    print("Even")
else:
    print("odd")

#find gretaest of 3 numbers
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
num3=int(input("enter num3:"))

if(num1 >= num2 and num1 >=  num3):
    print(num1,"is greater")
elif(num2 >= num1 and num2 >= num3):
    print(num2 ,"is greater")
else:
    print(num3,"is greater")

#leap year
year = int(input("Enter the year:"))

if(year % 400 ==0):
    print("its a leap year")
else:
    print("its not a leap year")

#grade calculator
totalMarks = int(input("enter the total marks:"))

if(totalMarks >= 85 ):
    print("Grade A")
elif(totalMarks >= 75 and totalMarks < 85):
    print("Grade B")
elif(totalMarks >= 65 and totalMarks < 75):
    print("Grade C")
else:
    print("Fail")
