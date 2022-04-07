'''
Title     : Python: Division
Domain    : Python
Author    : Aadarshkumar Madhukar Jadhav
Created   : 07 April 2022
Problem   : https://www.hackerrank.com/challenges/python-division/problem?
'''

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    '''
    # Directly we print using / and // Division Operators
    print(a//b)
    print(a/b)
    '''
    
    # \n is new line character.
    # Here we store result in variable and then print it.
    floor_div, div = (a//b), (a/b)
    print(f"{floor_div}\n{div}")    
