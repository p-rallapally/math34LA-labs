# Set up continuous editing and publishing

Copy .github/workflows/deploy.yml and .gitignore into your existing math34la_week6_marimo folder, alongside notebook.py, requirements.txt, and validate.py. Finder hides dotfiles: Command-Shift-period shows them. Extracting this archive elsewhere does not install the workflow into your lab folder automatically.

## First-time setup

1. On GitHub, create a new empty repository called math34la-labs. Choose Public if using free GitHub Pages. Do not initialize a README, license, or gitignore: your local folder already has content.
2. In Terminal, from the existing lab folder, run the following. Replace YOUR_USERNAME with your GitHub account name:

```bash
cd ~/Downloads/math34la_week6_marimo
git init
git branch -M main
git add .
git status
git commit -m "Add interactive Week 6 lab and publishing workflow"
git remote add origin https://github.com/YOUR_USERNAME/math34la-labs.git
```

Before pushing, open repository Settings → Pages. Under Build and deployment, set Source to GitHub Actions. If the empty repository does not expose Pages yet, push first, enable Pages, then rerun the failed workflow from Actions (or use Run workflow).

```bash
git push -u origin main
```

HTTPS authentication uses your configured GitHub credentials, GitHub CLI, or a personal access token—not your GitHub account password. If no credential helper is configured, GitHub CLI users can run `gh auth login` then `gh auth setup-git`. An existing SSH setup also works with GitHub's SSH remote URL.

3. Open the repository's Actions tab. The Validate and publish marimo lab workflow should run. A successful deployment provides a URL in the deploy job / repository Pages settings, normally https://YOUR_USERNAME.github.io/math34la-labs/.
4. Open that URL on a student-like device and test every input. The workflow checks Python execution and export generation; it does not automate browser interaction or WebAssembly package loading.

## Every editing session

From your lab folder:

```bash
git pull --ff-only
source .venv/bin/activate
python -m marimo edit --no-sandbox notebook.py
```

Edit in the marimo browser editor. Changes save to notebook.py. The server occupies its terminal; use a second terminal in the same folder for Git commands, or stop the server with Control-C after editing.

Review and publish:

```bash
git diff -- notebook.py
git add notebook.py
git commit -m "Clarify Euler timestep activity"
git push
```

If you edited other files, stage those explicitly too (for example, `git add requirements.txt README.md`). GitHub validates, exports with code hidden, and publishes automatically after a push to main. Students keep the same website link. You do not have to export or upload HTML manually. Saving alone does not publish: commit and push when ready.

## Optional review before publication

```bash
git switch -c revise-week6
# edit and save, then:
git add notebook.py
git commit -m "Revise Week 6 explanations"
git push -u origin revise-week6
```

Create a pull request targeting main on GitHub. The workflow validates and exports the proposed changes without publishing them. Merge when ready; the push to main publishes the update. Return locally with `git switch main` and `git pull --ff-only`.

## What is tracked

Commit the Python notebook, requirements, validator, source Rmd, documentation, workflow, and .gitignore. Generated HTML, virtual environments, session caches, and validation results are ignored. If you already committed a generated file, .gitignore will not untrack it; optionally use `git rm --cached week6_browser.html validation_results.json` when those files are tracked, then commit. Do not run that command for files Git does not track.

The workflow runs from repository root. Put the contents of your lab folder directly at that root, rather than adding an extra math34la_week6_marimo directory inside it. Start with this single-lab repository; add a multi-lab index and export loop when the next lab is ready.

## Environment behavior and limitations

The workflow installs requirements.txt and supplies --no-sandbox so marimo does not prompt or select newer packages from the notebook's unpinned inline metadata. Your existing local venv can be used the same way. Update tested pins deliberately if needed.

Publication uses GitHub Pages and the notebook's browser runtime; Python computations execute in each student's browser. Package compatibility (especially Plotly loading) still needs testing. Code is hidden in the interface, but browser exports embed the source and do not provide source confidentiality.

These files were prepared and structurally checked locally. They have not been run on your GitHub account or deployed: repository creation, connecting your local Git remote, enabling Pages, and the first successful Actions run remain your setup steps.
