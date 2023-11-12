from nltk import download
from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentAnalyze:

    def __init__(self):
        # download('vader_lexicon')
        self.__intensityAnalyze = SentimentIntensityAnalyzer()

    def analyzeByText(self, text: str) -> str:
        
        analyze = self.__intensityAnalyze.polarity_scores(text)
        print(analyze)
        
        if(analyze['compound'] > 0):
            return "positive"
        else:
            return "negative"