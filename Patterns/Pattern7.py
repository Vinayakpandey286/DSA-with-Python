n=int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==j):
            print("*",end="\t")
            break
        else:
            print("",end="\t")
        
    print()
