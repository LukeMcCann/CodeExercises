# Write a program which can compute the factorial of a given number.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    print("The factorial of " + str(n) + " is : " + str(fact))

# Run

factorial(5)
factorial(1)
factorial(20)
factorial(23)
factorial(10)