# Basic Condition
num = -12

if num > 0 :
    print('Positive')
else :
    print('Negative')

# Example: Check if a number is positive, negative, or zero
num = 5

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Example: Check if a number is positive, negative, or zero
# with nested if-elif statements
num = 5

if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")
