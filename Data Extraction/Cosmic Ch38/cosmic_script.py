import pandas as pd
import re

# Load data
file_path = 'Cosmic_CompleteTargetedScreensMutant_Vcf_v101_GRCh38/Cosmic_CompleteTargetedScreensMutant_v101_GRCh38.vcf/Cosmic_CompleteTargetedScreensMutant_v101_GRCh38.vcf'  # Change to your actual file path
df = pd.read_csv(file_path, delimiter='\t', comment='#', header=None, names=['CHROM','POS','ID','REF','ALT','QUAL','FILTER','INFO'])

# Extract Gene and p. data using regex
def extract_gene_and_p(info):
    gene_match = re.search(r'GENE=([^;]+)', info)
    p_match = re.search(r'AA=p\.([^;]+)', info)
    gene_name = gene_match.group(1) if gene_match else None
    p_name = f"p.{p_match.group(1)}" if p_match else None
    return gene_name, p_name

data = df['INFO'].apply(extract_gene_and_p)
df[['Gene', 'p_name']] = pd.DataFrame(data.tolist(), index=df.index)

# Group by Gene and combine unique p. names with spaces and '|'
def format_p_names(x):
    clean_names = sorted(set(x.dropna()))
    return ' | '.join(clean_names)

gene_p_data = df.groupby('Gene')['p_name'].apply(format_p_names).reset_index()

# Save to CSV
gene_p_data.to_csv('cosmic_vcf_output.csv', index=False)

print("Extraction complete. Results saved to 'gene_p_data_vcf_output.csv'")