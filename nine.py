n=int(input())
row=0
col=6
for i in range(n):
    for j in range(n):
        if(i==j):
            print("*",end="")
        elif(i==row) and (j==col):
             print("*",end="")
             row=row+1
             col=col-1
        else:
            print(end=" ")
    print()
