# sentiment/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

def home(request):
    return render(request, 'sentiment/home.html')

@login_required
def index(request):
    if request.method == 'POST':
        text = request.POST['text']
        model = request.POST['model']
        sentiment = None
        if model == 'vader':
            sid = SentimentIntensityAnalyzer()
            sentiment = sid.polarity_scores(text)
        elif model == 'textblob':
            blob = TextBlob(text)
            sentiment = {
                'pos': blob.sentiment.polarity,
                'neu': 0.0,  # TextBlob does not provide neutral scores
                'neg': 1 - blob.sentiment.polarity,
                'compound': blob.sentiment.polarity
            }
        return render(request, 'sentiment/index.html', {'sentiment': sentiment, 'model': model, 'text': text})
    return render(request, 'sentiment/index.html')
