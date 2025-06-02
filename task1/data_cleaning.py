import numpy as np
import pandas as pd

import plotly.express as px

data = pd.read_csv('./netflix_titles.csv')
data.head()

data.info()

# Drop Columns
data.drop(columns=['show_id', 'cast', 'director', 'description'], inplace=True)

# Replacments
data['country'] = data['country'].fillna(data['country'].mode()[0])

# Drop the rest
data.dropna(inplace=True)

# Change Data Type to DateTime
data["date_added"] = pd.to_datetime(data['date_added'])

# Let's leave only first country from each list
data['principal_country'] = data['country'].apply(lambda x: x.split(",")[0])

"""<h2 style = "font-family:garamond; font-size:30px; background-color: white; color : #E50914; border-radius: 100px 100px; text-align:left">Rating Ages</h2>"""

ratings_ages = {
    'TV-PG': 'Older Kids',
    'TV-MA': 'Adults',
    'TV-Y7-FV': 'Older Kids',
    'TV-Y7': 'Older Kids',
    'TV-14': 'Teens',
    'R': 'Adults',
    'TV-Y': 'Kids',
    'NR': 'Adults',
    'PG-13': 'Teens',
    'TV-G': 'Kids',
    'PG': 'Older Kids',
    'G': 'Kids',
    'UR': 'Adults',
    'NC-17': 'Adults'
}

# Replace Rating values with age targets, they are based on
data['ages'] = data['rating'].replace(ratings_ages)
data['ages'].unique()


data.head()
data.to_csv('./netflix_title_cleaned.csv')
