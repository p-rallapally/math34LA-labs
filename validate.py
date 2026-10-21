"""Run from this folder: python validate.py. No test-only dependencies."""
from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace
import importlib.util
import json
import numpy as np

spec = importlib.util.spec_from_file_location("week6", Path(__file__).with_name("notebook.py"))
notebook = importlib.util.module_from_spec(spec)
spec.loader.exec_module(notebook)
outputs, default = notebook.app.run()
simulate = default["simulate"]
checks = 0
for c in [0, 0.3256, 1, 5]:
    for p in [0, 1000, 10000, 100000, 200000]:
        for step in [1, 0.5, 0.1, 0.01]:
            t, v = simulate(c, p, step=step)
            # Independent closed-form discrete Euler recurrence, not the ODE solution.
            reference = (185000 + p * t if c == 0 else
                         p/c + (185000 - p/c) * (1-c*step)**np.arange(len(t)))
            np.testing.assert_allclose(v, reference, rtol=1e-10, atol=1e-6)
            assert len(t) == round(20 / step) + 1
            assert t[0] == 0 and t[-1] == 20 and np.isfinite(v).all()
            checks += 1
np.testing.assert_allclose(default['manual_values'], [float(Decimal('185000') * Decimal('0.6744')**i) for i in range(4)], atol=1e-8)
np.testing.assert_allclose(default['manual_values'], default['loop_v'])
assert len(default['fine_t']) == 2001
assert len(default['clearance_fig'].data) == len(default['production_fig'].data) == 3
assert default['production_max'] > 300000
errors = []
for h in [1, .5, .1, .01]:
    _, d = notebook.app.run(defs={
        'timestep': SimpleNamespace(value=h), 'show_exact': SimpleNamespace(value=True)})
    assert len(d['fine_t']) == round(20/h)+1
    errors.append(d['max_error'])
assert all(a > b for a, b in zip(errors, errors[1:]))
_, c_changed = notebook.app.run(defs={'c2': SimpleNamespace(value=.1), 'c3': SimpleNamespace(value=1.)})
assert c_changed['clearance_rows'][1]['V at day 20'] > default['clearance_rows'][1]['V at day 20']
assert c_changed['clearance_rows'][2]['V at day 20'] < default['clearance_rows'][2]['V at day 20']
_, p_changed = notebook.app.run(defs={
    'p1': SimpleNamespace(value=0), 'p2': SimpleNamespace(value=20000),
    'p3': SimpleNamespace(value=200000), 'expand_axis': SimpleNamespace(value=True)})
assert p_changed['production_rows'][0]['V at day 20'] < default['production_rows'][0]['V at day 20']
assert p_changed['production_rows'][2]['V at day 20'] > default['production_rows'][2]['V at day 20']
assert p_changed['production_fig'].layout.yaxis.range[1] > p_changed['production_max']
for kw in [{'step':0}, {'step':.3}, {'clearance':-1}, {'production':float('nan')}]:
    try:
        simulate(**kw)
    except ValueError:
        pass
    else:
        raise AssertionError(f'Expected invalid-input rejection: {kw}')
report = {
    'status':'PASS', 'default_cells_executed': len(outputs),
    'independent_recurrence_scenarios':checks,
    'recurrence_tolerance':{'rtol':1e-10,'atol':1e-6},
    'first_four_values':default['manual_values'],
    'maximum_absolute_errors_by_step':dict(zip(['1','.5','.1','.01'],errors)),
    'default_production_endpoints':[r['V at day 20'] for r in default['production_rows']],
    'reactive_override_runs':6,
    'limitations':['Rscript unavailable: no live R comparison.',
                   'Controls tested through app.run definition overrides; browser clicking and visual QA not performed.',
                   'Browser WebAssembly execution not tested.'],
}
Path(__file__).with_name('validation_results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
