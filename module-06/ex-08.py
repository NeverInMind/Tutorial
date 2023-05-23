grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}


def formatted_grades(students):
    res_arr = []
    i = 1
    for name, grade in students.items():
        res_arr.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(
            i, name, grade, grades[grade]))
        i += 1
    return res_arr


for el in formatted_grades(students):
    print(el)
