def main():
    n=int(input())
    nst=1
    for i in range(n):
        for j in range(nst):
            if(j<=nst):
                print("*",end="\t")
        print()

        nst+=1


main()
