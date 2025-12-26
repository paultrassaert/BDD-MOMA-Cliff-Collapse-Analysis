# Statistical Analysis & Modeling of Cliff Collapses in Normandy 🌊📉

![Status](https://img.shields.io/badge/Status-Completed-success)
![Python](https://img.shields.io/badge/Python-Data_Processing-blue)
![R](https://img.shields.io/badge/R-Statistical_Modelling-blue)

> **Project Goal:** Understand and model the meteorological and marine factors triggering cliff collapses (rockfalls) along the Seine-Maritime coast using statistical learning.

---

## 📍 Context & Objectives

Cliff erosion in Normandy is a major risk for coastal management. [cite_start]Working with **Laboratoire LETG (CNRS)**, this project analyzes **693 recorded collapses** between 2000 and 2022[cite: 65].

**The Challenge:**
Identify which variables (rain, waves, tides, geology) best explain the frequency of collapses across:
1.  **Time:** Why do some periods have more collapses?
2.  [cite_start]**Space:** Why are some cliff sections (sub-cells) more vulnerable? [cite: 604-617]

![Study Area Map](images/map_study_area.png)
*(Figure: Map of the hydro-sedimentary sub-cells in Seine-Maritime - based on report p.3)*

---

## 🛠️ Methodology

We built a complete data pipeline from raw sources to predictive models:

| Step | Description | Tools |
| :--- | :--- | :--- |
| **1. Collection** | [cite_start]Aggregating data from SHOM (tides), Météo-France, CANDHIS (waves), and IGN. [cite: 197] | Python |
| **2. Processing** | [cite_start]Cleaning and computing **72 indicators** (e.g., Cumulative wave energy, Freeze-thaw cycles). [cite: 205] | Python (Pandas) |
| **3. Analysis** | [cite_start]Correlation matrices, Poisson regression, Negative Binomial, and CART Trees. [cite: 200] | R |
| **4. Validation** | [cite_start]Leave-One-Out Cross-Validation (LOOCV) due to small sample size. [cite: 828] | R |

---

## 📊 Key Visualizations & Analysis

### 1. Correlation Analysis (Temporal)
We identified strong correlations between collapse rates and storm-related indicators.

![Correlation Graph](images/correlation_plot.png)
[cite_start]*Strong positive correlation ($r \approx 0.8$) found with days of strong wind (>60 km/h) and cumulative wave energy[cite: 549, 562].*

### 2. Decision Trees (CART Method)
To understand threshold effects, we used Classification and Regression Trees.

![CART Tree](images/cart_tree_periodes.png)
[cite_start]*The model highlights that **cumulative rainfall** (> 3000mm) and **tidal range** are the primary splitters for high-risk periods[cite: 703].*

---

## 🏆 Results & Conclusions

Despite the challenge of a small dataset ($n=5$ periods, $n=6$ cells), we established robust findings:

### ✅ Temporal Drivers (When does it fall?)
The variation in collapses over time is driven by **hydro-meteorological forcing**:
* [cite_start]**Storms:** High winds (>60 km/h) and wave energy[cite: 583].
* [cite_start]**Rain & Tides:** Combination of heavy cumulative rainfall and high tidal coefficients[cite: 710].

### ✅ Spatial Drivers (Where does it fall?)
The spatial vulnerability is structural:
* [cite_start]**Retreat Rate:** The historical erosion rate is the #1 predictor[cite: 937].
* [cite_start]**Lithology:** Specific chalk layers (Campanian/Coniacian) are more sensitive[cite: 975].

### ✅ Model Performance
We tested LASSO, Poisson, and Composite models. [cite_start]The **Composite Model** (score-based) proved to be the most stable and accurate for prediction, avoiding the overfitting seen in complex models[cite: 902].

---

## 🔮 Perspectives

* [cite_start]**Seasonality:** Downscaling the analysis to a seasonal mesh to capture winter/summer variations[cite: 1061].
* [cite_start]**Advanced ML:** Testing Random Forest or XGBoost with a larger dataset[cite: 1041].
* [cite_start]**Lagged Features:** Investigating if rain/storms from the *previous* period influence the current one[cite: 1043].

---

## 📂 Project Structure

```text
├── data/               # Processed datasets (CSV/Excel)
├── python_scripts/     # ETL, Swell & Weather indicators calculation
├── r_scripts/          # Statistical models (Poisson, CART, LOOCV)
└── docs/               # Detailed documentation of the 72 indicators
