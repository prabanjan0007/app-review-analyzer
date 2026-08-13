# 📱 Mobile App Review Analyzer

An end-to-end data analytics project for analyzing mobile application reviews using Python, sentiment analysis, data visualization, and an interactive Streamlit dashboard.

## 🎯 Project Overview

The Mobile App Review Analyzer turns review data into practical insights about user ratings, sentiment, feedback patterns, common complaints, and positive feedback.

## ⚓Features

- ⭐ Average rating and rating distribution
- 💬 Total review analysis
- 🟢 Positive, 🟡 neutral, and 🔴 negative sentiment analysis
- 📈 Rating dynamics visualization
- 🧠 Sentiment distribution
- 🎯 Sentiment score gauge
- 🔎 Application and review-type filters
- 🔄 Dashboard refresh control
- 🌙 Light and dark themes
- 💡 Common complaints and positive feedback analysis

## 🏗️ Project Structure
MOBILE APP REVIEW ANALYZER
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── processed/
│   │   ├── cleaned_reviews.csv
│   │   ├── common_complaints.csv
│   │   ├── common_positive_feedback.csv
│   │   └── sentiment_reviews.csv
│   └── raw/
│       └── reviews.csv
│
├── images/
│   ├── common_complaints.png
│   ├── common_positive_feedback.png
│   ├── rating_distribution.png
│   └── sentiment_distribution.png
│
├── src/
│   ├── eda.py
│   ├── feedback_analysis.py
│   ├── feedback_visualization.py
│   ├── rating_sentiment.py
│   ├── review_analysis.py
│   ├── sentiment_analysis.py
│   ├── sentiment_visualization.py
│   └── visualization.py
│
├── .gitignore
└── requirements.txt
```

## 🛠️ Technology Stack

- **Python** — data processing and analysis
- **Pandas** — data manipulation
- **NLTK** — natural language processing
- **Plotly** — interactive visualizations
- **Streamlit** — interactive dashboard
- **Git & GitHub** — version control and project hosting

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/prabanjan0007/app-review-analyzer.git
cd app-review-analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Dashboard

```bash
streamlit run dashboard/app.py
```

Then open:

```text
http://localhost:8501
```


##  What This Project Demonstrates

This project demonstrates an end-to-end workflow covering:

- Data preprocessing
- Exploratory data analysis
- Review analysis
- Sentiment analysis
- Feedback analysis
- Data visualization
- Interactive dashboard development
- Python project organization
- Git version control
- GitHub project management

## 🚀 Future Improvements

- Add more application datasets
- Add review-date trend analysis
- Add advanced NLP models
- Add keyword and topic extraction
- Add review search and advanced filtering
- Add automated data updates
- Add additional business-oriented insights

## 👨‍💻 Author

**Prabanjan** 
GitHub: https://github.com/prabanjan0007
