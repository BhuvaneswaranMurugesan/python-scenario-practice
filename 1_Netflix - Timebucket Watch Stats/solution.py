import pandas as pd
from datetime import date

# Data Available in this Dataframe:
df = data.copy() # Data is Loaded via app using docker

# Write your solution code here
df['ts'] = pd.to_datetime(df['ts'])
df['date'] = df['ts'].dt.date
df['time'] = df['ts'].dt.time
df['hour'] = df['ts'].dt.hour
df = df[df['date'] == date(2025,10,21)]

# return the Dataframe
result = df.groupby('hour',as_index=False)['seconds'].sum().sort_values('seconds',
        ascending=False).head(5)

print(result)