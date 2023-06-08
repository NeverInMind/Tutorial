from normalize import normalize
import sys
import shutil
from pathlib import Path

CATEGORIES = {
    'archives': ['.rar', '.zip'],
    'audio': ['.mp3', '.wav'],
    'documents': ['.docx', '.pptx'],
    'video': ['.avi', '.mp4'],
    'images': ['.jpeg', '.png']
}


def move_file(path: Path, root_dir: Path, cat: str) -> None:
    target_dir = root_dir.joinpath(cat)
    if not target_dir.exists():
        target_dir.mkdir()
    new_name = target_dir.joinpath(f"{normalize(path.stem)}{path.suffix}")
    path.replace(new_name)


def get_categories(path: Path) -> str:
    ext = path.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    return 'Other'


def sort_folder(path: Path) -> None:
    for item in path.glob('**/*'):
        if item.is_file():
            cat = get_categories(item)
            if cat == 'archives':
                new_path = path.joinpath(cat).joinpath(item.stem)
                print(new_path)
                unpack_archive(item, new_path)
                move_file(item, path, cat)
            else:
                move_file(item, path, cat)
        elif item.name in CATEGORIES:
            pass
        else:
            new_name = item.parent.joinpath(normalize(item.name))
            item.replace(new_name)


def unpack_archive(path: Path, new_path: Path):
    shutil.unpack_archive(path, new_path)
    pass


def main():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return 'No path to folder'

    if not path.exists():
        return f'Folder with path {path} doesn"t exist'
    sort_folder(path)
    return 'All ok'


if __name__ == "__main__":
    print(main())
