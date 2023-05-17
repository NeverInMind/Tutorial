score = [1, 2, 3, 3, 4, 5, 5 ]
ects = ['F', 'FX', 'E', 'D', 'C', 'B', 'A']
description = ['Unsatisfactorily', 'Unsatisfactorily', 'Enough', 'Satisfactorily', 
               'Good', 'Very good', 'Perfectly']
score_table = []
for i in ects:
    g_index = ects.index(i)
    score_tab = {
        'score': score[g_index],
        'ects': ects[g_index],
        'description': description[g_index]
    }
    score_table.append(score_tab)


def get_grade(key):
    global score_table
    for i in score_table:
        if i.get('ects') == key:
            return(i.get('score'))


def get_description(key):
    global score_table
    for i in score_table:
        if i.get('ects') == key:
            return(i.get('description'))