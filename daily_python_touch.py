string = input("Enter the string:")

first_char = string[0]
last_char = string[-1]

print("first char is:",first_char)
print("last char is:",last_char)

text = input("Enter the string:")

if len(text) > 0 and text[0].lower() in "aeiou":
    print("starts with vowel")
else:
    print("does'nt starts with vowel")

