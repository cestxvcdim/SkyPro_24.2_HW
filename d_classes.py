import marshmallow_dataclass
from dataclasses import dataclass
from typing import List


@dataclass
class Params:
    cmd1: List[str]
    cmd2: List[str]
    value1: str
    value2: str
    filename: str


@dataclass
class Greetings:
    message: str
    params: Params


GreetingsSchema = marshmallow_dataclass.class_schema(Greetings)
