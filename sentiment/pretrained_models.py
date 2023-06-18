from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

#Using TextBlob sentiment analyzer
def sentiment_textblob(sentence):

    classifier = TextBlob(sentence)
    polarity = classifier.sentiment.polarity
    # subjectivity = classifier.sentiment.subjectivity

    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"

    return  "neutral"



#Using Vader sentiment analyzer
def sentiment_vader(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    compound = sentiment_dict['compound']

    if sentiment_dict['compound'] >= 0.05 :
        return "positive"
    elif sentiment_dict['compound'] <= - 0.05 :
        return "negative"

    return "neutral"

