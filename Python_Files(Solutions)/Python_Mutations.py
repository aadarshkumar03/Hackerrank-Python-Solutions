'''
Title     : Python: Print Full Name
Domain    : Python
Author    : Aadarshkumar Madhukar Jadhav
Created   : 12 April 2022
Problem   : https://www.hackerrank.com/challenges/python-mutations/problem?
'''

def mutate_string(string, position, character):
    # We can do easilt with string concatenation
    '''
    result = string[:position]+character+string[position+1:]
    return result
    '''

    # Here first we convert string into list and then assign a value 
    l = list(string)
    l[position] = character
    s = ''.join(l)
    return s

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
