a=int(input())
first=0
second=1
print(first)
print(second)
for i in range(1,a-1):
    temp=first+second
    print(temp)
    first=second
    second=temp

