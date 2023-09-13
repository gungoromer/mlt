import numpy as np
import pandas as pd

height = [170,180,190,200]

x = np.percentile(height, 90)

print(x)


df = pd.DataFrame(height)
print(df.describe())