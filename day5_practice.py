print("day 5 python practice")

count=2

while count<=5:
    print("count:",count)
    count += 1

number = int(input("Enter the number:"))

i=1
while i<=number:
    print(i)
    i += 1

password = "python90"
user_input=input("Enter password:")

while user_input != password:
    print("Wrong password")
    user_input = input("Enter password again:")

print("Login successfully")

number = int(input("Enter the number:"))

i=1
while i<=10:
    print(number*i)
    i += 1