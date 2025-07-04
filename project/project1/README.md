# Project Summary

## Project-7: 📊 Financial KPI Analysis for a Startup

**Author:** Dimple Anjara  
**Duration:** 2 Weeks Internship Project  
**Tools Used:** Python, Excel, Power BI

---

## 🧠 Project Summary

This project simulates and analyzes financial data for a fictional startup over a period of 18 months. The objective is to track growth, spending efficiency, and customer value using key performance indicators (KPIs) such as:

- **Revenue**
- **Customer Acquisition Cost (CAC)**
- **Customer Lifetime Value (LTV)**
- **Burn Rate**
- **LTV:CAC Ratio**

An interactive dashboard was built in Power BI to visualize trends, compare performance across months, and support data-driven decision making.

---

## 📦 Dataset Overview

| Column | Description | Typical Use |
|--------------------------|--------------------------------------------------|-----------------------------|
| `Date` | Daily records from 1 Jan 2024 to 1 Jul 2025 | Time-series analysis |
| `Revenue` | Daily gross revenue (₹) | Trend & Run-Rate |
| `Marketing_Spend` | Daily marketing cost (₹) | CAC calculation |
| `Expenses` | Other operating expenses (₹) | Burn-Rate |
| `New_Customers` | New customers acquired that day | CAC denominator |
| `Retained_Customers` | Returning customers | LTV numerator |
| `Burn_Rate` | Expenses + Marketing – Revenue | Cash-flow health |
| `CAC` | Marketing / New_Customers | Acquisition efficiency |
| `Avg_Revenue_per_Customer` | Revenue / (All customers that day) | Basis for LTV |
| `LTV` | Avg Rev × 6-month lifetime assumption | Customer value |
| `LTV_CAC_Ratio` | LTV / CAC | Investment return gauge |
| `Run_Rate` | Revenue × 12 | Annualized revenue |

---

## 📁 Deliverables

| File | Description |
|------|-------------|
| `finance_data.xlsx`, `finance_data.csv` | Synthetic dataset with calculated KPIs |
| `Financial_KPI_Project_Report.pdf` | 2-page PDF report |
| `Financial_KPI_Startup.pbix` | Power BI dashboard file |
| `README.md` | Project summary (you’re reading it) |

---

## 📊 Dashboard Highlights (Power BI)

- **KPI Cards:** Total Revenue, Avg CAC, Avg LTV, Burn Rate  
- **Line Chart:** Revenue vs Total Spend  
- **Bar Chart:** Monthly LTV vs CAC  
- **Pie Chart:** Customer Composition (New vs Retained)  
- **Burn Rate Trend (Column Chart):** Profitable vs loss-making months  
- **Slicer:** `YearMonth` filter to explore by date

---

## 📈 Key Insights

- ✅ LTV:CAC ratio consistently stayed **above 3.0**
- ✅ Burn Rate turned **positive** in later months
- ✅ Retained customers formed a **significant share** of the user base
- ✅ Revenue growth aligned with reduced acquisition cost

---

## ✅ Conclusion

The startup displays **strong financial health** with sustainable unit economics. The combination of clean KPI design and effective Power BI visualizations demonstrates the power of data in evaluating real-world business performance.

---
