import pandas as pd
import matplotlib.pyplot as plt

# ========================================
# 1. LOAD SENTIMENT DATA
# ========================================

df = pd.read_csv("data/processed/sentiment_reviews.csv")

# ========================================
# 2. COUNT SENTIMENTS
# ========================================

sentiment_counts = df["sentiment"].value_counts()

print("🧠 SENTIMENT DISTRIBUTION")
print("=" * 40)

print(sentiment_counts)


# ========================================
# 3. CREATE BAR CHART
# ========================================

plt.figure(figsize=(8, 5))

plt.bar(
    sentiment_counts.index,
    sentiment_counts.values
)

plt.title("Mobile App Review Sentiment")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

# ========================================
# 4. SAVE CHART
# ========================================

plt.savefig(
    "images/sentiment_distribution.png",
    bbox_inches="tight"
)

print("\n✅ Chart saved!")
print("📁 images/sentiment_distribution.png")

plt.show()