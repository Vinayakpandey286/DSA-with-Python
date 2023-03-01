n=int(input())
nst=1
val=1

for i in range(n):
    for j in range(nst):
        print(val,end="	")

        val+=1
    print()

    nst+=1