# How do we make function in python
def add_two_number(num1, num2):
    """
    This function adds two numbers

    Args:
        num1 (int/float): first number to be added
        num2 (int/float): second number to be added
    
    Returns
        int/float: The sum of two numbers
    """
    return num1 + num2

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))

print(f"Sum is: {add_two_number(num1, num2)}")