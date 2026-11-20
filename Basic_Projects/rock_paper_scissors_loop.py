import random

print("_________________________________________________") 
print("------wellcome to rock,paper,scissors-game------")
user_=0
computer_=0
tie_=0
print("_________________________________________________")  
while True:
    list=['rock','paper','scissors']
    computer=random.choice(list) 
    man=input("enter a rock , paper or scissors:").lower()
    print("_________________________________________________")  
    print(f"your choice {man}..\t..computer choice {computer}")
    print("_________________________________________________")  
    if computer==man:
        print("game tie...")
        tie_ += 1
    elif computer=='rock':
        if man=='paper':
            print("you are the winner..")
            user_ +=1
        elif man=='scissors':
            print("you lose the game..")
            computer_ +=1
        else:
            print("you typed a wrong keyword.")
    elif computer=='scissors':
        if man=='rock':
            print("you are the winner..")
            user_ +=1
        elif man=='paper':
            print("you lose the game..")
            computer_ +=1
        else:
            print("you typed a wrong keyword.")
    elif computer=='paper':
        if man=='scissors':
            print("you are the winner..")
            user_ +=1
        elif man=='rock':
            print("you lose the game..")
            computer_ +=1
        else:
            print("you typed a wrong keyword.")
    else:
        print("hi")
    
    man=input("(continue-c or Exit-e ) :")
    if man=='c':
        continue
    else:
        break

print("_________________________________________________")    
print(f'.your score:{user_},,how game tie {tie_},,computer score{computer_}.')
