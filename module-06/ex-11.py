def get_credentials_users(path):
    with open(path, 'rb') as pf:
        new_arr = []
        data = pf.readlines()
        for i in data:
            new_arr.append(i.strip().decode())
        print(new_arr)


file_path = ".\\user_info.txt"
get_credentials_users(file_path)
