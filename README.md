# imdb_scraper
Does IMDb (owned by Amazon) inflate the ratings of Amazon original programming as compared to other streaming services?


# How it works:
Step 1.) Pulls show titles of original programming for desired streaming services from the links found at:
https://en.wikipedia.org/wiki/Category:Lists_of_television_series_by_streaming_service

Step 2.) Scrubs through a reduced version of IMDb's datasets to find information about a show based on the title found in the previous step.

Step 3.) Imports show rating data into matplotlib

Step 4.) Displays data as boxplot with each box representing a streaming service set in main.py.


# Results and Conclusion:
Amazon's original programming did have a higher mean rating than it's counterparts in Netflix and Hulu. However, the method for collecting this rating data is very imperfect as it is now, and only having a higher mean is hardly scientific evidence. Does Amazon inflate their own IMDb scores? ¯\\_(ツ)_/¯
