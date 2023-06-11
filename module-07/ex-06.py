def get_recipe(path, search_id):
    with open(path, 'r') as pf:
        lines = pf.readlines()
        for i in lines:
            res = i.strip().split(',')
            if res[0] == search_id:
                recipe = {
                    "id": res[0],
                    "name": res[1],
                    "ingredients": res[2:]
                }
                return recipe


file_path = ".\ex-06.txt"
src_id = '60b90c4613067a15887e1ae5'

get_recipe(file_path, src_id)
