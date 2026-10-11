def split_and_join(line):
    f=[]
    a=line.split(" ")
    for i in a:
        f.append(i)
        if i==a[-1]:
            continue
        else:
            f.append("-")
    return "".join(f)

a=split_and_join("satish mansaram patil")
print(a)
