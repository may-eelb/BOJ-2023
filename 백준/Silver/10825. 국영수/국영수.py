from sys import stdin
from collections import deque
input = stdin.readline
def sort_criteria(student):
    name, korean, english, math = student
    return (-korean, english, -math, name)

def main():
    N = int(input())
    students = []

    for _ in range(N):
        name, korean, english, math = input().split()
        korean, english, math = int(korean), int(english), int(math)
        students.append((name, korean, english, math))

    sorted_students = sorted(students, key=sort_criteria)

    for student in sorted_students:
        print(student[0])

if __name__ == "__main__":
    main()