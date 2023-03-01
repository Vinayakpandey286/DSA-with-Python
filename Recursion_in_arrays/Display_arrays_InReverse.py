def display(arr,n):
    if(n==0):
        return
    
    print(arr[n-1])
    display(arr,n-1)
    

 
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
        
    display(arr,n)
    
    
main()