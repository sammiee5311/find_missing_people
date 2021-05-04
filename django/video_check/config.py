from configparser import ConfigParser
from typing import Dict

def Config(filename: str ='database.ini', section: str ='postgresql') -> Dict:
    parser = ConfigParser()
    parser.read(filename)

    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
                db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db