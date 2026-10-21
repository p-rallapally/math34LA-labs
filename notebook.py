# /// script
# requires-python = ">=3.11"
# dependencies = ["marimo==0.25.2", "numpy", "plotly==7.1.0"]
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App(width="full", app_title="MATH 34LA: Week 6 Analysis File")


@app.cell(hide_code=True)
def imports():
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    return go, make_subplots, mo, np




@app.cell(hide_code=True)
def title(mo):
    mo.md(r"""
    # MATH 34LA: Week 6 Analysis File

    *MATH 34 LA Students · Fall 2026*
    """)
    return


@app.cell(hide_code=True)
def narrative_0(mo):
    mo.md(r"""
    # Python and marimo Tutorial

    NOTE: This section is provided as background information for you to better understand how Python and programming work. In this class, you will be working with pre-existing code, and we will always provide you with very clear instructions for how to edit that code, if you need to. You will also not be tested on how to code in quizzes or on exams. Our goal is to help you feel more familiar and more confident looking at and, ultimately using computer code to further explore the calculus models we are studying in this class.

    This is a Python marimo notebook. Markdown is a simple formatting syntax for authoring formatted text. For more details on using marimo see <https://docs.marimo.io/>.

    When you run this notebook, a document will be displayed that includes both content as well as the output of any embedded Python code cells within the document.

    For the purposes of this class, we will be using Python in the computer lab to help us execute Euler's Method rapidly to *simulate the dynamics* of biological systems. To do this, there are a few details about how Python works that you'll need to know.

    ## Chunks of code

    marimo lets us separate *code* from *text*, which makes it easier to see and describe what we are doing. You can recognize cells of code by the Python syntax highlighting and the code background.
    """)
    return


@app.cell(hide_code=True)
def code_1(mo):
    def run_chunk_1():
        _outputs = []
        pass
        return _outputs

    mo.show_code(position="above")
    return (run_chunk_1,)


@app.cell(hide_code=True)
def output_1(run_chunk_1):
    chunk_1_result = run_chunk_1()
    return


@app.cell(hide_code=True)
def narrative_1(mo):
    mo.md(r"""
    Within a chunk, you must write in code. For example, we can use Python like a calculator. In the marimo editor, press the play button for a cell to execute that cell. In the published companion, the code runs automatically; changing an input updates the relevant results.
    """)
    return


@app.cell(hide_code=True)
def code_2(mo):
    def run_chunk_2():
        _outputs = []
        _outputs.append(3 + 4)
        return _outputs

    mo.show_code(position="above")
    return (run_chunk_2,)


@app.cell(hide_code=True)
def output_2(mo, run_chunk_2):
    chunk_2_result = run_chunk_2()
    mo.vstack([mo.as_html(_value) for _value in chunk_2_result])
    return


@app.cell(hide_code=True)
def narrative_2(mo):
    mo.md(r"""
    We can put multiple lines of code into a chunk, and we can use comments to say what those lines of code do. Comments are preceded by a # symbol, and marimo highlights that text for us so that we can easily recognize it.
    """)
    return


@app.cell(hide_code=True)
def code_3(mo):
    def run_chunk_3():
        _outputs = []
        _outputs.append(3 + 4) # Addition
        _outputs.append(3 - 4) # Subtraction
        _outputs.append(3 * 4) # Multiplication
        _outputs.append(3 / 4) # Division
        return _outputs

    mo.show_code(position="above")
    return (run_chunk_3,)


@app.cell(hide_code=True)
def output_3(mo, run_chunk_3):
    chunk_3_result = run_chunk_3()
    mo.vstack([mo.as_html(_value) for _value in chunk_3_result])
    return


@app.cell(hide_code=True)
def narrative_3(mo):
    mo.md(r"""
    But the real power of code is that we can save our work using something called "variable assignment." The equals sign tells Python to save the number, vector, or other information on the right using the name on the left.
    """)
    return


@app.cell(hide_code=True)
def code_4(mo):
    def run_chunk_4():
        _outputs = []
        a = 7 # Assign the letter "a" the value of 7

        # Check to see if Python saved this information correctly by typing the name of the assigned variable
        _outputs.append(a)
        return _outputs

    mo.show_code(position="above")
    return (run_chunk_4,)


@app.cell(hide_code=True)
def output_4(mo, run_chunk_4):
    chunk_4_result = run_chunk_4()
    mo.vstack([mo.as_html(_value) for _value in chunk_4_result])
    return


@app.cell(hide_code=True)
def narrative_4(mo):
    mo.md(r"""
    Conveniently, Python can also us save strings of numbers using variable assignment.
    """)
    return


@app.cell(hide_code=True)
def code_5(mo, np):
    def run_chunk_5():
        _outputs = []
        vector_a = np.array([1, 2, 3, 4]) # Here, "np.array()" creates a numerical vector from four numbers separated by commas.

        # Now we can see that "vector_a" has four values saved within it.
        _outputs.append(vector_a)
        return _outputs

    mo.show_code(position="above")
    return (run_chunk_5,)


@app.cell(hide_code=True)
def output_5(mo, run_chunk_5):
    chunk_5_result = run_chunk_5()
    mo.vstack([mo.as_html(_value) for _value in chunk_5_result])
    return


@app.cell(hide_code=True)
def narrative_5(mo):
    mo.md(r"""
    Once we have saved information, we can perform mathematical operations with that saved information. For example, we can multiply our vector by our constant.
    """)
    return


@app.cell(hide_code=True)
def code_6(mo, np):
    def run_chunk_6():
        _outputs = []
        a = 7
        vector_a = np.array([1, 2, 3, 4])

        _outputs.append(a*vector_a) # Is this the answer you expected?
        return _outputs

    mo.show_code(position="above")
    return (run_chunk_6,)


@app.cell(hide_code=True)
def output_6(mo, run_chunk_6):
    chunk_6_result = run_chunk_6()
    mo.vstack([mo.as_html(_value) for _value in chunk_6_result])
    return


@app.cell(hide_code=True)
def narrative_6(mo):
    mo.md(r"""
    # Simulating viral dynamics using Euler's Method

    The real beauty of Python is that it allows us to do many, long calculations **even faster than Google Sheets**!

    Let's explore that by using Euler's Method to simulate how viral load decays over time.

    ## A protease inhibitor-treated patient

    We'll begin by considering a patient who has been treated with protease inhibitors, so that their viral production $p$ is temporarily 0.

    $$
    V' = \frac{dV}{dt} = p-cV = 0-cV = -cV
    $$

    According to Euler's Method, we can simulate the decay in viral load by repeatedly adding up small changes calculated by using V'. You've just practiced this on your Google Sheet. Let's do the same calculations here.
    """)
    return


@app.cell(hide_code=True)
def code_7(mo):
    def run_chunk_7():
        _outputs = []
        c = 0.3256 # Average decay value of the three patients
        p = 0 # Production rate when treated by protease inhibitors

        ## Starting timepoint
        V0 = 185000 # Starting viral load
        t0 = 0 # Starting timepoint

        # First calculation
        t1 = 1 # First timepoint
        dt = t1 - t0 # Change in time
        Vprime = p-c*V0 # Change in virus, based on the differential equation above
        V1 = V0 + dt*Vprime # New viral amount

        # Second calculation
        t2 = 2 # First timepoint
        dt = t2 - t1 # Change in time
        Vprime = p-c*V1 # Change in virus, based on the differential equation above
        V2 = V1 + dt*Vprime # New viral amount

        # First calculation
        t3 = 3 # First timepoint
        dt = t3 - t2 # Change in time
        Vprime = p-c*V2 # Change in virus, based on the differential equation above
        V3 = V2 + dt*Vprime # New viral amount

        # Print the results
        _outputs.append(V0)
        _outputs.append(V1)
        _outputs.append(V2)
        _outputs.append(V3)
        return _outputs

    mo.show_code(position="above")
    return (run_chunk_7,)


@app.cell(hide_code=True)
def output_7(mo, run_chunk_7):
    chunk_7_result = run_chunk_7()
    mo.vstack([mo.as_html(_value) for _value in chunk_7_result])
    return


@app.cell(hide_code=True)
def narrative_7(mo):
    mo.md(r"""
    Check these answers against your Google Sheet. Do they agree?


    ### Speeding up our calculation

    While not as bad as writing out calculations by hand, having four lines of code for every Python calculation doesn't seem very efficient! That's where **for loops** come in. These are programming tools that let us repeat calculations many times. Let's rewrite our last three calculations in a for loop. Look over the comments on the code and see if you can recognize how the calculation repeats itself.
    """)
    return


@app.cell(hide_code=True)
def code_8(mo, np):
    def run_chunk_8():
        _outputs = []
        c = 0.3256 # Average decay value of the three patients
        p = 0 # Production rate when treated by protease inhibitors

        ## Starting timepoint
        V0 = 185000 # Starting viral load
        t0 = 0 # Starting timepoint

        ## Setting up vectors to hold our information
        vector_t = np.linspace(0, 3, int(round(3 / 1)) + 1) # The "np.linspace" function tells Python to create a vector that counts from 0 to 3 to hold our timepoints.
        vector_V = np.full(vector_t.shape, np.nan) # NaN stands for "Not a Number" and is a way of telling Python to create a vector that's full of empty placeholders for future viral load data.
        vector_V[0] = V0 # This tells Python to save the initial viral load in the first position in our vector

        for i in range(1, len(vector_t)): # This is our for loop. It's basically telling Python: "For each timestep, do Euler's method..."
            dt = vector_t[i] - vector_t[i-1] # by first calculating the change in time based on the current value minus the past value,
            Vprime = p-c*vector_V[i-1] # then calculating the change in V based on the past value of V, and finally
            vector_V[i] = vector_V[i-1] + dt*Vprime # adding the change in V to the previous value of V

        # Print the results
        _outputs.append(vector_V)
        return _outputs

    mo.show_code(position="above")
    return (run_chunk_8,)


@app.cell(hide_code=True)
def output_8(mo, run_chunk_8):
    chunk_8_result = run_chunk_8()
    mo.vstack([mo.as_html(_value) for _value in chunk_8_result])
    return


@app.cell(hide_code=True)
def narrative_8(mo):
    mo.md(r"""
    Check your results. Did you get the same series of V values as the above chunk of code and as the Google Sheet?


    ### Plotting our results

    Python also excels as a flexible piece of plotting software. Here, we're going to use it to visualize our results so far.
    """)
    return


@app.cell(hide_code=True)
def code_9(go, make_subplots, mo, np):
    def run_chunk_9():
        _outputs = []
        # The "height" and "width" arguments below tell Python how large to make the figure.

        # Running our simulation
        c = 0.3256 # Average decay value of the three patients
        p = 0 # Production rate when treated by protease inhibitors

        ## Starting timepoint
        V0 = 185000 # Starting viral load
        t0 = 0 # Starting timepoint

        ## Setting up vectors to hold our information
        vector_t = np.linspace(0, 3, int(round(3 / 1)) + 1) # The "np.linspace" function tells Python to create a vector that counts from 0 to 3 to hold our timepoints.
        vector_V = np.full(vector_t.shape, np.nan) # NaN stands for "Not a Number" and is a way of telling Python to create a vector that's full of empty placeholders for future viral load data.
        vector_V[0] = V0 # This tells Python to save the initial viral load in the first position in our vector

        for i in range(1, len(vector_t)): # This is our for loop. It's basically telling Python: "For each timestep, do Euler's method..."
            dt = vector_t[i] - vector_t[i-1] # by first calculating the change in time based on the current value minus the past value,
            Vprime = p-c*vector_V[i-1] # then calculating the change in V based on the past value of V, and finally
            vector_V[i] = vector_V[i-1] + dt*Vprime # adding the change in V to the previous value of V

        # Making our Plot

        _fig = make_subplots(rows=1, cols=1, shared_yaxes=True) # This line tells Python how to set up the figure margins on all sides.
        _fig.update_layout(template="plotly_white", height=300, width=400, showlegend=False, margin=dict(l=65, r=25, t=45, b=55))
        _scenarios = []

        _x = vector_t # Tell Python what to put on the x-axis
        _y = vector_V # Tell Python what to put on the y-axis
        _mode = "lines" # Plot as a line
        _fig.update_xaxes(title_text='Time (days)', row=1, col=1) # Label the x-axis
        _fig.update_yaxes(title_text='Viral Load (particles per mL)', row=1, col=1) # Label the y-axis
        _fig.add_trace(go.Scatter(x=_x, y=_y, mode=_mode, name=f"c = {c:g}, p = {p:g}"), row=1, col=1)
        _scenarios.append({"c": c, "p": p, "times": vector_t.copy(), "values": vector_V.copy()})
        return _fig, _scenarios

    mo.accordion({"Show Python code": mo.show_code(position="above")})
    return (run_chunk_9,)


@app.cell(hide_code=True)
def output_9(run_chunk_9):
    chunk_9_result = run_chunk_9()
    chunk_9_result[0]
    return


@app.cell(hide_code=True)
def narrative_9(mo):
    mo.md(r"""
    So far, this isn't so impressive. But let's run our simulation for much longer, now that we have a for-loop tool to do so!
    """)
    return


@app.cell(hide_code=True)
def code_10(go, make_subplots, mo, np):
    def run_chunk_10():
        _outputs = []
        # Running our simulation

        c = 0.3256 # Average decay value of the three patients
        p = 0 # Production rate when treated by protease inhibitors

        ## Starting timepoint
        V0 = 185000 # Starting viral load
        t0 = 0 # Starting timepoint

        ## Setting up vectors to hold our information
        vector_t = np.linspace(0, 20, int(round(20 / 1)) + 1) # The "np.linspace" function tells Python to create a vector that counts from 0 to 3 to hold our timepoints.
        vector_V = np.full(vector_t.shape, np.nan) # NaN stands for "Not a Number" and is a way of telling Python to create a vector that's full of empty placeholders for future viral load data.
        vector_V[0] = V0 # This tells Python to save the initial viral load in the first position in our vector

        for i in range(1, len(vector_t)): # This is our for loop. It's basically telling Python: "For each timestep, do Euler's method..."
            dt = vector_t[i] - vector_t[i-1] # by first calculating the change in time based on the current value minus the past value,
            Vprime = p-c*vector_V[i-1] # then calculating the change in V based on the past value of V, and finally
            vector_V[i] = vector_V[i-1] + dt*Vprime # adding the change in V to the previous value of V

        # Making our plot

        _fig = make_subplots(rows=1, cols=1, shared_yaxes=True) # This line tells Python how to set up the figure margins on all sides.
        _fig.update_layout(template="plotly_white", height=300, width=400, showlegend=False, margin=dict(l=65, r=25, t=45, b=55))
        _scenarios = []

        _x = vector_t # Tell Python what to put on the x-axis
        _y = vector_V # Tell Python what to put on the y-axis
        _mode = "lines" # Plot as a line
        _fig.update_xaxes(title_text='Time (days)', row=1, col=1) # Label the x-axis
        _fig.update_yaxes(title_text='Viral Load (particles per mL)', row=1, col=1) # Label the y-axis
        _fig.add_trace(go.Scatter(x=_x, y=_y, mode=_mode, name=f"c = {c:g}, p = {p:g}"), row=1, col=1)
        _scenarios.append({"c": c, "p": p, "times": vector_t.copy(), "values": vector_V.copy()})
        return _fig, _scenarios

    mo.accordion({"Show Python code": mo.show_code(position="above")})
    return (run_chunk_10,)


@app.cell(hide_code=True)
def output_10(run_chunk_10):
    chunk_10_result = run_chunk_10()
    chunk_10_result[0]
    return


@app.cell(hide_code=True)
def narrative_10(mo):
    mo.md(r"""
    How does this compare to using the Google Sheet?

    Finally, remember that Euler's Method gets more accurate the smaller the timesteps that we take. With Python, we can flexibly adjust our timestep value easily without needing to add more rows to a Google Sheet or needing to do more calculations by hand. In the chunk below, we are adding a "delta_t" that tells Python how large of timesteps to take.
    """)
    return


@app.cell(hide_code=True)
def timestep_controls(mo):
    timestep = mo.ui.dropdown(options={"1": 1.0, "0.5": 0.5, "0.1": 0.1, "0.01": 0.01}, value="0.01", label="delta_t (days)")
    timestep
    return (timestep,)


@app.cell(hide_code=True)
def code_11(go, make_subplots, mo, np):
    def run_chunk_11(selected_step):
        _outputs = []
        # Running our simulation

        c = 0.3256 # Average decay value of the three patients
        p = 0 # Production rate when treated by protease inhibitors

        ## Starting timepoint
        V0 = 185000 # Starting viral load
        t0 = 0 # Starting timepoint

        delta_t = selected_step # Length of timesteps

        ## Setting up vectors to hold our information
        vector_t = np.linspace(0, 20, int(round(20 / delta_t)) + 1) # The "np.linspace" function tells Python to create a vector that counts from 0 to 3 to hold our timepoints.
        vector_V = np.full(vector_t.shape, np.nan) # NaN stands for "Not a Number" and is a way of telling Python to create a vector that's full of empty placeholders for future viral load data.
        vector_V[0] = V0 # This tells Python to save the initial viral load in the first position in our vector

        for i in range(1, len(vector_t)): # This is our for loop. It's basically telling Python: "For each timestep, do Euler's method..."
            dt = vector_t[i] - vector_t[i-1] # by first calculating the change in time based on the current value minus the past value,
            Vprime = p-c*vector_V[i-1] # then calculating the change in V based on the past value of V, and finally
            vector_V[i] = vector_V[i-1] + dt*Vprime # adding the change in V to the previous value of V

        # Making our plot

        _fig = make_subplots(rows=1, cols=1, shared_yaxes=True) # This line tells Python how to set up the figure margins on all sides.
        _fig.update_layout(template="plotly_white", height=300, width=400, showlegend=False, margin=dict(l=65, r=25, t=45, b=55))
        _scenarios = []

        _x = vector_t # Tell Python what to put on the x-axis
        _y = vector_V # Tell Python what to put on the y-axis
        _mode = "lines" # Plot as a line
        _fig.update_xaxes(title_text='Time (days)', row=1, col=1) # Label the x-axis
        _fig.update_yaxes(title_text='Viral Load (particles per mL)', row=1, col=1) # Label the y-axis
        _fig.add_trace(go.Scatter(x=_x, y=_y, mode=_mode, name=f"c = {c:g}, p = {p:g}"), row=1, col=1)
        _scenarios.append({"c": c, "p": p, "times": vector_t.copy(), "values": vector_V.copy()})
        return _fig, _scenarios

    mo.accordion({"Show Python code": mo.show_code(position="above")})
    return (run_chunk_11,)


@app.cell(hide_code=True)
def output_11(run_chunk_11, timestep):
    chunk_11_result = run_chunk_11(timestep.value)
    chunk_11_result[0]
    return


@app.cell(hide_code=True)
def narrative_11(mo):
    mo.md(r"""
    Notice how that smoothed out our curve!

    ### Using Python to explore different parameter values: c

    Now the real fun can begin! We're going to use Python to simulate different values of viral loss. In the code below, choose two new values of c (c2 and c3) to try. Draw your results on your worksheet.
    """)
    return


@app.cell(hide_code=True)
def clearance_controls(mo):
    c2 = mo.ui.number(start=0, stop=5, step=0.0001, value=0.3256, label="c2")
    c3 = mo.ui.number(start=0, stop=5, step=0.0001, value=0.3256, label="c3")
    mo.hstack([c2, c3], justify="start")
    return c2, c3


@app.cell(hide_code=True)
def code_12(go, make_subplots, mo, np):
    def run_chunk_12(selected_c2, selected_c3):
        _outputs = []
        # Running our simulation

        c2 = selected_c2 # <--- FILL IN A NEW CHOICE OF C HERE

        c3 = selected_c3 # <--- FILL IN A NEW CHOICE OF C HERE


        ## Starting timepoint
        V0 = 185000 # Starting viral load
        t0 = 0 # Starting timepoint

        delta_t = 0.01 # Length of timesteps

        # Simulation 1
        ## Setting up vectors to hold our information
        c = 0.3256 # Average decay value of the three patients; DON'T CHANGE THIS VALUE
        p = 0 # Production rate when treated by protease inhibitors

        vector_t = np.linspace(0, 20, int(round(20 / delta_t)) + 1) # The "np.linspace" function tells Python to create a vector that counts from 0 to 3 to hold our timepoints.
        vector_V = np.full(vector_t.shape, np.nan) # NaN stands for "Not a Number" and is a way of telling Python to create a vector that's full of empty placeholders for future viral load data.
        vector_V[0] = V0 # This tells Python to save the initial viral load in the first position in our vector

        for i in range(1, len(vector_t)): # This is our for loop. It's basically telling Python: "For each timestep, do Euler's method..."
            dt = vector_t[i] - vector_t[i-1] # by first calculating the change in time based on the current value minus the past value,
            Vprime = p-c*vector_V[i-1] # then calculating the change in V based on the past value of V, and finally
            vector_V[i] = vector_V[i-1] + dt*Vprime # adding the change in V to the previous value of V

        # Making our plot
        _fig = make_subplots(rows=1, cols=3, shared_yaxes=True) # This line tells Python how to set up the figure margins on all sides.
        _fig.update_layout(template="plotly_white", height=300, width=1200, showlegend=False, margin=dict(l=65, r=25, t=45, b=55))
        _scenarios = []
        _x = vector_t # Tell Python what to put on the x-axis
        _y = vector_V # Tell Python what to put on the y-axis
        _mode = "lines" # Plot as a line
        _fig.update_xaxes(title_text='Time (days)', row=1, col=1) # Label the x-axis
        _fig.update_yaxes(title_text='Viral Load (particles per mL)', row=1, col=1) # Label the y-axis
        _fig.add_annotation(text=f"c = {c}", x=0.5, y=1.08, xref="x domain", yref="y domain", showarrow=False) # Add a title so we can distinguish the plots
        _fig.update_yaxes(range=[0, V0], row=1, col=1) # Add y-axis limits so all plots scale the same
        _fig.add_trace(go.Scatter(x=_x, y=_y, mode=_mode, name=f"c = {c:g}, p = {p:g}"), row=1, col=1)
        _scenarios.append({"c": c, "p": p, "times": vector_t.copy(), "values": vector_V.copy()})
        _fig.update_xaxes(tick0=0, dtick=5, gridcolor="lightgray", griddash="dash", row=1, col=1) # Add grid lines to make it easier to plot on your worksheet
        _fig.update_yaxes(tick0=0, dtick=50000, gridcolor="lightgray", griddash="dash", row=1, col=1)

        # Simulation 2
        ## Setting up vectors to hold our information
        c = c2 # Choose the second simulation value
        p = 0 # Production rate when treated by protease inhibitors

        vector_t = np.linspace(0, 20, int(round(20 / delta_t)) + 1) # The "np.linspace" function tells Python to create a vector that counts from 0 to 3 to hold our timepoints.
        vector_V = np.full(vector_t.shape, np.nan) # NaN stands for "Not a Number" and is a way of telling Python to create a vector that's full of empty placeholders for future viral load data.
        vector_V[0] = V0 # This tells Python to save the initial viral load in the first position in our vector

        for i in range(1, len(vector_t)): # This is our for loop. It's basically telling Python: "For each timestep, do Euler's method..."
            dt = vector_t[i] - vector_t[i-1] # by first calculating the change in time based on the current value minus the past value,
            Vprime = p-c*vector_V[i-1] # then calculating the change in V based on the past value of V, and finally
            vector_V[i] = vector_V[i-1] + dt*Vprime # adding the change in V to the previous value of V

        # Making our plot
        _x = vector_t # Tell Python what to put on the x-axis
        _y = vector_V # Tell Python what to put on the y-axis
        _mode = "lines" # Plot as a line
        _fig.update_xaxes(title_text='Time (days)', row=1, col=2) # Label the x-axis
        _fig.update_yaxes(title_text='Viral Load (particles per mL)', row=1, col=2) # Label the y-axis
        _fig.add_annotation(text=f"c = {c2}", x=0.5, y=1.08, xref="x2 domain", yref="y2 domain", showarrow=False) # Add a title so we can distinguish the plots
        _fig.update_yaxes(range=[0, V0], row=1, col=2) # Add y-axis limits so all plots scale the same
        _fig.add_trace(go.Scatter(x=_x, y=_y, mode=_mode, name=f"c = {c:g}, p = {p:g}"), row=1, col=2)
        _scenarios.append({"c": c, "p": p, "times": vector_t.copy(), "values": vector_V.copy()})
        _fig.update_xaxes(tick0=0, dtick=5, gridcolor="lightgray", griddash="dash", row=1, col=2) # Add grid lines to make it easier to plot on your worksheet
        _fig.update_yaxes(tick0=0, dtick=50000, gridcolor="lightgray", griddash="dash", row=1, col=2)

        # Simulation 3
        ## Setting up vectors to hold our information
        c = c3 # Choose the third simulation value
        p = 0 # Production rate when treated by protease inhibitors

        vector_t = np.linspace(0, 20, int(round(20 / delta_t)) + 1) # The "np.linspace" function tells Python to create a vector that counts from 0 to 3 to hold our timepoints.
        vector_V = np.full(vector_t.shape, np.nan) # NaN stands for "Not a Number" and is a way of telling Python to create a vector that's full of empty placeholders for future viral load data.
        vector_V[0] = V0 # This tells Python to save the initial viral load in the first position in our vector

        for i in range(1, len(vector_t)): # This is our for loop. It's basically telling Python: "For each timestep, do Euler's method..."
            dt = vector_t[i] - vector_t[i-1] # by first calculating the change in time based on the current value minus the past value,
            Vprime = p-c*vector_V[i-1] # then calculating the change in V based on the past value of V, and finally
            vector_V[i] = vector_V[i-1] + dt*Vprime # adding the change in V to the previous value of V

        # Making our plot
        _x = vector_t # Tell Python what to put on the x-axis
        _y = vector_V # Tell Python what to put on the y-axis
        _mode = "lines" # Plot as a line
        _fig.update_xaxes(title_text='Time (days)', row=1, col=3) # Label the x-axis
        _fig.update_yaxes(title_text='Viral Load (particles per mL)', row=1, col=3) # Label the y-axis
        _fig.add_annotation(text=f"c = {c3}", x=0.5, y=1.08, xref="x3 domain", yref="y3 domain", showarrow=False) # Add a title so we can distinguish the plots
        _fig.update_yaxes(range=[0, V0], row=1, col=3) # Add y-axis limits so all plots scale the same
        _fig.add_trace(go.Scatter(x=_x, y=_y, mode=_mode, name=f"c = {c:g}, p = {p:g}"), row=1, col=3)
        _scenarios.append({"c": c, "p": p, "times": vector_t.copy(), "values": vector_V.copy()})
        _fig.update_xaxes(tick0=0, dtick=5, gridcolor="lightgray", griddash="dash", row=1, col=3) # Add grid lines to make it easier to plot on your worksheet
        _fig.update_yaxes(tick0=0, dtick=50000, gridcolor="lightgray", griddash="dash", row=1, col=3)
        return _fig, _scenarios

    mo.accordion({"Show Python code": mo.show_code(position="above")})
    return (run_chunk_12,)


@app.cell(hide_code=True)
def output_12(c2, c3, run_chunk_12):
    chunk_12_result = run_chunk_12(c2.value, c3.value)
    chunk_12_result[0]
    return


@app.cell(hide_code=True)
def narrative_12(mo):
    mo.md(r"""
    ### Using Python to explore different parameter values: p

    Last, we can explore the dynamics of viral load in a patient who *isn't* being treated with protease inhibitors. For this patient, p > 0.
    """)
    return


@app.cell(hide_code=True)
def production_controls(mo):
    p1 = mo.ui.number(start=0, stop=200000, step=1000, value=1000, label="p1")
    p2 = mo.ui.number(start=0, stop=200000, step=1000, value=10000, label="p2")
    p3 = mo.ui.number(start=0, stop=200000, step=1000, value=100000, label="p3")
    mo.hstack([p1, p2, p3], justify="start")
    return p1, p2, p3


@app.cell(hide_code=True)
def code_13(go, make_subplots, mo, np):
    def run_chunk_13(selected_p1, selected_p2, selected_p3):
        _outputs = []
        p1 = selected_p1

        p2 = selected_p2

        p3 = selected_p3


        ## Starting timepoint
        V0 = 185000 # Starting viral load
        t0 = 0 # Starting timepoint

        delta_t = 0.01 # Length of timesteps

        # Simulation 1
        ## Setting up vectors to hold our information
        c = 0.3256 # Average decay value of the three patients; DON'T CHANGE THIS VALUE
        p = p1 # Production rate when treated by protease inhibitors; using first choice

        vector_t = np.linspace(0, 20, int(round(20 / delta_t)) + 1) # The "np.linspace" function tells Python to create a vector that counts from 0 to 3 to hold our timepoints.
        vector_V = np.full(vector_t.shape, np.nan) # NaN stands for "Not a Number" and is a way of telling Python to create a vector that's full of empty placeholders for future viral load data.
        vector_V[0] = V0 # This tells Python to save the initial viral load in the first position in our vector

        for i in range(1, len(vector_t)): # This is our for loop. It's basically telling Python: "For each timestep, do Euler's method..."
            dt = vector_t[i] - vector_t[i-1] # by first calculating the change in time based on the current value minus the past value,
            Vprime = p-c*vector_V[i-1] # then calculating the change in V based on the past value of V, and finally
            vector_V[i] = vector_V[i-1] + dt*Vprime # adding the change in V to the previous value of V

        # Making our plot
        _fig = make_subplots(rows=1, cols=3, shared_yaxes=True) # This line tells Python how to set up the figure margins on all sides.
        _fig.update_layout(template="plotly_white", height=300, width=1200, showlegend=False, margin=dict(l=65, r=25, t=45, b=55))
        _scenarios = []
        _x = vector_t # Tell Python what to put on the x-axis
        _y = vector_V # Tell Python what to put on the y-axis
        _mode = "lines" # Plot as a line
        _fig.update_xaxes(title_text='Time (days)', row=1, col=1) # Label the x-axis
        _fig.update_yaxes(title_text='Viral Load (particles per mL)', row=1, col=1) # Label the y-axis
        _fig.add_annotation(text=f"p = {p1}", x=0.5, y=1.08, xref="x domain", yref="y domain", showarrow=False) # Add a title so we can distinguish the plots
        _fig.update_yaxes(range=[0, 3e5], row=1, col=1) # Add y-axis limits so all plots scale the same
        _fig.add_trace(go.Scatter(x=_x, y=_y, mode=_mode, name=f"c = {c:g}, p = {p:g}"), row=1, col=1)
        _scenarios.append({"c": c, "p": p, "times": vector_t.copy(), "values": vector_V.copy()})
        _fig.update_xaxes(tick0=0, dtick=5, gridcolor="lightgray", griddash="dash", row=1, col=1) # Add grid lines to make it easier to plot on your worksheet
        _fig.update_yaxes(tick0=0, dtick=50000, gridcolor="lightgray", griddash="dash", row=1, col=1)

        # Simulation 2
        ## Setting up vectors to hold our information
        c = 0.3256 # Average decay value of the three patients; DON'T CHANGE THIS VALUE
        p = p2 # Production rate when treated by protease inhibitors; using second choice

        vector_t = np.linspace(0, 20, int(round(20 / delta_t)) + 1) # The "np.linspace" function tells Python to create a vector that counts from 0 to 3 to hold our timepoints.
        vector_V = np.full(vector_t.shape, np.nan) # NaN stands for "Not a Number" and is a way of telling Python to create a vector that's full of empty placeholders for future viral load data.
        vector_V[0] = V0 # This tells Python to save the initial viral load in the first position in our vector

        for i in range(1, len(vector_t)): # This is our for loop. It's basically telling Python: "For each timestep, do Euler's method..."
            dt = vector_t[i] - vector_t[i-1] # by first calculating the change in time based on the current value minus the past value,
            Vprime = p-c*vector_V[i-1] # then calculating the change in V based on the past value of V, and finally
            vector_V[i] = vector_V[i-1] + dt*Vprime # adding the change in V to the previous value of V

        # Making our plot
        _x = vector_t # Tell Python what to put on the x-axis
        _y = vector_V # Tell Python what to put on the y-axis
        _mode = "lines" # Plot as a line
        _fig.update_xaxes(title_text='Time (days)', row=1, col=2) # Label the x-axis
        _fig.update_yaxes(title_text='Viral Load (particles per mL)', row=1, col=2) # Label the y-axis
        _fig.add_annotation(text=f"p = {p2}", x=0.5, y=1.08, xref="x2 domain", yref="y2 domain", showarrow=False) # Add a title so we can distinguish the plots
        _fig.update_yaxes(range=[0, 3e5], row=1, col=2) # Add y-axis limits so all plots scale the same
        _fig.add_trace(go.Scatter(x=_x, y=_y, mode=_mode, name=f"c = {c:g}, p = {p:g}"), row=1, col=2)
        _scenarios.append({"c": c, "p": p, "times": vector_t.copy(), "values": vector_V.copy()})
        _fig.update_xaxes(tick0=0, dtick=5, gridcolor="lightgray", griddash="dash", row=1, col=2) # Add grid lines to make it easier to plot on your worksheet
        _fig.update_yaxes(tick0=0, dtick=50000, gridcolor="lightgray", griddash="dash", row=1, col=2)

        # Simulation 3
        ## Setting up vectors to hold our information
        c = 0.3256 # Average decay value of the three patients; DON'T CHANGE THIS VALUE
        p = p3 # Production rate when treated by protease inhibitors; using third choice

        vector_t = np.linspace(0, 20, int(round(20 / delta_t)) + 1) # The "np.linspace" function tells Python to create a vector that counts from 0 to 3 to hold our timepoints.
        vector_V = np.full(vector_t.shape, np.nan) # NaN stands for "Not a Number" and is a way of telling Python to create a vector that's full of empty placeholders for future viral load data.
        vector_V[0] = V0 # This tells Python to save the initial viral load in the first position in our vector

        for i in range(1, len(vector_t)): # This is our for loop. It's basically telling Python: "For each timestep, do Euler's method..."
            dt = vector_t[i] - vector_t[i-1] # by first calculating the change in time based on the current value minus the past value,
            Vprime = p-c*vector_V[i-1] # then calculating the change in V based on the past value of V, and finally
            vector_V[i] = vector_V[i-1] + dt*Vprime # adding the change in V to the previous value of V

        # Making our plot
        _x = vector_t # Tell Python what to put on the x-axis
        _y = vector_V # Tell Python what to put on the y-axis
        _mode = "lines" # Plot as a line
        _fig.update_xaxes(title_text='Time (days)', row=1, col=3) # Label the x-axis
        _fig.update_yaxes(title_text='Viral Load (particles per mL)', row=1, col=3) # Label the y-axis
        _fig.add_annotation(text=f"p = {p3}", x=0.5, y=1.08, xref="x3 domain", yref="y3 domain", showarrow=False) # Add a title so we can distinguish the plots
        _fig.update_yaxes(range=[0, 3e5], row=1, col=3) # Add y-axis limits so all plots scale the same
        _fig.add_trace(go.Scatter(x=_x, y=_y, mode=_mode, name=f"c = {c:g}, p = {p:g}"), row=1, col=3)
        _scenarios.append({"c": c, "p": p, "times": vector_t.copy(), "values": vector_V.copy()})
        _fig.update_xaxes(tick0=0, dtick=5, gridcolor="lightgray", griddash="dash", row=1, col=3) # Add grid lines to make it easier to plot on your worksheet
        _fig.update_yaxes(tick0=0, dtick=50000, gridcolor="lightgray", griddash="dash", row=1, col=3)
        return _fig, _scenarios

    mo.accordion({"Show Python code": mo.show_code(position="above")})
    return (run_chunk_13,)


@app.cell(hide_code=True)
def output_13(p1, p2, p3, run_chunk_13):
    chunk_13_result = run_chunk_13(p1.value, p2.value, p3.value)
    chunk_13_result[0]
    return


@app.cell(hide_code=True)
def narrative_13(mo):
    mo.md(r"""
    Draw these results on your worksheet and answer the questions about them there.
    """)
    return


if __name__ == "__main__":
    app.run()
