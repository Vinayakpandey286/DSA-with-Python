n=int(input())
nst=1
nsp=n//2

for i in range(1,n+1):
    for j in range(nsp):
        if (i==(n//2)+1):
            print("*",end="	")
        else:
            print("",end="	")
    for k in range(nst):
        print("*",end="	")

    print()

    if(i<=n//2):
        nst+=1
    else:
        nst-=1