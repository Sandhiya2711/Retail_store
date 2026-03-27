import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r"c:\Users\Ganesh\Downloads\retail_store.csv")
df["Revenue"] = df["Quantity"] * df["Unit_Price"]
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month
product_sales = df.groupby("Product_ID")["Revenue"].sum()
monthly = df.groupby("Month")["Revenue"].sum()
corr = df[["Quantity", "Unit_Price", "Revenue"]].corr()
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

axs[0, 0].bar(product_sales.index, product_sales.values)
axs[0, 0].set_title("Product Sales")

axs[0, 1].plot(monthly.index, monthly.values, marker='o')
axs[0, 1].set_title("Monthly Trend")

axs[1, 0].pie(product_sales.values, labels=product_sales.index, autopct='%1.1f%%')
axs[1, 0].set_title("Product Share")
cax = axs[1, 1].imshow(corr, cmap="viridis")
fig.colorbar(cax, ax=axs[1, 1])
axs[1, 1].set_xticks(range(len(corr.columns)))
axs[1, 1].set_yticks(range(len(corr.columns)))
axs[1, 1].set_xticklabels(corr.columns)
axs[1, 1].set_yticklabels(corr.columns)

for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        axs[1, 1].text(j, i, f"{corr.iloc[i, j]:.2f}",
                       ha="center", va="center", color="white")

axs[1, 1].set_title("Heatmap")

plt.tight_layout()
plt.show()
