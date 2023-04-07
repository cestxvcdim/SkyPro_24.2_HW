import re
from typing import Union, List, Dict, TextIO
from marshmallow.exceptions import ValidationError
from d_classes import GreetingsSchema, Greetings


def make_query_response(cmd: str, val: str, rof_obj: Union[str, List, TextIO]) -> Union[str, List]:
    match cmd:
        case "filter":
            return list(filter(lambda x: val in x, rof_obj))
        case "map":
            return '\n'.join([x.split()[int(val)] for x in rof_obj])
        case "unique":
            return list(set(rof_obj))
        case "sort":
            return sorted(rof_obj, reverse=val == 'desc')
        case "limit":
            return list(rof_obj)[:int(val)]
        case "regex":
            regexp: re.Pattern = re.compile(val)
            return list(filter(lambda v: regexp.findall(v), rof_obj))
        case _:
            return ""


def get_greetings(data: Dict) -> Greetings:
    try:
        return GreetingsSchema().load(data)
    except ValidationError:
        raise TypeError
