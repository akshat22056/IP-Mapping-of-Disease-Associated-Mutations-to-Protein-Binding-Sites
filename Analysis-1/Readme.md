## 🔬 Mutation-to-Binding Site Mapping in Human Genes (Analysis-1)
This repository contains the first part of a bioinformatics project focused on identifying whether amino acid (AA) mutations in human genes occur within or outside of known protein binding sites.

## 📌 Objective
To evaluate the functional impact of mutations by determining if they fall within critical binding regions of proteins—suggesting potential disruption to molecular function, disease relevance, or drug targeting potential.

## 🧬 Data Sources
We used mutation data from major genomic databases:
COSMIC (Catalogue of Somatic Mutations in Cancer)
dbSNP (Database of Single Nucleotide Polymorphisms)
ClinVar (Clinical Variants Database)
These were preprocessed to remove duplicates and merged into a unified dataset of:
~2,412 unique genes
>840,000 amino acid mutations

## 🧾 Workflow Summary
## 1. Gene & Mutation Integration
Unified mutations (p.A336T, p.T89Y, etc.) were gathered for each gene.
Each entry contains: GENE_NAME, UniProt_ID, MUTATION_AA, binding site positions, and other metadata.

## 2. UniProt Binding Site Extraction
For each gene, we retrieved binding site residue positions from UniProtKB, which included:
Single positions (e.g., 54)
Ranges (e.g., 70–100)
Positions were parsed using custom logic to create a set of valid positions per gene.

## 3. Mutation Position Extraction
From entries like p.H45G, the numeric position (e.g., 45) was extracted.
These were compared against the gene's known binding site positions.

## 4. Classification
Each mutation was labeled as:
Inside Binding Site: if its position matched the parsed binding site set
Outside Binding Site: otherwise

## 5. Result Summary
For each gene, we calculated:
Total number of mutations
Number of mutations inside vs. outside binding regions
Percentage of binding-site-associated mutations

## 📊 Key Results
Total genes analyzed: 2,412
Total amino acid mutations: 844,538
Mutations inside binding sites: 16,612
Mutations outside binding sites: 827,926
Percentage of mutations in binding regions: 1.97%

| **Metric**                        | **Value** |
| --------------------------------- | --------- |
| Total Genes Analyzed              | 2,412     |
| Total Amino Acid Mutations        | 844,538   |
| Mutations Inside Binding Sites    | 16,612    |
| Mutations Outside Binding Sites   | 827,926   |
| **Percentage in Binding Regions** | **1.97%** |


## 🧠 Insights
Binding sites are highly conserved, with a disproportionately low mutation frequency.
Only ~2% of all mutations affect known binding residues—suggesting evolutionary pressure to preserve these functionally critical regions.
This insight could inform drug design and pathogenic variant filtering.

## 🛠️ Tools & Technologies
Python (Pandas, Regex, Matplotlib)
UniProt API (for binding site & FASTA data)
Manual curation from COSMIC, dbSNP, ClinVar
