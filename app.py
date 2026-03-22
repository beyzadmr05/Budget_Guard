import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("expenses.csv")

print("Kategori ve Amount:")
print(df[["category", "amount"]])

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

category_totals.plot(kind="bar")

plt.title("Kategoriye Gore Toplam Harcama")
plt.xlabel("Kategori")
plt.ylabel("Toplam Tutar")

plt.savefig("chart.png")

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