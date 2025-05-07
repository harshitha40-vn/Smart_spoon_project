
from textblob import TextBlob
import json
import pandas as pd

def load_feedback():
    with open('sentiment_analysis/feedback.json') as f:
        return json.load(f)

def analyze_sentiment(feedback):
    results = []
    for entry in feedback:
        text = entry['review']
        polarity = TextBlob(text).sentiment.polarity
        results.append({'user': entry['user'], 'sentiment': polarity})
    return pd.DataFrame(results)
