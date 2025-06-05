import pandas as pd
import re

# Load data
file_path = 'filtered_dbsnp_data_30000-2.csv'  # Change to your actual file path
df = pd.read_csv(file_path)

# Extract Gene and p. data using regex
def extract_p_name(aa_mutation):
    match = re.search(r'p\.[^ ]+', str(aa_mutation))
    return match.group(0) if match else None

df['p_name'] = df['AA Mutation'].apply(extract_p_name)
gene_p_data = df.groupby('Gene')['p_name'].apply(lambda x: ' | '.join(sorted(set(x.dropna())))).reset_index()

# Save to CSV
gene_p_data.to_csv('filtered_data_30k_output.csv', index=False)

print("Extraction complete. Results saved to 'gene_p_data_aa_output.csv'")