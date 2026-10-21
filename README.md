# MATH 34LA Week 6 — interactive marimo lab

This converts `MATH34LA_Week6_Rscript.Rmd` into a Python marimo notebook. No input datasets, API keys, R installation, or external local assets are needed. Keep your existing worksheet and LMS submission process.

## 1. Open the notebook on your computer

Install Python 3.11 or newer (tested with 3.12). Extract this folder, open Terminal, and change into it, for example:

```bash
cd ~/Downloads/math34la_week6_marimo
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m marimo edit notebook.py
```

On Windows, activate using `.venv\Scripts\activate` instead. The editor opens in your browser. Read the lab from top to bottom. Code cells remain available for instruction and editing; controls update dependent results automatically. Changes to code are saved in notebook.py. The original source is preserved separately under source/.

To present the lab with code editing disabled:

```bash
python -m marimo run notebook.py
```

## 2. Use the controls

- Timestep: select 1, 0.5, 0.1, or 0.01 days. Only the timestep exploration changes; later comparisons intentionally retain the original 0.01-day timestep.
- Exact-reference checkbox: add the analytical curve and maximum sampled absolute error. This extension is off by default.
- Clearance c₂ and c₃: enter values from 0 to 5 per day; the baseline remains 0.3256. Defaults reproduce the source (three identical curves).
- Production p₁, p₂, p₃: enter 0–200,000 particles/mL/day. Original defaults are 1,000, 10,000, and 100,000. Zero is allowed as an explicit extension for comparison with treatment.
- Expanded-axis checkbox: reveal values above the original 300,000-particle/mL ceiling while retaining a common scale across panels.
- Hover or zoom in the Plotly graphs; double-click to reset zoom. Tables display the current scenario results.

Predict changes first, then experiment and record your interpretation on the worksheet. Tables and explanatory text follow the controls; answers are not automatically submitted or stored in an LMS.

## 3. Try browser-only student delivery

`week6_browser.html` is an editable WebAssembly export. Open it in a modern browser with internet access; it downloads its runtime and packages. Export generation succeeded, but browser execution has not been verified here. The exporter warned that Plotly is outside the Pyodide lockfile and may fail to install; local Python execution above is the validated route. Before assigning the browser version, test on a student-like device/network: reload, change every control, inspect plots, and confirm how students save their work. Do not assume browser edits survive a refresh.

Regenerate it after editing notebook.py:

```bash
python -m marimo export html-wasm notebook.py --single-file --mode edit -o week6_browser.html -f
```

For students who should use controls without editing code, replace `--mode edit` with `--mode run`. Upload the HTML as a downloadable LMS attachment, or host an exported directory on a static website. An LMS preview may block scripts: test the download/open route rather than assuming Canvas will execute it inline. Internet is required for the supplied export; this is not an offline bundle.

For a hosted directory:

```bash
python -m marimo export html-wasm notebook.py --mode edit -o web
python -m http.server --directory web 8000
```

Open http://localhost:8000 for your local test. For public access, publish the generated web directory using your institution's static hosting process. The local server is not public hosting.

## 4. Verify before class

```bash
python -m marimo check notebook.py
python validate.py
```

The validator executes every cell, checks the Euler calculations against an independent discrete formula, and runs control-value overrides through the notebook graph. It writes validation_results.json. Read conversion_notes.md for assumptions and precise validation limits.

## 5. Complete the course migration

1. Launch the editable notebook and review the full teaching sequence against your worksheet.
2. Try different c and p choices and all timestep settings. Decide whether to retain the optional exact-solution extension.
3. Test the student delivery route on the actual browser/network used in class.
4. Keep worksheet submission unchanged for the pilot. If you require notebook submissions later, establish and test a download/save workflow first.
5. Pilot Week 6 with a few students or a co-instructor, then apply the same inputs → simulation → plot → interpretation structure to subsequent labs.

## Files

- notebook.py: complete portable lab with inline dependency metadata.
- requirements.txt: tested direct dependency versions for local execution.
- README.md: setup, use, distribution, and next steps.
- conversion_notes.md: source inventory, mapping, differences, validation.
- validate.py and validation_results.json: reproducible numerical and notebook checks.
- week6_browser.html: generated editable browser export.
- source/MATH34LA_Week6_Rscript.Rmd: unchanged original for comparison.
