n=int(input())
nst=1
nsp=(n*2)-3

for i in range(1,n):
    val=1
    for j in range(nst):
        print(val,end="	")
        new_val=val
        val+=1

    for k in range(nsp):
        print("",end="	")

    for j in range(nst):
        print(new_val,end="	")
        new_val-=1 
    print()
    nsp-=2
    nst+=1

temp=1
for a in range((n*2)-1):
    print(temp,end="	")

    if (a<((n*2)-1)//2):
        temp+=1

    else:
        temp-=1