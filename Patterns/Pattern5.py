n=int(input())
nst=1
csp=n//2

for i in range(1,n+1):
    for j in range(csp):
        print("",end="\t")
            
    for k in range(nst):
        print("*",end="\t")
            
    print()
    
    if (i<=(n//2)):
        nst+=2
        csp-=1
        
    else:
        nst-=2
        csp+=1
        