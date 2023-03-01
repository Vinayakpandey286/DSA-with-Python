n=int(input())
nst=1
nsp=n//2

val=1
for i in range(n):
    for j in range(nsp):
        print("",end="	")

    new_val=val
    for k in range(nst):
        print(new_val,end="	")

        if(k<nst//2):
            new_val+=1
        else:
            new_val-=1

    
    if (i<(n//2)):
        nst+=2
        nsp-=1
        val+=1

    else:
        nst-=2
        nsp+=1
        val-=1

    print()