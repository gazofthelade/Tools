# Script to read an excel file and produce a json file using the data
# Created By: Gareth Durban
# Date: 24/07/2025

import pandas as pd
import json
import os

# Path to your Excel file
file_name = "trick_probabilities"
file_path = f"{file_name}.xlsx"

# Load the Excel file
excel_data = pd.ExcelFile(file_path)

# Directory to save the output JSON files
output_dir = "trick_probabilities_json"
os.makedirs(output_dir, exist_ok=True)

# Convert each sheet to a JSON file
for sheet in excel_data.sheet_names:
    df = excel_data.parse(sheet)
    tricks = {}

    # Assuming first column is 'Level', others are trick names
    for trick in df.columns[1:]:
        level_probabilities = {
            str(row['Level']): row[trick]
            for _, row in df.iterrows()
        }
        tricks[trick] = level_probabilities

    # Save to JSON
    output_path = os.path.join(output_dir, f"{sheet.lower()}_probabilities.json")
    with open(output_path, "w") as json_file:
        json.dump(tricks, json_file, indent=4)

    print(f"Saved {output_path}")
