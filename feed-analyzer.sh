#!/bin/bash
FILE="${1:-twitter_dataset.csv}"  #file to be checked for users

if [ ! -f "$FILE" ]; then
	echo "Error thr file '$FILE' not found."
	exit 1 
fi

echo "Top 5 Most Active Users:"
grep -E '^[0-9]+,[^,"]+,' "$FILE" | cut -d',' -f2 | sort | uniq -c | sort -nr | head -5
