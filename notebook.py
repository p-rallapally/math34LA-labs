# /// script
# requires-python = ">=3.11"
# dependencies = ["marimo", "numpy", "plotly"]
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App(width="full", app_title="MATH 34LA · Week 6")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    return go, make_subplots, mo, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # MATH 34LA: Week 6 Analysis File
    *MATH 34 LA Students · Fall 2026 · Adapted from the original R Markdown lab*

    # Python and marimo Tutorial
    NOTE: This section is background to help you understand programming. You will work with pre-existing code and clear instructions for edits. You will not be tested on coding in quizzes or exams. Our goal is to help you feel more familiar and confident using computer code to explore the calculus models in this class.

    This is a marimo notebook: explanatory Markdown, equations, code, and results live together. Run a code cell with its play button; marimo updates dependent cells automatically. Use the controls below to explore models without editing their implementation. Your answers still belong on your worksheet.

    The original lab used [R Markdown](http://rmarkdown.rstudio.com). Here, Python executes Euler's method rapidly to **simulate the dynamics** of biological systems.

    ## Cells of code
    Code cells play the role of R Markdown chunks. Within a code cell, write Python. Python can act as a calculator. A `#` starts a comment. Unlike R's automatic printing of multiple expressions, we collect results in a table so every result is visible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.ui.table([
        {"Calculation": "3 + 4  # Addition", "Result": 3 + 4},
        {"Calculation": "3 - 4  # Subtraction", "Result": 3 - 4},
        {"Calculation": "3 * 4  # Multiplication", "Result": 3 * 4},
        {"Calculation": "3 / 4  # Division", "Result": 3 / 4},
    ], selection=None)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Variable assignment and vectors
    The real power of code is saving values under names. Python uses `=` where R uses `<-`. NumPy arrays are numerical vectors; `np.array([1, 2, 3, 4])` replaces R's `c(1,2,3,4)`. Multiplication by a scalar acts on each element of an array.

    Read the following code, then check the results. Is the product what you expected?
    """)
    return


@app.cell
def _(mo, np):
    a = 7  # Save the value 7 under the name a
    vector_a = np.array([1, 2, 3, 4])  # A vector of four numbers
    mo.md(f"`a = {a}`,   `vector_a = {vector_a.tolist()}`,   `a * vector_a = {(a * vector_a).tolist()}`")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Simulating viral dynamics using Euler's Method
    Python lets us do many long calculations **even faster than Google Sheets**! Let's explore how viral load decays over time.

    ## A protease inhibitor-treated patient
    We begin with the original lab's simplified assumption: treatment temporarily sets viral production $p$ to zero.

    $$V' = \frac{dV}{dt} = p-cV = 0-cV = -cV.$$

    Euler's method adds small changes calculated using $V'$:

    $$V_{i+1}=V_i+(t_{i+1}-t_i)(p-cV_i).$$

    You've practiced this in Google Sheets. Use $c=0.3256$ per day (the source's average for three patients), $V_0=185000$ particles per mL, and one-day steps.
    """)
    return


@app.cell
def _(mo):
    # Explicit first steps: match the spreadsheet before introducing a loop.
    _baseline_c = 0.3256
    _baseline_p = 0
    _V0 = 185000.0
    _t0, _t1, _t2, _t3 = 0, 1, 2, 3
    _V1 = _V0 + (_t1 - _t0) * (_baseline_p - _baseline_c * _V0)
    _V2 = _V1 + (_t2 - _t1) * (_baseline_p - _baseline_c * _V1)
    _V3 = _V2 + (_t3 - _t2) * (_baseline_p - _baseline_c * _V2)
    manual_values = [_V0, _V1, _V2, _V3]
    mo.ui.table([{"Time (days)": i, "Viral load (particles per mL)": v}
                 for i, v in enumerate(manual_values)], selection=None)
    return (manual_values,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Check these answers against your Google Sheet. Do they agree?

    ### Speeding up our calculation
    Four lines per step is inefficient. A **for loop** repeats the same calculation. The function below creates timepoints and empty placeholders, assigns the initial viral load, then fills each next value. Python counts positions from zero, so position `0` holds the initial value.

    The same function will be reused for every experiment; it does not replace Euler's method with a different solver.
    """)
    return


@app.cell(hide_code=True)
def _(np):
    def simulate(clearance=0.3256, production=0.0, initial=185000.0, end=20.0, step=0.01):
        """Explicit Euler on an inclusive grid; step must divide end."""
        if not all(np.isfinite(x) for x in (clearance, production, initial, end, step)):
            raise ValueError("Parameters must be finite.")
        if clearance < 0 or production < 0 or initial < 0 or end <= 0 or step <= 0:
            raise ValueError("Use nonnegative model parameters and positive time/step.")
        count = int(round(end / step))
        if not np.isclose(count * step, end, rtol=0, atol=1e-10):
            raise ValueError("The timestep must divide the duration exactly.")
        times = np.linspace(0.0, end, count + 1)
        values = np.full(times.shape, np.nan)  # Empty placeholders, like NaN * vector_t
        values[0] = initial  # Save initial viral load in the first position
        for i in range(1, len(times)):
            dt = times[i] - times[i - 1]  # Current minus previous time
            derivative = production - clearance * values[i - 1]  # Previous V
            values[i] = values[i - 1] + dt * derivative  # Euler update
        return times, values

    def exact_solution(times, clearance, production=0.0, initial=185000.0):
        """Optional analytical reference; never used to generate Euler values."""
        if clearance == 0:
            return initial + production * times
        equilibrium = production / clearance
        return equilibrium + (initial - equilibrium) * np.exp(-clearance * times)

    return exact_solution, simulate


@app.cell(hide_code=True)
def _(manual_values, mo, np, simulate):
    loop_t, loop_v = simulate(end=3, step=1)
    mo.vstack([
        mo.ui.table([{"Time (days)": float(t), "Loop viral load": float(v)}
                     for t, v in zip(loop_t, loop_v)], selection=None),
        mo.md(f"Loop and explicit steps agree: **{np.allclose(loop_v, manual_values)}**. "
              "Did you get the same series in Google Sheets?"),
    ])
    return loop_t, loop_v


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Plotting our results
    Plots visualize the simulated values. The first plot uses days 0–3. The next runs for 20 days with one-day steps. How does this compare with Google Sheets?
    """)
    return


@app.cell(hide_code=True)
def _(go, make_subplots, simulate):
    def single_plot(times, values, title, reference=None):
        fig = go.Figure(go.Scatter(x=times, y=values, mode="lines", name="Euler"))
        if reference is not None:
            fig.add_trace(go.Scatter(x=times, y=reference, mode="lines",
                                    name="Exact reference", line={"dash": "dash"}))
        fig.update_layout(title=title, template="plotly_white", height=360,
                          xaxis_title="Time (days)", yaxis_title="Viral load (particles per mL)",
                          margin={"l": 65, "r": 25, "t": 60, "b": 55})
        return fig

    def scenario_plot(clearances, productions, labels, upper):
        fig = make_subplots(rows=1, cols=3, subplot_titles=labels, shared_yaxes=True)
        rows = []
        for col, (clearance, production) in enumerate(zip(clearances, productions), start=1):
            times, values = simulate(clearance, production)
            fig.add_trace(go.Scatter(x=times, y=values, mode="lines", name=labels[col-1]), row=1, col=col)
            fig.update_xaxes(title_text="Time (days)", dtick=5, row=1, col=col)
            fig.update_yaxes(range=[0, upper], dtick=50000, row=1, col=col)
            rows.append({"Scenario": labels[col-1], "c (per day)": clearance,
                         "p (particles/mL/day)": production, "V at day 20": float(values[-1]),
                         "Maximum simulated V": float(max(values))})
        fig.update_yaxes(title_text="Viral load (particles per mL)", row=1, col=1)
        fig.update_layout(template="plotly_white", height=390, showlegend=False)
        return fig, rows

    return scenario_plot, single_plot


@app.cell(hide_code=True)
def _(loop_t, loop_v, mo, simulate, single_plot):
    _long_t, _long_v = simulate(step=1)
    mo.vstack([single_plot(loop_t, loop_v, "First three days · Δt = 1 day"),
               single_plot(_long_t, _long_v, "Twenty days · Δt = 1 day")])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Finally, Euler's method gets more accurate as the timestep decreases (for this model over a fixed duration). Instead of adding spreadsheet rows, choose a smaller $\Delta t$.

    Predict what will change before using the control. The original fine-step example used $\Delta t=0.01$ days. Notice how this smooths the curve! The optional exact reference is an added teaching aid, not a replacement for Euler's method.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    timestep = mo.ui.dropdown(options={"1 day": 1.0, "0.5 days": 0.5, "0.1 days": 0.1, "0.01 days (original)": 0.01}, value="0.01 days (original)", label="Euler timestep")
    show_exact = mo.ui.checkbox(value=False, label="Show exact solution (extension)")
    mo.hstack([timestep, show_exact], justify="start")
    return show_exact, timestep


@app.cell
def _(exact_solution, np, simulate, timestep):
    fine_t, fine_v = simulate(step=timestep.value)
    fine_exact = exact_solution(fine_t, 0.3256)
    max_error = float(np.max(np.abs(fine_v - fine_exact)))
    return fine_exact, fine_t, fine_v, max_error


@app.cell(hide_code=True)
def _(
    fine_exact,
    fine_t,
    fine_v,
    max_error,
    mo,
    show_exact,
    single_plot,
    timestep,
):
    mo.vstack([
        single_plot(fine_t, fine_v, "Timestep exploration", fine_exact if show_exact.value else None),
        mo.md(f"**Δt = {timestep.value:g} days** · **{len(fine_t)-1:,} Euler steps** · "
              f"**V(20) ≈ {fine_v[-1]:,.2f} particles/mL**"),
        mo.md(f"Optional exact-reference comparison: maximum absolute error across the sampled times "
              f"is **{max_error:,.2f} particles/mL**.") if show_exact.value else mo.md("Compare this curve with the one-day calculation above."),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Using Python to explore different parameter values: c
    Now choose two new values of viral clearance, $c_2$ and $c_3$. Draw the results on your worksheet. The first panel retains $c=0.3256$; $p=0$, $V_0=185000$, $\Delta t=0.01$, and the 20-day duration remain fixed.

    Predict: will faster clearance change the starting value, the rate of decline, or both? All three controls begin with the original lab's defaults.
    """)
    return


@app.cell
def _(mo):
    c2 = mo.ui.number(start=0, stop=5, step=0.0001, value=0.3256, label="c₂ (per day)")
    c3 = mo.ui.number(start=0, stop=5, step=0.0001, value=0.3256, label="c₃ (per day)")
    mo.hstack([c2, c3], justify="start")
    return c2, c3


@app.cell(hide_code=True)
def _(c2, c3, scenario_plot):
    clearance_fig, clearance_rows = scenario_plot(
        [0.3256, c2.value, c3.value], [0, 0, 0],
        ["c = 0.3256 (baseline)", f"c₂ = {c2.value:g}", f"c₃ = {c3.value:g}"], 185000)
    return clearance_fig, clearance_rows


@app.cell(hide_code=True)
def _(c2, c3, clearance_fig, clearance_rows, mo):
    mo.vstack([clearance_fig, mo.ui.table(clearance_rows, selection=None),
               mo.md(f"Compared with the fixed baseline, your clearance choices are **{c2.value:g}** and **{c3.value:g}** per day. "
                     "Which curve falls most rapidly? Draw the curves on your worksheet.")])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Using Python to explore different parameter values: p
    Last, explore a patient who **isn't** being treated with protease inhibitors. In the original model, $p>0$.

    The original production choices are 1,000, 10,000, and 100,000 particles/mL/day. Clearance remains $c=0.3256$, with the same initial load, duration, and fine timestep. Predict which trajectories will increase or decrease before changing the inputs.

    The original plot uses a common 0–300,000 vertical axis. The last curve can exceed that limit; the optional expanded axis makes that part visible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    p1 = mo.ui.number(start=0, stop=200000, step=1000, value=1000, label="p₁ (particles/mL/day)")
    p2 = mo.ui.number(start=0, stop=200000, step=1000, value=10000, label="p₂ (particles/mL/day)")
    p3 = mo.ui.number(start=0, stop=200000, step=1000, value=100000, label="p₃ (particles/mL/day)")
    expand_axis = mo.ui.checkbox(value=False, label="Expand common y-axis to include all simulated values")
    mo.vstack([mo.hstack([p1, p2, p3], justify="start"), expand_axis])
    return expand_axis, p1, p2, p3


@app.cell(hide_code=True)
def _(expand_axis, p1, p2, p3, scenario_plot):
    production_fig, production_rows = scenario_plot(
        [0.3256] * 3, [p1.value, p2.value, p3.value],
        [f"p₁ = {p1.value:g}", f"p₂ = {p2.value:g}", f"p₃ = {p3.value:g}"], 300000)
    production_max = max(row["Maximum simulated V"] for row in production_rows)
    if expand_axis.value:
        production_fig.update_yaxes(range=[0, max(300000, production_max * 1.05)])
    return production_fig, production_max, production_rows


@app.cell(hide_code=True)
def _(expand_axis, mo, production_fig, production_max, production_rows):
    mo.vstack([
        production_fig, mo.ui.table(production_rows, selection=None),
        mo.md("**Axis note:** some simulated values exceed the original 300,000 limit. Enable the expanded axis to see them.")
        if production_max > 300000 and not expand_axis.value else mo.md("All simulated values fit within the displayed vertical range."),
        mo.md("Draw these results on your worksheet and answer the questions about them there. "
              "Explain why changing production can change whether the viral load grows or decays."),
    ])
    return


if __name__ == "__main__":
    app.run()
