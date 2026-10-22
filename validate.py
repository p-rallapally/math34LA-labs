from pathlib import Path
from types import SimpleNamespace
import importlib.util
import numpy as np

root = Path(__file__).parent
spec = importlib.util.spec_from_file_location(
    "lab", root / "notebook.py"
)
lab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab)

outputs, values = lab.app.run()


def check(result, step):
    t, V, c, p = (
        result[key] for key in ("t", "V", "c", "p")
    )

    # Independent formula for the discrete Euler recurrence.
    # This is not the continuous differential-equation solution.
    expected = (
        185000 + p * t
        if c == 0
        else p / c
        + (185000 - p / c)
        * (1 - c * step) ** np.arange(len(t))
    )

    np.testing.assert_allclose(
        V, expected, rtol=1e-10, atol=1e-6
    )
    assert np.isfinite(V).all()
    assert len(t) == round(t[-1] / step) + 1


for key, step in [
    ("short_result", 1),
    ("long_result", 1),
    ("fine_result", values["timestep"].value),
]:
    check(values[key], step)


for key in ["clearance_results", "production_results"]:
    for result in values[key]:
        check(result, 0.01)

assert len(values["long_result"]["t"]) == 21
assert len(values["fine_result"]["t"]) == (
    round(20 / values["timestep"].value) + 1
)
assert len(values["clearance_fig"].data) == 3
assert len(values["production_fig"].data) == 3

# Check each timestep through the notebook dependency graph.
for step in [1, 0.5, 0.1, 0.01]:
    _, changed = lab.app.run(
        defs={"timestep": SimpleNamespace(value=step)}
    )
    check(changed["fine_result"], step)
    assert len(changed["fine_result"]["t"]) == round(20 / step) + 1

# Check that clearance inputs affect their scenarios.
_, changed = lab.app.run(
    defs={
        "c2": SimpleNamespace(value=0.1),
        "c3": SimpleNamespace(value=1),
    }
)
assert [
    r["c"] for r in changed["clearance_results"]
] == [0.3256, 0.1, 1]

for result in changed["clearance_results"]:
    check(result, 0.01)

# Check that production inputs affect their scenarios.
_, changed = lab.app.run(
    defs={
        "p1": SimpleNamespace(value=0),
        "p2": SimpleNamespace(value=20000),
        "p3": SimpleNamespace(value=200000),
    }
)
assert [
    r["p"] for r in changed["production_results"]
] == [0, 20000, 200000]

for result in changed["production_results"]:
    check(result, 0.01)

print(
    f"PASS: {len(outputs)} cells execute; "
    "Euler results and reactive controls validated."
)