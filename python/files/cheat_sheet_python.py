# === Python Cheat Sheet ===


# === Modules ===

# NumPy
import numpy as np

# Matplotlib
import matplotlib.pyplot as plt
import matplotlib

# Regular Expressions
import re


# === Python ===



# === Jupyter Notebooks ===

# Set warnings of Jupyter Notebooks to ignore / only once
import warnings
warnings.filterwarnings('ignore')
warnings.filterwarnings(action='once')






# === Pandas ===

# Import Dataframe library
import pandas as pd

# Create empty DataFrame
df = pd.DataFrame()
df = pd.DataFrame(None)

# Read CSV file into DataFrame
df = pd.DataFrame(pd.read_csv('data.csv'))
df = pd.read_csv('data.csv')

skiprows=5          # Skip first 5 rows
header=2            # row number which contains the column names
sep="\t"            # Separator (default ",")
index_col=0         # column to use as index
encoding='latin-1'  # Set encoding for import
name=['column']     # Rename columns (new name)
engine='python'     # Engine to use for import
dtype={'Name': str, 'Grade': int} # Specify data type for columns
usecols=[0, 1]      # Columns to import
nrows=10            # Number of rows to import
na_values=['NA']    # Values for NA to use for import
mode='a'            # Mode to use for import (a: append, overwrite, etc.)

# Pandas Settings for better output in Jupyter Notebooks
pd.set_option("display.max_colwidth", None)
pd.set_option("display.max_rows", 100)
pd.set_option("display.max_columns", 50)

# Pandas Dataframe Statistics
df.describe(include='all')

# Sets text align to left for single DataFrame
df = df.style.set_properties(**{'text-align': 'left'})


# === Code Snippets (Pandas) ===

# Create Statistics for DataFrame (mean, std, min, max, etc.) & inklude strings
df.describe(include='all')

# Delete selected Columns (inplace=True)
df.drop(columns=['column'], inplace=True)

# Extract strings from column and concate strings with '@@
df['column'].str.findall(r'(.*?)').apply('@@'.join)





# === Advertools ===


