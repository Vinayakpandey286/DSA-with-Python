# import sys
# sys.setrecursionlimit (10000)

def get_kpc(st):
    if(len(st)==1):
        return key[st]
    
    ch=st[0]
    ros=st[1:]
    arr=get_kpc(ros)
    new_arr=[]
    for i in range(len(key[ch])):
        for j in range(len(arr)):
            new_arr.append(key[ch][i]+arr[j])
        
    return new_arr
        
        
    
st=str(input())
key={"0":[".",";"],
    "1":["a","b","c"],
    "2":["d","e","f"],
    "3":["g","h","i"],
    "4":["j","k","l"],
    "5":["m","n","o"],
    "6":["p","q","r","s"],
    "7":["t","u"],
    "8":["v","w","x"],
    "9":["y","z"]}
res=get_kpc(st)
print("["+", ".join(res)+"]")