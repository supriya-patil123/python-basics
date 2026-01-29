print("Day 7 python practice")

#Function that takes a number &
#prints all the numbers from 1 to that number
def print_numbers(num):
    i=1
    while i<=num:
        print(i)
        i+=1


num = int(input("Enter the number:"))
print_numbers(num)


#function that takes the number and returns the 
#square of that number
def square(num):
    return num*num


num = int(input("Enter the number:"))
print("the sqaure is:",square(num))


#function that takes the number and prints wheteher 
#the number is positive negative or zero
def pos_neg(num):
    if num>0:
        return "postive"
    elif num<0:
        return "negative"
    else:
        return "Zero"
    

num = int(input("Enter the number:"))
print("The number is",pos_neg(num))
    

#Function that prints the multiplication table of the number

def mul_of(num):
    i=1
    while i<=10:
        print(i*num)
        i += 1

num = int(input("Enter the number:"))
mul_of(num)