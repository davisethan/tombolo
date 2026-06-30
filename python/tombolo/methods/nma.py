import jsonschema

from .run import _run

schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "studlab": {"type": "string"},
            "treat1": {"type": "string"},
            "treat2": {"type": "string"},
            "TE": {"type": "number"},
            "seTE": {"type": "number"},
        },
        "required": ["studlab", "treat1", "treat2", "TE", "seTE"],
        "additionalProperties": False,
    },
}


def nma(data: list[dict], greater_is_better: bool = True) -> dict:
    jsonschema.validate(instance=data, schema=schema)
    return _run("nma", data, greater_is_better)
