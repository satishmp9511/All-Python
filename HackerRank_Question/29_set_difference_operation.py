n=int(input())

s1=set(input().split(" "))

N=int(input())

s2=set(input().split(" "))

s=s1.difference(s2)

print(len(s))
