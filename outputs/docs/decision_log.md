# Setup
While researching, I came across a file structure I decided to use for this project:
- Use directories for datasets, notebooks, outputs, and a src folder for reusable modules.
- Create a `config.py` to manage paths and global variables.
- Install src as an editable packege to enable module imports within notebooks.

# Data Validation

## Null Values
- An early check of the dataset showed that the _categories_ and _genres_ column had NaN values. I decided to drop those rows.
- `Null` values are a negligible amount compared with the rest of the dataset. However, I decided to drop only the rows where _genres_ and _categories_ are null to keep as most information as possible.
- Rows where _developer_ and _publisher_ are null were replaced with `Unknow`.

## Column Validation

**Text cleanup**
- _name_: Trim whitespace. The games have a unique ID (there's no duplication), so I don't need to worry about games with the same name, I'll use the names just for visualizations.
- _developer_: Trim whitespace. Keep names for visualizations.
- _publisher_: Trim whitespace. Keep names for visualizations.

**Range / value validation**
- *release_year*: Validate all games are from 2021 to 2025.
- *release_date*: Validate all games are from 2021 to 2025 and drop rows where date is not specified.
- _price_: Ensure price values are non-negative.
- _recommendations_: Ensure price values are non-negative.

**Deduplication**
- _genres_ and _categories_: Deduplicate values.

## Limitations
Due to the nature of the dataset, I couldn't perform a comparison beetween Deluxe Editions and Remakes to it's original game. So I decided not to infer a Deluxe or Remake game using their names.

## Lessons Learned
- Utilized `uint8` to represent binary values, significantly reducing the memory footprint compared to `int64`.
- Using `Parquet files` preserves schema and dtypes, so I don't need to specify `uint8` and datetime types on reading.

## Next Steps
I can use a `One-Hot-Encoding` to parse all genres and categories to facilitate subsequent analysis.

# Exploratory Data Analysis
Decided to split the analysis into univariate and multivariate sections. Also, answer example research questions found on the dataset page: 
- Q1: How has the market share of "Indie" games changed from 2021 to 2025? 
- Q2: Does price truly determine a game's popularity? 
- Q3: Which genres are growing the fastest in 2025? 
- Q4: Which months have the highest number of game releases?

## Univariate Analysis
In addition to analyzing each column, I performed the following analysis in order to find insights and answer research questions:
- Months with the most game releases across years (Q4).
- Most popular _genres_/_categories_ and _genre_/_category_ combinations, to identify trends (Q3 and Q1).
- Most popular game prices (Q2). 
- Number of Free to Play and paid games (Q2).
- Top developers and publishers.
- Distribution of Free to Play and paid games' popularity (Q2).
- Distribution of Free to Play and paid games' popularity just for games with a certain amount of recommendations (Q2).

## Multivariate Analysis
- Years with the most game releases over time (Q1).
- Median price over time across years (Q2).
- Statistics comparing pandemic and non-pandemic releases.

## Lessons Learned
- Generating a frequency of frequencies could be seen as a redundant process, but it is useful to help understand how common a given __frequency__ is.
- Columns like _price_ and _recommendations_ have very large outliers, which are still useful for analysis because they are not mistakes, they are real data.

## Next Steps
Using `log1p` would help mitigate the impact of outliers, plus a `StandardScaler` to keep data on the same scale.

# Feature Engineering
The data has a particular property: video games are multi-categorical in terms of genres and categories. This property is the reason why it is hard to deal with class imbalance—a genre like _indie_ appears in 70% of the games, so if I drop games with low-frequency genres or categories, I will also drop games that are _indie_ or belong to other common genres and categories.
In order to avoid this problem, I decided to keep only the most common genres and categories.

## Based on the EDA Findings
- Select relevant numeric columns (_price_ and _recommendations_) to identify clusters using an unsupervised model.
- *release_date* was deemed irrelevant for video game classification.
- *release_year* was excluded to prevent cluster bias (the transformed year representations would not vary enough between clusters).
- Generate one dataset with `One-Hot-Encoding` and another with `Inverse Document Frequency` for the most relevant, high-frequency genres and categories, to convert them into numeric features.
- Apply `log1p` to mitigate the influence of outliers on _price_ and _recommendations_.
- Use the `StandardScaler` function to scale the `log1p` columns. This prevents high-scale features like _price_ from dominating the variance of other numerical variables (such as _recommendations_ and `log1p` columns) due to scale differences, ensuring balanced feature weights for optimal `PCA` visualization and model performance.

## Data Type Optimization
Transform numeric columns to `int8` and `float32` as a best practice to reduce training memory footprint and improve performance.

# Model Training
I decided to compare two approaches in order to determine which one is capable of generating more predictable clusters. Going forward, I will refer to the dataset that uses `One-Hot Encoding` as OHE data, and the dataset that uses `Inverse Document Frequency` as weighted data.

## Weighted Data
- Use the `IDF` (Inverse Document Frequency) dataset to assign a weight to every genre and category, so the most common ones get a lower weight and the less common ones have more influence. With this approach, I tried to generate significant differentiation among clusters by letting less common features have more influence on each cluster.
- Use `PCA` to visualize the data.
- Use the default `KMeans` (Euclidean distance) model to generate clusters. The idea is to let less common genres and categories act as a "bias" for the clusters.
- Test the `Elbow Method` and `Silhouette Score` to decide which number of clusters produces the most distinguishable clusters.

## OHE Data
- Use the `One-Hot Encoded` dataset to generate boolean columns for genres and categories. In theory, this is the "most correct" way to manage this kind of data.
- Use `FAMD` (Factor Analysis of Mixed Data) to visualize the data, since it can handle both categorical and numerical features.
- Use the default `KPrototypes` model to generate clusters. The idea is to test the most correct methodology for this data. This method combines the `KMeans` and `KModes` methodologies, so both types of data contribute to the model as they are.
- Test the `Elbow Method` and `Silhouette Score` using Gower distance, since it can handle mixed categorical and numerical data, to decide which number of clusters produces the most distinguishable clusters. Because Gower distance requires computing a full distance matrix, it is computationally expensive, so I used a sample of the training data to calculate the Silhouette Score. I also implemented a custom dissimilarity function to perform this calculation.

## Lessons Learned
- The tested methods for defining an optimal K value are useful, but I also needed the resulting clusters to be interpretable and useful. So I chose the optimal K by comparing the results of each method alongside the interpretability of the models generated at different K values. I determined that 3 clusters was a feasible choice.
- Although both methods aim to generate distinguishable clusters, high-frequency genres and categories still influence the results. However, the goal is to test which method produces a dataset that is better suited for training a supervised model capable of correctly predicting new data.
- Clusters are still mainly determined by the _price_ and _recommendations_ values: when both are high, games tend to form one cluster; when both are low, they tend to form another; and when the values are inverse (one high, one low), they tend to form a third cluster. Both methods share this pattern.
- The weighted data produces interesting results, but it is hard to define labels for each cluster—for example, how do I label a cluster that has more _action_ and less _single-player_ than another? This would be much easier on a balanced dataset, but the nature of the data doesn't allow that kind of processing, since reducing the number of games with a specific genre also reduces the count of other genres as a side effect.

# Model Evaluation
The intention of this training is to generate a supervised model capable of labeling new, unseen data. Keeping that in mind, I made the following decisions:

## Model Selection
- Use a model capable of learning the boundaries of the previous clustering, so I decided to use Random Forest, which can meet this requirement.
- Train a model for each clustering method, resulting in two Random Forest models.

## Evaluation Strategy
- Evaluate the training set against its respective training labels. The score should be high, since the models are learning directly from the previous clustering.
- Evaluate the resulting models on test data. Scores might be high if the data shows the same patterns across the five years spanned by the original dataset. I used `KFold` to evaluate and average the model's performance across all the test data.

## Robustness Testing
Add noise to the test data and compare predictions on the original test set versus the noisy test set.