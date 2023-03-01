def dec_to_bin(n,arr):
    msb=2**n
    for dec in range(msb):
        ans=[]
        max=0
        while(max<n):
            rem=dec%2
            ans.insert(0,rem)
            dec=dec//2
            
            max+=1
        
        for index in range(len(ans)):
            if(ans[index]==0):
                print("-\t",end="")
            else:
                print(f"{arr[index]}\t",end="")
        print()

def main():
    n=int(input())
    arr=[]
    
    for i in range(n):
        val=int(input())
        arr.append(val)
    
    dec_to_bin(n,arr)
    

main()