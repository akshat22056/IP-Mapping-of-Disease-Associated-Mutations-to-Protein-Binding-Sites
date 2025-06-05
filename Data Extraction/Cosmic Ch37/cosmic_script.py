# import pandas as pd

# #GENE_SYMBOL
# #MUTATION_AA

# #C:\Users\91935\Desktop\IP\Cosmic_CompleteTargetedScreensMutant_Tsv_v101_GRCh37\Cosmic_CompleteTargetedScreensMutant_v101_GRCh37.tsv\Cosmic_CompleteTargetedScreensMutant_v101_GRCh37.tsv

import pandas as pd

def merge_gene_mutations(input_path, output_path):
    # Read TSV
    df = pd.read_csv(input_path, sep='\t', usecols=['GENE_SYMBOL', 'MUTATION_AA'])

    # Drop duplicates to keep only unique GENE_SYMBOL and MUTATION_AA combinations
    df = df.drop_duplicates()

    # Group by GENE_SYMBOL and combine all unique mutations using ' | '
    merged_df = df.groupby('GENE_SYMBOL')['MUTATION_AA'].apply(lambda x: ' | '.join(x.dropna().unique())).reset_index()

    # Save to output TSV
    merged_df.to_csv(output_path, sep='\t', index=False)
    print("File saved successfully to:", output_path)

# Usage
merge_gene_mutations(
    'Cosmic_CompleteTargetedScreensMutant_Tsv_v101_GRCh37/Cosmic_CompleteTargetedScreensMutant_v101_GRCh38.tsv/Cosmic_CompleteTargetedScreensMutant_v101_GRCh38.tsv',
    'Cosmic_CompleteTargetedScreensMutant_v101_GRCh38_output.tsv'
)

# import pandas as pd

# def merge_gene_mutations(input_path, output_path):
#     # Read TSV
#     df = pd.read_csv(input_path, sep='\t')

#     # Group by GeneSymbol and join mutations using ' | '
#     merged_df = df.groupby('GENE_SYMBOL')['MUTATION_AA'].apply(lambda x: ' | '.join(x.dropna().unique())).reset_index()

#     # Save to output
#     merged_df.to_csv(output_path, sep='\t', index=False)
#     print("File saved successfully to:", output_path)

# # Usage
# merge_gene_mutations('C:/Users/91935/Desktop/IP/Cosmic_CompleteTargetedScreensMutant_Tsv_v101_GRCh37/Cosmic_CompleteTargetedScreensMutant_v101_GRCh37.tsv/Cosmic_CompleteTargetedScreensMutant_v101_GRCh37.tsv', 'Cosmic_CompleteTargetedScreensMutant_v101_GRCh37_output-2.tsv')
