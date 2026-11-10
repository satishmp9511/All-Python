import random

name_list=['satish', 'mahendra', 'nilesh', 'virat', 'a mumbai cat', 'rahul', 'priya', 'amit', 'neha', 'rohit', 'pooja', 'sachin', 'a delhi boy', 'an Indian player', 'a smart boy', 'a cute dog', 'my friend', 'our teacher', 'the clever fox', 'the big car']
action=['accept', 'ask', 'begin', 'break', 'bring', 'build', 'buy', 'catch', 'choose', 'clean', 'close', 'come', 'cry', 'dance', 'do', 'draw', 'drink', 'drive', 'explain', 'fall', 'feel', 'find', 'fly', 'forget', 'get', 'give', 'go', 'grow', 'happen', 'have', 'hear', 'help', 'hold', 'keep', 'know', 'learn', 'leave', 'like', 'listen', 'live', 'look', 'make', 'meet', 'move', 'open', 'pay', 'play', 'put', 'read', 'run']
places=['delhi', 'mumbai', 'pune', 'nagpur', 'school', 'college', 'hospital', 'market', 'park', 'house', 'room', 'kitchen', 'station', 'airport', 'garden', 'temple', 'office', 'beach', 'hotel', 'shop']
all_word=[]
link=r"C:\Users\INOOOOOOO\OneDrive\Desktop\random_file\for_py_project\fake_news.txt"

def random_choose():
    random_name=random.choice(name_list)
    random_action=random.choice(action)
    random_places=random.choice(places)
    word=f"breking news : {random_name} {random_action} {random_places}."
    all_word.append(word)
    return word
def choose(word):
    choose_3=input("enter(y/n)save file:")
    if choose_3.lower().strip()=="y":
        save_file(word)
    else:
        print("ok")
def show_all():
    for i in all_word:
        print(i)
    print("--------------------------------------------")
    choose_2=input("save in file(y/n):")
    if choose_2.lower().strip()=="y":
        for i in all_word:
            save_file(i)
    else:
        print("ok")
    print("--------------------------------------------")
def save_file(aa):
    with open(link,'a') as f:
        f.write(f'{aa}\n')
        print("save in your file")

while True:
    print("--------------------------------------------")
    print("---welcome--")
    print("--------------------------------------------")
    print("1.genertar news\n2.show all news\n3.exit")
    choose_1=input("choose one number:")
    print("--------------------------------------------")
    if choose_1.strip()=='1':
        random_news=random_choose()
        print(random_news)
        choose(random_news)
        print("--------------------------------------------")
    elif choose_1.strip()=='2':
        show_all()
        print("--------------------------------------------")
    elif choose_1.strip()=='3':
        print("Good By")
        print("--------------------------------------------")
        break
    else:
        print("you choose wrong number")
        print("--------------------------------------------")
    
