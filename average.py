import pandas as pd
import numpy as np

same_Data = {
    'name': ['anastasia', 'dima', 'katherine', 'james', 'emily', 'michael', 'matthew',
             'laura', 'kevin', 'jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(same_Data, index=labels)
print("original dataframe:")
print(df)
averageScore = df['score'].mean()

print("\nThe average score is:", round(averageScore, 2))