def add_numbers(a,b,c,d):
    sum = a+b+c+d
    return sum

c=add_numbers(8,2,3,7)
print("The sum of two numbers is:",c)

def isEven_Odd(a):
    if a%2 == 0:
        print("Even")
    else:
        print("Odd")

isEven_Odd(6)

def larOf3(a,b,c):
    if a>= b and a >= c:
        print(a," is greater")
    elif b >= a and b >= c:
        print(b," is greater")
    else:
        print(c,"is greater")

larOf3(4,9,2)

def factOfNum(a):
    fact =1
    for i in range(1,a+1):
       fact = fact * i
    return fact

    
res = factOfNum(5)
print("Factorial is ",res)

def mulOfNum(a,b,c,d):
    res = a*b*c*d
    return res

res = mulOfNum(8,2,3,7)
print(res)

def string_rev(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[index -1]
        index = index - 1
    return rstr1

print(string_rev('1234abcd'))
    
    




    
    

