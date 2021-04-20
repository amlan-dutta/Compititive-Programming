'''
You will be given two relatively prime integers a and b. You must 
give two coefficients u and v, such that au+bv=1.

Input Format:   A single line with two integers, a and b. These integers are guaranteed to be relatively 
                prime.

Output Format:  Two space-separated integers u and v.
'''
def extended_euclid_algo(x,y):
    if y==0:
        a=1
        b=0
    else:
        a1,b1=extended_euclid_algo(y,x%y)
        a=b1
        b=a1-b1*(x//y)
    return a,b

x,y=map(int,input().split())
a,b=extended_euclid_algo(max(x,y),min(x,y))
print(a,b)
#gcd=a*x+b*y
#print(gcd)
