import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from textblob import TextBlob
from wordcloud import WordCloud


df = pd.read_csv('train.csv')


df.dropna(inplace=True)


def get_sentiment(text):
    return TextBlob(text).sentiment.polarity


df['Sentiment_Score'] = df['tweet'].apply(get_sentiment)


df['Sentiment'] = df['Sentiment_Score'].apply(
    lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Neutral'
)


sns.countplot(data=df, x='Sentiment', hue='Sentiment', palette='pastel', legend=False)
plt.title('Sentiment Analysis on Tweets')
plt.xlabel('Sentiment')
plt.ylabel('Tweet Count')
plt.show()


text = " ".join(df['tweet'])
wc = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title("WordCloud of Tweets")
plt.show()





test_df = pd.read_csv('test.csv')
test_df.dropna(inplace=True)  # Remove any missing tweets

# Step 2: Apply sentiment analysis to test tweets
test_df['Sentiment_Score'] = test_df['tweet'].apply(get_sentiment)
test_df['Sentiment'] = test_df['Sentiment_Score'].apply(
    lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Neutral'
)


print(test_df[['tweet', 'Sentiment']].head())


test_df.to_csv('test_predictions.csv', index=False)
print("\n✅ Predictions saved to 'test_predictions.csv'")
print(df.head())          # To see output after reading CSV
print(test_df.head())     # To see predictions (if using test.csv)
