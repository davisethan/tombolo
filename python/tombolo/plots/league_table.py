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
    "required": ["league"],
    "properties": {
        "league": {
            "type": "object",
            "required": ["md", "lower", "upper"],
            "properties": {
                "md": _matrix,
                "lower": _matrix,
                "upper": _matrix,
                "pval": _matrix,
            },
        }
    },
}


def league_table(data: dict) -> plt.Figure:
    jsonschema.validate(instance=data, schema=_schema)
    return _grid(data["league"])
