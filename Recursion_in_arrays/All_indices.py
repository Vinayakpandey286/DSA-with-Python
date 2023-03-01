import sys
sys.setrecursionlimit (10000)

def All_Indices(arr,n,val,new_arr):
    if(n==len(arr)):
        return
    if(arr[n]==val):
        new_arr.append(n)
        
        
    All_Indices(arr,n+1,val,new_arr)

        
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    val=int(input())
    new_arr=[]
    
        
    All_Indices(arr,0,val,new_arr)
    if len(new_arr)==0:
        print("")
    else:    
        for a in new_arr:
            print(a)
    
main()