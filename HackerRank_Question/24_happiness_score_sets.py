
m,n=map(int , input().split())


list_=map(int ,input().split())

set_1=set(map(int,input().split()))
set_2=set(map(int,input().split()))

k=0

for i in list_:
    if i in set_1:
        k+=1
    elif i in set_2:
        k-=1
print(k)
