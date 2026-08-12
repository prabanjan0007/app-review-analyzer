import pandas as pd
import matplotlib.pyplot as plt

# ========================================
# LOAD DATA
# ========================================

complaints = pd.read_csv(
    "data/processed/common_complaints.csv"
)

positive = pd.read_csv(
    "data/processed/common_positive_feedback.csv"
)


# ========================================
# COMMON COMPLAINTS
# ========================================

plt.figure(figsize=(9, 5))

plt.barh(
    complaints["keyword"],
    complaints["count"]
)

plt.title("Common App Complaints")
plt.xlabel("Number of Mentions")
plt.ylabel("Complaint Keyword")

plt.tight_layout()

plt.savefig(
    "images/common_complaints.png",
    bbox_inches="tight"
)

plt.close()


# ========================================
# POSITIVE FEEDBACK
# ========================================

plt.figure(figsize=(9, 5))

plt.barh(
    positive["keyword"],
    positive["count"]
)

plt.title("Common Positive Feedback")
plt.xlabel("Number of Mentions")
plt.ylabel("Positive Keyword")

plt.tight_layout()

plt.savefig(
    "images/common_positive_feedback.png",
    bbox_inches="tight"
)

plt.close()


# ========================================
# COMPLETION
# ========================================

print("========================================")
print("✅ FEEDBACK VISUALIZATIONS CREATED")
print("========================================")

print("📁 images/common_complaints.png")
print("📁 images/common_positive_feedback.png")