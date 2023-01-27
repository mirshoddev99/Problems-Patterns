"""Write a Python program to convert GPAs to letter grades according to the
following table: Go to the editor
GPAs Grades
4.0: A+
3.7: A
3.4: A-
3.0: B+
2.7: B
2.4: B-
2.0: C+
1.7: C
1.4: C-
below: F
Input:
[4.0, 3.5, 3.8]
Output:
['A+', 'A-', 'A']
Input:
[5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]
Output:
['A+', 'A+', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'F']"""


def test(gpa):
    grades = []
    for i in gpa:
        if 3.7 < i >= 4.0:
            grades.append('A+')
        elif 3.7 <= i < 4.0:
            grades.append('A')
        elif 3.4 <= i < 3.7:
            grades.append('A-')

        elif 3.0 <= i < 3.4:
            grades.append('B+')
        elif 2.7 <= i < 3.4:
            grades.append('B')
        elif 2.4 <= i < 2.7:
            grades.append('B-')

        elif 2.0 <= i < 2.4:
            grades.append('C+')
        elif 1.7 <= i < 2.0:
            grades.append('C')
        elif 1.4 <= i < 1.7:
            grades.append('C-')
        else:
            grades.append('F')

    return grades


gpa_list = [4.0, 3.5, 3.8]
print(test(gpa_list))

gpa_list = [5.0, 4.7, 3.4, 3.0, 2.7, 2.4, 2.0, 1.7, 1.4, 0.0]
print(test(gpa=gpa_list))