#!/usr/bin/python
""" main

#FIXME Description

Author: datadonk23
Date: 23.10.18 
"""

import numpy as np
import pandas as pd
from tabulate import tabulate

from preprocessing import Collections, load_corpus, tfidf_vectorizer
from model import make_pipeline, make_model


def plot_df(corpus, topic_distribution, n_topics=5):
    """ Output: Plot Dataframe to CLI

    :param corpus: Bunch - Text corpus
    :param topic_distribution: array - Topic distribution for each doc
    :param n_topics: int - Number of topics in topic model
    :return: -
    """

    orig_collections = Collections().original
    novel_collections = Collections().novel

    topics = ["Topic" + str(i) for i in range(n_topics)]
    docs = [" ".join(f_name.split("/")[-1].split(".")[0].split("_"))
            for f_name in corpus.filenames]

    df = pd.DataFrame(np.round(topic_distribution, 3),
                      columns=topics, index=docs)
    df["assigned_topic"] = np.argmax(df.values, axis=1)
    df["orig_collection"] = [orig_collections.get(item, item)
                             for item in corpus.target]
    df["novel_collection"] = [novel_collections.get(item, item)
                              for item in df.assigned_topic.values]

    df_assignment = df.sort_values("assigned_topic").loc[:,
                    ["orig_collection", "novel_collection"]]
    df_assignment.columns = ["Original Collection", "Novel Collection"]
    print(tabulate(df_assignment, headers="keys", tablefmt="fancy_grid"))


def main():
    """ Main loop

    :return: -
    """
    
    n_topics = 5
    corpus = load_corpus("data/")

    # NLP pipeline
    tfidf = tfidf_vectorizer()
    model = make_model(n_topics=n_topics)

    # Training
    pipeline = make_pipeline(tfidf, model)
    topic_distr = pipeline.fit_transform(corpus.data)

    # Output
    plot_df(corpus, topic_distr, n_topics)


if __name__ == "__main__":
    main()
