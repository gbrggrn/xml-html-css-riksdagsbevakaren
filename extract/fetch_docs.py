import requests
import os
import time
import xml.etree.ElementTree as ET

# ====================================
# This script fetches the 5 latest motions by intressent_id (5 latest per staff).
# ====================================

# Create dir and define output path
os.makedirs('docs', exist_ok=True)
output_path = 'docs/curr_docs_raw.xml'

# Readability-variables
root_element = '<curr_docs>'
root_element_close = '</curr_docs>'
doktyp = "mot"
size = 5

with open(output_path, 'w', encoding="utf-8") as f:
    f.write(f"{root_element}\n") # Write the opening root element tag

tree = ET.parse('staff/all_staff_raw.xml')
root = tree.getroot()

# Iterate over all person-elements
for p in root.findall('.//person'):
    iid = p.findtext('intressent_id')
    url = f"https://data.riksdagen.se/dokumentlista/?iid={iid}&doktyp={doktyp}&utformat=xml&sz={size}"

    print(f"[fetch_docs] Hämtar 5 senaste motionerna för intressentid: {iid}")
    response = requests.get(url)

    if response.status_code == 200 and '<dokumentlista' in response.text:
        clean_response = response.text.replace('<?xml version="1.0" encoding="utf-8"?>', '') # Replace duplicate xml-declaration
        with open(output_path, 'a', encoding="utf-8") as f:
            f.write(clean_response)
    else:
        print(f"[fetch_docs] Inga motioner funna för intressentid: {iid}\nStatus: {response.status_code}")

    time.sleep(0.5)

# Write the result to file
with open(output_path, 'a', encoding="utf-8") as f:
    f.write(f"\n{root_element_close}") # Write the closing root element tag