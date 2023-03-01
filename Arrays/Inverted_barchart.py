def Inverted_Barchart(n,arr,max):
    for i in range(1,max+1):
        for j in range(n):
            if(i<=arr[j]):
                print("*",end="\t")
            else:
                print("",end="\t")
                
        print()
            
        

def main():
    n=int(input())
    arr=[]
    max=0
    for i in range(n):
        val=int(input())
        arr.append(val)
        if (val>max):
            max=val
            
    Inverted_Barchart(n,arr,max)
    
main()