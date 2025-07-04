## 🧬  Mutation Binding Site Impact Analysis (Independent Project)
🔍 Overview
This project analyzes amino acid mutations across thousands of genes from public mutation databases (COSMIC, dbSNP, ClinVar), with the goal of identifying which mutations occur within known protein binding sites. It further classifies each mutation based on biochemical amino acid category changes (e.g., hydrophobic → hydrophilic, acidic → basic), and visualizes the functional impact distribution.
The pipeline is built entirely in Python using pandas, regex, and matplotlib, and is designed to help understand the functional consequences of point mutations with respect to structural and binding relevance.



## 📌 Objectives
Integrate mutation data from major clinical databases
Map each gene to its UniProt ID and retrieve its binding site positions
Check whether each amino acid mutation lies inside or outside annotated binding regions
Analyze amino acid property conversions for each mutation
Quantify and visualize patterns across mutation types



## 🧪 Project Workflow

## 1. Data Collection
Downloaded mutation data in bulk from:
COSMIC (Catalogue of Somatic Mutations in Cancer)
dbSNP
ClinVar
Merged all unique gene entries with their corresponding amino acid (AA) mutations
Removed redundant and duplicate entries


## 2. UniProt Mapping
For each unique gene name, fetched the corresponding UniProt ID
This allowed access to canonical protein sequences and structural annotation


## 3. Binding Site Retrieval
Queried UniProt for binding site information using:
Position annotations (e.g., Position_1 to Position_20)
Sequence fragments at those positions
Each gene had 5–20 binding positions (both integers and ranges like 80-95)


## 4. Mutation Matching
Parsed each mutation (e.g., p.A336T , p.A4S) using regex
Checked whether the mutated position (e.g., 336 or 4) matched the gene's annotated binding positions
Labeled each mutation as:
In Binding Site if the position overlaps with any binding site
Out of Binding Site otherwise


## 5. FASTA Retrieval
Retrieved full-length FASTA sequences for each gene from UniProt (for downstream sequence-based analysis and alignment)


## 6. Biochemical Category Analysis
Categorized all amino acids into 4 groups:

| Category    | Residues                  |
| ----------- | ------------------------- |
| Hydrophobic | A, V, I, L, M, F, W, P, G |
| Hydrophilic | S, T, C, N, Q, Y          |
| Acidic      | D, E                      |
| Basic       | K, R, H                   |

For each mutation, classified the change as:
Cross-category: e.g., hydrophobic → hydrophilic
Same-category: e.g., acidic → acidic


## 7. Statistical Analysis
Counted how many mutations of each type occurred inside vs outside binding sites



## 📊 Output & Visualization
Pie charts for each conversion type showing the proportion of mutations that fall inside vs outside binding sites
A single combined chart for all same-category conversions
Clean tabular breakdown with percentage calculations



## 📊 Key Insights from Analysis
## 1. Binding Site Enrichment in Mutations
Total Mutations Analyzed: 844,538 (across 2,412 genes)
Mutations inside Binding Sites: 16,612 (1.97%)
Mutations outside Binding Sites: 827,926 (98.03%)


📌 Observations:
Binding site regions are highly conserved and mutations are strongly underrepresented in these regions. This suggests evolutionary pressure to preserve binding-site integrity due to their critical role in protein function and interactions.




## 2. Biochemical Class Conversion Patterns
Mutation categories are grouped as either cross-category (e.g., hydrophobic → hydrophilic) or same-category (e.g., hydrophobic → hydrophobic):
| Conversion Type           | Inside Binding Site | Total Mutations | % Inside |
| ------------------------- | ------------------- | --------------- | -------- |
| Hydrophobic → Hydrophilic | 941                 | 80,241          | 1.17%    |
| Hydrophilic → Hydrophobic | 1,186               | 57,243          | 2.07%    |
| Acidic → Basic            | 733                 | 29,694          | 2.47%    |
| Basic → Acidic            | 130                 | 4,069           | 3.19%    |
| **Same Category Total**   | 6,861               | 405,208         | 1.69%    |


📌 Observations:
Charge-changing mutations (acidic ↔ basic) are relatively rare but show higher enrichment within binding sites — possibly due to their role in maintaining ionic interactions.
Hydrophobic ↔ hydrophilic mutations, while more frequent, are less likely to occur in binding sites — likely due to disruption of hydrophobic packing or solvation structures.
Same-category mutations dominate by volume (~405k total) but still show only ~1.69% binding site overlap.




## 🧠 Interpretation and Biological Significance
Mutations in binding sites are rare — consistent with their functional importance.
When mutations do occur in binding regions, they are more likely to involve charge shifts, which may directly alter molecular binding interfaces (e.g., ligand binding, metal ion coordination, protein-protein interactions).
Same-category mutations likely represent neutral or tolerated substitutions, while cross-category mutations, especially in binding sites, could indicate pathogenic potential or functional adaptation.

## 🧱 PDB Structural Filtering and Chain Cleanup
To complement our sequence-based mutation analysis with structural insights, we extended our pipeline to incorporate 3D protein structure data from the Protein Data Bank (PDB). This structural layer enables downstream tasks like surface accessibility prediction, ligand-binding analysis, and mutation impact modeling.

## 🧬 Workflow Summary

## Mapping to PDB Structures via UniProt
For each gene with a known UniProt ID, we accessed the “Structure” section of the UniProt entry to extract all associated PDB entries and their corresponding chains. This ensures that we’re using biologically validated 3D models relevant to the gene.

## Generated Structured CSV for Mapping
We created a clean, flattened CSV file with the format:

GENE_NAME, UniProt_ID, PDB_ID, CHAIN, RESIDUE_RANGE

This includes all available chains and residue coverage for each PDB structure associated with the gene.
Genes with multiple PDB structures or multiple chains appear in multiple rows.

## Bulk Download of PDB Files (~25,000+)

Using RCSB’s PDB REST API, we automated the retrieval of all unique PDB files.
A tracking mechanism was implemented to log successful and failed downloads, so corrupt or unavailable structures can be handled later.

## Chain Filtering on PDB Files

Each downloaded .pdb file was cleaned to retain only the chains explicitly listed in our master CSV.
Non-matching chains (irrelevant to our gene or UniProt context) were deleted.
Only ATOM and HETATM lines were filtered—other metadata (e.g., REMARK, HELIX, SHEET, SEQRES) were left untouched to preserve structural integrity.
This step ensures the resulting files are suitable for precise structural analysis focused solely on biologically relevant chains.

## ✅ Example:
If a gene with UniProt ID Q9HB90 maps to PDB 1a00 with chain assignment B/D, then:
Only chains B and D from the file 1a00.pdb were retained.
Chains like A, C, or others (if present) were removed.
The cleaned file was saved as 1a00_filtered.pdb.

## 🧪 Ready for Structure-Based Analysis
These chain-filtered .pdb files are now ready for use in structure-aware mutation workflows, including:

🧩 Surface Accessibility Analysis (e.g., via DSSP, PyMOL or custom scripts)

🧠 Binding Interface Prediction

🔬 Protein–Ligand or Protein–Protein Interaction Modeling

📐 Structural Visualization and Mutation Annotation

By filtering irrelevant chains and preserving all structural metadata, this step ensures high accuracy and efficiency in downstream protein structure analysis tools like:

🔬 PyMOL
🧬 Chimera / ChimeraX
🔎 PISA (PDBePISA)
🧱 DSSP / STRIDE
🧠 Custom ML or Molecular Dynamics pipelines

