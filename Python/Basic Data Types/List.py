if __name__ == '__main__':
    N = int(input())
    list_command = []
    final_list =[]

    for _ in range(N):
        list_command.append(input().split())

    for item in list_command:
        if item[0] == "insert":
            final_list.insert(int(item[1]), int(item[2])) 
        elif item[0] == "print":
            print(final_list)
        elif item[0] == "remove":
            final_list.remove(int(item[1]))
        elif item[0] == "append":
            final_list.append(int(item[1]))
        elif item[0] == "sort":
            final_list.sort()
        elif item[0] == "pop":
            if not(not final_list):
                final_list.pop()
        elif item[0] == "reverse":
            if not(not final_list):
                final_list.reverse()
