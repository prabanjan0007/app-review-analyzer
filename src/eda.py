import pandas as pd

# ========================================
# 1. LOAD CLEANED DATA
# ========================================

df = pd.read_csv("data/processed/cleaned_reviews.csv")

print("📊 MOBILE APP REVIEW ANALYSIS")
print("=" * 45)


# ========================================
# 2. TOTAL REVIEWS
# ========================================

total_reviews = len(df)

print("\n📌 Total Reviews:")
print(total_reviews)


# ========================================
# 3. AVERAGE RATING
# ========================================

average_rating = df["rating"].mean()

print("\n⭐ Average Rating:")
print(round(average_rating, 2))


# ========================================
# 4. MOST COMMON RATING
# ========================================

most_common_rating = df["rating"].mode()[0]

print("\n🏆 Most Common Rating:")
print(most_common_rating, "stars")


# ========================================
# 5. RATING DISTRIBUTION
# ========================================

rating_counts = df["rating"].value_counts().sort_index()

print("\n⭐ Rating Distribution:")

for rating, count in rating_counts.items():
    print(f"{rating} stars: {count} reviews")


# ========================================
# 6. POSITIVE REVIEWS
# ========================================

positive_reviews = df[df["rating"] >= 4]

positive_percentage = (
    len(positive_reviews) / total_reviews
) * 100

print("\n🟢 Positive Reviews:")
print(len(positive_reviews))

print("Positive Percentage:")
print(round(positive_percentage, 2), "%")


# ========================================
# 7. NEGATIVE REVIEWS
# ========================================

negative_reviews = df[df["rating"] <= 2]

negative_percentage = (
    len(negative_reviews) / total_reviews
) * 100

print("\n🔴 Negative Reviews:")
print(len(negative_reviews))

print("Negative Percentage:")
print(round(negative_percentage, 2), "%")


# ========================================
# 8. NEUTRAL REVIEWS
# ========================================

neutral_reviews = df[df["rating"] == 3]

neutral_percentage = (
    len(neutral_reviews) / total_reviews
) * 100

print("\n🟡 Neutral Reviews:")
print(len(neutral_reviews))

print("Neutral Percentage:")
print(round(neutral_percentage, 2), "%")


# ========================================
# 9. SUMMARY
# ========================================

print("\n" + "=" * 45)
print("📱 APP REVIEW SUMMARY")
print("=" * 45)

print(f"Total Reviews     : {total_reviews}")
print(f"Average Rating    : {average_rating:.2f} ⭐")
print(f"Positive Reviews  : {positive_percentage:.2f}%")
print(f"Neutral Reviews   : {neutral_percentage:.2f}%")
print(f"Negative Reviews  : {negative_percentage:.2f}%")

print("\n✅ EDA COMPLETED!")