n=int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        if ((i+j)==(n+1)):
            print("*",end="	")
            break
        else:
            print("",end="	")
    
    print()