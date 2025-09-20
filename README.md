# 🎥 IMDb India Movie Prediction and Dashboard

This project analyzes and visualizes Indian movie data from IMDb using a machine learning model and an interactive dashboard. It is built using **pandas**, **seaborn**, **Plotly**, **Dash**, and **CatBoost**.

🗂️ **Dataset Source**: [IMDb India Movies - Kaggle Dataset](https://www.kaggle.com/datasets/adrianmcmahon/imdb-india-movies)

---

## 🔍 Project Overview

### 1️⃣ Movie Rating Prediction (`movies.ipynb`)
- Performs **exploratory data analysis (EDA)** on features like:
  - Release Year
  - Duration
  - IMDb Rating
  - Top Directors
- Trains a **CatBoost Regression Model** to predict IMDb ratings using:
  - Title
  - Genre
  - Duration
  - Director
  - Cast
- Visualizes feature importance and prediction results.

### 2️⃣ Dashboard App (`dashboard.py`)
- Interactive web-based dashboard using **Dash + Plotly**
- Features:
  - Dropdown filter for Genre
  - Dynamic histogram of number of movies per year
  - Responsive design

---


