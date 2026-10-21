# Conversion notes

## Source inspection and analytical purpose

The sole project Rmd is MATH34LA_Week6_Rscript.Rmd: 13 chunks, including one empty demonstration chunk. YAML title: MATH 34LA: Week 6 Analysis File; author: MATH 34 LA Students; date: Fall 2025; output: html_document. Title, attribution, and historical term are preserved in the notebook; the output directive is replaced by marimo execution/export.

Purpose: introduce computation to beginning calculus students through explicit Euler simulation of V' = p - cV. This is a deterministic teaching simulation, not statistical estimation. There are no fitted coefficients, confidence intervals, hypothesis tests, external datasets, imports, filesystem paths, random sampling, inline R expressions, or package declarations. The three patient measurements underlying c = 0.3256 are not supplied; the stated average is retained as an input, not re-estimated. The worksheet and Google Sheet are referenced but not supplied; prompts remain and no answers or spreadsheet contents are invented.

The input model assumes constant clearance/production, V0 = 185000 particles/mL, and time in days. Treatment means p=0 within the source's simplified model. Parameter-comparison duration is 20 days; step is 0.01 days. Original defaults: c2=c3=0.3256; p1=1000, p2=10000, p3=100000. Results include arithmetic/vector demonstrations, four viral loads, and line plots. Execution originally followed chunk order, repeatedly overwriting global names.

## Complete R inventory

No contributed R packages. Base R functions: c(), seq(), length(), paste(); graphics functions: par(), plot(), abline(). Constructs/operators: for/in; indexing []; <- assignment; : range; +, -, *, / arithmetic; NaN placeholders; direct expression printing. NaN is an intermediate unfilled value, not observed missing data. No factors, dates, formulas for fitted models, groups, filters, categorical variables, or missing-data exclusions.

- c() numerical vectors → NumPy arrays (or parameter lists).
- seq(from=0,to=end,by=step) → inclusive linspace grid after validating that step divides duration; matches every supplied/allowed grid. Arbitrary non-divisor steps are rejected rather than silently changing endpoints.
- length() → len(); 1-based R positions and inclusive 2:length range → zero-based positions and range(1, len(times)).
- NaN*vector_t → np.full(..., np.nan); initialize first value and fill all others.
- paste() → formatted strings; multiple bare printed results → displayed tables/Markdown.
- par(mar=...), fig.height/fig.width → responsive Plotly dimensions/margins, not identical inch-based sizing.
- par(mfrow=c(1,3)) → three aligned subplots with shared scales.
- plot(type='l') → Plotly line traces; abline grid → axis grid/ticks at 5 days and 50,000 particles/mL.
- Euler calculation → the same explicit recurrence, with floating-point arrays; no alternative ODE integrator.

## Section/chunk mapping

Cells are counted in notebook display order, including imports and narrative.

| Rmd material | Resulting cells |
|---|---|
| YAML + tutorial introduction, empty chunk 1 | 1 imports; 2 attribution and adapted Python/marimo instructions; empty chunk removed |
| Arithmetic chunks 2–3 | 3 all four calculator results in one table |
| Assignment/vector chunks 4–6 | 4 narrative; 5 assignment, vector and product display |
| Viral-dynamics introduction | 6 model, units, assumptions and Euler equation |
| Explicit steps chunk 7 | 7 worked V0–V3 table; 8 spreadsheet prompt and loop introduction |
| Loop chunk 8 | 9 visible reusable loop/function; 10 matching loop table |
| Plot chunk 9 (days 0–3), chunk 10 (days 0–20) | 11 plotting introduction; 12 plotting helpers; 13 both original coarse-step plots |
| Fine timestep chunk 11 | 14 explanatory narrative; 15 timestep/reference controls; 16 calculations; 17 reactive plot and summaries |
| Clearance chunk 12 | 18 narrative/worksheet prompt; 19 c2/c3 controls; 20 scenarios; 21 three panels, summaries and interpretation prompt |
| Production chunk 13 + final worksheet instruction | 22 narrative; 23 p1/p2/p3 and axis controls; 24 scenarios; 25 three panels, clipping note, table and worksheet prompt |

Python-specific setup replaces RStudio play-button, keyboard shortcut, Knit, and chunk-fence instructions. The original R Markdown reference link remains for provenance. Comments explaining the Euler loop are retained in Python form. Repeated setup and simulation code is consolidated; no model section is omitted. The standalone '3 + 4' example is combined with the arithmetic table. Figure labels, units, line-plot style, comparable axes, and worksheet workflow are retained; exact typography and R graphics margins are not.

## Interactive extensions and boundaries

The timestep menu defaults to 0.01; original coarse-step plots stay visible. Optional exact solution and maximum sampled error are teaching extensions, initially hidden. They do not generate or replace the Euler trajectories. c2/c3 are numeric inputs with original defaults and range 0–5; this upper limit keeps c*dt <= 0.05 in these comparisons. Production controls allow 0–200,000, including p=0 as an explicitly labeled comparison extension. Original R accepted unrestricted edits; instructors may change these bounds in the control cell.

The original clearance panels fix y to [0,185000], and production panels fix y to [0,300000]. These limits remain the defaults. The p3=100000 trajectory reaches about 306946 by day 20, beyond the source plot's ceiling. An optional expanded common axis exposes clipped values without changing the calculations. New summary tables retain unrounded internal values; Markdown summaries format to two decimals. There is no automatic student-answer persistence, grading, or submission feature.

Functions hold intermediate state locally. Each global definition belongs to one cell; underscore-prefixed temporaries are cell-local. Parameter controls feed scenario cells, which feed plots/tables/text; the dependency graph has no cycles. Later parameter comparisons deliberately do not depend on the earlier timestep demonstration. Calculations are inexpensive, so caching is unnecessary.

## Validation performed

Environment: Python 3.12, marimo 0.25.2, NumPy 2.3.5, Plotly 7.1.0. Exact direct dependencies are pinned in requirements.txt; inline notebook metadata also names dependencies for sandbox users (without pinning browser package versions).

- marimo check: passes without warnings after formatting and raw-string fixes for LaTeX.
- app.run(): all 25 cells execute from clean definitions, including every default plot and table.
- HTML export: successfully executes and exports the notebook using the local runtime.
- 80 scenarios checked against independent closed-form discrete Euler recurrence, with rtol=1e-10 and atol=1e-6 particles/mL; includes c=0 boundary and broad parameter values. Some validation-only coarse grids at high c are numerically unstable, but still correctly follow the recurrence; UI comparisons fix dt=.01.
- First four values also checked against high-precision decimal powers: 185000; 124764; 84140.8416; 56744.58357504.
- Confirmed grids of 21, 41, 201, and 2001 points over 20 days, finite filled results, baseline loop/manual agreement, three traces per comparison, and original-axis clipping.
- Six additional app.run calls override control definitions: four timestep/exact-checkbox cases, one pair of clearance changes, and one set of production/axis changes. Dependent values, row counts, and axis bounds change as expected.
- Maximum sampled absolute error decreases from about 12910.51 (step 1) to 110.95 (step .01) particles/mL; this is comparison with the exact ODE solution, not a statistical error measure.
- Invalid zero/nondivisor timesteps, negative clearance, and nonfinite production raise errors.
- Browser-editable WebAssembly HTML export generated successfully; generation does not prove execution within a browser. The exporter warned that Plotly is not bundled in the Pyodide lockfile and may fail to install in the browser; a browser will need to fetch a compatible package. Local execution with the pinned requirements is the validated delivery route.

See validation_results.json and run python validate.py to reproduce numerical and dependency checks. No live R comparison was possible because Rscript is absent. Browser clicking, visual rendering QA, WebAssembly package loading, and LMS/network behavior have not been tested here. These remaining delivery checks are described in README.md; no browser-validation claim is made.

The unchanged source is copied under source/; no source data or original file was overwritten.
