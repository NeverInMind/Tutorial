from pathlib import Path

def parse_folder(path):
    files = []
    folders = []
    for check in path.iterdir():
        if check.is_dir():
            folders.append(check.name)
        else:
            files.append(check.name)    
    return files, folders


path_input = Path('c:/Users/Sytnyk Volodymyr/Documents/GitHub/Tutorial/')
