from configparser import ConfigParser
from typing import Dict


class FileNotFound(Exception):
    pass


def config(filename: str ='database.ini', section: str ='postgresql') -> Dict:
    parser = ConfigParser()
    parser.read(filename)

    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
                db[param[0]] = param[1]
    else:
        raise FileNotFound(f'Section {section} not found in the {filename} file')

    return db
