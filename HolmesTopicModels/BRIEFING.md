*Project Briefing*
==================

# HolmesTopicModels
Topic Models of Sherlock Holmes stories.

In this project different approaches to Topic Modeling are compared. [Latent Dirichlet Allocation (LDA)](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation), [Latent Semantic Analysis (LSA)](https://en.wikipedia.org/wiki/Latent_semantic_analysis) and [Non-Negative Matrix Factorization (NNMF)](https://en.wikipedia.org/wiki/Non-negative_matrix_factorization) are applied on a corpus, which consists of stories of the famous [Sherlock Holmes](https://en.wikipedia.org/wiki/Sherlock_Holmes) series by Arthur Conan Doyle. The research goal is in finding a new assignment scheme for stories to collections based on the topic models. This scheme should then be compared to the original collections in the Sherlock Holmes canon.


## Project Goal
Apply LDA, LSI and NMF on Sherlock Holmes stories corpus and compare the results. Find a new assignment of stories to collections.


## Metrices
* Visually inspect topics.


## Termination Strategy
Project will terminate, if...

* Lack of time
* Data can not be acquired
* Topics are uninterpretable


## Target Group
* Data professional audience


## References
* [Applied Text Analysis with Python](http://shop.oreilly.com/product/0636920052555.do) by Benjamin Bengfort, Rebecca Bilbro, Tony Ojeda [2018]
* [Latent Dirichlet Allocation](http://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf) by David Blei, Andrew Ng, Michael Jordan [2003]
* [LDA in Python – How to grid search best topic models?](https://www.machinelearningplus.com/nlp/topic-modeling-python-sklearn-examples/)


### Benchmark
* [THE GAME IS AFOOT! TOPIC MODELING OF SHERLOCK HOLMES STORIES](https://juliasilge.com/blog/sherlock-holmes-stm/) by Julia Silge


## Data Management
* Provenance => `project/data/REFS.md`
* Architecture => file-based
* Persistence => file-based


## Technologies
* Processing => PyData Stack based on Anaconda. Libraries:
    * see `environment.yml`
* Modeling => scikit-learn
* IO => Jupyter, Yellowbrick, pyLDAvis

## Test Strategy
Model Testing:

* Inspect model outputs and examine on conclusivness
* Similarity of outputs from different models (Jaccard Index)

App Testing:

* Unittests


## Timetable
* Start => 23.10.2018
* Expected finish => 02.11.2018
* Actual finish => 02.11.2018

## Limitations / Further Improvements
* Different approaches for the assignment of stories to collections can be used (eg Clustering)
* Sherlock Holmes novels can be taken into account.
* Novel collection sequences can be learned by RNN.
