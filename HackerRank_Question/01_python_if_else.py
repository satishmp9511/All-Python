n=5
word="Weird"
if n%2==1:
    print(word)
elif n%2==0:
    if n>=2 and n<=5:
        print(f"Not {word}")    
    elif n>20:
        print(f"Not {word}")
    else:
        print(word)
