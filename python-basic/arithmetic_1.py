'''Task
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.'''

from unittest import result

def sum_of_twonumbers(a, b):
    result = a + b
    return result

def difference_of_twonumbers(a, b):
    result = a - b
    return result

def product_of_twonumbers(a, b):
    result = a * b
    return result

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(sum_of_twonumbers(a, b))
    print(difference_of_twonumbers(a, b))
    print(product_of_twonumbers(a, b))