import pandas as pd


df = pd.read_json("data/trends_2026-04-06.json")


df = df.drop_duplicates(subset="post_id")


df = df.dropna(subset=["post_id", "title", "score"])


df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].fillna(0).astype(int)


df = df[df["score"] >= 5]


df["title"] = df["title"].str.strip()



df.to_csv("data/trends_clean.csv", index=False)


print(f"Saved {len(df)} rows to data/trends_clean.csv")


print("\nStories per category:")
print(df["category"].value_counts())
