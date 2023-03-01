n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i<=n//2 and (j==1 or j==n)):
            print("*",end="	")
        elif(i>n//2 and (i==j or i+j==n+1 or j==1 or j==n)):
            print("*",end="	")
        else:
            print("",end="	")

    print()