import pandas as pd
from vininfo import Vin
import os
import re

# Step 1: Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the parent directory (the folder above the current "Probabilities" folder)
parent_dir = os.path.dirname(current_dir)

# Define the file name for the original database
file_name = 'database.xlsx'

# Create the full path to the file in the parent folder (adjusted for subfolder)
file_path = os.path.join(parent_dir, file_name)

# Load the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Step 2: Extract information from the VINs
def get_vin_info(vin):
    """Function to get information from the VIN number using vininfo"""
    try:
        vehicle = Vin(vin)
        return vehicle.manufacturer, vehicle.wmi, vehicle.years
    except Exception as e:
        # If there is an issue with the VIN, return NaN for all fields
        return None, None, None

# Step 3: Apply the get_vin_info function to the 'serie' column
df['make'], df['model'], df['year'] = zip(*df['serie'].apply(lambda vin: get_vin_info(str(vin))))

# Step 4: Save the updated DataFrame to a new Excel file called 'reviewed.xlsx'
output_file_path = os.path.join(current_dir, 'reviewed_vininfo.xlsx')
df.to_excel(output_file_path, index=False)

print(f"Reviewed file saved to: {output_file_path}")
