import pandas as pd
from textblob import TextBlob

# ========================================
# 1. LOAD CLEANED DATA
# ========================================

df = pd.read_csv("data/processed/cleaned_reviews.csv")

print("🧠 MOBILE APP SENTIMENT ANALYSIS")
print("=" * 45)


# ========================================
# 2. SENTIMENT FUNCTION
# ========================================

def get_sentiment(review):
    polarity = TextBlob(review).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


# ========================================
# 3. APPLY SENTIMENT ANALYSIS
# ========================================

df["sentiment"] = df["review"].apply(get_sentiment)


# ========================================
# 4. DISPLAY RESULTS
# ========================================

print("\n🔹 Review Sentiment:")
print(df[["rating", "review", "sentiment"]].to_string(index=False))


# ========================================
# 5. SENTIMENT DISTRIBUTION
# ========================================

sentiment_counts = df["sentiment"].value_counts()

print("\n🔹 Sentiment Distribution:")

for sentiment, count in sentiment_counts.items():
    print(f"{sentiment}: {count}")


# ========================================
# 6. SAVE RESULTS
# ========================================

df.to_csv(
    "data/processed/sentiment_reviews.csv",
    index=False
)

print("\n✅ Sentiment analysis completed!")
print("📁 Saved: data/processed/sentiment_reviews.csv")