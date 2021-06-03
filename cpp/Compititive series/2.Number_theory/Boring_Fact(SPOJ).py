'''
Sameer and Arpit have got bored of solving problems involving factorials. So to make things interesting 
for them, Aman - The Mathemagician, gives them a prime number P and an integer N close to P, and asks 
them to find N! modulo P.

Input:  First line contains an integer T, the number of queries asked.
        
        Next T lines contains T queries of the form N P.

Output: Output exactly T lines, containing N! modulo P.
'''

def fast_eponentiation(base,expo,p):
    res=1
    if base==0:
        return 0
    while expo:
        if expo %2==1:
            res=(res*base)%p
        expo=expo//2
        base=(base*base)%p
    return res

t=int(input())
for _ in range(t):
    n,p=map(int,input().split())

    if n>=p:
        #if n>=p then, n! mod p =0
        print(0)
    else:
        #if n<p then n!= (P-1)! * [(n+1)*(n+2)*(n+3)......(p-1)]^(-1)
        #now, [(n+1)*(n+2)*(n+3)......(p-1)]^(-1) mod p =[(n+1)*(n+2)*(n+3)......(p-1)]^(p-2) mod p
        # n! mod p  =(p-1) mod p * [(n+1)*(n+2)*(n+3)......(p-1)]^(p-2) mod p
        #           =(p-1) * [(n+1)*(n+2)*(n+3)......(p-1)]^(p-2) mod p
        mod=1
        for i in range(n+1,p):
            mod=(mod*i)%p
        mod=fast_eponentiation(mod,(p-2),p)
        mod=(mod*(p-1))%p
    print(mod)