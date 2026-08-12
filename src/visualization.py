import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/processed/cleaned_reviews.csv")

# Count each rating
rating_counts = df["rating"].value_counts().sort_index()

# Create bar chart
plt.figure(figsize=(8, 5))

plt.bar(
    rating_counts.index,
    rating_counts.values
)

plt.title("Mobile App Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Reviews")

plt.xticks([1, 2, 3, 4, 5])

# Save chart
plt.savefig("images/rating_distribution.png")

# Display chart
plt.show()