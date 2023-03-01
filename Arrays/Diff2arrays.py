def Diff_2_arrays(n1,arr1,n2,arr2):
    max=0
    if (n1>n2):
        max=n1
    else:
        max=n2
    
    ans=[0]*max
    
    i=n1-1
    j=n2-1
    a=max-1
    
    carry=0
    while(i>=0 or j>=0):
        diff=0
        if (carry==0):
            diff=arr2[j]
        else:
            diff=arr2[j]-1
        
        carry=0
        if(i>=0):
            diff-=arr1[i]
        if(diff<0):
            carry=1
            diff+=10

        ans[a]=diff

        i-=1
        j-=1
        a-=1
    
    start_zero=True
    for i in range(len(ans)):
        if (ans[i]!=0):
            start_zero=False
        if(start_zero==False):
            print(ans[i])


def main():
    n1=int(input())
    arr1=[0]*n1

    for i in range(n1):
        val=int(input())
        arr1[i]=val

    n2=int(input())
    arr2=[0]*n2

    for i in range(n2):
        val=int(input())
        arr2[i]=val

    Diff_2_arrays(n1,arr1,n2,arr2)

main()