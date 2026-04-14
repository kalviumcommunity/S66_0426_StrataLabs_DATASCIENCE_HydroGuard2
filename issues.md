# Issues Log

Date: 2026-04-14
Time: 15:06 IST
Generated At: 2026-04-14 15:06 IST

## Learning Unit 4.5 - Installing Python and Anaconda on the Local Machine

### Issue Description
Repository had only baseline files, making structural interpretation less explicit.

### When It Occurred
During initial repository navigation for Unit 4.5.

### Root Cause
Project scaffolding for learning-unit artifacts had not yet been established.

### Solution
Established the first set of mandatory learning-unit documentation files and linked them to the product roadmap so subsequent units can build incrementally.

---

### Issue Description
Potential blocker risk for GitHub workflow if CLI auth was missing.

### When It Occurred
Before branch workflow and PR operations.

### Root Cause
GitHub CLI authentication status is environment dependent.

### Solution
Validated `gh` authentication using `gh auth status` before proceeding; account is authenticated and ready for PR workflow.

---

## Learning Unit 4.6 - Verifying Python, Conda, and Jupyter Installation

### Issue Description
Repository had no shared environment specification.

### When It Occurred
During initial setup for tool verification.

### Root Cause
Environment dependencies were previously implied but not version-pinned in project files.

### Solution
Added `environment.yml` with a consistent Conda-based dependency baseline.

---

### Issue Description
Potential false confidence if tools exist but are not callable from shell.

### When It Occurred
While designing setup validation workflow.

### Root Cause
Different local PATH configurations can hide Conda/Jupyter command issues.

### Solution
Created `scripts/verify_python_tools.py` with command discovery and version checks.

---

## Learning Unit 4.7 - Launching Jupyter Notebook and Understanding the Home Interface

### Issue Description
Jupyter can start in unpredictable directories, causing file organization drift.

### When It Occurred
While preparing the first notebook-based workflow.

### Root Cause
Default Jupyter startup path depends on user shell location.

### Solution
Added `scripts/launch_jupyter.py` to consistently launch Jupyter in `notebooks/`.

---

### Issue Description
New contributors may not know what to verify on the home interface before creating notebooks.

### When It Occurred
During unit documentation and onboarding planning.

### Root Cause
Interface behavior is often assumed and left undocumented.

### Solution
Added `notebooks/04_07_jupyter_home_interface.ipynb` with a checklist and workspace verification cell.

---

## Learning Unit 4.8 - Understanding Notebook Cells: Code vs Markdown

### Issue Description
Notebook authors can blur documentation and execution, reducing clarity.

### When It Occurred
During preparation of the first analysis-style notebook template.

### Root Cause
No standard pattern existed for markdown and code cell responsibilities.

### Solution
Created `notebooks/04_08_code_vs_markdown_cells.ipynb` as a reference pattern.

---

### Issue Description
Notebook discoverability becomes difficult as units grow.

### When It Occurred
While adding a second notebook.

### Root Cause
Missing central index for notebook files.

### Solution
Added `notebooks/README.md` to track notebook purpose and sequence.

---

## Learning Unit 4.9 - Running, Restarting, and Interrupting Jupyter Kernels

### Issue Description
Notebook outputs can become inconsistent when execution order is not linear.

### When It Occurred
During planning for reproducible notebook workflows.

### Root Cause
Kernel state persists variables across cells, even when earlier logic changed.

### Solution
Added `notebooks/04_09_kernel_lifecycle_controls.ipynb` with restart and rerun guidelines.

---

### Issue Description
Long-running notebook cells need a controlled interrupt pattern.

### When It Occurred
While designing practical kernel lifecycle examples.

### Root Cause
No prior hands-on example existed for interrupt behavior.

### Solution
Added a timed processing loop to practice interrupt and restart decisions.
