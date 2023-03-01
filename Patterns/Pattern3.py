def main():
    n=int(input())
    nsp=n
    for i in range(n):
        for j in range(n):
            if(j<(nsp-1)):
                print("",end="\t")
            else:
                print("*",end="\t")
                
        nsp-=1
        print()
        
        
main()
            