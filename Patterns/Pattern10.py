n=int(input())

insp=n//2
onsp=-1

for i in range(1,n+1):
    for j in range(insp):
        print("",end="	")

    print("*",end="	")

    for l in range(onsp):
        print("",end="	")


    if (i>1 and i<n):
        print("*",end="	")

    print()

    if(i<=(n//2)):
        insp-=1
        onsp+=2
        
    else:
        insp+=1
        onsp-=2