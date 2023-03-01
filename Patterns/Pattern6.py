n=int(input())
nsp=1
nst=(n//2)+1

for i in range(1,n+1):
    for j in range(nst):
        print("*",end="\t")
        
    for k in range(nsp):
        print("",end="\t")
        
    for l in range(nst):
        print("*",end="\t")
        
    print()
        
    if(i<=(n//2)):
        nst-=1
        nsp+=2
        
    else:
        nst+=1
        nsp-=2
    
    