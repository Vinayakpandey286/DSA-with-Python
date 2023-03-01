n=int(input())
nsp=0
for i in range(n):
    for j in range(n):
        if (j<nsp):
            print("",end="\t")
        else:
            print("*",end="\t")
    print()
        
    nsp+=1
        