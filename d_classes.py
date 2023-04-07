import marshmallow_dataclass
from dataclasses import dataclass
from typing import List


@dataclass
class Params:
    cmd: List[str]
    value: str
    filename: str


@dataclass
class Greetings:
    message: str
    params: Params


GreetingsSchema = marshmallow_dataclass.class_schema(Greetings)
