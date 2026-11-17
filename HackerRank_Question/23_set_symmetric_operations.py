m=int(input())
a=set(map(int , input().split()))
n=int(input())
b=set(map (int , input().split()))

s=a.symmetric_difference(b)
for i in sorted(s):
    print(i)
