def first(arr,n,key):
    lo,hi=0,n-1
    while lo<=hi:
        mid=(lo+hi)//2
        if arr[mid]==key:
            if arr[mid]==arr[mid-1] and mid-1>=0:
                hi=mid-1
            else:
                return mid
        elif key>arr[mid]:
            lo=mid+1
        else:
            hi=mid-1
    return -1

def last(arr,n,key):
    lo,hi=0,n-1
    while lo<=hi:
        mid=(lo+hi)//2
        if arr[mid]==key:
            if arr[mid]==arr[mid+1] and mid+1<n:
                lo=mid+1
            else:
                return mid
        elif key>arr[mid]:
            lo=mid+1
        else:
            hi=mid-1
    return -1

if __name__ == '__main__':
    n=int(input())
    arr=[]
    for i in range(n):
        ele=int(input())
        arr.append(ele)
       
    key=int(input())
    
    fi=first(arr,n,key)
    la=last(arr,n,key)
    
    print(fi)
    print(la)