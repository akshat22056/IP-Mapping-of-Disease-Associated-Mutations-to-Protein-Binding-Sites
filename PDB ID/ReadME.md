## 🧬 PDB Structural Chain Filtering and Preparation
This repository contains scripts and data related to structure-level mutation mapping for human genes. As part of our broader project on binding-site mutation analysis, this stage focuses on preparing high-confidence PDB structure files for downstream tasks such as surface accessibility testing.

## 📌 Objectives
Map gene mutations to PDB-level protein structures.
Filter downloaded PDB files to retain only biologically relevant chains, as listed in UniProt annotations.
Ensure compatibility for structural analysis tools by keeping PDB files clean, chain-consistent, and correctly annotated.

## 📁 Data Sources
UniProtKB: For each gene, we retrieved the corresponding UniProt ID.
PDB (Protein Data Bank): From each UniProt structure section, all available PDB IDs and associated chains (with residue ranges) were extracted.

## The extracted PDB chain info was saved in a file with the following structure:

| GENE\_NAME | UniProt\_ID | PDB\_ID | CHAIN   | RESIDUE\_RANGE |
| ---------- | ----------- | ------- | ------- | -------------- |
| AADAT      | Q8N5Z0      | 2QLR    | A/B/C/D | 1-425          |
| ...        | ...         | ...     | ...     | ...            |

## ⚙️ Process Summary

## ✅ Step 1: Extract PDB IDs and Chain Information
Parsed UniProt structure section for each gene.
Stored PDB ID, chain(s), and residue range.
Chains were often listed like A/B=1-425, and later split into separate columns for clarity.

## ✅ Step 2: Bulk Download PDB Files
All .pdb files were downloaded using the RCSB PDB repository.
Logs were maintained:
successful_downloads.txt
failed_downloads.txt
Over 23,000 PDB files were successfully retrieved.

## ✅ Step 3: Filter PDB Chains
For each downloaded .pdb file:
Only chains listed in the CSV were retained.
All ATOM and HETATM lines belonging to unwanted chains were removed.
All other structural metadata (REMARK, HEADER, etc.) was left unchanged unless further cleanup is required by downstream tools.

