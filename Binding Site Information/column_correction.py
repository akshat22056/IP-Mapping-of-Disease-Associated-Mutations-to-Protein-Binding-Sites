import pandas as pd

# Load the CSV file
df = pd.read_csv("final_binding_site_data_2.csv")

# Ensure correct order: UniProt_ID, GENE_NAME
position_cols = [f"Position_{i}" for i in range(1, 21)]
sequence_cols = [f"Sequence_{i}" for i in range(1, 21)]

# Convert positions to integers (if not null)
for col in position_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').dropna().astype('Int64')

# Fill missing Position/Sequence columns if fewer than 20
for i in range(1, 21):
    if f"Position_{i}" not in df.columns:
        df[f"Position_{i}"] = pd.NA
    if f"Sequence_{i}" not in df.columns:
        df[f"Sequence_{i}"] = pd.NA

# Reorder columns
ordered_cols = ['UniProt_ID', 'GENE_NAME'] + position_cols + sequence_cols + ['MUTATION_AA']
df = df[ordered_cols]

# Save to a new CSV
df.to_csv("final_binding_site_data_cleaned.csv", index=False)
print("✅ Saved cleaned file as: final_binding_site_data_cleaned.csv")
