
n = int( input() )
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list( map(float, line))
    student_marks[name] = scores

query_name = input()

score = student_marks.get(query_name)
porcentage = sum(score)/len(score)


print("%2f" % porcentage)#Fijar un limite de decimales 

