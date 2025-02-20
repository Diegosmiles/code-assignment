import subprocess


subprocess.run(['python', '0_data_generation.py'], check=True)
subprocess.run(['python', '1_data_cleaning.py'], check=True)
subprocess.run(['python', '2_calculate_avg.py'], check=True)

print("All scripts executed successfully!")