def get_recipe(path, search_id):
    with open(path, 'r') as pf:
        lines = pf.readlines()
        if search_id in lines:
            print('Yes')
        else:
            print('No')


file_path = ".\ex-06.txt"
src_id = '60b90c4613067a15887e1ae5'

get_recipe(file_path, src_id)
