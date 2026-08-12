import pandas as pd

# ========================================
# 1. LOAD DATA
# ========================================

df = pd.read_csv("data/raw/reviews.csv")

print("📱 MOBILE APP REVIEW ANALYZER")
print("=" * 45)

print("\nOriginal dataset:")
print(df.head())

print("\nOriginal shape:", df.shape)


# ========================================
# 2. REMOVE DUPLICATES
# ========================================

df = df.drop_duplicates()

print("\nAfter removing duplicates:", df.shape)


# ========================================
# 3. REMOVE MISSING VALUES
# ========================================

df = df.dropna(subset=["rating", "review"])

print("After removing missing reviews:", df.shape)


# ========================================
# 4. CLEAN REVIEW TEXT
# ========================================

df["review"] = df["review"].str.strip()

print("\nReview text cleaned.")


# ========================================
# 5. KEEP ONLY VALID RATINGS
# ========================================

df = df[
    (df["rating"] >= 1) &
    (df["rating"] <= 5)
]

print("After checking ratings:", df.shape)


# ========================================
# 6. SAVE CLEANED DATA
# ========================================

df.to_csv(
    "data/processed/cleaned_reviews.csv",
    index=False
)

print("\n✅ Cleaned dataset saved!")
print("📁 data/processed/cleaned_reviews.csv")


# ========================================
# 7. FINAL DATA SUMMARY
# ========================================

print("\nFinal dataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nRating distribution:")
print(df["rating"].value_counts().sort_index())

print("\n🎉 DATA CLEANING COMPLETED!")