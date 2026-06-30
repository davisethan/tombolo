import jsonschema
import matplotlib.pyplot as plt

from .primitives.grid import _grid

_matrix = {
    "type": "object",
    "additionalProperties": {
        "type": "object",
        "additionalProperties": {"type": ["number", "null"]},
    },
}

_schema = {
    "type": "object",
    "required": ["prediction"],
    "properties": {
        "prediction": {
            "type": "object",
            "required": ["lower", "upper"],
            "properties": {"lower": _matrix, "upper": _matrix},
        }
    },
}


def prediction_table(data: dict) -> plt.Figure:
    jsonschema.validate(instance=data, schema=_schema)
    return _grid(data["prediction"])
