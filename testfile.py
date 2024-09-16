import pandas as pd
import spacy
import re

# Load the CSV file
file_path = 'D:\\Amazon_ML\\trained.csv'  # Ensure the path is correct
df = pd.read_csv(file_path)

# Limit to the first 1000 rows for processing
df = df.head(1000)

# Load English tokenizer, tagger, parser, and NER
nlp = spacy.load("en_core_web_sm")

# Define entity to unit mapping with both full terms and abbreviations
entity_unit_map = {
    'width': {'centimetre': 'centimetre', 'foot': 'foot', 'inch': 'inch', 'metre': 'metre', 'millimetre': 'millimetre', 'yard': 'yard'},
    'depth': {'centimetre': 'centimetre', 'foot': 'foot', 'inch': 'inch', 'metre': 'metre', 'millimetre': 'millimetre', 'yard': 'yard'},
    'height': {'centimetre': 'centimetre', 'foot': 'foot', 'inch': 'inch', 'metre': 'metre', 'millimetre': 'millimetre', 'yard': 'yard'},
    'item_weight': {'gram': 'gram', 'kilogram': 'kilogram', 'microgram': 'microgram', 'milligram': 'milligram', 'ounce': 'ounce', 'pound': 'pound', 'ton': 'ton', 'g': 'g', 'kg': 'kg', 'lb': 'lb', 'oz': 'oz'},  # Focus only on weight-related units
    'maximum_weight_recommendation': {'gram': 'gram', 'kilogram': 'kilogram', 'microgram': 'microgram', 'milligram': 'milligram', 'ounce': 'ounce', 'pound': 'pound', 'ton': 'ton'},
    'voltage': {'kilovolt': 'kilovolt', 'millivolt': 'millivolt', 'volt': 'volt'},
    'wattage': {'kilowatt': 'kilowatt', 'watt': 'watt'},
    'item_volume': {'centilitre': 'centilitre', 'cubic foot': 'cubic foot', 'cubic inch': 'cubic inch', 'cup': 'cup', 'decilitre': 'decilitre', 'fluid ounce': 'fluid ounce', 'gallon': 'gallon', 'imperial gallon': 'imperial gallon', 'litre': 'litre', 'microlitre': 'microlitre', 'millilitre': 'millilitre', 'pint': 'pint', 'quart': 'quart'}
}

# Normalize units like "Kgs" to "Kg", "gms" to "gm", "M" for "metre", etc.
unit_normalization = {
    'kgs': 'kilogram', 'kg': 'kilogram', 'gms': 'gram', 'gm': 'gram', 'grams': 'gram', 'lbs': 'pound', 'lb': 'pound',
    'm': 'metre', 'mm': 'millimetre', 'cm': 'centimetre', 'ft': 'foot', 'yd': 'yard', 'in': 'inch', 'oz': 'ounce',
    'ml': 'millilitre', 'l': 'litre', 'kv': 'kilovolt', 'mv': 'millivolt', 'v': 'volt', 'w': 'watt', 'kw': 'kilowatt'
}

# Function to normalize units
def normalize_unit(unit):
    unit_lower = unit.lower()
    return unit_normalization.get(unit_lower, unit_lower)

# Regular expression to find number-unit pairs
pattern = r'(\d+\.?\d*)\s*([a-zA-Zµ]+)'

# Function to extract both the value and the unit for a given entity
def extract_entity_value(text, entity_name):
    # Convert text to lowercase
    text = text.lower()
    
    # Process the document
    doc = nlp(text)
    
    # Get the allowed units for the given entity (e.g., item_weight, voltage)
    allowed_units = entity_unit_map.get(entity_name, {})
    
    # Find number-unit pairs
    matches = re.findall(pattern, doc.text)
    
    # Debugging: Check for found matches
    print(f"Found matches in text: {matches}")
    
    # Look for the matching unit and normalize it
    for match in matches:
        number, unit = match
        normalized_unit = normalize_unit(unit)
        
        # If the normalized unit is in the allowed units for the specified entity, return the value and unit
        if normalized_unit in allowed_units:
            return f"{number} {normalized_unit}"
    
    return "No matching entity found."

# Processing the rows from the dataframe
output = []
for index, row in df.iterrows():
    entity_to_extract = row.get('entity_name', None)
    text = row.get('extracted_text', None)
    
    # Debugging: Check if the row has valid data
    if not entity_to_extract or not text:
        print(f"Skipping row {index} due to missing data.")
        output.append("Invalid data")
        continue
    
    print(f"Processing row {index}: Entity - {entity_to_extract}, Text - {text[:50]}...")  # Print first 50 characters of text for context
    result = extract_entity_value(text, entity_to_extract)
    output.append(result)

# Add the results back to the dataframe
df['extracted_value'] = output

# Save the output to a new CSV file
output_file_path = 'D:\\Amazon_ML\\output.csv'
df.to_csv(output_file_path, index=False)

print(f"Processed {len(df)} rows and saved the output to {output_file_path}")
