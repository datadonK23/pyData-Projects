# KC_RecSys
Show of Concept. User rating based recommendation engines for Keep-current project.

More informations in project briefing: `BRIEFING.md`

# Conda Environment
Rename environment name in yml, run `conda env create -f environment.yml` and `source activate $ENVNAME`

# App Entry Point
Start app with `python event_dec/main.py` (or `cd` into `event_dec/`-directory and run `python main.py`)

# Project Structure
* `README.md`
* `BRIEFING.md` _(project briefing)_
* `TODO.md`
* `environment.yml`
* `project/` _#TODO rename_
    * `__init__.py`
    * `main.py` _(entry point)_
    * `model.py`
    * `test/` _(test directory)_
        * `__init__.py`
        * `test_main.py`
        * `test_model.py`
    * `notebook/` _(notebooks for exploration & model development)_
        * `0_Cleaning.ipynb`
        * `1_Exploration.ipynb`
        * `2_Modeling.ipynb`
        * `helpers/`
            * `__init__.py`
        * `plots/`
            * `...` 
    * `data/` _(data directory)_
        * `REFS.md`
        * * `...`
* `docs/` _(documentation & research content)_
    * `research_docs`
    * * `...`
* `LICENSE`

# License
Apache License Version 2.0
