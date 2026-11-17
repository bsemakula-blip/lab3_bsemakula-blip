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
    fixed_count = 0       # Rows where blank is replace with 0
    removed_count = 0     # removed rows

    for tweet in tweets:
        text = tweet.get("Text")          # .get() returns None instead of crashing if key is missing

        # If theres no text drop the whole row
        if text is None or text.strip() == "":
            removed_count += 1
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
            fixed_count += 1
        cleaned.append(tweet)

    print(f"Data audit: {fixed_count} rows fixed, {removed_count} rows removed.")
    return cleaned


def find_viral_tweet(tweets):
    """
    QUEST 2: Loop through the list to find the tweet with the highest 'Likes'.
    Do not use the max() function.
    """
    

def custom_sort_by_likes(tweets):
    """
    QUEST 3: Implement Bubble Sort or Selection Sort to sort the list 
    by 'Likes' in descending order. NO .sort() allowed!
    """
    pass

def search_tweets(tweets, keyword):
    """
    QUEST 4: Search for a keyword and extract matching tweets into a new list.
    """
    pass

if __name__ == "__main__":
    # Load the messy data
    dataset = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(dataset)} raw tweets.\n")
    
    # Call your functions here to complete the quests!
    clean_dataset = clean_dataset(dataset)
    
    # Example: clean_dataset = clean_data(dataset)
