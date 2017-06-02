# EventDec
By providing some information about an event, app predicts if registration is recommended.

This simple prototype app helps to make decision, if registration to an event is recommended. By providing three inputs ("Title", "Is the main topic data" and "Distance to location"), it predicts if it's worth to participate. It uses a decision tree classifier to make a binary prediction ("worth attending"|"not worth attending"). The model uses a self labeled dataset of prior attended events for training and testing. Due to expected limitations, the model performs poor (see model evaluation in modeling notebook) - nevertheless, at least better than a flip of coin ;) But, as an intended side-effect, a simple heuristic arose from the final model: "If event is located in central-region of Upper Austria, it is probably not worth attending. If the location is further away than Vienna, it is probably worth attending. And for locations in-between, check if the title is buzzwordy."

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
* `event_dec/`
    * `__init__.py`
    * `main.py` _(entry point)_
    * `model.py`
    * `test/` _(test directory)_
        * `__init__.py`
        * `test_main.py`
        * `test_model.py`
    * `notebook/` _(nb exploration & model development)_
        * `0_Cleaning.ipynb`
        * `1_Exploration.ipynb`
        * `2_Modeling.ipynb`
        * `helpers/`
            * `__init__.py`
        * `plots/` _(nb plots)_
            * `...`
    * `data/` _(data directory)_
        * `REFS.md`
        * `...`
* `docs/` _(documentation & research content)_
    * `research_docs/`
        * `REFS.md`
        * `...`
* `LICENSE`

# License
Apache License Version 2.0
