import csv
import sys
import os

def load_raw_data(filename):
    """
    Loads the CSV file into a list of dictionaries exactly as it is (messy).
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)
            
    return raw_tweets

def clean_data(tweets):
    """
    QUEST 1: Handle missing fields.
    Check for missing text, and replace empty likes/retweets with 0.
    Return a clean list of tweets.
    """
    def clean_data(tweets):
    cleaned = []          # New list to build up with append()
    fixednum = 0       # Rows where blank is replace with 0
    removednum = 0     # removed rows

    for tweet in tweets:
        text = tweet.get("Text")          # .get() returns None instead of crashing if key is missing

        # If theres no text drop the whole row
        if text is None or text.strip() == "":
            removednum += 1
            continue                      # go to the next tweet

        # convert blank Likes/Retweets to int 0
        row_was_fixed = False
        for field in ("Likes", "Retweets"):
            value = tweet.get(field)
            if value is None or value.strip() == "":
                tweet[field] = 0
                row_was_fixed = True
            else:
                try:
                    tweet[field] = int(value)
                except ValueError:        # example "abc" or "12.5"
                    tweet[field] = 0
                    row_was_fixed = True

        if row_was_fixed:
            fixednum += 1
        cleaned.append(tweet)

    print(f"Data audit: {fixednum} rows fixed, {removednum} rows removed.")
    return cleaned


def find_viral_tweet(tweets):
    """
    QUEST 2: Loop through the list to find the tweet with the highest 'Likes'.
    Do not use the max() function.
    """
    if len(tweets) == 0:          # avoid crashing if tweets[0] (nothing to search)
        print("No tweets to search.")
        return None

    viral = tweets[0]             # assume the first tweet is the most viral

    for tweet in tweets:          # look at every tweet
        if tweet["Likes"] > viral["Likes"]:
            viral = tweet         # new most viral

    print("Most viral post:")
    print("Username:", viral["Username"])
    print("Likes:", viral["Likes"])
    print("Text:", viral["Text"])
    return viral

def custom_sort_by_likes(tweets):
    """
    QUEST 3: Implement Bubble Sort or Selection Sort to sort the list 
    by 'Likes' in descending order. NO .sort() allowed!
    """
    num = len(tweets)

    for i in range(num - 1):            # i = the position we're filling next
        biggest_index = i             # assume the most liked is at position i

        for j in range(i + 1, num):     # scan everything after i
            if tweets[j]["Likes"] > tweets[biggest_index]["Likes"]:
                biggest_index = j

        # put the champion into position i
        tweets[i], tweets[biggest_index] = tweets[biggest_index], tweets[i]

    return tweets
   

def search_tweets(tweets, keyword):
    """
    QUEST 4: Search for a keyword and extract matching tweets into a new list.
    """
    keyword = keyword.strip().lower()

    if keyword == "":
        print("Error: search word cannot be empty. Example: Python")
        return []

    matched = []            # new list for the matches

    for tweet in tweets:
        if keyword in tweet["Text"].lower():
            matches.append(tweet)

    return matches

if __name__ == "__main__":
    # Load the messy data
    dataset = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(dataset)} raw tweets.\n")
    
    # Call your functions here to complete the quests!
    clean_dataset = clean_dataset(dataset)
    
    viral = find_viral_tweet(clean_dataset)
    
    sorted_tweets = custom_sort_by_likes(clean_dataset)
    print("Top 10 Most Liked Tweets:")
    for tweet in sorted_tweets[:10]:
        print(tweet["Likes"], tweet["Username"])

    word = input("Enter a search word. Example: Python . ")
    results = search_tweets(clean_dataset, word)

    print(f"\n{len(results)} tweets matched '{word}'.")
    for tweet in results:
        print(f"@{tweet['Username']}: {tweet['Text']}\n")
        
    # Example: clean_dataset = clean_data(dataset)
