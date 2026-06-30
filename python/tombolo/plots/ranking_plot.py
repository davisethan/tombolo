import jsonschema
import matplotlib.pyplot as plt

from .primitives.barh import _barh

_schema = {
    "type": "object",
    "required": ["ranking"],
    "properties": {
        "ranking": {
            "type": "object",
            "additionalProperties": {"type": "number", "minimum": 0, "maximum": 1},
        }
    },
}


def ranking_plot(data: dict) -> plt.Figure:
    jsonschema.validate(instance=data, schema=_schema)
    return _barh(data["ranking"])
