p = 10000
n = 12
r = 0.08

t_str = input("Enter the number of years:")
t = int(t_str)

A = p*(1 + r/n)**(n*t)

print(f"the final amount after {t} years is {A:.2f}")


str = input("Enter the string:")

print(len(str))
print(str.upper())
print(str.lower())
print(str[::-1])


#list and set operations
"""
 You are given a list of numbers with duplicates. Create a new list containing only the unique elements.
 Then, find the common elements between the original unique list and a separate set
  of numbers from 5 to 15. 
"""
original_list = [1,2,3,4,5,3,3,4,6,6,9,7,1,7]

unique_list = set(original_list)
print(f"list with unique elements are {unique_list}")

separate_set = set(range(5,16))
print(f"separate set elements are:{separate_set}")

common_elements = set(unique_list).intersection(separate_set)
print(f"The common elements are:{common_elements}")