def substring(st):
    for i in range(len(st)):
        for j in range(i+1,len(st)+1):
            s=st[i:j]
            if (palindrome(s)==True):
                print(s)

def palindrome(s):
    i=0
    j=len(s)-1
    while(i<=j):
        if(s[i]!=s[j]):
            return False
        else:
            i+=1
            j-=1
            
    return True
            
st = str(input())
substring(st)