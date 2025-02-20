import pandas as pd

#Read the CSV file
df = pd.read_csv("src_files/f1_lap_times_cleaned.csv")

#Calculate average lap time and fastest lap time for each driver
result = df.groupby('Driver').agg(
    avg_lap_time=('Time', 'mean'),
    fastest_lap_time=('Time', 'min')
).reset_index()

#Average time for each driver, sorted in ascending order:
avg_times = result.sort_values(by='avg_lap_time')

#Print avg_times for all drivers in ascending order
print(avg_times)

#Sort by average lap time (ascending order) and get top 3 drivers
top_3_drivers = avg_times.head(3)

# Step 4: Output the result (e.g., to CSV or JSON)
top_3_drivers.to_csv('top_3_drivers.csv', index=False)
