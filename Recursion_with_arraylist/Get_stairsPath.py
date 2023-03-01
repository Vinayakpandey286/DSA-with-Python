def Get_stairpath(n):
    if (n==0):
        lp=[]
        lp.append("")
        return lp
    elif(n<0):
        lp=[]
        return lp
        
    path1=Get_stairpath(n-1)
    path2=Get_stairpath(n-2)
    path3=Get_stairpath(n-3)
    
    path=[]
    for x in path1:
        path.append(str(1)+x)
    
    for y in path2:
        path.append(str(2)+y)
    
    
    for z in path3:
        path.append(str(3)+z)
    
    return path
n=int(input())
path=Get_stairpath(n)
print("["+", ".join(path)+"]")