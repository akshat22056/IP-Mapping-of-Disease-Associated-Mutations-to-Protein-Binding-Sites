## 🔁 Amino Acid Property Conversion vs Binding Site Overlap (Analysis-2)
This analysis investigates the biochemical nature of amino acid (AA) mutations—such as shifts from hydrophobic to hydrophilic residues—and determines whether these mutations occur inside or outside of known binding sites in proteins.

## 🧬 Objective
To classify mutations by their biochemical property conversion (e.g., acidic → basic) and assess the positional significance of these changes in the context of known functional binding sites. This helps evaluate whether functionally disruptive mutations are more likely to occur within critical regions of a protein.

## 🗂️ Data Used
Source: Same curated dataset from Analysis-1
Key fields used:
GENE_NAME
UniProt_ID
MUTATION_AA (e.g., p.A336T)
Position_1 to Position_20 (binding site info from UniProt)
FASTA sequences (used for validation)

## ⚙️ Methodology
1. Amino Acid Classification
Each AA is grouped by biochemical properties:

| **Amino Acid**    | **Category** | **Amino Acid** | **Category** | **Amino Acid**    | **Category** |
| ----------------- | ------------ | -------------- | ------------ | ----------------- | ------------ |
| A (Alanine)       | Hydrophobic  | S (Serine)     | Hydrophilic  | D (Aspartic Acid) | Acidic       |
| V (Valine)        | Hydrophobic  | T (Threonine)  | Hydrophilic  | E (Glutamic Acid) | Acidic       |
| I (Isoleucine)    | Hydrophobic  | C (Cysteine)   | Hydrophilic  | K (Lysine)        | Basic        |
| L (Leucine)       | Hydrophobic  | N (Asparagine) | Hydrophilic  | R (Arginine)      | Basic        |
| M (Methionine)    | Hydrophobic  | Q (Glutamine)  | Hydrophilic  | H (Histidine)     | Basic        |
| F (Phenylalanine) | Hydrophobic  | Y (Tyrosine)   | Hydrophilic  |                   |              |
| W (Tryptophan)    | Hydrophobic  |                |              |                   |              |
| P (Proline)       | Hydrophobic  |                |              |                   |              |
| G (Glycine)       | Hydrophobic  |                |              |                   |              |

## 2. Mutation Parsing
Mutations like p.A336T are interpreted as:
Original AA: A (Alanine)
Mutated AA: T (Threonine)
Position: 336
Both amino acids are looked up in the category dictionary to determine the conversion type (e.g., hydrophobic → hydrophilic).

## 3. Binding Site Comparison
For each mutation, the numeric position is checked against the known binding site positions for that gene.

Labeled as:
In_Binding_Site ✅
Out_Binding_Site ❌

## 4. Conversion Categories Tracked
Hydrophobic → Hydrophilic
Hydrophilic → Hydrophobic
Acidic → Basic
Basic → Acidic
Same-category transitions (e.g., hydrophobic → hydrophobic)

## 📊 Results Summary
| **Conversion Type**       | **In Binding Site** | **Total Mutations** | **Percentage Inside** |
| ------------------------- | ------------------- | ------------------- | --------------------- |
| Hydrophobic → Hydrophilic | 941                 | 80,241              | 1.17%                 |
| Hydrophilic → Hydrophobic | 1,186               | 57,243              | 2.07%                 |
| Acidic → Basic            | 733                 | 29,694              | 2.47%                 |
| Basic → Acidic            | 130                 | 4,069               | 3.19%                 |
| **Same Category (all)**   | **6,861**           | **405,208**         | **1.69%**             |

(💡 Same-category transitions include all hydrophobic → hydrophobic, hydrophilic → hydrophilic, etc.)

## 📈 Visualizations
Pie charts display the distribution of mutations inside vs outside binding regions for each category.


## 🧠 Insights
Cross-category biochemical shifts are more likely to appear in binding sites compared to random mutations.
However, most mutations—especially same-category—still occur outside functional sites, suggesting evolutionary preservation of these regions.
This analysis is useful for functional annotation and pathogenicity prediction of novel mutations.

## 🛠️ Technologies
Python (Pandas, Regex, Matplotlib)
UniProt API (for binding site data)
Custom CSV pipelines
