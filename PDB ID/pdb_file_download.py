
# import pandas as pd
# import os
# import requests
# from concurrent.futures import ThreadPoolExecutor, as_completed

# # Load the CSV
# df = pd.read_csv("pdb ids/gene_pdb_chain_mapping_cleaned.csv")
# unique_pdb_ids = df['PDB_ID'].dropna().unique()
# unique_pdb_ids = list(set(pdb.strip().lower() for pdb in unique_pdb_ids))

# # Output directory
# output_dir = "pdb_files"
# os.makedirs(output_dir, exist_ok=True)

# # Function to download a single PDB file
# def download_pdb(pdb_id):
#     url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
#     path = os.path.join(output_dir, f"{pdb_id}.pdb")

#     if os.path.exists(path):
#         return f"Already exists: {pdb_id}"

#     try:
#         response = requests.get(url, timeout=10)
#         if response.status_code == 200:
#             with open(path, 'w') as f:
#                 f.write(response.text)
#             return f"Downloaded: {pdb_id}"
#         else:
#             return f"Failed [{response.status_code}]: {pdb_id}"
#     except Exception as e:
#         return f"Error: {pdb_id} -> {e}"

# # Download using multithreading
# max_threads = 20
# print(f"Starting download with {max_threads} threads...")

# with ThreadPoolExecutor(max_workers=max_threads) as executor:
#     futures = [executor.submit(download_pdb, pdb_id) for pdb_id in unique_pdb_ids]
#     for i, future in enumerate(as_completed(futures), 1):
#         print(f"[{i}/{len(futures)}] {future.result()}")

# print("\n✅ All downloads attempted.")

import pandas as pd
import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Load CSV
df = pd.read_csv("pdb ids/gene_pdb_chain_mapping_cleaned.csv")
unique_pdb_ids = df['PDB_ID'].dropna().unique()
unique_pdb_ids = list(set(pdb.strip().lower() for pdb in unique_pdb_ids))

# Output folders
output_dir = "pdb_files"
os.makedirs(output_dir, exist_ok=True)

# Logging files
failed_log_path = "failed_downloads.txt"
success_log_path = "successful_downloads.txt"

# Function to download a single PDB file
def download_pdb(pdb_id):
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    path = os.path.join(output_dir, f"{pdb_id}.pdb")

    if os.path.exists(path):
        return ("exists", pdb_id)

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(path, 'w') as f:
                f.write(response.text)
            return ("success", pdb_id)
        else:
            return ("fail", pdb_id)
    except Exception:
        return ("fail", pdb_id)

# Start downloading with threads
max_threads = 20
print(f"Downloading with {max_threads} threads...")

results = []
with ThreadPoolExecutor(max_workers=max_threads) as executor:
    futures = [executor.submit(download_pdb, pdb_id) for pdb_id in unique_pdb_ids]
    for i, future in enumerate(as_completed(futures), 1):
        status, pdb_id = future.result()
        results.append((status, pdb_id))
        print(f"[{i}/{len(futures)}] {status.upper()} → {pdb_id}")

# Save logs
with open(success_log_path, 'w') as s_file, open(failed_log_path, 'w') as f_file:
    for status, pdb_id in results:
        if status == "success":
            s_file.write(pdb_id + "\n")
        elif status == "fail":
            f_file.write(pdb_id + "\n")

print(f"\n✅ Finished. Success: {sum(1 for r in results if r[0]=='success')}, Failed: {sum(1 for r in results if r[0]=='fail')}")
print(f"📁 Check '{failed_log_path}' and '{success_log_path}' for details.")
