'''
Title     : Python If-Else
Domain    : Python
Author    : Aadarshkumar Madhukar Jadhav
Created   : 06 April 2022
Problem   : https://www.hackerrank.com/challenges/py-if-else/problem
'''

if __name__ == '__main__':
    n = int(input().strip())
    if (n%2!=0):
        print("Weird")
    else:
        if 2<=n<=5:
            print("Not Weird")
        elif 6<=n<=20:
            print("Weird")
        elif n>20:
            print("Not Weird")