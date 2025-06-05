import pandas as pd
import re

# Load data
file_path = 'variant_summary.txt/variant_summary-2.csv'  # Change to your actual file path
df = pd.read_csv(file_path, delimiter='\t')

# Extract GeneSymbol and p. data using regex
def extract_p_name(name):
    match = re.findall(r'\(p\.[^)]+\)', str(name))
    clean_names = [m.strip('()') for m in match]
    return ' | '.join(sorted(set(clean_names))) if clean_names else None

df['p_name'] = df['Name'].apply(extract_p_name)
gene_p_data = df.groupby('GeneSymbol')['p_name'].apply(lambda x: ' | '.join(x.dropna().unique())).reset_index()

# Save to CSV
gene_p_data.to_csv('variant_summary_output.csv', index=False)

print("Extraction complete. Results saved to 'gene_p_data_output.csv'")

