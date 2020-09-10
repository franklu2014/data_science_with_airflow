# Apache Airflow for building pipeline
In the field of Data Science, a data pipeline usually represents a system that ingests, processes, analyzes data.  Sometimes a pipeline also fits and evaluates machine learning models and produce predictions.  As I have came across quite a bit of job postings that ask for experience in building data pipelines with Apache Airflow, I decided to give it a try and increase my own competency.  

Apache Airflow is an open source pipeline building library that all the coding can be based on Python.  Since I mostly practice data science in Python, building pipelines with Airflow becomes a great option for me.

## Project goal
As the purpose is building a data pipeline, I want to dig out something interesting from open data source.  As social media has been a major way of communications, my idea is to cross-analyze Tweeter messages and other societal or environmental factors.

For example, it'll be interesting to see if human communications are affected by the weather, or if results of sports games spur more discussion than government policies do.

As this idea involves multiple data sources and various areas in machine learning, I try to lay out the plan of attack in different phases:  
- [Phase 1: Ingest and aggregate weather data.]((Airflow_pipeline.ipynb))  
    I'm planning to use the API of OpenWeatherMap to get region specific weather data.  Thankfully, OpenWeatherMap provides free-tier of service that allows 1M api calls per month, which suits my requirement very well
    
- Phase 2: Ingest Tweeter data and perform topic modeling.  
    Tweeter also provides free-tier API registration and is suitable for my needs.  For now, I am planning to do topics modeling using Gensim to find the trend of subject matters in people's tweets.  
    
- Phase 3: Ingest news feeds and perform topic modeling.  
    As I'll start by focusing on Canadian news, CBC has RSS feeds to be used.  I am interested in comparing the popular topics of Canadian news with the hot topics on Tweeter.

- Phase 4: Semantic analysis on Tweeter messages.  
    After the trend has been found, I am also interested in finding whether semantics of Tweeter messages do get affected by the weather and the news.