import re
import pandas as pd
#from tqdm import tqdm

"""
Reads the csv dataset available at
http://thinknook.com/wp-content/uploads/2012/09/Sentiment-Analysis-Dataset.zip
and splits it into two files (.pos and .neg) containing the positive and
negative tweets.
Does some word preprocessing during the parsing.
"""

# import pandas as pd
# df = pd.read_csv('twitter-sentiment-dataset/sentiment-dataset.csv',
#                  error_bad_lines=False)
#
# df.SentimentText = df.SentimentText.str.strip()
# df.SentimentText = df.SentimentText.str.replace(r'http://.*', '<link/>')
# df.SentimentText = df.SentimentText.str.replace('#', '<HASHTAG/> ')
# df.SentimentText = df.SentimentText.str.replace('&quot;', ' \" ')
# df.SentimentText = df.SentimentText.str.replace('&amp;', ' & ')
# df.SentimentText = df.SentimentText.str.replace('&gt;', ' > ')
# df.SentimentText = df.SentimentText.str.replace('&lt;', ' < ')

try:
    pd_full_dataset = pd.read_csv("twitter-dataset/trainingData.csv")#,encoding = "ISO-8859-1")
    #full_dataset = open("twitter-dataset/Ed_Miliband.csv", "r")
    pos_dataset = open("twitter-dataset/tw-data.pos", "w")
    neg_dataset = open("twitter-dataset/tw-data.neg", "w")
except IOError:
    print("Failed to open file")
    quit()

#csv_lines = full_dataset.readlines()
i = 0.0

for row in pd_full_dataset.iterrows():
    i += 1.0
    line = row[1].values
    tweet = line[1].strip() #was 3
    new_tweet = ''

    #Add below any recurrent words you want to group
    tweet = re.sub('strong\s*and\s*stable', 'strongandstable', tweet);

    for word in tweet.split():
        # String preprocessing
        if re.match('^.*@.*', word):
            word = '<NAME/>'
        if re.match('^.*http://.*', word):
            word = '<LINK/>'
        if re.match('^.*https://.*', word):
            word = '<LINK/>'
        word = word.replace('#', '<HASHTAG/> ')
        word = word.replace('&quot;', ' \" ')
        word = word.replace('&amp;', ' & ')
        word = word.replace('&gt;', ' > ')
        word = word.replace('&lt;', ' < ')
        new_tweet = ' '.join([new_tweet, word])

    tweet = new_tweet.strip() + '\n'

    if line[0].strip() == 'Labour':
        pos_dataset.write(tweet)
    else:
        neg_dataset.write(tweet)
