import sys
sys.setrecursionlimit (10000)

def First_index(arr,n,val):
    if(n==len(arr)):
        return -1
    if(arr[n]==val):
        return n
    else:
        FI=First_index(arr,n+1,val)
        return FI
        
    
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    val=int(input())
        
    FI1=First_index(arr,0,val)
    print(FI1)
main()