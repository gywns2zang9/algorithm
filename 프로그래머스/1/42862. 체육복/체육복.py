def solution(n, lost, reserve):
    lost_students = set(lost) - set(reserve)
    spare_students = set(reserve) - set(lost)

    for student in sorted(spare_students):
        if student - 1 in lost_students:
            lost_students.remove(student - 1)
        elif student + 1 in lost_students:
            lost_students.remove(student + 1)

    return n - len(lost_students)
