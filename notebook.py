# /// script
# requires-python = ">=3.11"
# dependencies = ["marimo", "numpy", "plotly"]
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App(width="full", app_title="MATH 34LA · Week 6")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import math as math
    import numpy as np
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    return go, make_subplots, math, mo, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # MATH 34LA: Week 6 Analysis File
    *MATH 34LA · Fall 2026 · Adapted from the original R Markdown lab by Pratyush Rallapally*

    # Python and marimo Tutorial
    NOTE: This section is background to help you understand programming. You will work with pre-existing code and clear instructions for edits. **You will not be tested on coding in quizzes or exams**. The goal is to help you feel more familiar and confident using computer code to explore the calculus models in this class.

    This is a marimo notebook: it mixes Python code with Markdown to make code and text look aesthetic. Run a code cell with the play button; marimo updates dependent cells automatically. Use the controls below to explore models without editing their implementation. **Your answers still belong on your worksheet.**

    Here, Python executes Euler's method rapidly to **simulate the dynamics** of biological systems.

    ## Cells of code
    Within a code cell, write Python. Python can act as a calculator. A `#` starts a comment.
    """)
    return


@app.cell
def _(mo):
    mo.ui.table([
        {"Calculation": "3 + 4", "Result": 3 + 4}, #this is an example of a comment; it's helpful to explain what the code is doing 
        {"Calculation": "3 - 4", "Result": 3 - 4},
        {"Calculation": "3 * 4", "Result": 3 * 4}, #in this row, the console is multiplying 3 and 4, and the result is displayed in the table
        {"Calculation": "3 / 4", "Result": 3 / 4},
    ], selection=None)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Variable assignment and vectors
    The real power of code is assigning values to variables. Python uses `=`. NumPy arrays are numerical vectors; for example, `np.array([1, 2, 3, 4])`. Multiplication by a scalar acts on each element of an array.

    Read the following code, then run the code and check the results. Is the product what you expected?
    """)
    return


@app.cell
def _(np):
    a = 7  # Assigning the value 7 to the variable a (feel free to change any of these and rerun the cell to see what happens!)
    vector_a = np.array([1, 2, 8, 4])  # A vector of four numbers

    print(f"a = {a}")

    print(f"vector_a = {vector_a.tolist()}") #if you were curious, '.tolist()' makes things into lists

    print(f"a * vector_a = {(a * vector_a).tolist()}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Simulating viral dynamics using Euler's Method

    Python lets us do many long calculations **even faster than Google Sheets**! Let's explore how viral load decays over time.

    ## A protease inhibitor-treated patient
    We'll begin by considering a patient who has been treated with protease inhibitors, so that their viral production p is temporarily 0.

    $$V' = \frac{dV}{dt} = p-cV = 0-cV = -cV.$$

    Euler's method adds small changes calculated using $V'$:

    $$V_{i+1}=V_i+(t_{i+1}-t_i)(p-cV_i).$$

    You've practiced this in Google Sheets. Use $c=0.3256$ per day (the source's average for three patients), $V_0=185000$ particles per mL, and one-day steps.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    c = 0.3256  # Average decay value of the three patients
    p = 0  # Production rate when treated by protease inhibitors

    ## Starting timepoint
    V0 = 185000.0  # Starting viral load
    t0 = 0  # Starting timepoint

    # First calculation
    t1 = 1  # First timepoint
    dt = t1 - t0  # Change in time
    Vprime = p - c * V0  # Change in virus, based on the differential equation above
    V1 = V0 + dt * Vprime  # New viral amount

    # Second calculation
    t2 = 2  # First timepoint
    dt = t2 - t1  # Change in time
    Vprime = p - c * V1  # Change in virus, based on the differential equation above
    V2 = V1 + dt * Vprime  # New viral amount

    # First calculation
    t3 = 3  # First timepoint
    dt = t3 - t2  # Change in time
    Vprime = p - c * V2  # Change in virus, based on the differential equation above
    V3 = V2 + dt * Vprime  # New viral amount

    # Print the results
    manual_values = [V0, V1, V2, V3]

    mo.ui.table( #conveniently formats it into a table
        [
            {
                "Time (days)": i,
                "Viral load (particles per mL)": round(v, 2),
            }
            for i, v in enumerate(manual_values)
        ],
        selection=None,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Speeding up our calculation
    While not as bad as writing out calculations by hand, having four lines of code for every calculation doesn’t seem very efficient! That’s where **for loops** come in. These are programming tools that let us repeat calculations many times. Let’s rewrite our last three calculations in a for loop. Look over the comments on the code and see if you can recognize how the calculation repeats itself.

    Python counts positions from zero, so position `0` holds the initial value.
    """)
    return


@app.cell
def _(math, mo):
    c_loop = 0.3256  # Average decay value of the three patients
    p_loop = 0  # Production rate when treated by protease inhibitors

    ## Starting timepoint
    V0_loop = 185000.0  # Starting viral load
    t0_loop = 0  # Starting timepoint

    ## Setting up lists to hold our information
    vector_t_loop = list(range(0, 4, 1))  # Create a list counting from 0 to 3 to hold our timepoints.
    vector_V_loop = [math.nan] * len(vector_t_loop)  # NaN stands for "Not a Number" and creates a list of empty placeholders for future viral load data.
    vector_V_loop[0] = V0_loop  # Save the initial viral load in the first position in our list

    for i in range(1, len(vector_t_loop)):  # For each timestep, apply Euler's method...
        dt_loop = vector_t_loop[i] - vector_t_loop[i - 1]  # Calculate the change in time based on the current value minus the past value,
        Vprime_loop = p_loop - c_loop * vector_V_loop[i - 1]  # then calculate the change in V based on the past value of V, and finally
        vector_V_loop[i] = vector_V_loop[i - 1] + dt_loop * Vprime_loop  # add the change in V to the previous value of V

    # Print the results
    mo.ui.table(
        [
            {
                "Time (days)": t,
                "Viral load (particles per mL)": round(v, 2),
            }
            for t, v in zip(vector_t_loop, vector_V_loop)
        ],
        selection=None,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Check these answers against your Google Sheet. Do they agree?

    ### Plotting our results

    Python also excels as a flexible piece of plotting software. Here, we're going to use it to visualize our results so far.
    """)
    return


@app.cell
def _(go, np):
    # Running our simulation
    _c = 0.3256  # Average decay value of the three patients
    _p = 0  # Production rate when treated by protease inhibitors

    # Starting timepoint
    _V0 = 185000.0  # Starting viral load
    _t0 = 0  # Starting timepoint

    # Setting up vectors to hold our information
    _t = np.arange(_t0, 4, 1, dtype=float)  # Timepoints 0, 1, 2, 3
    _V = np.full(_t.shape, np.nan)  # Empty placeholders for future viral load data
    _V[0] = _V0  # Save the initial viral load in the first position

    for _i in range(1, len(_t)):  # For each timestep, apply Euler's method...
        _dt = _t[_i] - _t[_i - 1]  # Calculate the change in time,
        _Vprime = _p - _c * _V[_i - 1]  # then calculate the change in V using the past value,
        _V[_i] = _V[_i - 1] + _dt * _Vprime  # and add the change to the previous value

    # Save the results for verification
    short_result = {"t": _t, "V": _V, "c": _c, "p": _p}

    # Making our plot
    short_fig = go.Figure(
        go.Scatter(x=_t, y=_V, mode="lines")
    )
    short_fig.update_layout(
        template="plotly_white",
        height=350,
        xaxis_title="Time (days)",
        yaxis_title="Viral Load (particles per mL)",
    )

    short_fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    So far, this isn't so impressive. But let's run our simulation for much longer, now that we have a for-loop tool to do so!
    """)
    return


@app.cell
def _(go, np):
    # Running our simulation
    _c = 0.3256  # Average decay value of the three patients
    _p = 0  # Production rate when treated by protease inhibitors

    # Starting timepoint
    _V0 = 185000.0  # Starting viral load
    _t0 = 0  # Starting timepoint

    # Setting up vectors to hold our information
    _t = np.arange(_t0, 21, 1, dtype=float)  # Days 0 through 20, inclusive
    _V = np.full(_t.shape, np.nan)
    _V[0] = _V0

    for _i in range(1, len(_t)):
        _dt = _t[_i] - _t[_i - 1]
        _Vprime = _p - _c * _V[_i - 1]
        _V[_i] = _V[_i - 1] + _dt * _Vprime

    long_result = {"t": _t, "V": _V, "c": _c, "p": _p}

    # Making our plot
    long_fig = go.Figure(
        go.Scatter(x=_t, y=_V, mode="lines")
    )
    long_fig.update_layout(
        template="plotly_white",
        height=350,
        xaxis_title="Time (days)",
        yaxis_title="Viral Load (particles per mL)",
    )

    long_fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Finally, Euler's method gets more accurate as the timestep decreases (for this model over a fixed duration). Instead of adding spreadsheet rows, choose a smaller $\Delta t$.

    Predict what will change before using the control. The original fine-step example used $\Delta t=0.01$ days.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    timestep = mo.ui.dropdown(
        options={
            "1": 1.0,
            "0.5": 0.5,
            "0.1": 0.1,
            "0.01": 0.01,
        },
        value="0.01",
        label="delta_t (days)",
    )
    timestep
    return (timestep,)


@app.cell(hide_code=True)
def _(go, np, timestep):
    # Running our simulation
    _c = 0.3256  # Average decay value of the three patients
    _p = 0  # Production rate when treated by protease inhibitors

    # Starting timepoint
    _V0 = 185000.0  # Starting viral load
    _t0 = 0  # Starting timepoint
    _delta_t = timestep.value  # Length of timesteps, selected above

    # Setting up vectors to hold our information
    _steps = int(round(20 / _delta_t))
    _t = np.linspace(_t0, 20, _steps + 1)
    _V = np.full(_t.shape, np.nan)
    _V[0] = _V0

    for _i in range(1, len(_t)):
        _dt = _t[_i] - _t[_i - 1]
        _Vprime = _p - _c * _V[_i - 1]
        _V[_i] = _V[_i - 1] + _dt * _Vprime

    fine_result = {"t": _t, "V": _V, "c": _c, "p": _p}

    # Making our plot
    fine_fig = go.Figure(
        go.Scatter(x=_t, y=_V, mode="lines")
    )
    fine_fig.update_layout(
        template="plotly_white",
        height=350,
        xaxis_title="Time (days)",
        yaxis_title="Viral Load (particles per mL)",
    )

    fine_fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice how that smoothed out our curve!

    ### Using Python to explore different parameter values: c

    Now the real fun can begin! We're going to use Python to simulate different values of viral loss. In the code below, choose two new values of c (c2 and c3) to try. Draw your results on your worksheet.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    c2 = mo.ui.number(
        start=0, stop=5, step=0.0001,
        value=0.3256, label="c2",
    )
    c3 = mo.ui.number(
        start=0, stop=5, step=0.0001,
        value=0.3256, label="c3",
    )
    mo.hstack([c2, c3], justify="start")
    return c2, c3


@app.cell(hide_code=True)
def _(c2, c3, go, make_subplots, np):
    # Running our simulation
    _c2 = c2.value  # Choose a new value using the c2 input above
    _c3 = c3.value  # Choose a new value using the c3 input above

    _V0 = 185000.0  # Starting viral load
    _t0 = 0  # Starting timepoint
    _delta_t = 0.01  # Length of timesteps
    _p = 0  # Production rate when treated by protease inhibitors

    # DON'T CHANGE the first, baseline value
    _clearances = [0.3256, _c2, _c3]

    clearance_results = []
    clearance_fig = make_subplots(
        rows=1,
        cols=3,
        shared_yaxes=True,
        subplot_titles=[
            f"c = {_value:g}" for _value in _clearances
        ],
    )

    # Simulations 1, 2, and 3 repeat the same Euler calculation
    for _panel, _c in enumerate(_clearances, start=1):
        # Setting up vectors to hold our information
        _t = np.linspace(
            _t0, 20, int(round(20 / _delta_t)) + 1
        )
        _V = np.full(_t.shape, np.nan)
        _V[0] = _V0

        for _i in range(1, len(_t)):
            _dt = _t[_i] - _t[_i - 1]
            _Vprime = _p - _c * _V[_i - 1]
            _V[_i] = _V[_i - 1] + _dt * _Vprime

        clearance_results.append(
            {"t": _t, "V": _V, "c": _c, "p": _p}
        )

        # Making our plot
        clearance_fig.add_trace(
            go.Scatter(x=_t, y=_V, mode="lines"),
            row=1,
            col=_panel,
        )
        clearance_fig.update_xaxes(
            title_text="Time (days)",
            tick0=0,
            dtick=5,
            row=1,
            col=_panel,
        )
        clearance_fig.update_yaxes(
            range=[0, _V0],
            tick0=0,
            dtick=50000,
            row=1,
            col=_panel,
        )  # Same scale and grid lines for drawing on your worksheet

    clearance_fig.update_yaxes(
        title_text="Viral Load (particles per mL)",
        row=1,
        col=1,
    )
    clearance_fig.update_layout(
        template="plotly_white",
        height=350,
        showlegend=False,
    )

    clearance_fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Using Python to explore different parameter values: p

    Last, we can explore the dynamics of viral load in a patient who *isn't* being treated with protease inhibitors. For this patient, p > 0.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    p1 = mo.ui.number(
        start=0, stop=200000, step=1000,
        value=1000, label="p1",
    )
    p2 = mo.ui.number(
        start=0, stop=200000, step=1000,
        value=10000, label="p2",
    )
    p3 = mo.ui.number(
        start=0, stop=200000, step=1000,
        value=100000, label="p3",
    )
    mo.hstack([p1, p2, p3], justify="start")
    return p1, p2, p3


@app.cell(hide_code=True)
def _(go, make_subplots, np, p1, p2, p3):
    # Use the first, second, and third production choices from the inputs above.
    _productions = [p1.value, p2.value, p3.value]

    ## Starting timepoint
    _V0 = 185000.0  # Starting viral load
    _t0 = 0  # Starting timepoint

    _delta_t = 0.01  # Length of timesteps

    _c = 0.3256  # Average decay value of the three patients; DON'T CHANGE THIS VALUE

    # Set up three plots side by side.
    production_fig = make_subplots(
        rows=1,
        cols=3,
        shared_yaxes=True,
        subplot_titles=[
            f"p = {_value:g}" for _value in _productions
        ],  # Add titles so we can distinguish the plots
    )

    production_fig.update_layout(
        template="plotly_white",
        height=350,
        showlegend=False,
        margin=dict(l=70, r=25, t=60, b=60),
    )  # Set up the figure margins on all sides

    production_results = []

    # Simulations 1, 2, and 3:
    # Repeat the same calculation using the first, second, and third production choices.
    for _panel, _p in enumerate(_productions, start=1):
        # _p is the production rate for the current simulation.
        # Unlike the treated-patient example, these production choices can be positive.

        ## Setting up vectors to hold our information
        _t = np.linspace(
            _t0,
            20,
            int(round(20 / _delta_t)) + 1,
        )  # Create a vector counting from 0 to 20 in steps of delta_t to hold our timepoints

        _V = np.full(
            _t.shape,
            np.nan,
        )  # NaN stands for "Not a Number" and creates empty placeholders for future viral load data

        _V[0] = _V0  # Save the initial viral load in the first position in our vector; Python starts at position 0

        for _i in range(1, len(_t)):  # For each timestep, do Euler's method...
            _dt = _t[_i] - _t[_i - 1]  # by first calculating the change in time based on the current value minus the past value,
            _Vprime = _p - _c * _V[_i - 1]  # then calculating the change in V based on the past value of V, and finally
            _V[_i] = _V[_i - 1] + _dt * _Vprime  # adding the change in V to the previous value of V

        # Save each simulation's results for verification.
        production_results.append(
            {"t": _t, "V": _V, "c": _c, "p": _p}
        )

        # Making our plot
        production_fig.add_trace(
            go.Scatter(
                x=_t,  # Tell Python what to put on the x-axis
                y=_V,  # Tell Python what to put on the y-axis
                mode="lines",  # Plot as a line
            ),
            row=1,
            col=_panel,  # Place this simulation in its corresponding panel
        )

        production_fig.update_xaxes(
            title_text="Time (days)",  # Label the x-axis
            range=[0, 20],
            tick0=0,
            dtick=5,
            showgrid=True,
            gridcolor="lightgray",
            griddash="dash",
            row=1,
            col=_panel,
        )  # Add vertical grid lines every 5 days to make it easier to plot on your worksheet

        production_fig.update_yaxes(
            range=[0, 300000],  # Add y-axis limits so all plots scale the same
            tick0=0,
            dtick=50000,
            showgrid=True,
            gridcolor="lightgray",
            griddash="dash",
            row=1,
            col=_panel,
        )  # Add horizontal grid lines every 50,000 particles per mL

    production_fig.update_yaxes(
        title_text="Viral Load (particles per mL)",  # Label the y-axis
        row=1,
        col=1,
    )

    production_fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    Draw these results on your worksheet and answer the questions about them there.
    """)
    return


if __name__ == "__main__":
    app.run()
