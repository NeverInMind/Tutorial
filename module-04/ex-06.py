def split_list(grade):
    more_arr =[]
    less_arr = []
    try:
        avg_score = sum(grade) / len(grade)
        for score in grade:
            if score <= avg_score:
                less_arr.append(score)
            elif score > avg_score:
                more_arr.append(score)
        return less_arr, more_arr
    except ZeroDivisionError:
        return less_arr, more_arr