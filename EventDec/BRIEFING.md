*Project Briefing*
==================

# EventDec
By providing some information about an event, app predicts if registration is recommended.

This simple prototype app should help to make decision, if registration to an event is recommended. By providing inputs it should predict if it's worth to participate - binary prediction ("worth attending"|"not worth attending"). The model uses a self labeled dataset of prior attended events for training and testing. A simple heuristic for ad-hoc decisions should be derived from model.


## Project Goal
Prediction, if event is worth to attend.


## Metrices
* Accuracy of rating predictions. Model should perform better than benchmark Model (simple, untuned Linear Regression).
* Usability of App. Should be usable for quick checks, if an event is worth to register.

## Termination Strategy
Project will terminate, if...

* Lack of sparetime
* Project goal becomes unattainable in time limit
* G calendar data are inaccessible
* Model misses metric expectations


## Target Group
* Me, personal use. Should be easy to use for quick decisions - perhaps visualization (Decision Tree) helpful.


## Research
* Feature Selection: Predicting Event Attendance, Zhang et al
* scikit-learn Docs: [Decision Trees](http://scikit-learn.org/stable/modules/tree.html)


### Benchmark
* Meetup RecSys: For event recommendations


## Data Management
* Provenance => `project/data/REFS.md`
* Architecture => File based: csv. Schemas in `project/data/REFS.md`
* Persistence => Pickled files in project directory


## Technologies
* Processing => PyData Stack based on Anaconda. Libraries:
    * `environment.yml`
* Modeling => scikit-learn
* CLI => Python tools


## Test Strategy
Model Testing:

* Benchmark: LinReg. Model should perform better than untuned benchmark.
* IO: Unit tests with edge cases
* Real world application of prediction: 3 done, 3 passed

App Testing:

* Unit tests
* Final (simple) integration test


## Timetable
* Start => 08.05.2017
* Expected finish => 03.06.2017
* Actual finish => 02.06.2017

## Limitations / Further Improvements
* Generalization - small, personal dataset. -> collect more data. Perhaps enhancement with online webinars. Decision Tree not good in generalizing.
* Model performance - due to small dataset and limited features.
* Static model. -> Feedback loop: ratings after attended event.
