import shutil


def create_backup(path, file_name, employee_residence):



    with open(path + '/' + file_name, 'wb') as fh:
        for key, value in employee_residence.items():
            employee_data = f"{key} {value}\n"
            fh.write(employee_data.encode())

    archive_name = shutil.make_archive('backup_folder', 'zip', path)
    return archive_name