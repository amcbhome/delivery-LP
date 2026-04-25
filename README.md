# 🚚 Logistics Route Optimizer: A Prescriptive Analytics Case Study

This project is a Python-based implementation of a **Transportation Optimization Problem**, designed to solve complex logistics challenges through mathematical modeling. 

The logic and business scenario for this project are inspired by the **ACCA (Association of Chartered Certified Accountants)** technical article on [Big Data and Business Analytics](https://www.accaglobal.com/uk/en/student/exam-support-resources/professional-exams-study-resources/strategic-business-leader/technical-articles/big-data-sbl.html).

---

## 🧠 Prescriptive Analytics in Action

While descriptive analytics explains *what happened* and predictive analytics forecasts *what might happen*, this tool performs **Prescriptive Analytics**. It doesn't just present data; it prescribes the **optimal course of action**.

By evaluating the trade-offs between depot supply, store capacity, and transport costs, the model provides a specific shipping schedule that yields the absolute minimum cost, helping management make data-driven decisions that are mathematically guaranteed to be the most efficient.



---

## 📖 Project Overview

The application optimizes the delivery of **6,850 units** of inventory from three regional depots to three retail locations.

### The Problem
* **Source Context:** Derived from the ACCA Strategic Business Leader (SBL) syllabus regarding resource optimization and big data.
* **Depots:** 3 supply locations with fixed inventory levels.
* **Stores:** 3 retail locations with maximum receiving capacities.
* **Goal:** Minimize total shipping expenditure while ensuring 100% of depot inventory is distributed without exceeding store limits.



---

## 🛠️ Technical Stack

* **Optimization Engine:** `scipy.optimize.linprog` (using the HiGHS solver).
* **User Interface:** `Streamlit` for a real-time, interactive dashboard.
* **Data Handling:** `NumPy` and `Pandas` for matrix calculations and reporting.

## 📊 Mathematical Objective

The solver minimizes the cost function:

$$Z = \sum (x_{ij} \times D_{ij} \times P)$$

**Where:**
* $x$ = Units shipped per route.
* $D$ = Distance between Depot $i$ and Store $j$.
* $P$ = Price per unit per mile.

---

## 🚀 Deployment & Usage

The application is designed for hosting via **Streamlit Community Cloud**. It allows users to adjust supply levels, store capacities, and unit costs dynamically to see how the "prescription" changes in real-time.

### To run locally:
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/amcbhome/your-repo-name.git](https://github.com/amcbhome/your-repo-name.git)
