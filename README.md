# 🧠 Tweet Sentiment Classifier

This project analyzes the sentiment of tweets using **TextBlob** and provides:

- ✅ A Python backend script that reads tweets from CSV files, performs sentiment analysis, and visualizes results.
- 🌐 A **Streamlit-based frontend app** for real-time tweet sentiment prediction with color-coded word highlights.

---

## 🔍 Features

- Perform sentiment analysis (Positive, Negative, Neutral) on tweet data.
- Visualize:
  - 📊 Sentiment distribution using Seaborn bar charts.
  - ☁️ Most frequent words using a WordCloud.
- Input new tweets through a Streamlit UI for instant sentiment feedback.
- Export predicted sentiments from test data to a CSV file.

---

## 🛠️ Technologies Used

- **Python 3**
- **Pandas**
- **TextBlob**
- **Matplotlib & Seaborn**
- **WordCloud**
- **Streamlit**

---

## 📁 Project Structure
project/
├── train.csv # Training tweets
├── test.csv # Test tweets for prediction
├── sentiment_analysis.py # Backend script (CSV-based sentiment analysis + visualization)
├── app.py # Streamlit frontend app
├── test_predictions.csv # Output predictions from test.csv
└── README.md # Project documentation

## 📥 Setup Instructions

1. 🔽 **Clone the project or download the files.**

2. 💻 **Install the required libraries:**

```bash
pip install pandas matplotlib seaborn textblob wordcloud streamlit
python -m textblob.download_corpora

▶️ Running the Project
🔹 Run Backend Script:

 ``` python sentiment_analysis.py ```

Cleans and analyzes train.csv & test.csv
Predicts sentiment
Generates bar chart + word cloud
Saves results to test_predictions.csv

🔹 Run Streamlit Web App:
``` streamlit run app.py ``` 

Input a tweet
See polarity score and emoji feedback
Highlights each word:

🟩 Green = Positive

🟥 Red = Negative

⚪ Neutral = No color

📊 Example Output
Tweet:
I absolutely love this product. It's brilliant!

Result:
😊 Positive (Score: 0.6)
I absolutely :green[love] this product. It's :green[brilliant]!

📌 Notes

Sentiment is based on:
``` TextBlob(text).sentiment.polarity > 0 → Positive < 0 → Negative = 0 → Neutral ``` 

Missing data is dropped automatically

🚀 Future Improvements
Replace TextBlob with advanced models (VADER, BERT)
Host frontend on Streamlit Cloud
Add more NLP features like named entity recognition or emotion tagging

## 👩‍💻 Author
Created as a mini project to explore NLP and sentiment analysis.

