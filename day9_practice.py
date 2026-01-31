print("Day 9 python practice")
#print numbers from 1 to N
n = int(input("Enter the number:"))

for i in range(1,n+1):
    print(i)

#Count even numbers
n = int(input("Enter the number:"))

count = 0
for i in range(1,n+1):
    if i%2 == 0:
        count += 1

print("the even numbers bet 1 and n are:",count)

#Multiplication table
n = int(input("Enter the number:"))

for i in range(1,11):
    print(i*n)
    
