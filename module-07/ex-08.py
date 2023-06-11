
def save_applicant_data(source, output):
    with open(output, 'w') as pf:
        for i in source:
            write_data = f"{i['name']},{i['specialty']},{i['math']},{i['lang']},\
                {i['eng']}\
                \n"
            pf.writelines(write_data)


data = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
output_path = ".\output-08.txt"
save_applicant_data(data, output_path)
