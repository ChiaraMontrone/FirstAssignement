if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    for name, score in student_marks.items():
        if name == query_name:
            print("{:.2f}".format(round(sum(score)/len(score),2)))