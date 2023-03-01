# import sys
# sys.setrecursionlimit (10000)

def get_subsequence(st):
    if (len(st)==0):
        myres=[]
        myres.append("")
        return myres
    fs=st[0]
    ros=st[1:]
    arr=get_subsequence(ros)
    
    real_arr=[]
    for val in arr:
        real_arr.append(""+val)
    
    for val in arr:
        real_arr.append(fs+val)
    
    return real_arr
    

st=str(input())
res=get_subsequence(st)
print("["+", ".join(res)+"]")