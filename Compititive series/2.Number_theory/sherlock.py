'''
Sherlock receives a note from Moriarty boasting about infecting The Beast with a virus. He also gives him 
a clue: an integer. Sherlock determines a key to remove the virus is to find the largest Decent Number 
having that number of digits.

A Decent Number has the following properties:
    1.  Its digits can only be 3's and/or 5's.
    2.  The number of 3's it contains is divisible by 5.
    3.  The number of 5's it contains is divisible by 3.
    4.  It is the largest such number for its length.

Input format:   The first line is an integer, , the number of test cases.

                The next  lines each contain an integer , the number of digits in the number to create.

Output format:  Print the decent number for the given length, or -1 if a decent number of that length 
                cannot be formed.

'''

import sys

def decentNumber(n):
    if n<3:
        print(-1)
        return
    #if n is divisable by 3 the maximmum possible number is n 5s
    elif n%3==0:
        for _ in range(n):
            sys.stdout.write('5')
        sys.stdout.write('\n')
        return
    else:
        #here a is number of 3s and b is number of 5s and a+b=n
        #but a should be divisable by 5 and b should be divisable by 3
         a=5
         b=n-5
         while b>0:
            if b%3==0:
                break
            else:
                a+=5
                b-=5
         if b>=0:
            for _ in range(b):
                sys.stdout.write('5')
            for _ in range(a):
                sys.stdout.write('3')
            sys.stdout.write('\n')
            return
         else:
            print(-1)
            return
                

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        decentNumber(n)
