import pandas as pd
import re
from collections import Counter

# ========================================
# 1. LOAD SENTIMENT DATA
# ========================================

df = pd.read_csv("data/processed/sentiment_reviews.csv")

print("🔎 COMMON COMPLAINTS & POSITIVE FEEDBACK")
print("=" * 50)


# ========================================
# 2. STOP WORDS
# ========================================

stop_words = {
    "the", "and", "is", "a", "an", "to", "of", "in",
    "it", "this", "that", "for", "on", "with", "my",
    "very", "but", "i", "app", "application", "can",
    "be", "are", "was", "after", "too", "often",
    "has", "have", "its", "not", "or", "from",
    "as", "at", "up", "me"
}


# ========================================
# 3. FUNCTION TO EXTRACT WORDS
# ========================================

def get_words(text):
    text = text.lower()

    # Keep alphabetic words only
    words = re.findall(r"\b[a-z]+\b", text)

    # Remove common words
    words = [
        word for word in words
        if word not in stop_words and len(word) > 2
    ]

    return words


# ========================================
# 4. NEGATIVE REVIEWS
# ========================================

negative_reviews = df[df["sentiment"] == "Negative"]

negative_words = []

for review in negative_reviews["review"]:
    negative_words.extend(get_words(review))

negative_counts = Counter(negative_words)


print("\n🔴 COMMON COMPLAINT KEYWORDS")

for word, count in negative_counts.most_common(10):
    print(f"{word}: {count}")


# ========================================
# 5. POSITIVE REVIEWS
# ========================================

positive_reviews = df[df["sentiment"] == "Positive"]

positive_words = []

for review in positive_reviews["review"]:
    positive_words.extend(get_words(review))

positive_counts = Counter(positive_words)


print("\n🟢 COMMON POSITIVE FEEDBACK")

for word, count in positive_counts.most_common(10):
    print(f"{word}: {count}")


# ========================================
# 6. SAVE RESULTS
# ========================================

complaints = pd.DataFrame(
    negative_counts.most_common(10),
    columns=["keyword", "count"]
)

positive_feedback = pd.DataFrame(
    positive_counts.most_common(10),
    columns=["keyword", "count"]
)

complaints.to_csv(
    "data/processed/common_complaints.csv",
    index=False
)

positive_feedback.to_csv(
    "data/processed/common_positive_feedback.csv",
    index=False
)

print("\n✅ Analysis completed!")

print("\n📁 Files created:")
print("common_complaints.csv")
print("common_positive_feedback.csv")