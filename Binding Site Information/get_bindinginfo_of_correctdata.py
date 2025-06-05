import pandas as pd
import requests
from tqdm import tqdm

# Load your corrected file with UniProt_ID and GENE_NAME
corrected_df = pd.read_csv('corrected_human_uniprot_ids.csv')

# Output structure
output_data = []

# UniProt Proteins API endpoint for retrieving binding site info
def get_binding_sites(uniprot_id):
    url = f"https://www.ebi.ac.uk/proteins/api/features/{uniprot_id}"
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return [], ""
    
    data = response.json()
    features = data.get("features", [])
    binding_sites = []

    for feature in features:
        if feature.get("type") == "BINDING":
            position = feature.get("begin")
            if position:
                binding_sites.append(int(position))
    
    sequence = data.get("sequence", "")
    return binding_sites, sequence

# Go through each row
for _, row in tqdm(corrected_df.iterrows(), total=len(corrected_df)):
    uniprot_id = row['UniProt_ID']
    gene_name = row['GENE_NAME']
    
    try:
        positions, full_sequence = get_binding_sites(uniprot_id)
        position_cols = {}
        sequence_cols = {}
        
        for i, pos in enumerate(positions[:20]):  # limit to first 20
            aa = full_sequence[pos - 1] if pos <= len(full_sequence) else ""
            position_cols[f"Position_{i+1}"] = pos
            sequence_cols[f"Sequence_{i+1}"] = aa
        
        combined = {
            "UniProt_ID": uniprot_id,
            "GENE_NAME": gene_name,
            **position_cols,
            **sequence_cols,
            "MUTATION_AA": row.get("MUTATION_AA", "")
        }
        output_data.append(combined)
    
    except Exception as e:
        print(f"Error processing {uniprot_id}: {e}")

# Save the output
binding_df = pd.DataFrame(output_data)
binding_df.to_csv("final_binding_site_data_2.csv", index=False)
print("✅ Binding site data saved to: final_binding_site_data.csv")
