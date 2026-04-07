# Setup
- Standard project structure with directories for datasets, notebooks, outputs, and a src folder for reusable modules..
- Create a config.py to manage paths and global variables.
- Install src as an editable packege to enable module imports within notebooks.
## Lessons Learned
I adopted this structure as a standard for better project organization, discovered during research.

# Data Validation
## Null values 
- Null values are a negligible amount compared with the rest of the dataset. However, I decided to drop only the rows where 'genres' and 'categories' are null to keep as most information as possible.
- Rows where 'developer' and 'publisher' are null were replaced with 'Unknow'.
- An early check of the dataset showed that the 'categories' and 'genres' column had NaN values. I decided to drop those rows.
## Colum Validation 
- 'name': Trim whitespace. The games have a unique ID, so I don't need to worry about games with the same name, I'll use the names just for visualizations.
- 'release_year': Validate all games are from 2021 to 2025.
- 'release_date': Validate all games are from 2021 to 2025 and manage rows where date is not specified.
- 'genres' and 'categories': Deduplicate values.
- 'price': Ensure price values are non-negative.
- 'recommendations': Ensure price values are non-negative.
- 'developer': Trim whitespace. Keep names for visualizations.
- 'publisher': Trim whitespace. Keep names for visualizations.
## Limitations
- Due to the nature of the dataset, I couldn't perform a comparison beetween Deluxe Editions and Remakes to it's original game. So I decided not to infer a Deluxe or Remake game using their names.
## Lessons Learned
- Sparse columns reduce memory usage by storing only non-zero values, something useful when training models with a lot of data. 
- Utilized uint8 to represent binary values, significantly reducing the memory footprint compared to int64.
- Using Parquet files preserves schema and dtypes, so I don't need to specify uint8 and datetime types on reading.
- I can use a One-Hot-Encoding to parse all genres and categories to facilitate subsequent analysis.

# Exploratory Data Analysis
- Learned about sparse columns and how they are useful to save memory storing only non-zero values. Additionally, used uint8 to represent the 1's in a smaller format than int64.
