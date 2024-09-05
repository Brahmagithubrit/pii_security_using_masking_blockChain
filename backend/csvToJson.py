import pandas as pd
import json

# Load CSV data
df = pd.read_csv('./dataset/dataset2.csv')

# Prepare data for NER training
def create_json(df):
    data = []
    for _, row in df.iterrows():
        name = str(row['name'])  # Convert to string to avoid errors
        tokens = name.split()
        tags = ['B-PER' for _ in tokens]  # Assuming all tokens in the name are part of the person entity
        data.append({"tokens": tokens, "tags": tags})
    return data

# Convert to JSON format
data = create_json(df)

# Save to JSON file
with open('formatted_data_for_ner.json', 'w') as f:
    json.dump(data, f, indent=2)

print("CSV data has been converted to JSON format.")
