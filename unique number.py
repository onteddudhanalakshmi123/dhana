n=int(input())
ar=list(map(int,input().split()))
l=[]
for i in range(n):
    c=0
    for j in range(n):
        if(ar[i]==ar[j]):
            c=c+1
    if c==1:
        l.append(ar[i])
print(" ".join(map(str,l)))
        
