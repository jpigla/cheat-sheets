# === Python Cheat Sheet ===


# === Modules ===

# NumPy
from tkinter.tix import InputOnly
import numpy as np

# Matplotlib
import matplotlib.pyplot as plt
import matplotlib

# Regular Expressions
import re

# Time Information / Manipulation
import time


# === Python ===



# === Jupyter Notebooks ===

  # Set warnings of Jupyter Notebooks to ignore / only once
  import warnings
  warnings.filterwarnings('ignore')
  warnings.filterwarnings(action='once')


# === Jupyter Notebooks / Examples ===

  # Get excecution time of code
  startTime = time.time()
  # --> Your code here !
  print (f'The script took {time.time() - startTime} seconds!')


# === Pandas ===

  # Import Dataframe library
  import pandas as pd

  # Create empty DataFrame
  df = pd.DataFrame()
  df = pd.DataFrame(None)

  # Read CSV file into DataFrame
  df = pd.DataFrame(pd.read_csv('data.csv'))
  df = pd.read_csv('data.csv')

  skiprows = 5                        # Skip first 5 rows
  header = 2                          # row number which contains the column names
  sep = '\t'                          # Separator (default ',')
  index_col = 0                       # column to use as index
  encoding = 'latin-1'                # Set encoding for import
  name = ['column']                   # Rename columns (new name)
  engine = 'python'                   # Engine to use for import
  dtype = {'Name': str, 'Grade': int} # Specify data type for columns
  usecols = [0, 1]                    # Columns to import
  nrows = 10                          # Number of rows to import
  na_values = ['NA']                  # Values for NA to use for import
  mode = 'a'                          # Mode to use for import (a: append, overwrite, etc.)

  # Pandas Settings for better output in Jupyter Notebooks
  pd.set_option('display.max_colwidth', None)
  pd.set_option('display.max_rows', 100)
  pd.set_option('display.max_columns', 50)

  # Pandas Dataframe Statistics
  df.describe(include='all')

  # Sets text align to left for single DataFrame
  df = df.style.set_properties(**{'text-align': 'left'})


# === Pandas / Basic Data Information ===

  # Create Statistics for DataFrame (mean, std, min, max, etc.) & inklude strings
  df.describe(include='all')

  include = 'all' / None # Include strings or numeric values only

  # Get number of rows and columns
  df.shape
  df.shape[0] # Number of rows
  df.shape[1] # Number of columns

  # Get distinct values in column
  df['column'].unique()

  # Get count of distinct values in column
  df['column'].value_counts()

  # Get list of columns
  df.columns

  # Get information about DataFrame
  df.info()

  # Get count of non-NA values in DataFrame
  df.count()
  df.count(axis=1)  # Get count of columns in DataFrame
  df.count(axis=0)  # Get count of rows in column
  len(df)           # Get count of rows in DataFrame

  # Get number of rows with each unique value in column
  df['column'].value_counts()


# === Pandas / Data Summarising ===

  # Get minimum / maximum value of column
  df['column'].min()
  df['column'].max()

  # Get (cumulative) mean of column
  df['column'].mean()
  df['column'].cumsum() / df['column'].count()

  # Get median of column
  df['column'].median()

  # Get mode of column
  df['column'].mode()

  # Get (cumulative) sum of column
  df['column'].sum()
  df['column'].cumsum()

  # Get standard deviation of column
  df['column'].std()

  # Get variance of column
  df['column'].var()

  # Get skewness of column
  df['column'].skew()

  # Get kurtosis of column
  df['column'].kurt()

  # Get quantile of column
  df['column'].quantile(0.5)

  # Get minimum / maximum index value of column
  df['column'].idxmin()
  df['column'].idxmax()


# === Pandas / Row Manipulation ===

  # Delete duplicated Rows by selected column (inplace)
  df.drop_duplicates(subset=['column'], keep="first", inplace=True)
  df.drop_duplicates(subset=['column', 'column2'], keep="first", inplace=True)

  keep = 'first' / 'last' / False # Keep first / last / no duplicates


# === Pandas / Column Manipulation ===

  # Delete selected Columns (inplace)
  df.drop(columns=['column'], inplace=True)


# === Pandas / Data Extraction ===

  # Extract strings from column
  df['column'].str.findall(r'(.*?)')


# === Pandas / Data Extraction / Examples ===

  # Extract strings from column and concate strings with '@@
  df['column'].str.findall(r'(.*?)').apply('@@'.join)


# === Pandas / Data Sorting ===

  # Sort DataFrame by column (inplace)
  df.sort_values('column1', ascending=True, inplace=True)
  df.sort_values(['column1', 'column2'], ascending=[True, True], inplace=True)


# === Pandas / Data Filtering ===

  # Groups Data in column (unique) and keep top 5 values
  df.groupby(['column']).head(5)

  # Select columns by name with regex
  df.filter(regex='.*string.*')

  # Select columns by dtype (include / exclude)
  df.select_dtypes(include='number', exclude='object')


# === Pandas / Applying Functions ===

  # Apply function to column
  df['column'].apply(lambda x: x + 1)

  # Apply function element-wise to column
  df['column'].applymap(lambda x: x + 1)


# === Pandas / Handling Missing Data ===

  # Replace missing values with 0
  df['column'].fillna(0)
  df['column'].fillna(np.nan)                             # Replace missing values with NaN
  df['column'].fillna(df['column'].mean())                # Replace missing values with mean
  df['column'].fillna({'column': 'value'}, inplace=True)  # Replace missing values with column specific value
  df['column'].fillna(method='ffill')                     # Replace missing values with previous value
  df['column'].fillna(method='bfill')                     # Replace missing values with next value

  method = 'ffill' / 'bfill' / 'pad' / 'backfill' / None  # Method to use for filling missing values (default: 'ffill'; 'ffill' / 'pad': previous value, 'bfill' / 'backfill': next value)

  # Drop rows (all columns) with missing values
  df.dropna()
  df.dropna(subset=['column']) # Drop rows (selected columns) with missing values

  how = 'any' / 'all' # How to drop rows (any: drop rows if any column has missing values, all: drop rows if all columns have missing values)

  # Keep rows (all columns) where rows of selected column are not NaN
  df[df['column'].notnull()]
  df[df['column'].notna()]


# === Pandas / Cleaning Data ===

  # Replace old string with new string
  df['column'].str.replace({'old string', 'new string'})
  df['column'].str.replace({'old string', 'new string'}, case=False) # case insensitive

  # Replace string (regex) with new string
  df['column'].str.replace(r'^www.', 'https://www.', regex=True)

  # Remove white spaces from string
  df['column'].str.strip()


# === Pandas / Merging Data ===

  # Merge DataFrames on column
  pd.concat([df, df], axis=1)
  pd.concat([df, df], axis=1, join='inner') # Inner join

  # Merge DataFrames only on selected columns
  pd.merge(df, df, on='column', how='inner')
  pd.merge(df, df[['column', 'column1']], on='column', how='inner') # Merge on selected columns with selected columns


# === Pandas / Convert Data ===

  # Convert DataFrame to list
  df.to_list()

  # Make DataFrame from list
  pd.DataFrame([{'column': 'value'}])

  # Convert DataFrame to JSON
  df.to_json()

  # Convert JSON to DataFrame
  pd.read_json('path/to/json')

  # Round values in DataFrame (.00)
  df.round(2)
  df.round({'column': 2, 'column1': 3}) # Round values in selected columns


# === Pandas / String Manipulation ===

  # Convert string to ... 
  df['column'].str.lower() # All characters to lower case
  df['column'].str.upper() # All characters to upper case
  df['column'].str.title() # Title case (first letter of each word capitalized)
  df['column'].str.capitalize() # Capitalize first letter of each word
  df['column'].str.swapcase() # Swap case of each letter (upper to lower, lower to upper)
  df['column'].str.casefold() # Case folding (lower case)


# === Code Snippets (Pandas) ===

  # Groups GSC daily data into weekly intervals from Monday to Sunday (right closed / included)
  df.resample('W-SUN', on='date').agg({'clicks':'sum','impressions':'sum','ctr':'mean','position':'mean'})


# === Advertools ===

