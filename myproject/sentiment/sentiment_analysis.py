from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

def analyze_sentiment(text, model):
    if model == 'vader':
        analyzer = SentimentIntensityAnalyzer()
        sentiment = analyzer.polarity_scores(text)
    elif model == 'textblob':
        blob = TextBlob(text)
        sentiment = {
            'pos': blob.sentiment.polarity if blob.sentiment.polarity > 0 else 0,
            'neu': 1 - abs(blob.sentiment.polarity),
            'neg': abs(blob.sentiment.polarity) if blob.sentiment.polarity < 0 else 0,
            'compound': blob.sentiment.polarity
        }
    return sentiment
