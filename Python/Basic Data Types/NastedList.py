if __name__ == '__main__':
    
    list1 = []
 
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
    list1.sort(key=lambda lis:lis[1])
    
    snd_lowest = []
    
    list_number=[]
    for student in list1:
        list_number.append(student[1])
    list_number = list(dict.fromkeys(list_number))
    list_number.sort()
    for student in list1:
        if float(list_number[1]) == float(student[1]):
            snd_lowest.append(student[0])
    
    snd_lowest.sort()
    print (snd_lowest[0])
    if len(snd_lowest) > 1:
        print (snd_lowest[1])