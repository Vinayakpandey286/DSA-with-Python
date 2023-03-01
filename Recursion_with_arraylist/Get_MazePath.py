def Get_Mazepath(sr,sc,dr,dc):
    if (sr==dr and sc==dc):
        temp=[]
        temp.append("")
        return temp
    
    path_H=[]
    path_V=[]
    if (sc<dc):
        path_H=Get_Mazepath(sr,sc+1,dr,dc)
    if (sr<dr):
        path_V=Get_Mazepath(sr+1,sc,dr,dc)
    
    path=[]
    
    for x in path_H:
        path.append("h"+x)
        
    
    for y in path_V:
        path.append("v"+y)
        
    return path
    
n=int(input())
m=int(input())
path=Get_Mazepath(1,1,n,m)
print("["+", ".join(path)+"]")