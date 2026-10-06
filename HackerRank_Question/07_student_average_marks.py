if __name__ == '__main__':
    n = int(input())
    s = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        s[name] = scores
    q = input()
 
a=s[q][0]
b=s[q][1]
c=s[q][2]
avg=(a+b+c)/3
print(f"{avg:.2f}")
