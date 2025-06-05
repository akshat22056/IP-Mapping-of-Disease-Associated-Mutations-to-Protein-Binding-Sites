import pandas as pd
import requests
from time import sleep

# Load your CSV
df = pd.read_csv("fatsa sequence fetching/main_updated.csv")

# Function to get FASTA sequence using UniProt ID
def get_fasta_sequence(uniprot_id):
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            lines = response.text.strip().split('\n')
            sequence = ''.join(lines[1:])  # Skip the header line
            return sequence
        else:
            return None
    except:
        return None

# Add FASTA sequence for each UniProt ID
fasta_sequences = []
for i, row in df.iterrows():
    fasta_seq = get_fasta_sequence(row['UniProt_ID'])
    fasta_sequences.append(fasta_seq)
    sleep(0.5)  # Avoid hitting the server too fast (rate limit)

df['FASTA_SEQUENCE'] = fasta_sequences

# Save the new CSV
df.to_csv("main_updated_with_fasta_sequences.csv", index=False)

print("✅ FASTA sequences added and file saved as: with_fasta_sequences.csv")
