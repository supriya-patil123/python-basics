print("Day  6 python practice")

def greet():
    print("Hello,welcome to pyhton")

greet()

def greet_user(name):
    print("Hello",name)

greet_user("Supriya")
greet_user("Engineer")

def add(a,b):
    return a+b

result = add(10,6)
print("sum is ",result)

def is_even_or_odd(num):
    if num % 2 == 0:
        return "Even" 
    else:
        return "Odd"
    

num =int(input("Enter number:"))
result=is_even_or_odd(num)
print(result)



