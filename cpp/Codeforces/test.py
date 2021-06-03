t=int(input())
for _ in range(t):
    s=input()
    su,cont,c0=0,0,0
    for i in s:
        a=int(i)
        su+=a
        if a%2==0:
            cont+=1
        if a==0:
            c0+=1
    if su%3==0 and cont>=2 and c0>=1:
        print("red")
    else:
        print("cyan")