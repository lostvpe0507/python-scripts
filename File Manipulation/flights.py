import pandas as pd
from pathlib import Path

root = Path(__file__).parent.parent
file= root / 'Resources' / 'flights.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(file)

# Convert ScheduledDepart and ScheduledArrival to datetime
df['ScheduledDepart'] = pd.to_datetime(df['ScheduledDepart'], format='%H:%M')
df['ScheduledArrival'] = pd.to_datetime(df['ScheduledArrival'], format='%H:%M')

# Calculate the difference in minutes between ScheduledArrival and ScheduledDepart
df['CalculatedDuration'] = (df['ScheduledArrival'] - df['ScheduledDepart']).dt.total_seconds() / 60

# Filter flights where CalculatedDuration matches ScheduledDuration
same_timezone_flights = df[df['CalculatedDuration'] == df['ScheduledDuration']]

# Count the number of flights
count_same_timezone_flights = len(same_timezone_flights)

print("Number of flights set to depart and arrive in the same timezone:", count_same_timezone_flights)

