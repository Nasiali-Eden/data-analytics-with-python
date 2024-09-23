#IMPORT REQUIRED LIBRARIES
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import os
# for dirname, _, filenames in os.walk('/kagggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))


#DATA INPUT
income_df = pd.read_csv('Inc_Exp_Data.csv')

# Display the first few rows of the dataframe
print(income_df.head())