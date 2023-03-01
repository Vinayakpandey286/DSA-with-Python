n=int(input())
nst=1
n1=0
n2=1

for i in range(n):
    if nst==1:
        for j in range(nst):
            print(n1,end="	")
    
    else:
        for j in range(nst):
            print(n2,end="	")

            temp=n1
            n1=n2
            n2+=temp


        
    print()

    nst+=1