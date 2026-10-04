n = int(input())
arr = map(int, input().split())

a=list(set(arr)) #set =automatically remove duplicate
a.sort()         #list function sort

print(a) 
