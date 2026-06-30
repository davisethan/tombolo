import jsonschema
import matplotlib.pyplot as plt

from .primitives.table import _table

_schema = {
    "type": "object",
    "required": ["convergence"],
    "properties": {
        "convergence": {
            "type": "object",
            "required": ["rhat_max", "ess_bulk_min", "ess_tail_min"],
            "properties": {
                "rhat_max": {"type": "number"},
                "ess_bulk_min": {"type": "number"},
                "ess_tail_min": {"type": "number"}
            }
        }
    }
}


def convergence_table(data: dict) -> plt.Figure:
    jsonschema.validate(instance=data, schema=_schema)
    return _table(data["convergence"])
