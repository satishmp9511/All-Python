x = int(input())
y = int(input())
z = int(input())
n = int(input())
result=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(n+1):
            if (i+j+k)!=n:
                result.append([i,j,k])        

print(result)  
