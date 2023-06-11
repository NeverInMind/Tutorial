def get_cats_info(path):
    with open(path, 'r') as pf:
        lines = pf.readlines()
        new_arr = []
        for i in lines:
            data = i.split('\n')[0]
            data_split = data.split(',')
            new_dict = {'id': data_split[0],
                        'name': data_split[1],
                        'age': data_split[2]
                        }
            new_arr.append(new_dict)
        return new_arr


file_path = ".\ex-05.txt"

get_cats_info(file_path)
