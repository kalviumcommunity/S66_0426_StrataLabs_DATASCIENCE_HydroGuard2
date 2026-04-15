### Learning Unit: 4.5 Installing Python and Anaconda on the Local Machine

- Branch Name: lu-4-5-python-anaconda-setup

- Commits:
  - docs(lu-4.5): initialize setup and repository orientation artifacts

- Merge Description:
  - Established unit-level documentation artifacts (`video_script.md`, `issues.md`, `DUMMY-README.md`, `git_log.md`)
  - Confirmed GitHub CLI authentication and branch-isolated workflow readiness
  - Mapped setup activities to the Flood Early Warning System product pipeline for continuity into next units

### Learning Unit: 4.6 Verifying Python, Conda, and Jupyter Installation

- Branch Name: python-tools-verification

- Commits:
  - chore(env): add shared conda environment and tool verification script

- Merge Description:
  - Added `.gitignore` entries for unit markdown artifacts as requested
  - Added `environment.yml` to standardize local data science dependencies
  - Added `scripts/verify_python_tools.py` and README setup instructions for executable environment checks

### Learning Unit: 4.7 Launching Jupyter Notebook and Understanding the Home Interface

- Branch Name: jupyter-home-interface

- Commits:
  - feat(notebook): add guided jupyter launch workflow and home interface notebook

- Merge Description:
  - Added `scripts/launch_jupyter.py` to launch notebook server in the project workspace
  - Added `notebooks/04_07_jupyter_home_interface.ipynb` with a practical interface checklist
  - Updated README with a direct command to start Jupyter for project work

### Learning Unit: 4.8 Understanding Notebook Cells: Code vs Markdown

- Branch Name: notebook-code-markdown-cells

- Commits:
  - docs(notebook): add code-vs-markdown reference notebook structure

- Merge Description:
  - Added `notebooks/04_08_code_vs_markdown_cells.ipynb` to demonstrate cell-type responsibilities
  - Added `notebooks/README.md` for notebook discovery and progression
  - Established a reusable notebook communication pattern for upcoming analysis units

### Learning Unit: 4.9 Running, Restarting, and Interrupting Jupyter Kernels

- Branch Name: jupyter-kernel-controls

- Commits:
  - docs(notebook): add kernel lifecycle practice notebook

- Merge Description:
  - Added `notebooks/04_09_kernel_lifecycle_controls.ipynb` with run/interrupt/restart examples
  - Extended `notebooks/README.md` to include kernel lifecycle workflow
  - Documented reproducibility-focused kernel handling guidance for future units

### Learning Unit: 4.10 Writing Markdown for Headings, Lists, and Code Blocks in Notebooks

- Branch Name: notebook-markdown-writing

- Commits:
  - docs(notebook): add markdown style reference notebook

- Merge Description:
  - Added `notebooks/04_10_markdown_patterns.ipynb` with headings, lists, and fenced code blocks
  - Linked markdown examples to executable code for practical usage
  - Updated notebook index to keep onboarding progression clear

### Learning Unit: 4.11 Creating a Project Folder Structure for Data Science Work

- Branch Name: project-folder-structure

- Commits:
  - feat(structure): add baseline data science folder architecture

- Merge Description:
  - Added staged project directories for raw data, processed data, outputs, and source code
  - Documented folder intent in `data/README.md`, `README.md`, and onboarding notebook `04_11`
  - Established structure baseline for upcoming data artifact and script units

### Learning Unit: 4.12 Organizing Raw Data, Processed Data, and Output Artifacts

- Branch Name: data-artifact-organization

- Commits:
  - feat(data): add raw-to-processed staging workflow and artifact folders

- Merge Description:
  - Added sample raw rainfall dataset and a script to produce processed staged output
  - Added dedicated output artifact folders (`reports`, `figures`, `models`) with usage guidance
  - Updated README and onboarding notebook documentation for stage-separation workflow

### Learning Unit: 4.13 Creating and Running a First Python Script for Data Analysis

- Branch Name: first-analysis-script

- Commits:
  - feat(script): add first executable rainfall analysis workflow

- Merge Description:
  - Added `scripts/first_data_analysis.py` to analyze processed rainfall and generate report output
  - Generated first report artifact at `outputs/reports/first_analysis_summary.md`
  - Added unit notebook documentation and run instructions in README
