
import pandas as pd
import numpy as np

# Step 1: Create a list of 20 crops
crops = [
    "Wheat", "Rice", "Maize", "Mustard", "Barley",
    "Sugarcane", "Cotton", "Soybean", "Groundnut", "Potato",
    "Tomato", "Onion", "Gram", "Peas", "Millet",
    "Sorghum", "Lentil", "Chickpea", "Sunflower", "Jute"
]

# Step 2: Create the DataFrame
df = pd.DataFrame({
    "Crop": crops
})

# Step 3: Add agriculture data
df["Area_Hectares"] = np.random.randint(100, 1000, size=len(df))
df["Production_Tons"] = np.random.randint(200, 5000, size=len(df))
df["Rainfall_mm"] = np.random.randint(400, 1200, size=len(df))
df["Fertilizer_Kg"] = np.random.randint(50, 500, size=len(df))
df["Cost_Rs"] = np.random.randint(10000, 100000, size=len(df))
df["Sales_Rs"] = np.random.randint(20000, 150000, size=len(df))

# Step 4: Display results
print(df.head())
print("Dataset shape:", df.shape)

print(df.to_string(index=False))
print(df.columns)


# Step 1: Calculate crop yield per hectare
df["Yield_Tons_Per_Hectare"] = (
    df["Production_Tons"] / df["Area_Hectares"]
)

# Step 2: Calculate profit or loss
df["Profit_Rs"] = df["Sales_Rs"] - df["Cost_Rs"]

# Step 3: Identify profit or loss using if-like logic
df["Status"] = np.where(
    df["Profit_Rs"] >= 0,
    "Profit",
    "Loss"
)

# Step 4: Display the result
print(df[[
    "Crop",
    "Production_Tons",
    "Area_Hectares",
    "Yield_Tons_Per_Hectare",
    "Profit_Rs",
    "Status"
]].to_string(index=False))

# Filter crops that are making a profit
profitable_crops = df[df["Profit_Rs"] > 0]

print("Profitable Crops:")
print(profitable_crops[["Crop", "Profit_Rs"]].to_string(index=False))

print("Total profitable crops:", len(profitable_crops))

# Sort crops by profit from highest to lowest
top_crops = df.sort_values(
    by="Profit_Rs",
    ascending=False
)

print("Top 5 Profitable Crops:")
print(top_crops[["Crop", "Profit_Rs"]].head(5).to_string(index=False))

lowest_crops = df.sort_values(
    by="Profit_Rs",
    ascending=True
)

print("Lowest 5 Profit Crops:")
print(
    lowest_crops[["Crop", "Profit_Rs"]]
    .head(5)
    .to_string(index=False)
)

average_production = df["Production_Tons"].mean()

print("Average Crop Production:", round(average_production, 2), "tons")

# Step 1: Average production
average_production = df["Production_Tons"].mean()
print("Average Production:", round(average_production, 2), "tons")

# Step 2: Highest production
highest_production = df["Production_Tons"].max()
print("Highest Production:", highest_production, "tons")

# Step 3: Lowest production
lowest_production = df["Production_Tons"].min()
print("Lowest Production:", lowest_production, "tons")

# Step 4: Total production
total_production = df["Production_Tons"].sum()
print("Total Production:", total_production, "tons")

# Step 5: Count profitable crops
profit_count = (df["Profit_Rs"] > 0).sum()
print("Profitable Crops:", profit_count)

# Step 6: Count loss-making crops
loss_count = (df["Profit_Rs"] < 0).sum()
print("Loss-making Crops:", loss_count)

top_production = df.sort_values(
    by="Production_Tons",
    ascending=False
)

print("\nTop 5 Crops by Production:")

print(
    top_production[
        ["Crop", "Area_Hectares", "Production_Tons"]
    ].head(5).to_string(index=False)
)

# Assign categories to crops
category_map = {
    "Wheat": "Cereal",
    "Rice": "Cereal",
    "Maize": "Cereal",
    "Mustard": "Oilseed",
    "Barley": "Cereal",
    "Sugarcane": "Commercial",
    "Cotton": "Commercial",
    "Soybean": "Oilseed",
    "Groundnut": "Oilseed",
    "Potato": "Vegetable",
    "Tomato": "Vegetable",
    "Onion": "Vegetable",
    "Gram": "Pulse",
    "Peas": "Pulse",
    "Millet": "Cereal",
    "Sorghum": "Cereal",
    "Lentil": "Pulse",
    "Chickpea": "Pulse",
    "Sunflower": "Oilseed",
    "Jute": "Commercial"
}

df["Category"] = df["Crop"].map(category_map)

print(df[["Crop", "Category"]].to_string(index=False))

category_production = df.groupby("Category")["Production_Tons"].sum()

print("\nCategory-wise Total Production:")
print(category_production)
import matplotlib.pyplot as plt

top_5 = df.sort_values(
    by="Production_Tons",
    ascending=False
).head(5)

plt.bar(top_5["Crop"], top_5["Production_Tons"])
plt.title("Top 5 Crops by Production")
plt.xlabel("Crop")
plt.ylabel("Production (Tons)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(
    data=top_5,
    x="Crop",
    y="Production_Tons"
)

plt.title("Top 5 Crops by Production - Seaborn")
plt.xlabel("Crop")
plt.ylabel("Production (Tons)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
df["Production_Category"] = np.where(
    df["Production_Tons"] >= 2500,
    "High Production",
    "Low Production"
)

print(df[["Crop", "Production_Tons", "Production_Category"]].to_string(index=False))
df["Production_Level"] = np.where(
    df["Production_Tons"] >= 3500,
    "High",
    np.where(
        df["Production_Tons"] >= 2000,
        "Medium",
        "Low"
    )
)

print(
    df[["Crop", "Production_Tons", "Production_Level"]]
    .to_string(index=False)
)

production_count = df["Production_Level"].value_counts()

print("Crop Count by Production Level:")
print(production_count)

plt.show()
plt.savefig("top_5_crops_seaborn.png", dpi=300, bbox_inches="tight")

top5 = df.nlargest(5, "Production_Tons")

plt.figure(figsize=(10, 6))
plt.bar(top5["Crop"], top5["Production_Tons"], color="green")
plt.title("Top 5 Crops by Production")
plt.xlabel("Crop")
plt.ylabel("Production (Tons)")
plt.savefig("graphs/top_5_crops_matplotlib.png", dpi=300, bbox_inches="tight", facecolor="white")
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(data=top5, x="Crop", y="Production_Tons")
plt.title("Top 5 Crops by Production")
plt.savefig("graphs/top_5_crops_seaborn.png", dpi=300, bbox_inches="tight", facecolor="white")
plt.show()