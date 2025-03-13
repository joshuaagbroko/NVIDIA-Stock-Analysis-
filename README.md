# NVIDIA Stock Analysis & Benchmark Comparison
## 📌 Project Overview

This project analyzes NVIDIA's stock performance and compares it to the S&P 500 benchmark using R and Python (reticulate). The goal is to determine whether an equally weighted, long-only trading strategy based on NVIDIA's relative performance can outperform the S&P 500 index.

## 📊 Key Objectives

✔ Fetch stock data using Python (yfinance) and integrate with R using reticulate.
✔ Perform Exploratory Data Analysis (EDA) to understand stock trends, volatility, and returns.
✔ Calculate daily returns and compare NVIDIA to the S&P 500.
✔ Conduct a t-test to evaluate if NVIDIA significantly outperforms the index.
✔ Implement a simple trading strategy that invests in NVIDIA only when it beats the S&P 500.
✔ Compare cumulative returns and risk-adjusted performance (Sharpe Ratio).

## 📂 Project Structure

📁 Nvidia_vs_SP500_Analysis/
│── 📜 README.md           # Project Documentation  
│── 📜 stock_analysis.R    # Main R script for analysis  
│── 📜 fetch_data.py       # Python script to retrieve stock data (used in reticulate)   
│── 📜 renv.lock           # R package dependencies  

## 🛠️ Tools & Libraries Used
R Packages

    tidyverse → Data manipulation & visualization
    ggplot2 → Stock trend visualization
    lubridate → Date handling
    PerformanceAnalytics → Sharpe Ratio & performance metrics
    reticulate → Python integration in R

Python Libraries (Used via reticulate)

    yfinance → Fetching NVIDIA and S&P 500 stock data
    pandas → Data cleaning
    numpy → Financial calculations


# 📌 General Conclusion
This project set out to analyze NVIDIA's stock performance relative to the S&P 500 index and evaluate whether an equally weighted, long-only investment strategy in NVIDIA could outperform the benchmark.

Through exploratory data analysis (EDA), return calculations, and statistical testing (t-test), we found that:

1️⃣ NVIDIA consistently outperformed the S&P 500 in terms of average daily returns (1.34% vs. 0.0659%).
2️⃣ A trading strategy that invests in NVIDIA when it beats the S&P 500 achieved higher cumulative returns.
3️⃣ Risk-adjusted performance was superior, as reflected in the higher Sharpe Ratio (0.592 vs. 0.508).
4️⃣ However, the strategy exhibited higher volatility, meaning that while returns were higher, the fluctuations in price were more significant than those of the S&P 500.

## 📌 Final Takeaways

✅ Yes, NVIDIA outperformed the S&P 500, making it an attractive stock for active investment.
⚠️ Higher returns came with higher risk, requiring risk management strategies such as stop-losses or portfolio diversification.
📊 Future research could expand this approach to other stocks to assess whether NVIDIA’s outperformance is consistent or part of a larger market trend.

## 📌 Key Decision

💡 Based on these findings, an investor might choose to invest in NVIDIA only when it exhibits a strong performance trend relative to the S&P 500, rather than blindly holding it long-term.

## 📌 Future Improvements

🔹 Implement stop-loss & take-profit rules for better risk management.
🔹 Use rolling moving averages to refine entry points.
🔹 Expand the analysis to include other tech stocks (AMD, Intel, etc.).

## 📜 License

This project is released under the MIT License.


