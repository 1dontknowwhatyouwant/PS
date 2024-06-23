submitted = [int(input()) for _ in range(28)]
all_students = set(range(1, 31))
submitted_set = set(submitted)
missing_students = all_students - submitted_set

for student in sorted(missing_students):
    print(student)
