def Get_MazepathWJump(sr,sc,dr,dc):
    if (sr==dr and sc==dc):
        temp=[]
        temp.append("")
        return temp
    elif (sr>dr or sc>dc):
        temp=[]
        return temp
    
    path=[]
    for i in range(1,(dc-sc)+1):
        path_H=Get_MazepathWJump(sr,sc+i,dr,dc)
        for x in path_H:
            path.append("h"+str(i)+x)
    
    
    for j in range(1,(dr-sr)+1):
        path_V=Get_MazepathWJump(sr+j,sc,dr,dc)
        for y in path_V:
            path.append("v"+str(j)+y)
    
    k=1
    while(k<=dr-sr and k<=dc-sc):
        path_D=Get_MazepathWJump(sr+k,sc+k,dr,dc)
        for z in path_D:
            path.append("d"+str(k)+z)
        k+=1

    return path

n=int(input())
m=int(input())
path=Get_MazepathWJump(1,1,n,m)
print("["+", ".join(path)+"]")