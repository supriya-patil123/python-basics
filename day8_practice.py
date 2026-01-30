print("Day 8 python practice")

def can_vote(age):
    if age>=18:
        return "Eligible"
    else:
        return "Not Eligible"
    
age = int(input("Enter your age:"))
result = can_vote(age)
print("you are",result,"to vote")

def find_max(a,b):
    return max(a,b)
    
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
print("The maxinmun number is ",find_max(a,b))

def sum_of(num):
    total = 0
    i=1
    for i in range(1,num+1):
        total += i
    return total
      
num = int(input("enter the number :"))
print("The sum of first" ,num, "Number is ",sum_of(num))

