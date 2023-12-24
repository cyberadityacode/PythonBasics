print("Hello Strings Lesson 1")     
# Program to reverse the given string

given_string = input("Enter the string: ")
reverse_string = ""

for i in given_string:
    reverse_string = i + reverse_string
    
print(reverse_string)
