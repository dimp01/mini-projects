import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('task1/netflix_titles.csv')
data.head()

data.info()

# Drop Columns
data.drop(columns=['show_id', 'cast', 'director', 'description'], inplace=True)

# Replacments
data['country'] = data['country'].fillna(data['country'].mode()[0])

# Drop the rest
data.dropna(inplace=True)

# Change Data Type to DateTime
data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce', format = '%d-%m-%Y')
print(data.dtypes)

# Let's leave only first country from each list
data['principal_country'] = data['country'].apply(lambda x: x.split(",")[0])

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





#find the data type of each column.

netflix_2019_file_path = 'task1/netflix_titles.csv'

data = pd.read_csv(netflix_2019_file_path)
data

data.dtypes

#find the number of rows and columns, the dataset contains, use the .shape method.

data.shape

"""# 1. Identify Missing Data"""

#Create a percentage list with .isnull()

data.isnull().sum().sort_values(ascending=False)

# % of rows missing in each column

for column in data.columns:
    percentage = data[column].isnull().mean()
    print(f'{column}: {round(percentage*100,2)}%')

"""# 2. Dealing with Missing Data"""
## Remove a column or row with .drop, .dropna or .isnull


#drop column
data.drop('director', axis=1)

#drop row

no_director = data[data['director'].isnull()].index
data.drop(no_director, axis=0)

#~ + .isnull()
data[~data['director'].isnull()]

#dropna()
data.dropna(subset=['director']) #, inplace=True)

data[data['rating'].isnull()]

"""## Replace it by the mean, median or mode"""

mode = ''.join(data['rating'].mode())
data['rating'].fillna(mode, inplace=True)

mode

for column in data.columns:
    percentage = data[column].isnull().mean()
    print(f'{column}:{round(percentage*100,2)}%')

"""## Replace it by an arbitrary number with .fillna()<\2>"""

data['duration'].fillna(0, inplace=True)

"""Also, we can use the ffill , bfill to propagate the last valid observation forward and backward, respectively."""



df_movie = data[data['type'] == 'Movie']

df_movie

df_movie['duration']

df_movie = df_movie.assign(minute = df_movie['duration'].str.extract(r'(\d+)', expand=False).dropna().astype(int))

df_movie

df_movie['minute'].describe()


"""# 3. Dealing with Inconsistent Data Before Merging 2 Dataframes"""

data_originals = pd.read_csv(netflix_2019_file_path)
data_originals

"""## Dealing with inconsistent column names

"""

data_originals.rename(columns={'titles':'title', 'years':'release_year'}, inplace=True)

data_originals

"""## Dealing with inconsistent data type

"""

data_originals.info()

data_originals = data_originals.astype({'release_year': int})

data_originals.info()

"""# 4. Text Normalization"""

data_originals['title'] = data_originals['title'].apply(lambda x:x.lower())
data_originals['title'] = data_originals['title'].str.lower()
data_originals

"""## Remove blank spaces with .strip()"""

data_originals['title'] = data_originals['title'].apply(lambda x:x.strip())
data_originals['title'] = data_originals['title'].str.strip()
data_originals

data = pd.merge(data_originals,data, on = ['title', 'type', 'release_year'], how='outer')

data.drop_duplicates(['title'], keep='first', inplace=True)

data['type'].value_counts()

data

data.info()