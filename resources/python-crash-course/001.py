'''
When you use input you get information from the user
 - This information obtained from input is always of type string
 - When you pass the information recieved from input to int() it gets typecasted
 - Typecasting is simply converting a type from one form to the other e.g. string to int
'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2

print(f"{num1} + {num2} = {sum}")