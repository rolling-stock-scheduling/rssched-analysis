import json
import re
from datetime import datetime
from pathlib import Path

from rssched.model.request import Request
from rssched.model.response import Info, ObjectiveValue, Response, Schedule


def parse_datetime(dt_str: str):
    return datetime.fromisoformat(dt_str)


def camel_to_snake(name):
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def convert_keys_to_snake_case(data):
    if isinstance(data, dict):
        new_dict = {}
        for k, v in data.items():
            new_key = camel_to_snake(k)
            new_dict[new_key] = convert_keys_to_snake_case(v)
        return new_dict
    elif isinstance(data, list):
        return [convert_keys_to_snake_case(item) for item in data]
    else:
        return data


def import_request(file_path: Path) -> Request:
    with open(file_path, "r", encoding="utf-8") as file:
        data = convert_keys_to_snake_case(json.load(file))
    return Request(**data)


def import_response(file_path: Path) -> Response:
    with open(file_path, "r", encoding="utf-8") as file:
        data = convert_keys_to_snake_case(json.load(file))

    info = Info(**data["info"])
    objective_value = ObjectiveValue(**data["objective_value"])
    schedule = Schedule(**data["schedule"])

    return Response(info=info, objective_value=objective_value, schedule=schedule)
