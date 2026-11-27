a=int(input())

s1=set(input().split(" "))

b=int(input())

s2=set(input().split(" "))

s=s1.intersection(s2)

print(len(s))
