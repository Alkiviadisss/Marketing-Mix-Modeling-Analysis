#  Advertising Channel Analysis

A data-driven analysis of advertising spend across **TV**, **Radio**, and **Newspaper** channels, using linear regression to model the relationship between ad spend and sales performance.

---

##  Project Structure

```
├── Analysis_Script.py        # Main analysis script
├── advertising.csv           # Dataset (200 observations)
└── README.md                 # This file
```

---

##  Dependencies

```bash
pip install pandas numpy matplotlib scikit-learn
```

---

##  Usage

Run the script and follow the interactive prompts:

```bash
python Analysis_Script.py
```

The script walks through four stages, each triggered by a `Y/N` input:

| Prompt | What it does |
|--------|-------------|
| `Print Data Cleaning Results?` | Shows head, null checks, descriptive stats, and total spend |
| `Print Plots?` | Bar chart of total spend per channel |
| `Print Correlations & Heatmap?` | Correlation matrix + heatmap |
| `Print Regression Model & Correlations?` | Linear regression (TV → Sales), R, R², scatter plot |

---

##  Key Results

### 1. Return on Ad Spend (ROAS)

| Channel | ROAS | Units per $1,000 | Risk |
|---------|------|------------------|------|
| TV | 0.091 | ~91 units | Low Risk / High Stability |
| Radio | 0.544 | ~544 units | Low Risk / High Stability |
| Newspaper | 0.237 | ~236 units | High Risk / Irrelevant |

> **Radio delivers the highest return** per dollar invested. TV provides the strongest sales correlation and stability. Newspaper shows the weakest link to sales outcomes.

### 2. Linear Regression — TV vs Sales

- **Model:** `Sales = f(TV spend)`
- **R²:** Indicates a strong fit between TV spend and sales
- **Correlation (R ≈ 0.78):** Strong positive relationship

### 3. Model Accuracy

| Metric | Value |
|--------|-------|
| MAE | `1.8305872641932412` |
| Total Units | `15,130` |
| Avg. Deviation | ~1.83 units |

The model deviates by an average of **1.83 units** out of 15,130 total — an error rate of roughly **0.012%**, confirming high predictive accuracy.

---

##  Strategic Recommendations

1. **Prioritize Radio** — highest ROAS (0.544), low risk, strong ROI
2. **Maintain TV** — strongest sales correlation, ideal for volume and brand stability
3. **Reassess Newspaper** — weakest correlation, highest risk; consider reallocating budget

---

##  Presentation

A full PowerPoint presentation (`Advertising_Channel_Analysis.pptx`) summarizing all findings is included, covering:

- Executive Summary with KPI cards
- ROAS comparison chart
- Channel deep dive
- Strategic recommendations
- Model accuracy (MAE)
- Conclusion
