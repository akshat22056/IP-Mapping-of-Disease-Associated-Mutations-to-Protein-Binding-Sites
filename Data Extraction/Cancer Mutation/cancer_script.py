import pandas as pd

# Load data
file_path = 'CancerMutationCensus_AllData_Tsv_v101_GRCh37/CancerMutationCensus_AllData_v101_GRCh37.tsv/cmc_export.tsv'  # Change to your actual file path
df = pd.read_csv(file_path, delimiter='\t')

# Extract relevant columns
gene_mutations = df.groupby('GENE_NAME')['Mutation AA'].apply(lambda x: ', '.join(x.dropna().unique())).reset_index()

# Save to CSV
gene_mutations.to_csv('cancer_output.csv', index=False)

print("Extraction complete. Results saved to 'gene_mutations_output.csv'")