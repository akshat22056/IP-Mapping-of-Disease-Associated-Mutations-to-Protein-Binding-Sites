import pandas as pd
import glob

# List of your 6 CSV file paths
csv_files = [
    "pos filtered data/cancer_final_cleaned.csv",
    "pos filtered data/cosmic_vcf_final.csv",
    "pos filtered data/filtered_30k_final.csv",
    "pos filtered data/GRCh37_final.csv",
    "pos filtered data/GRCh38_final.csv",
    "pos filtered data/variant_summary_final.csv"
]

# Read and concatenate all files
combined_df = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)

# Save to a new CSV file
combined_df.to_csv("main_output.csv", index=False)
