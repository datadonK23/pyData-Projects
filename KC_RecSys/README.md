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
        * `Recommenders_5Star.ipynb` _(Various recommenders on 5 Star ratings)_
        * `Recommenders_binary.ipynb` _(__main notebook__: Various recommenders on binary encoded ratings)_
        * `helpers/`
            * `__init__.py`
        * `plots/`
            * `__init__.py`
            * `ratings.png`
            * `ratings_binary.png`
    * `data/` _(data directory)_
        * `REFS.md`
        * `petdata_1000_100.csv`
        * `petdata_binary_1000_100.csv`
        * `ai_docs_1000.json`
        * `db_docs_1000.json`
        * `ml_docs_1000.json`
* `docs/` _(documentation & research content)_
    * `info.md`
    * `research_docs`
    * * `...`
* `LICENSE`

# License
Apache License Version 2.0
