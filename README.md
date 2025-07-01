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
Parsed each mutation (e.g., p.H45G, p.T89Y) using regex
Checked whether the mutated position (e.g., 45 or 89) matched the gene's annotated binding positions
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
