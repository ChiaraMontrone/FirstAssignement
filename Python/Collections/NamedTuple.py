from collections import namedtuple
n_students = int(input())
Student = namedtuple('Student',input())
marks=0
for i in range(0,n_students):
    a,b,c,d = input().split()
    named_student_tuple = Student(a,b,c,d)
    marks = marks + int(named_student_tuple.MARKS)
print(marks/n_students)
