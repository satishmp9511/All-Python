
# list=[]
# list.insert(0,5) 
# list.insert(1,10)
# list.insert(0,6) 
# print(list)
    
# list.remove(6)
# list.append(9)
# list.append(1)   
# list.sort()
# print(list)

# list.pop()
# list.reverse()
# print(list)

if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        command = input().split()
        
        action = command[0]
        
        if action == "insert":
            index = int(command[1])
            element = int(command[2])
            my_list.insert(index, element)
            
        elif action == "print":
            print(my_list)
            
        elif action == "remove":
            element = int(command[1])
            my_list.remove(element)
            
        elif action == "append":
            element = int(command[1])
            my_list.append(element)
            
        elif action == "sort":
            my_list.sort()
            
        elif action == "pop":
            my_list.pop()
            
        elif action == "reverse":
            my_list.reverse()














