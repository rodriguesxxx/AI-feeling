import pandas as pd
from utils.text_manipulation import TextManipulation
from services.sentiment_analyze import SentimentAnalyze

file_response = './form_responses/responses.xlsx'

df = pd.read_excel(file_response);

sentimentAnalyze = SentimentAnalyze()

data = pd.DataFrame()

data = df['Descreva como você está se sentindo agora'].apply(TextManipulation.normalizer)

df['models'] = data.to_list()

polarities = []

for model in df['models']:
    polarity = sentimentAnalyze.analyzeByText(model)
    polarities.append(polarity)
    
print(polarities)