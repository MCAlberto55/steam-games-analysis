# Steam Games Analysis
Trend analysis and success prediction for video games, based on the 2021–2025 Steam Games Dataset (65k+ entries).

## Motivation
- Apply the knowledge gained throughout my software engineering degree, along with data science courses and certifications.
- Demonstrate my understanding of the end-to-end data science process.
- Build a project portfolio to strengthen my professional profile.

## Methodology
1. Clean the data and perform exploratory data analysis.
2. Since this is an unlabeled dataset, build an unsupervised model to identify clusters.
3. Evaluate the model and use it to assign labels to the clusters, effectively labeling each row.
4. Train a supervised model using these labels, and use it to predict cluster assignments for new data.

## Research Questions

**Project questions:**
- What is the trend for genres and categories in late 2025?
- Does price truly determine a game's popularity?
- What are the primary differences between trends during and after the COVID-19 pandemic?
- Is it possible to determine whether a game will be successful?

**Dataset-defined questions** (from the dataset's page, addressed during EDA):
- How has the market share of "Indie" games changed from 2021 to 2025?
- Does price truly determine a game's popularity? *(overlaps with a project question above)*
- Which genres are growing the fastest in 2025?
- Which months have the highest number of game releases?

## Key Achievements
- Trained two clustering models using different approaches: one using `One-Hot Encoding` and another using `Inverse Document Frequency`.
- Models perform correctly even on new data, as tested by adding noise to the test data.
- Three clusters were determined during the clustering stage.
- Pre-COVID trends were maintained and became even more pronounced after the pandemic, alongside higher user participation in game page recommendations on Steam.

Detailed findings, decisions, and lessons learned throughout each stage of the project are documented in [`decision_log.md`](outputs/docs/decision_log.md).
Detailed results are documented in [`results.md`](outputs/docs/results.md).

## Project Structure
- `data`: Datasets generated during the project.
- `notebooks`: A notebook file for every data science stage.
- `outputs`: Contains docs, models, params, and plots generated during the project.
- `src/data`: Scripts that load, read, and process data.
- `src/utils`: Config- and model-related loaders and exporters.
- `src/visualization`: Scripts for custom plots, prints, and plot exports.