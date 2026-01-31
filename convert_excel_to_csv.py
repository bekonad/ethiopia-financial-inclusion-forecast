# convert_excel_to_csv.py
import pandas as pd

# Convert unified data (main sheet)
pd.read_excel('data/raw/ethiopia_fi_unified_data.xlsx', sheet_name='ethiopia_fi_unified_data') \
  .to_csv('data/raw/ethiopia_fi_unified_data.csv', index=False)

# Convert reference codes
pd.read_excel('data/raw/reference_codes.xlsx', sheet_name='reference_codes') \
  .to_csv('data/raw/reference_codes.csv', index=False)

print("Conversion complete! CSV files created in data/raw/")