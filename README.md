# 💰 Budget Guard

Budget Guard is a simple Python project that analyzes personal expenses using data visualization.

## 📊 Features

- Reads expense data from CSV file
- Calculates total spending by category
- Identifies highest spending category
- Generates visual insights:
  - Bar Chart (Total Spending by Category)
  - Pie Chart (Spending Distribution)

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib

## 📁 Project Structure

budget_guard/
│
├── app.py
├── expenses.csv
├── chart.png
├── pie_chart.png
└── README.md

## 📈 Sample Outputs

### Bar Chart
![Bar Chart](chart.png)

### Pie Chart
![Pie Chart](pie_chart.png)

## 📌 Insights

- Bills account for the majority of expenses (~57%)
- Groceries are the second largest category (~34%)
- Entertainment and Transport have minimal impact

## 🚀 How to Run

```bash
pip3 install pandas matplotlib
python3 app.py