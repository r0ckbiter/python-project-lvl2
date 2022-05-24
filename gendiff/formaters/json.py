from json import dumps as json_dumbs


def json(diff: dict) -> str:
    output = json_dumbs(diff)
    return output
