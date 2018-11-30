# HolmesClusteriing
Clustering Sherlock Holmes stories.

More informations in project briefing: `BRIEFING.md`

# Conda Environment
Run `conda env create -f environment.yml` and then `source activate holmes-clustering`

# App Entry Point
Run Jupyter notebooks located in `holmes_topic_models/notebook` directory.

# Project Structure
```bash
.
├── BRIEFING.md # project briefing
├── docs # documentation & research content
│   └── info.md
├── environment.yml # conda environment
├── LICENSE
├── holmes_clustering
│   ├── data # data files
│   │   ├── __init__.py
│   │   ├── His_Last_Bow/ # Collection texts
│   │   ├── The_Adventures_of_Sherlock_Holmes/ # Collection texts
│   │   ├── The_Case-Book_of_Sherlock_Holmes/ # Collection texts
│   │   ├── The_Memoirs_of_Sherlock_Holmes/ # Collection texts
│   │   ├── The_Return_of_Sherlock_Holmes/ # Collection texts
│   │   └── REFS.md
│   ├── __init__.py
│   └── notebook # jupyter NBs
│       ├── 1_Exploration.ipynb
│       ├── 2_Modeling.ipynb
│       ├── helpers
│       │   ├── __init__.py
│       │   └── tokenizer.py # custom tokenizer
│       └── plots
│           ├── __init__.py
│           └── ... # various plots
├── README.md
└── RESULTS.md # project results
```


# License
Apache License Version 2.0
