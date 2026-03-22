import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("expenses.csv")
df["date"] = pd.to_datetime(df["date"])
ym = df["date"].dt.to_period("M")

print("Kategori ve Amount:")
print(df[["category", "amount"]])

monthly_totals = df.groupby(ym)["amount"].sum()

print("\nAylık Harcama Özeti (Toplam):")
print(monthly_totals.to_string())

print("\nAylık Harcama Özeti (Kategoriye Göre):")
monthly_by_category = df.pivot_table(
    index=ym,
    columns="category",
    values="amount",
    aggfunc="sum",
    fill_value=0,
)
print(monthly_by_category.to_string())

print("\nTransport Toplamı:")
transport_total = df[df["category"] == "Transport"]["amount"].sum()
print(transport_total)

print("\nKategoriye Göre Toplam:")
category_totals = df.groupby("category")["amount"].sum()
print(category_totals.to_string())

print("\nEn fazla harcama yapılan kategori:")
print(category_totals.idxmax())

print("\nEn yüksek harcama miktarı:")
print(category_totals.max())

print("\nGrafik oluşturuluyor...")

plt.figure(figsize=(10, 6))

category_totals.plot(
    kind="bar",
    edgecolor="black"
)

plt.title("Kategoriye Gore Toplam Harcama", fontsize=14, fontweight="bold")
plt.xlabel("Kategori", fontsize=12)
plt.ylabel("Toplam Tutar", fontsize=12)

plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()

plt.savefig("chart.png")
plt.close()

print("\nPie chart oluşturuluyor...")

plt.figure(figsize=(8, 8))

category_totals.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Kategori Dagilimi")
plt.ylabel("")

plt.savefig("pie_chart.png")
plt.close()

print("\nAylık line chart oluşturuluyor...")

monthly_plot = monthly_by_category.copy()
monthly_plot.index = monthly_plot.index.astype(str)

plt.figure(figsize=(10, 6))

monthly_plot.plot(kind="line", marker="o", linewidth=2)

plt.title("Aylık Harcama (Kategoriye Göre)", fontsize=14, fontweight="bold")
plt.xlabel("Ay", fontsize=12)
plt.ylabel("Tutar", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.legend(title="Kategori", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()

plt.savefig("monthly_line.png", bbox_inches="tight")
plt.close()
