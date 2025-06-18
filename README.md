 ## Tweet Sentiment Analyzer

This is a simple Python app that reads tweets from a CSV file and analyzes their sentiment as " Positive, Negative, or Neutral using TextBlob.

 

## Make sure you have Python 3 installed.

Then install the required libraries:

```bash
pip install pandas textblob matplotlib
python -m textblob.download_corpora

## Put your tweets in the tweets.csv file like this:
tweet
"I love this movie!"
"This was boring."
"Great acting and visuals."

 ## Run the Python script:

python main.py
