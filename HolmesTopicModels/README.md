# HolmesTopicModels
Topic Models of Sherlock Holmes stories.

More informations in project briefing: `BRIEFING.md`

# Conda Environment
Run `conda env create -f environment.yml` and then `source activate holmes-topic-models`

# App Entry Point
Runnable app which assigns stories to collections: Start app with `python holmes_topic_models/main.py` (or `cd` into `holmes_topic_models/`-directory and run `python main.py`).

Comparison of Topic Models: Run Jupyter notebooks located in `holmes_topic_models/notebook` directory.

# Project Structure
* `README.md`
* `BRIEFING.md` _(project briefing)_
* `TODO.md`
* `environment.yml`
* `holmes_topic_models/`
    * `__init__.py`
    * `main.py` _(entry point)_
    * `model.py`
    * `preprocessing.py`
    * `test/` _(test directory)_
        * `__init__.py`
        * `test_main.py`
        * `test_model.py`
        * `test_preprocessing.py`
    * `notebook/` _(notebooks for exploration & model development)_
        * `1_Exploration.ipynb`
        * `2_Modeling.ipynb`
        * `helpers/`
            * `__init__.py`
            * `tokenizer.py`
        * `plots/`
            * `...` 
    * `data/` _(data directory)_
        *  `__init__.py`
        * `REFS.md`
        * `His_Last_Bow/` _(Collection texts)_
        * `The_Adventures_of_Sherlock_Holmes/` _(Collection texts)_
        * `The_Case-Book_of_Sherlock_Holmes/` _(Collection texts)_
        * `The_Memoirs_of_Sherlock_Holmes/` _(Collection texts)_
        * `The_Return_of_Sherlock_Holmes/` _(Collection texts)_
* `LICENSE`

# License
Apache License Version 2.0
