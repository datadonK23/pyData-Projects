# References

* (NOT in Repo!) events.csv <- self created dataset of attended events. Schema:
    * title [Str]
    * organizer [Str]
    * main_topic [Str]
    * date [Str dd.MM.YYY]
    * days [Int d]
    * start_time [Str ]
    * duration [Str ]
    * weekday [Str Mon-Sun]
    * location [Str]
    * city [Str]
    * state [Str]
    * country [Str]
    * distance [Int km]
    * ticket_prize [Str € $PRIZE]
    * rating [Int 1-10]    
* buzzwords_wiki.txt <- list of buzzwords listed on [Wikipedia](https://en.wikipedia.org/wiki/List_of_buzzwords)
* buzzwords_de.txt <- list of german buzzwords. Based on net research and visits on sites/blogs of usual suspects ;)
* buzzwords_personal.txt <- list of personal buzzwords, encountered at events or in articles
* buzzword_list.pkl <- pickled list of all buzzwords
* (NOT in Repo!) events_df.pkl <- cleaned & pickled DF
* df_model01 <- DF provided for modeling step
* model_trained.pkl <- trained model (Decision Tree CV)
