def get_denomination(n,money,key):
    lo,hi=0,n-1
    while lo<=hi:
        mid=(lo+hi)//2
        if key==money[mid]:
            return [money[mid]]
        elif key>money[mid]:
            lo=mid+1
        else:
            hi=mid-1
    return [money[lo],money[lo-1]]  
           
if __name__ == '__main__':
    n=int(input())
    money=[]
    for i in range(n):
        ele=int(input())
        money.append(ele)
       
    key=int(input())
   
    result=get_denomination(n,money,key)
    for i in result:
        print(i)