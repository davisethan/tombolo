import jsonschema

from .run import _run

schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "study": {"type": "string"},
            "treatment": {"type": "string"},
            "mean": {"type": "number"},
            "std.dev": {"type": "number"},
            "sampleSize": {"type": "integer"},
        },
        "required": ["study", "treatment", "mean", "std.dev", "sampleSize"],
        "additionalProperties": False,
    },
}


def bnma(data: list[dict], greater_is_better: bool = True) -> dict:
    jsonschema.validate(instance=data, schema=schema)
    return _run("bnma", data, greater_is_better)
