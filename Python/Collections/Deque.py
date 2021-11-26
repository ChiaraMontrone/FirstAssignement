from collections import deque
n_operation = int(input())
list_command = []
final_list =deque()
for _ in range(n_operation):
    list_command.append(input().split())

for item in list_command:
    if item[0] == "append":
        final_list.append(int(item[1])) 
    elif item[0] == "appendleft":
        final_list.appendleft(int(item[1]))
    elif item[0] == "clear":
        final_list.clear()
    elif item[0] == "count":
        final_list.count(int(item[1]))
    elif item[0] == "print":
        print(final_list)   
    elif item[0] == "extend":
        final_list.extend(int(item[1]))
    elif item[0] == "extendleft":
        final_list.extendleft(int(item[1]))
    elif item[0] == "pop":
        final_list.pop()
    elif item[0] == "popleft":
        final_list.popleft()  
    elif item[0] == "remove":
        final_list.remove(int(item[1]))
    elif item[0] == "reverse":
        final_list.reverse()
    elif item[0] == "rotate":
        final_list.rotate(int(item[1]))
#print(''.join(final_list))
out_list=''
for elem in final_list:
    out_list = out_list +' '+str(elem)  
print(out_list[1:])
