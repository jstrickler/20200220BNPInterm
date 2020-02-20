#!/usr/bin/env python
import pandas as pd
import numpy as np

dataset1 = np.arange(1, 4)
dataset2 = np.arange(4, 7)


df1 = pd.DataFrame(dataset1, columns=["A", "B", 'C'])
print(df1)
