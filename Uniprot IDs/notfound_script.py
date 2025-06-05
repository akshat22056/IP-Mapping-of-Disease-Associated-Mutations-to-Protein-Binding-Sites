# csv


import pandas as pd
import requests
import time

# Function to fetch UniProt IDs using batch requests
def fetch_uniprot_ids_batch(genes):
    ids = ['Not found'] * len(genes)
    chunk_size = 100
    for i in range(0, len(genes), chunk_size):
        batch = genes[i:i+chunk_size]
        query = " OR ".join([f"gene_exact:{gene}" for gene in batch])
        url = f'https://rest.uniprot.org/uniprotkb/search?query={query}&format=json&size=100'
        try:
            response = requests.get(url)
            if response.status_code == 200 and response.json().get('results'):
                results = {res['genes'][0]['geneName']['value']: res['primaryAccession'] for res in response.json()['results']}
                for j, gene in enumerate(batch):
                    if gene in results:
                        ids[i + j] = results[gene]
        except Exception as e:
            print(f"Error processing batch: {e}")
        time.sleep(1)  # Prevent rate limiting
    return ids

# Read CSV file
df = pd.read_csv('uniprot ids/variant_summary_vcf_output_with_uniprot_ids.csv')

# Filter genes with 'Not found'
genes_to_query = df.loc[df['UniProt_ID'] == 'Not found', 'GeneSymbol'].tolist()

# Perform batch queries
if genes_to_query:
    uniprot_ids = fetch_uniprot_ids_batch(genes_to_query)
    df.loc[df['UniProt_ID'] == 'Not found', 'UniProt_ID'] = uniprot_ids

# Save to CSV
df.to_csv('variant_summary_with_uniprot_ids_updated_file.csv', index=False)
print("UniProt ID update complete. Check 'cosmic_vcf_updated_file.csv'.")


#tsv

# import pandas as pd
# import requests
# import time

# # Function to fetch UniProt IDs using batch requests
# def fetch_uniprot_ids_batch(genes):
#     ids = ['Not found'] * len(genes)
#     chunk_size = 100
#     for i in range(0, len(genes), chunk_size):
#         batch = genes[i:i+chunk_size]
#         query = " OR ".join([f"gene_exact:{gene}" for gene in batch])
#         url = f'https://rest.uniprot.org/uniprotkb/search?query={query}&format=json&size=100'
#         try:
#             response = requests.get(url)
#             if response.status_code == 200 and response.json().get('results'):
#                 results = {res['genes'][0]['geneName']['value']: res['primaryAccession'] for res in response.json()['results']}
#                 for j, gene in enumerate(batch):
#                     if gene in results:
#                         ids[i + j] = results[gene]
#         except Exception as e:
#             print(f"Error processing batch: {e}")
#         time.sleep(1)  # Prevent rate limiting
#     return ids

# # Read TSV file
# df = pd.read_csv('uniprot ids/GRCh38_output_output_with_uniprot_ids_filtered.tsv', sep='\t')

# # Filter genes with 'Not found'
# genes_to_query = df.loc[df['UniProt_ID'] == 'Not found', 'GENE_SYMBOL'].tolist()

# # Perform batch queries
# if genes_to_query:
#     uniprot_ids = fetch_uniprot_ids_batch(genes_to_query)
#     df.loc[df['UniProt_ID'] == 'Not found', 'UniProt_ID'] = uniprot_ids

# # Save to TSV
# df.to_csv('GRCh38_output_output_with_uniprot_ids_filtered_updated.csv', sep='\t', index=False)
# print("UniProt ID update complete. Check 'cancer_updated_file.csv'.")
