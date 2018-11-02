#!/usr/bin/python
""" main

#FIXME Description

Author: datadonk23
Date: 23.10.18 
"""

import pandas as pd

from preprocessing import load_corpus, tfidf_vectorizer
from model import make_pipeline, make_model


def main():
    """
    Main Loop
    :return: -
    """

    corpus = load_corpus("data/")

    # NLP pipeline
    tfidf = tfidf_vectorizer()
    model = make_model(n_topics=5)

    pipeline = make_pipeline(tfidf, model)
    topic_distr = pipeline.fit_transform(corpus.data)



    #
    #
    # print("Novel Sherlock Holmes Short Stories Collections:")
    # for _, title in novel_collections_map.items():
    #     print("*", title)
    #
    # topics = ["Topic" + str(i) for i in range(n_topics)]
    # docs = [" ".join(f_name.split("/")[-1].split(".")[0].split("_"))
    #         for f_name in corpus.filenames]
    #
    # df_document_topic = pd.DataFrame(np.round(nmf_topic_distr, 3),
    #                                  columns=topics, index=docs)
    # df_document_topic["assigned_topic"] = np.argmax(df_document_topic.values,
    #                                                 axis=1)
    # df_document_topic["orig_collection"] = [collections_map.get(item, item) for
    #                                         item in corpus.target]
    # df_document_topic["novel_collection"] = [
    #     novel_collections_map.get(item, item)
    #     for item in df_document_topic.assigned_topic.values]
    #
    # df_novel_assignment = df_document_topic.sort_values("assigned_topic").loc[:,
    #                       ["orig_collection",
    #                        "novel_collection"]]
    # df_novel_assignment


if __name__ == "__main__":
    main()
