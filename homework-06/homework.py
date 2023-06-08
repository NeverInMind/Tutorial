from normalize import normalize
import sys
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


def get_categories(path: Path) -> str:
    ext = path.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
        return 'Other'


def sort_folder(path: Path) -> None:
    for item in path.glob('**/*'):
        print(item.stem)


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
