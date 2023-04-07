import re
from typing import Union, List, Dict, TextIO, Iterator, Generator
from marshmallow.exceptions import ValidationError
from d_classes import GreetingsSchema, Greetings


def slice_limit(it: Union[str, List, TextIO], limit: int) -> Generator:
    i = 0
    for item in it:
        if i < limit:
            yield item
        else:
            break
        i += 1


def make_query_response(cmd: str, val: str, it: Union[str, List, TextIO]) -> Union[Iterator, Generator, str]:
    match cmd:
        case "filter":
            return filter(lambda x: val in x, it)
        case "map":
            return map(lambda v: v.split(" ")[int(val)], it)
        case "unique":
            return iter(set(it))
        case "sort":
            return iter(sorted(it, reverse=val == 'desc'))
        case "limit":
            return slice_limit(it, int(val))
        case "regex":
            regexp: re.Pattern = re.compile(val)
            return filter(lambda v: regexp.findall(v), it)
        case _:
            return ""


def get_greetings(data: Dict) -> Greetings:
    try:
        return GreetingsSchema().load(data)
    except ValidationError:
        raise TypeError
