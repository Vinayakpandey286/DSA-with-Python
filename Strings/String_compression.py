def string_compression(st):
    temp1=st[0]
    temp2=st[0]
    count=1
    # wwwwaaadexxxxxx
    for i in range(1,len(st)):
        if(st[i]!=st[i-1]):
            temp1+=st[i]
            if(count==1):
                temp2+=""
            else:
                temp2+=str(count)
            temp2+=st[i]
            count=1
        else:
            count+=1
    if(count==1):
        temp2+=""
    else:
        temp2+=str(count)
            
    print(temp1) 
    print(temp2)
st = str(input())
string_compression(st)