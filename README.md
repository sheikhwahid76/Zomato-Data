# Zomato Data Analysis

This repository contains a basic exploratory data analysis (EDA) project using a sample Zomato-style dataset. The dataset includes restaurant information such as name, location, rating, cost, and a cleaned "rate" column.

## 📁 Files

- Zomato data.csv: The dataset containing restaurant details.
- main.py (or the Python script you used): Script that performs data cleaning, visualization, and analysis.
- README.md: Project overview and usage guide.

## 📊 Dataset Columns

- Restaurant: Name of the restaurant.
- Location: Location of the restaurant.
- Rating: Raw rating (as a string, e.g., "4.5/5").
- Cost: Average cost for two.
- rate: Cleaned numeric rating extracted from the Rating column.

## 🔍 What the Code Does

1. Loads the dataset using pandas.
2. Cleans the `Rating` column by extracting the numerical rating into a new column called rate.
3. Displays basic info and previews the data.
4. Visualizes data using seaborn and matplotlib:
   - Count plot for restaurant locations.
   - Histogram for rating distribution.
   - Box plot of ratings by location.
   - Heatmap of online order availability by location (if available).
5. Finds the restaurant(s) with the highest rating.

## 📦 Requirements

Install required libraries with:

```bash
pip install pandas numpy matplotlib seaborn
