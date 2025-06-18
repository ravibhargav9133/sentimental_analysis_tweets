import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("tweets.csv")

# Perform sentiment analysis
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df['Sentiment'] = df['tweet'].apply(get_sentiment)

# Show results
print(df)

# Plotting
df['Sentiment'].value_counts().plot(kind='bar', color=['green', 'red', 'gray'])
plt.title('Tweet Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.savefig("sentiment_plot.png")
plt.show()
