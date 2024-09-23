#IMPORT REQUIRED LIBRARIES
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set pandas to display all columns in one line (horizontally)
pd.set_option('display.width', 1000)  # Set a high enough value for width

# import os
# for dirname, _, filenames in os.walk('/kagggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))


#DATA INPUT
income_df = pd.read_csv('Inc_Exp_Data.csv')

# Show all columns in the DataFrame
pd.set_option('display.max_columns', None)

# If you want to display all rows as well, you can set this option too
pd.set_option('display.max_rows', None)

# Now, when you print the DataFrame, it will show all columns
print(income_df.head())
