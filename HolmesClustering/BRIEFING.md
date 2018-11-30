*Project Briefing*
==================

# HolmesClustering
Clustering of Sherlock Holmes stories.

This project aims to find the best assignment of [Sherlock Holmes](https://en.wikipedia.org/wiki/Sherlock_Holmes) stories to novel collections and compares this assignment to the original collections by Arthur Conan Doyle.


## Project Goal
Find the best assignment of stories to collections.


## Metrices
* Silhouette Score


## Termination Strategy
Project will terminate, if...

* Lack of time
* Clusters are uninterpretable


## Target Group
* Data professional audience


## References
* [Applied Text Analysis with Python](http://shop.oreilly.com/product/0636920052555.do) by Benjamin Bengfort, Rebecca Bilbro, Tony Ojeda [2018]


### Benchmark
* Original collections by Sir Arthur Conan Doyle


## Data Management
* Provenance => `project/data/REFS.md`
* Architecture => file-based
* Persistence => file-based


## Technologies
* Processing => PyData Stack based on Anaconda. Libraries:
    * see `environment.yml`
* Modeling => scikit-learn
* IO => Jupyter, Yellowbrick

## Test Strategy
Model Testing:

* Inspect clusters and examine on conclusivness
* Use Silhoutte plots to evaluate cluster consistency.
* Compare average Silhoutte scores for different cluster sizes.


## Timetable
* Start => 10.11.2018
* Expected finish => 16.11.2018
* Actual finish => 30.11.2018

## Limitations / Further Improvements
* Try word2vec instead of BOW (which means Gensim hassle)
* Try Hierarchical Clustering.
* Use Topic Modeling approach (-> got to HolmesTopicModels directory in Repo root)
