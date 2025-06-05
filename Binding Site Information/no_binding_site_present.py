import pandas as pd

# Load the cleaned file
df = pd.read_csv("final_binding_site_data_cleaned.csv")

# Drop rows where Position_1 is missing or null
df_cleaned = df.dropna(subset=["Position_1"])

# Save the filtered data
df_cleaned.to_csv("final_binding_site_data_cleaned_filtered.csv", index=False)
print("✅ Saved filtered file as: final_binding_site_data_cleaned_filtered.csv")
