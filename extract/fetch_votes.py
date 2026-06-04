import xml.etree.ElementTree as ET
import requests
import os
import time

# ====================================
# 1. This script retrieves the latest votes based on intressent_id:s of riksdag staff as XML and saves that to file.
# 2. This script retrieves the document metadata of the unique dok_id:s that have been voted on.
# 3. This script filters out {title, url} IN MEMORY.
# 3. This script adds the metadata as new tags with their own namespace to the votes xml-structure and saves to a new file.
# ====================================

# Declare and register custom namespace
CUSTOM_NAMESPACE = 'http://riksdagsinfo.se/votes'
ET.register_namespace('custom', CUSTOM_NAMESPACE)

# Readability-variables
output_path = 'votes/curr_votes_raw.xml'
root_element = '<curr_votes>'
root_element_close = '</curr_votes>'
empty = ''
xml_declaration = '<?xml version="1.0" encoding="utf-8"?>'

# If data-file doesn't already exist: fetch votes by iid and save to file.
if not os.path.exists(output_path):
    os.makedirs('votes', exist_ok=True)

    with open(output_path, 'w', encoding="utf-8") as f:
        f.write(f"{root_element}\n") # Write the opening root element tag

    tree = ET.parse('staff/all_staff_raw.xml')
    root = tree.getroot()

    for p in root.findall('.//person'):
        iid = p.findtext('intressent_id')
        size = 10
        format = 'xml'
        url = f"https://data.riksdagen.se/voteringlista/?iid={iid}&sz={size}&utformat={format}"

        print(f"[fetch_votes] Hämtar voteringslista för {iid}")
        response = requests.get(url)

        if response.status_code == 200 and '<votering' in response.text:
            clean_response = response.text.replace(xml_declaration, empty) # Remove double xml-declaration

            with open(output_path, 'a', encoding="utf-8") as f:
                f.write(clean_response)
        else:
            print(f"[fetch_votes] Ingen votering funnen för {iid}\nStatus: {response.status_code}")

        time.sleep(0.5) # Courtesy-sleep to not get banned

    with open(output_path, 'a', encoding="utf-8") as f:
        f.write(f"\n{root_element_close}") # Write the closing root element tag

# Parse the vote-file, retrieve root then assign all dok_id elements as a set to avoid duplicates.
votes_tree = ET.parse('votes/curr_votes_raw.xml')
votes_root = votes_tree.getroot()
dok_id_elements = set(votes_root.findall('.//votering/dok_id'))

# Iterate over dok_id elements and convert them to strings
unique_dok_ids = set()
for e in dok_id_elements:
    unique_dok_ids.add(e.text)

# Initiate empty dictionary
votes_doks_lookup = {}

# Retrieve document metadata by dok_id from riksdagens dokumentstatus-endpoint
for id in unique_dok_ids:
    format = 'xml'
    url = f"https://data.riksdagen.se/dokumentstatus/{id}&utformat={format}"

    print(f"[fetch_votes] Hämtar voterings-metadata för dokumentid: {id}")
    response = requests.get(url)

    if response.status_code == 200 and '<dokumentstatus' in response.text:
        response_root = ET.fromstring(response.text)

        title = response_root.findtext('.//dokument/titel') # Retrieve title element text
        doc_url = response_root.findtext('.//dokument/dokument_url_html') # Retrieve url element text

        votes_doks_lookup[id] = {'title': title, 'url': doc_url} # Assign title/url to the dictionary
    else:
        print(f"[fetch_votes] Fel vid dokumentid: {id} | Status: {response.status_code}")
    
    time.sleep(0.5) # Courtesy-sleep again to avoid ban

# Iterate over votering-elements and insert title/url as custom elements
for v in votes_root.findall('.//votering'):
    dok_id_raw = v.findtext('dok_id')

    if dok_id_raw:
        dok_id = dok_id_raw.strip() # Strip to make sure no \n or whitespace tags along

    if dok_id in votes_doks_lookup:
        metadata = votes_doks_lookup[dok_id]

        title_elem = ET.SubElement(v, f'{{{CUSTOM_NAMESPACE}}}title') # CLARK-notation to add the namespace (custom:title)
        title_elem.text = metadata['title']

        url_elem = ET.SubElement(v, f'{{{CUSTOM_NAMESPACE}}}url')
        url_elem.text = metadata['url']

# Write the "enriched" XML to a new file
votes_tree.write('votes/votes_enriched.xml', encoding="utf-8", xml_declaration=True)