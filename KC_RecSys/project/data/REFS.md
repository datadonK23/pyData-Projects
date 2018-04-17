# References

Datasets:

* petdata_1000_100.csv - Random generated dataset (shape=(1000,100)). Code in `project/notebook/Petdata_generator.ipynb`. Rating codes:
    * NaN - Document not seen
    * 0 - Document seen, but not rated
    * 1 - 1 star (poor)
    * 2 - 2 stars
    * 3 - 3 stars (mediocre)
    * 4 - 4 stars
    * 5 - 5 stars (excellent)
* petdata_binary_1000_100.csv - Random generated dataset (shape=(1000,100)). Code in `project/notebook/Petdata_generator.ipynb`. Rating codes:
    * NaN - Document not seen
    *  1 - Like
    * -1 - Dislike
* ai_docs_1000.json - References papers about AI, scraped from arXiv on 2018-04-13. N=1000. Fields:
    * authors
    * title
    * date
    * category
    * url
    * summary
* db_docs_1000.json - References papers about databases, scraped from arXiv on 2018-04-13. N=1000. Fields:
    * authors
    * title
    * date
    * category
    * url
    * summary
* ml_docs_1000.json - References papers about ML, scraped from arXiv on 2018-04-13. N=1000. Fields:
    * authors
    * title
    * date
    * category
    * url
    * summary
