'''
Title     : Arithmetic Operators
Domain    : Python
Author    : Aadarshkumar Madhukar Jadhav
Created   : 07 April 2022
Problem   : https://www.hackerrank.com/challenges/python-arithmetic-operators?
'''

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    '''
    # Easily we directly print outputs using Operators
    print(a+b)
    print(a-b)
    print(a*b)
    '''

    # \n is new line character.
    # Here we store results in variables and then print it.
    sum, sub, mul = a+b, a-b, a*b
    print(f"{sum}\n{sub}\n{mul}")
