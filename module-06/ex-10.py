def save_credentials_users(path, users_info):
    b_list = []
    for user, password in users_info.items():
        b_list.append((f"{user}:{password}\n").encode())
    with open(path, 'wb') as file:
        file.writelines(b_list)


data = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}
file_path = ".\\user_info.txt"

save_credentials_users(file_path, data)
