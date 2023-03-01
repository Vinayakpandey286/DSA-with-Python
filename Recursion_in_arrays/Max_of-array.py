import sys
sys.setrecursionlimit (10000)

def display(arr,n):
    if(n==0):
        return 0
    
    max_of_array=display(arr,n-1)
    if(arr[n-1]>max_of_array):
        return arr[n-1]
    return max_of_array

 
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
        
    temp=display(arr,n)
    print(temp)
    
main()