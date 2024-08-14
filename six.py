n=int(input())
for i in range(n):
    for j in range(n):
        if ((i==0)or(j==0)or(i==n//2))or(i==n-1)|((j==n-1)&(i>=n//2)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
