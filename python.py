import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os
for dirname, _, filenames in os.walk('/kagggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

income_df = pd.read_csv('')