import pandas as pd
import random

# Function to introduce edge cases with a 5% chance
def add_edge_case(driver, lap_time, last_valid_lap_time=None):
    """
    Introduces edge cases with a 5% chance.
    - 'empty' for missing values (None)
    - 'outlier' for extreme values
    - 'string' for invalid non-numeric values
    - 'duplicate' to simulate duplication of last valid lap time
    - 'driver_number' to simulate a numeric driver name
    - 'null_driver' to simulate a null (None) driver name
    """
    
    if random.random() < 0.1:  # 5% chance of adding an edge case
        case_type = random.choice(['empty', 'outlier', 'string', 'duplicate', 'driver_number', 'null_driver'])
        
        if case_type == 'empty':
            lap_time = None  # Empty value (missing data)
        
        elif case_type == 'outlier':
            lap_time = random.choice([100.0, 150.0, 200.0, 0.0, 0.01])  # Extreme outliers
        
        elif case_type == 'string':
            lap_time = random.choice(['N/A', 'Invalid', 'Error'])  # Non-numeric value
        
        elif case_type == 'duplicate' and last_valid_lap_time is not None:
            lap_time = last_valid_lap_time  # Repeat the last valid lap time
        
        elif case_type == 'driver_number':
            driver = random.randint(1, 100)  # Simulate a numeric driver (random number between 1 and 100)
        
        elif case_type == 'null_driver':
            driver = None  # Null (missing) driver name

    return [driver, lap_time]


drivers = [
    "Fangio", "Prost", "Senna", "Piquet", "Lauda", 
    "Clark", "Stewart", "Hill", "Fittipaldi", "Brabham",
    "Moss", "Hakkinen", "Rosberg", "Hunt", "Schumacher", 
    "Vettel", "Hamilton", "Alonso", "Raikkönen", "Piquet"]

data = []


# Generate 7 lap times for each driver
for driver in drivers:
    for _ in range(18):  # 18 lap times per driver
        lap_time = round(random.uniform(2.0, 7.0), 2)  # Generate random lap time between 2.0 and 7.0
        data.append(add_edge_case(driver, lap_time))

# Convert the list of data into a DataFrame
df = pd.DataFrame(data, columns=['Driver', 'Time'])

# Introduce some deliberate duplicates
df = pd.concat([df, df.sample(5)], ignore_index=True)  # Adding 5 random duplicate rows

# Save the DataFrame to a CSV file
df.to_csv('src_files/f1_lap_times_with_edge_cases.csv', index=False)