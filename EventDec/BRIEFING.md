*Project Briefing*
==================

# EventDec
By providing some information about an event, app predicts if registration is recommended.

App helps to make decision, if registration to an event is recommended. Uses self labeled dataset of prior attended events for training and testing. \#FIXME


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
* Model misses metric expactations


## Target Group
* Me, personal use. Should be easy to use for quick decisions - perhaps visualization (Decision Tree) helpful.


## Research
* Feature Selection: Predicting Event Attendance, Zhang et al
* \FIXME


### Benchmark
* Meetup RecSys: For event recommendations


## Data Management
* Provenance => `project/data/REFS.md`
* Architecture => File based: csv. Schemas in `project/data/REFS.md`
* Persistence => Pickled files in project directory


## Technologies
* Processing => PyData Stack based on Anaconda. Libraries:
    * `environment.yml`
* \#TODO


## Test Strategy
Model Testing:

* Benchmark: LinReg. Model should perform better than untuned benchmark.
* IO: Unit tests with edge cases

App Testing:
\#TODO


## Timetable
* Start => 08.05.2017
* Expected finish => 03.06.2017
* Actual finish => \#TODO

## Limitations / Further Improvements
* Generalization - small, personal dataset. -> collect more data. Perhaps enhancement with online webinars. Decision Tree not good in generalizing.
* Static model. -> Feedback loop: ratings after attended event.
