

print("--------------------------------------------------")
print("---------------------wellcome---------------------")
try:
    dis={
        1:["a","what is the correct extension of python filr?",'.py','.pyt','.p','.pyton'],
        2:["c","what...",'r','rr','rrr','rrrr'],
        3:["a","how....",'e','ee','eee','eeee']
    }
    with open(r"C:\Users\INOOOOOOO\OneDrive\Desktop\projet\Q.txt","r") as file:
        for i in file:
            p=i.split(",")
            w=p[0].strip()
            ans=p[1].strip()
            Qu=p[2].strip()
            a1=p[3].strip()
            a2=p[4].strip()
            a3=p[5].strip()
            a4=p[6].strip()
            dis[w]=[ans,Qu,a1,a2,a3,a4]
    sc=0
    e=4
    w=1
    Q=1 
    def an():
        print(f"a:{dis[w][2]}\nb:{dis[w][3]}\nc:{dis[w][4]}\nd:{dis[w][5]}")
        print("--------------------------------------------------")
    while True:
        print("--------------------------------------------------")
        print(f"Q{Q}.{dis[w][1]}")
        an()
        choose=input("enter options:")
        key=dis[w][0]
        if choose==key:
            print("correet answer..")
            sc+=1    
        else:
            print("wrong answer..")
        w+=1
        Q+=1
        
        if w==e:
            break
except ValueError as v:
    print(v)
except TypeError as t:
    print(t)
except FileNotFoundError as f:
    print(f)
print("--------------------------------------------------")
print(f"your correet answer is {sc}")
print("good by see next time..")
print("--------------------------------------------------")
 
