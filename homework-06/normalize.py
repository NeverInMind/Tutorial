import re
import os
from pathlib import Path
# unpacking the tuple

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n",
               "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je",
               "i", "ji", "g")

TRANS = {}
CYRILLIC_SYMBOLS_TUP = tuple(CYRILLIC_SYMBOLS)
for c, l in zip(CYRILLIC_SYMBOLS_TUP, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def translate(name):
    global TRANS
    result = name.translate(TRANS)
    return result


def normalize(folder):
    if folder.is_dir():
        name = translate(str(folder))
        name = re.sub(r'\W', '_', name)
    else:
        name, file_extension = os.path.splitext(folder)
        name = translate(name)
        name = re.sub(r'\W', '_', name)
    print(name)
