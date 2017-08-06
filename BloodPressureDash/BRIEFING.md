*Project Briefing*
==================

# BloodPressureDash
Dashboard of blood pressure measures

Dashboard presents a report of blood pressure and pulse values, collected with blood pressure monitor. Its purpose is to control actual hypertension therapy and also the process of stopping the medication after few weeks.


## Project Goal
Dashboard should visualize and provide some analytics of blood pressure measures.


## Metrices
* Personal usability of report (measured with self-X)


## Termination Strategy
Project will terminate, if...

* Jupyter Dashboard doesn't work (maybe refactor to Dash)
* Expected finish after appointment with Internist


## Target Group
* Self-use
* Internist


## Research
* Googeling standard values


### Benchmark
* Fever chart in patient maps at hospital


## Data Management
* Provenance => `project/data/REFS.md`
* Persistence => filebased (.csv)


## Technologies
* Processing => PyData Stack based on Anaconda. Libraries:
    * `environment.yml`
* Visualization => Matplotlib
* Reporting => Jupyter Dashboard


## Test Strategy
No testing for script.

Usability: Self-testing of dashboard.


## Timetable
* Start => 16.07.2017
* Expected finish => 03.08.2017
* Actual finish => 06.08.2017


## Limitations / Further Improvements
* Frontend: Automate input
* Large number of observations will decrease usability. Too many weekly visualizations for single page
* ATM pdf export doesn't work well with Jupyter Dashboard