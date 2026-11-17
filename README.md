# Lab 3: The Social Media Data Detective
Repository contents

data-detective.py:	        Python application (Quests 1 to 4)

feed-analyzer.sh:	        Bash script that prints the Top 5 most active users

twitter_dataset.csv:	      The dataset (columns: Tweet_ID, Username, Text, Retweets, Likes, Timestamp)

README.md:	This file


### How the Python program works
1. Data Auditor	clean_data
   Removes tweets with missing text. Replaces blank or non-numeric Likes and Retweets with 0 and converts them to integers. Prints how many rows were fixed and removed.
2. Viral Post	find_viral_tweet
   Loops through the tweets, keeping the one with the highest Likes so far (a manual replacement for max()). Prints its username, likes and text.
3. Algorithm Builder
   custom_sort_by_likes	Selection Sort, highest likes first (no .sort() or sorted()). The Top 10 are then taken with the slice [:10].
4. Content Filter	search_tweets
   Case-insensitive search for a keyword in the tweet text. Matching tweets are collected in a new list, and the number of matches is printed before the tweets.

Error handling

If the CSV file is missing, load_raw_data prints a clear message and exits.

clean_data handles missing keys, blank values and non-numeric values without crashing.

find_viral_tweet reports when there are no tweets to search.

search_tweets rejects an empty search word and shows an example of valid input.


### How the shell script works (feed-analyzer.sh)

The script prints the Top 5 most active users by chaining commands with pipes:

**grep -E '^[0-9]+,[^,"]+,' "$FILE" | cut -d',' -f2 | sort | uniq -c | sort -nr | head -5**

(Command)	Job

(grep -E '^[0-9]+,[^,"]+,')	Keeps only lines that start a real tweet (digits, a comma, a username, a comma)

(cut -d',' -f2)	Extracts the Username column

(sort)	Puts identical usernames next to each other

(uniq -c)	Counts each group of identical usernames

(sort -nr)	Sorts by the count, highest first

(head -5)	Keeps the top 5

It also uses the first argument as the file name (default twitter_dataset.csv) and, if the file does not exist, prints an error and exits with code 1.
