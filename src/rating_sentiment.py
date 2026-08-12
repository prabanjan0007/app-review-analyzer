import pandas as pd

# Load sentiment data
df = pd.read_csv("data/processed/sentiment_reviews.csv")

print("⭐ RATING vs 🧠 SENTIMENT")
print("=" * 50)

# Create rating-based sentiment
def rating_sentiment(rating):
    if rating >= 4:
        return "Positive"
    elif rating <= 2:
        return "Negative"
    else:
        return "Neutral"


df["rating_sentiment"] = df["rating"].apply(rating_sentiment)

# Display comparison
print("\nReview comparison:")
print(
    df[
        ["rating", "review", "rating_sentiment", "sentiment"]
    ].to_string(index=False)
)

# Find mismatches
mismatches = df[
    df["rating_sentiment"] != df["sentiment"]
]

print("\n⚠️ Sentiment mismatches:")
print(len(mismatches))

print("\nMismatch reviews:")

if len(mismatches) > 0:
    print(
        mismatches[
            ["rating", "review", "rating_sentiment", "sentiment"]
        ].to_string(index=False)
    )
else:
    print("No mismatches found.")

print("\n✅ Rating vs sentiment analysis completed!")