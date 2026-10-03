def is_leap(year):
    leap = False
    y=int(year)
    if y%4==0:
        if y%100==0:
            if y%400==0:
                leap=True
            else:
                leap=False
        else:
            leap=True
    return leap

year = int(input())
print(is_leap(year))
