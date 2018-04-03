# KC_RecSys
Show of Concept. User rating based recommendation engines for Keep-current project.

More informations in project briefing: `BRIEFING.md`

# Conda Environment
Rename environment name in yml, run `conda env create -f environment.yml` and `source activate $ENVNAME`

# App Entry Point
`cd` into `project/notebook/`-directory, run `jupyter notebook` and choose `Recommenders.ipynb`-notebook

# Project Structure
* `README.md`
* `BRIEFING.md` _(project briefing)_
* `TODO.md`
* `environment.yml`
* `project/`
    * `__init__.py`
    * `notebook/` _(notebooks for exploration & model development)_
        * `Petdata_generator.ipynb` _(generates random dataset)_
        * `Recommenders.ipynb` _(__main notebook__: Try different recommenders)_
        * `helpers/`
            * `__init__.py`
        * `plots/`
            * `__init__.py`
            * `ratings.png`
    * `data/` _(data directory)_
        * `REFS.md`
        * `petdata_1000_100.csv`
* `docs/` _(documentation & research content)_
    * `info.md`
    * `research_docs`
    * * `...`
* `LICENSE`

# License
Apache License Version 2.0
