### Project Summary: Netflix Titles Data Analysis & Cleaning
1. Data Loading & Initial Exploration
Imported Netflix titles dataset (netflix_titles.csv).

Inspected structure using .head(), .info(), .shape(), and .dtypes.

Identified missing values and calculated their percentage per column.

2. Data Cleaning & Preprocessing
Dropped unnecessary columns: show_id, cast, director, and description.

Handled missing values:

Replaced null values in country with the mode.

Removed rows with remaining nulls.

Replaced missing rating with mode and duration with 0.

Converted date_added to datetime format.

Extracted primary country from comma-separated lists (principal_country column).

Mapped Netflix ratings to age groups (e.g., “TV-MA” → “Adults”).

3. Feature Engineering
Created new column ages using a dictionary mapping.

For Movies, extracted numerical duration (in minutes) and analyzed it using .describe().

4. Inconsistency Handling (Before Merge)
Standardized column names and data types (title, release_year).

Normalized text: converted titles to lowercase, removed extra whitespace.

5. Merging Datasets
Merged original and cleaned datasets using title, type, and release_year.

Removed duplicate entries based on title.

6. Exploratory Insights
Counted content types (Movie, TV Show).

Descriptive statistics provided for movie durations (minute).

Cleaned and structured data saved to netflix_title_cleaned.csv.

### Insights:
Missing Data was significant in columns like director, cast, and country.

Movies dominate the dataset over TV Shows.

Adults are the primary target audience based on rating distribution.

Principal Country typically defaults to the first listed country, often the United States.

Duration analysis gives insight into movie lengths and viewing patterns.
