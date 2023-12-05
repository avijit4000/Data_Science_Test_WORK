import pandas as pd
import numpy as np

# Load your dataset
df = pd.read_csv("D:\Pyn\MSDSM\itn\InsectCountfinalcsv.csv")

# Convert 'TimeStamp' to datetime
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'], format='%Y-%m-%d %H-%M-%S')

# Split the timestamp into 'date' and 'time'
df['date'] = df['TimeStamp'].dt.date
df['time'] = pd.to_datetime(df['TimeStamp']).dt.time

length = []
count = 0
start_time = None

for index, row in df.iterrows():
    if start_time is None:
        start_time = row['time']
        count = 1
    elif row['time'].minute // 10 != start_time.minute // 10:
        length.append(count)
        start_time = row['time']
        count = 1
    else:
        count += 1

# Append the count of the last interval
length.append(count)

# Include an empty column in the dataframe df called 'sum_'
df['sum_'] = np.nan

# Calculate the sum of the 'APISME' values for each 10-minute interval
sum_list = []

start_index = 0
for chunk_length in length:
    end_index = start_index + chunk_length
    chunk_sum = df['APISME'][start_index:end_index].sum()
    sum_list.append(chunk_sum)
    start_index = end_index

# Add the sum values to the 'sum_' column
start_index = 0
for chunk_length, sum_value in zip(length, sum_list):
    end_index = start_index + chunk_length
    df.loc[start_index:end_index, 'sum_'] = sum_value
    start_index = end_index

# Drop duplicates based on 'sum_' column
filtered_data = df.drop_duplicates(subset=['sum_'])

# Drop unnecessary columns
filtered_data = filtered_data.drop(['TimeStamp'], axis=1)
filtered_data = filtered_data.drop(['DeviceId'], axis=1)

# Modify the time value
filtered_data['time'] = filtered_data['time'].apply(lambda x: x.replace(second=0))
filtered_data['time'] = filtered_data['time'].apply(lambda x: x.replace(minute=(x.minute // 10) * 10, second=0))

# Create a new DataFrame with desired columns
final_df = pd.DataFrame()
final_df['date'] = filtered_data['date']
final_df['time'] = filtered_data['time']
final_df['sum / 10 min'] = filtered_data['sum_']

# print(final_df)
# print(df)
# final_df.to_csv("out.csv", index=False)

# df.info()

df['time'] = df['time'].apply(lambda x: x.replace(second=0, minute=(x.minute // 10) * 10))
# df['time'] = df['time'].dt.strftime('%H:%M:%S')

df.to_csv('unique_data.csv', index=False)
print(df)