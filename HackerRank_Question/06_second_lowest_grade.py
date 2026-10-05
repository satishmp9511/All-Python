l=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
all=[]
for i in l:
    all.append(i[1])
sc=list(set(all))
sc.sort()
sel_1=sc[1]
sel_2=sc[0]
sename=[]
for i in l:
    if sel_1==i[1]:
        sename.append(i[0])
    # if sel_2==i[1]:
    #     sename.append(i[0])
sename.sort()
for i in sename:
    print(i)
