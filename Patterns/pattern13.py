n=int(input())
nst=1
for i in range(n):
    icj=1
    for j in range(nst):
        print(icj,end="	")
        icja1=(icj*(i-j))//(j+1)
        icj=int(icja1)

    print()
    nst+=1