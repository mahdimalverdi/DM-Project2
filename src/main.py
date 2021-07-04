import numpy as np
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as sia
import time

start_time = time.time()
interactions = pd.read_excel('..\interactions.xlsx')

interactions = interactions.head(1000)

analyser = sia()
scores = []
text = interactions['Extracted Interaction Text']

def analyse(row):
    return analyser.polarity_scores(row['Extracted Interaction Text'])

interactions['score'] = interactions.apply(analyse, axis=1)

counter = 1
for  sentence in text:
    score = analyser.polarity_scores(sentence)
    scores.append(score)
    counter += 1

end_time = time.time()
print(end_time - start_time)
# Converting List of Dictionaries into Dataframe
dataFrame = pd.DataFrame(scores)
# dataFrame.head(20)

for em in interactions.fromEmailId.unique():
    #interactions.loc[(interactions['fromEmailId']==em),'compound']=(interactions['compound'].where(interactions['fromEmailId']==em)).mean()
    sales_data.loc[sales_data['SalesAgentEmailID']==em,'interaction_score']=(interactions['compound'].where(interactions['fromEmailId']==em)).mean()