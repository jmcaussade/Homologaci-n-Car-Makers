import pandas as pd
import re
import os
from rapidfuzz import process, fuzz

# Step 1: Define car makers list
car_makers = [
    "acura", "alfa romeo", "audi", "baic", "bajaj", "bentley", "bmw", "buick", 
    "byd", "cadillac", "chevrolet", "changan", "chery", "chrysler", "cupra", "daewoo", "dodge", 
    "ducati", "fiat", "ford", "foton", "freightliner", "gmc", "great wall", 
    "haval", "harley", "hino", "honda", "hummer", "hyundai", "infiniti", "isuzu", "italika", 
    "jac", "jaguar", "jeep", "jmc", "kenworth", "kia", "kurazai", "land rover", 
    "lexus", "lincoln", "mack", "masserati", "mazda", "mercedes-benz", "mercedesbenz","mg", "mini", 
    "mitsubishi", "nissan", "peugeot", "peterbilt", "piaggio", "pontiac", 
    "porsche", "ram", "renault", "saab", "scania", "seat", "sinotruk", "subaru", 
    "suzuki", "tesla", "tiggo", "toyota", "volkswagen", "volvo", "yamaha", "vento", 
    "kawazaki", "ktm", "aprilia", "bimota", "mv agusta", "royal enfield", "harley-davidson", 
    "hero", "husqvarna", "indian", "vespa", "zanella", "benelli", "cf moto", 
    "kymco", "norton", "sym"
]


# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the file name
file_name = 'database.xlsx'

# Create the full file path
file_path = os.path.join(current_dir, file_name)

# Load the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Print the DataFrame
print(df)

# Clean car_brand column
df["clean_car_brand"] = (
    df["car_brand"]
    .fillna("")  # Replace NaN with an empty string
    .astype(str)  # Ensure all values are strings
    .str.lower()  # Convert all strings to lowercase
    .apply(lambda x: re.sub(r'[^a-z]', '', x))  # Apply regex
)

# Step 3: Calculate similarity and best match
def get_best_match(brand, car_makers):
    match = process.extractOne(brand, car_makers, scorer=fuzz.ratio)
    return match[0], match[1]

df["best_match"], df["similarity"] = zip(*df["clean_car_brand"].apply(lambda x: get_best_match(x, car_makers)))

# Final DataFrame
print(df)

# Export the processed DataFrame to Excel
output_file_path = os.path.join(current_dir, 'processed_database.xlsx')
df.to_excel(output_file_path, index=False)

print(f"Processed file saved to: {output_file_path}")
