def solve_riddle(riddle, word_length, start_letter, reverse=False):
    new_one = riddle.find(start_letter)
    finder = ''
    if new_one != -1:
        if reverse:
            start = new_one - word_length
            finder = riddle[new_one:start:-1]
        else:
            start = new_one + word_length
            finder = riddle[new_one:start]
        return finder
    else:
        return finder


test = 'mi1rewopretmi1rewopret'
print(solve_riddle(test, 5, 'y', False))
