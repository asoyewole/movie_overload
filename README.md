# Movie Recommendation System

This repository contains the implementation of a cost-aware movie recommendation system that integrates production budgets into traditional collaborative filtering models. Built using the MovieLens 25M dataset and The Movie Database (TMDb) budget data, the project explores the impact of incorporating budget information into recommendation algorithms, with a focus on predictive accuracy and fairness across budget tiers. The system employs both Alternating Least Squares (ALS) and Neural Collaborative Filtering (NCF) models, implemented with Apache Spark and TensorFlow, respectively.  
  
## Table of Contents
Project Overview (#project-overview)
Features (#features)
Dataset (#dataset)
Requirements (#requirements)
Installation (#installation)
Project Structure (#project-structure)
Usage (#usage)
Methodology (#methodology)
Results (#results)
Fairness Analysis (#fairness-analysis)
Future Work (#future-work)
Contributing (#contributing)
License (#license)
Contact (#contact)

## Project Overview
The goal of this project is to enhance movie recommendation systems by incorporating production budgets as a feature, aiming to balance recommendation accuracy with fairness across low-, medium-, and high-budget films. The system processes large-scale data using Spark for scalability and employs advanced machine learning techniques to model user preferences. Exploratory Data Analysis (EDA) uncovers patterns in ratings and budgets, while fairness analysis ensures equitable representation of films across budget tiers.FeaturesData Integration: Combines MovieLens 25M ratings with TMDb budgets and IMDb metadata using Spark for efficient processing.
Exploratory Data Analysis (EDA): Analyzes distributions of ratings (mean: 3.54, right-skewed), budgets (mean: $20.5M, right-skewed), and release years (2000–2020, near-uniform).
Modeling: Implements budget-aware and baseline ALS (Spark MLlib) and NCF (TensorFlow) models.
Fairness Evaluation: Assesses diversity in top-10 recommendations across budget tiers (Low: ≤$1.3M, Medium: ≤$5.15M, High: >$5.15M).
Statistical Analysis: Uses paired t-tests to compare model performance (e.g., ALS vs. NCF: p=0.0000).
Visualizations: Generates plots for distributions, correlations, and fairness metrics using Matplotlib and Seaborn.

## Dataset
The project uses the following datasets:
MovieLens 25M: Contains 25,000,095 ratings from 330,975 users across 83,239 movies (ratings: 0.5–5.0). Available at MovieLens.
TMDb Budgets: Fetched via TMDb API for 85,305 movies, with 842 missing budgets (1.7%). Mean budget: $20.5M.
IMDb Title Basics: Provides metadata (title, genres, release year) for merging with MovieLens data.

## Requirements
Python 3.8+
Apache Spark 3.3.0+
TensorFlow 2.10+
Libraries: pandas, numpy, matplotlib, seaborn, scipy, requests, python-dotenv
Java 8+ (for Spark)
Hadoop 3.3.6 (for Windows compatibility)
TMDb API key (set in .env file)

## Installation 
### Clone the repository:bash

git clone https://github.com/asoyewole/movie_overload.git
cd movie_overload

### Set up a virtual environment:bash

python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

### Install dependencies:bash

pip install -r requirements.txt

HADOOP_HOME=C:\hadoop-3.3.6  # Windows only

### Download datasets: 

Download MovieLens 25M from here and extract to ml-25m/.
Download IMDb title basics from here and place in imdb/.
Budgets are fetched programatically via TMDb API.

## Project Structure

cost-aware-recommendation/
├── ml-25m/                    # MovieLens dataset
├── imdb/                      # IMDb dataset
├── eda_plots/                 # EDA visualizations and logs
├── preprocessed_ratings/       # Preprocessed ratings (Parquet)
├── preprocessed_movies/        # Preprocessed movies (Parquet)
├── als_model/                 # Saved ALS model
├── als_model_cv/              # Saved cross-validated ALS model
├── als_baseline_model/        # Saved baseline ALS model
├── ncf_model.h5               # Saved NCF model
├── ncf_baseline_model.h5      # Saved baseline NCF model
├── notebook1_eda.ipynb        # EDA and data preprocessing
├── notebook2_modeling.ipynb    # Model training and evaluation
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables
├── tmdb_budgets.csv           # TMDb budget data
├── *.pkl                      # User and movie mappings
├── *.txt                      # Evaluation results and logs
├── README.md                  # This file

## Usage
Run EDA :bash

jupyter notebook eda.ipynb

Loads and preprocesses data.
Performs EDA (distributions, correlations, genre trends).
Saves visualizations (eda_plots/).

Run Modeling and Evaluation (movie_modelling): bash

jupyter notebook movie_modelling.ipynb

Fetches TMDb budgets (if not pre-fetched).
Trains budget-aware and baseline ALS/NCF models.
Evaluates models (RMSE, Precision@10, Recall@10, NDCG@10).
Conducts statistical (t-tests) and fairness analysis.
Saves visualizations (rmse_comparison.png, diversity_comparison.png).

View Results:
Check eda_plots/ for histograms and scatter plots.
Review als_evaluation_results.txt and ncf_evaluation_results.txt for model performance.
See statistical_fairness_results.txt for t-tests and fairness metrics.

## Methodology
Data Preprocessing: 
Merged MovieLens, TMDb, and IMDb datasets using Spark.
Filtered movies (2000–2025), removed sparse ratings (<10 per movie).
Imputed missing budgets with genre-specific medians and normalized using log transformation.

EDA:
Analyzed rating distribution (mean: 3.54, Shapiro-Wilk: W=0.9294, p<0.05, not normal).
Examined budget distribution (mean: $20.5M, log-transformed W=0.8670, p<0.05, not normal).
Plotted genre trends and budget-rating correlation (0.09).

Modeling:
ALS: Matrix factorization with budget normalization (Spark MLlib, maxIter: [5, 10, 15], regParam: [0.01, 0.1, 0.5], 3-fold CV).
NCF: Neural embeddings with budget features (TensorFlow, 50-dimensional embeddings, 10 epochs).
Baseline models exclude budget features.

Evaluation
:Metrics: RMSE, Precision@10, Recall@10, NDCG@10.
Statistical tests: Paired t-tests (scipy.stats) to compare errors.
Fairness: Diversity across budget tiers (Low: ≤$1.3M, Medium: ≤$5.15M, High: >$5.15M).

## Results
Performance:Budget-aware ALS: RMSE 0.8027, Precision@10: 0.4434, Recall@10: 0.8339, NDCG@10: 0.8836.
Cross-validated ALS: RMSE 0.7987 (best), Precision@10: 0.4439, Recall@10: 0.8341.
Baseline ALS: RMSE 0.8181, Precision@10: 0.4994 (highest).
Budget-aware NCF: RMSE 0.8468, Precision@10: 0.4350, Recall@10: 0.8242.
Baseline NCF: RMSE 0.8459, Precision@10: 0.4364, Recall@10: 0.8253.

Statistical Significance:
ALS vs. NCF: t=4.9065, p=0.0000 (ALS outperforms).
ALS vs. Baseline: t=-0.1304, p=0.8963 (non-significant).
NCF vs. Baseline: t=1.6081, p=0.1081 (non-significant).

**Key Insight: Budgets have limited predictive power (correlation: 0.09).**


## Fairness Analysis
Budget-aware NCF showed a strong bias toward high-budget films (9 High in top-10 recommendations).
Baseline NCF was more balanced (3 High, 2 Low, 1 Medium).
ALS models showed moderate diversity (e.g., ALS: 1 High, 2 Medium).
Implication: Budget-aware models risk marginalizing low-budget films, necessitating fairness-aware algorithms like re-ranking.

## Future Work
Enhanced Data Collection: Integrate IMDbPro for missing budgets (842 films, 1.7%).
Fairness Algorithms: Implement re-ranking or adversarial training to promote low-budget films.
Extended Scope: Apply the framework to TV shows or music streaming.
Additional Features: Incorporate content-based features (e.g., cast, director) to improve accuracy.

Contributing 
Contributions are welcome! Please: Fork the repository.
Create a feature branch (git checkout -b feature/new-feature).
Commit changes (git commit -m "Add new feature").
Push to the branch (git push origin feature/new-feature).
Open a pull request with a detailed description.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or collaboration, reach out via:
LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/asoyewole/)
GitHub: https://github.com/asoyewole/





