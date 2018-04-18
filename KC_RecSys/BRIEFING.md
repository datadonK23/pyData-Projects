*Project Briefing*
==================

# KC_RecSys
Recommender systems for Keep-current project

Show of Concept. User rating based recommendation engines for Keep-current project.


## Project Goal
Show different approaches for recommendation system


## Metrices
* Accuracy of ratings, measured with RMSE and MAE


## Termination Strategy
Project will terminate, if...

* Lack of time
* Surprise lib unusable


## Target Group
* Co-workers on project


## Research
* [Surprise Docs](http://surprise.readthedocs.io/en/stable/)


### Benchmark
* Baseline model, which predicts ratings based on distribution of data in trainset


## Data Management
* Provenance => `project/data/REFS.md`
* Persistence => file based (CSV)


## Technologies
* Processing => PyData Stack based on Anaconda. Libraries:
    * `environment.yml`
* Dissemination => Jupyter notebook
* Modeling => scikit-surprise


## Test Strategy
Model Testing:

* Assertions to ensure right data formats
* K-fold validation of models
* Accuracy evaluation of final model (using RMSE)

App Testing:

* Nothing (no app)


## Timetable
5 Star Rating:

* Start => 29.03.2018
* Expected finish => 29.04.2018
* Actual finish => 03.04.2018

Binary Rating:

* Start => 17.04.2018
* Expected finish => 20.04.2018
* Actual finish => 

## Limitations / Further Improvements
* Uses randomly generated data -> real world data needed
* Only model-based collaborative filtering techniques used - memory-based worth a try, but this wouldn't be a scalable approach
