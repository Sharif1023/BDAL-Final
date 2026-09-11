import os
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS = os.path.join(ROOT, "results")
OUT = os.path.join(ROOT, "visualization")

os.makedirs(OUT, exist_ok=True)


# -------------------------------------------------
# Pig 1 - Top 5 Products by Number of Reviews
# -------------------------------------------------

products = []
counts = []

file1 = os.path.join(
    RESULTS,
    "pig",
    "pig1_top5_products.txt"
)

with open(file1, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("|")

        if len(parts) == 2:
            products.append(parts[0])
            counts.append(int(parts[1]))

plt.figure(figsize=(9, 5))
plt.bar(products, counts)
plt.title("Top 5 Amazon Products by Number of Reviews")
plt.xlabel("Product ID")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    os.path.join(OUT, "pig1_top5_products.png"),
    dpi=300
)

plt.close()


# -------------------------------------------------
# Pig 2 - Top 10 Most Helpful Reviews
# -------------------------------------------------

review_ids = []
helpful_votes = []

file2 = os.path.join(
    RESULTS,
    "pig",
    "pig2_top10_helpful_reviews.txt"
)

with open(file2, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("|")

        if len(parts) == 4:
            review_ids.append(parts[0])
            helpful_votes.append(int(parts[3]))

plt.figure(figsize=(10, 6))
plt.barh(review_ids[::-1], helpful_votes[::-1])
plt.title("Top 10 Most Helpful Amazon Reviews")
plt.xlabel("Helpful Votes")
plt.ylabel("Review ID")
plt.tight_layout()

plt.savefig(
    os.path.join(OUT, "pig2_top10_helpful_reviews.png"),
    dpi=300
)

plt.close()


# -------------------------------------------------
# Pig 3 - Top Helpful Reviews by Rating Score
# -------------------------------------------------

score_values = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
}

file3 = os.path.join(
    RESULTS,
    "pig",
    "pig3_top10_helpful_by_score.txt"
)

with open(file3, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("|")

        if len(parts) == 4:
            score = int(parts[2])
            helpful = int(parts[3])

            if score in score_values:
                score_values[score].append(helpful)

plt.figure(figsize=(9, 6))

for score, values in score_values.items():
    x = [score] * len(values)
    plt.scatter(x, values)

plt.title("Helpful Votes of Top 10 Reviews by Rating Score")
plt.xlabel("Rating Score")
plt.ylabel("Helpful Votes")
plt.xticks([1, 2, 3, 4, 5])
plt.tight_layout()

plt.savefig(
    os.path.join(OUT, "pig3_helpful_reviews_by_score.png"),
    dpi=300
)

plt.close()


# -------------------------------------------------
# Pig 4 - Top 10 Products by Helpful Votes
# -------------------------------------------------

product_ids = []
votes = []

file4 = os.path.join(
    RESULTS,
    "pig",
    "pig4_top10_products_helpful.txt"
)

with open(file4, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("|")

        if len(parts) == 2:
            product_ids.append(parts[0])
            votes.append(int(parts[1]))

plt.figure(figsize=(10, 6))
plt.barh(product_ids[::-1], votes[::-1])
plt.title("Top 10 Products by Total Helpful Votes")
plt.xlabel("Total Helpful Votes")
plt.ylabel("Product ID")
plt.tight_layout()

plt.savefig(
    os.path.join(OUT, "pig4_top10_products_helpful.png"),
    dpi=300
)

plt.close()


# -------------------------------------------------
# Pig 5 - Products by Helpful Votes for Each Score
# -------------------------------------------------

score_product_values = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
}

file5 = os.path.join(
    RESULTS,
    "pig",
    "pig5_top10_products_helpful_by_score.txt"
)

with open(file5, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("|")

        if len(parts) == 3:
            score = int(parts[0])
            votes = int(parts[2])

            if score in score_product_values:
                score_product_values[score].append(votes)

plt.figure(figsize=(9, 6))

for score, values in score_product_values.items():
    x = [score] * len(values)
    plt.scatter(x, values)

plt.title("Top Product Helpful Votes by Rating Score")
plt.xlabel("Rating Score")
plt.ylabel("Total Helpful Votes")
plt.xticks([1, 2, 3, 4, 5])
plt.tight_layout()

plt.savefig(
    os.path.join(
        OUT,
        "pig5_products_helpful_by_score.png"
    ),
    dpi=300
)

plt.close()


print("Visualization completed successfully.")
print()
print("Generated files:")
print("1. pig1_top5_products.png")
print("2. pig2_top10_helpful_reviews.png")
print("3. pig3_helpful_reviews_by_score.png")
print("4. pig4_top10_products_helpful.png")
print("5. pig5_products_helpful_by_score.png")