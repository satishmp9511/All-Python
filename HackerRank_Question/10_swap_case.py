def swap_case(s):
    f=[]
    for i in s:
        if i.isupper():
            f.append(i.lower())
        elif i.islower():
            f.append(i.upper())
        else:
            f.append(i)
    return "".join(f)

s=swap_case("AaBb")
print(s)
