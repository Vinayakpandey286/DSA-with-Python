n=int(input())
nst=n
nsp=0
for i in range(n):
    for k in range(nsp):
        print("",end="	")
    for j in range(nst):
        if(i==0 or i==n-1):
            print("*",end="	")
        elif(i>=n//2):
            print("*",end="	")
        else:
            if((j==0 or j==nst-1) and i<n//2):
                print("*",end="	")
            else:
                print("",end="	")
    for l in range(nsp):
        print("",end="	")
    


    print()

    if(i<n//2):
        nst-=2
        nsp+=1
    else:
        nst+=2
        nsp-=1