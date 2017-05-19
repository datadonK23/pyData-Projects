# EventDec
By providing some information about an event, app predicts if registration is recommended.

More informations in project briefing: `BRIEFING.md`

# Conda Environment
Rename environment name in yml, run `conda env create -f environment.yml` and `source activate $ENVNAME`

# Project Structure
* `README.md`
* `BRIEFING.md` _(project briefing)_
* `TODO.md`
* `environment.yml`
* `event_dec/`
    * `__init__.py`
    * `main.py` _(entry point)_
    * `model.py`
    * `test/` _(test directory)_
        * `__init__.py`
        * `test_main.py`
        * `test_model.py`
    * `notebook/` _(nb exploration & model development)_
        * `1_exploration.ipynb`
        * `helpers/`
            * `__init__.py`
        * `plots/` _(nb plots)
    * `data/` _(data directory)_
        * `REFS.md`
* `docs/` _(documentation & research content)_
    * `research_docs/`
        * `REFS.md`
* `LICENSE`

# License
Apache License Version 2.0
