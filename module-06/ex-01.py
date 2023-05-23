def total_salary(path):
    pf = open(path, 'r')
    sum = 0.0
    while True:
        line = pf.readline()
        if not line:
            break
        sum += float(line.split(',')[1])
    pf.close()
    return sum


print(total_salary(".\ex-01.txt"))
