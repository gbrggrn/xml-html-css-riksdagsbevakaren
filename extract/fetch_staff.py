import requests
import os

# ===========================
# This script simply fetches all staff data from riksdagens personlista-endpoint.
# ===========================

os.makedirs('staff', exist_ok=True)
output_path = 'staff/all_staff_raw.xml'

root_element = '<all_staff>'
root_element_close = '</all_staff>'

with open(output_path, 'w', encoding="utf-8") as f:
    f.write(f"{root_element}\n")

url = f"https://data.riksdagen.se/personlista/?utformat=xml&utskickat=1"

print(f"[fetch_docs] Hämtar riksdagens personlista")
response = requests.get(url)

if response.status_code == 200 and '<personlista' in response.text:
    clean_response = response.text.replace('<?xml version="1.0" encoding="utf-8"?>', '')
    with open(output_path, 'a', encoding="utf-8") as f:
        f.write(clean_response)

else:
    print(f"[fetch_votes] Inga ledamöter funna.\nStatus: {response.status_code}")

with open(output_path, 'a', encoding="utf-8") as f:
    f.write(f"\n{root_element_close}")