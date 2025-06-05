-------------------------------------------------
COSMIC Complete Mutation Data (Targeted Screens)
-------------------------------------------------
 A tab separated table of the complete curated COSMIC dataset (targeted screens) from the current release. It includes all coding point mutations, and the negative data set. [ Cosmic_CompleteTargetedScreensMutant_v101_GRCh37.tsv.gz ]
 The Cosmic_Mutant file can be re-created by linking the Cosmic_GenomeScreensMutant with the positive data (data with mutation ids) from this file Cosmic_CompleteTargetedScreensMutant

  File Description

[column number:label] Heading                                           Description
--------------------------------------------------------------------------------------------------------
[1:A]                 GENE_SYMBOL                  The gene name for which the data has been curated in COSMIC. In most cases this is the accepted HGNC identifier.
[2:B]                 COSMIC_GENE_ID               A unique COSMIC gene identifier (COSG) is used to identify a gene within the file. This identifier can be used to retrieve additional Gene information from the Cosmic_Genes file.
[3:C]                 TRANSCRIPT_ACCESSION         Unique Ensembl Transcript identifier (ENST). For details see: https://www.ensembl.org/info/genome/stable_ids/index.html. This identifier can be used to retrieve additional Transcript information from the Cosmic_Transcripts file.
[4:D]                 COSMIC_SAMPLE_ID             A unique COSMIC sample identifier (COSS) is used to identify a sample. This identifier can be used to retrieve additional Sample information from the Cosmic_Sample file.
[5:E]                 SAMPLE_NAME                  The sample name can be derived from a number of sources. In many cases it originates from the cell line name. Other sources include names assigned by the annotators, or an incremented number assigned during an anonymization process.
[6:F]                 COSMIC_PHENOTYPE_ID          A unique COSMIC identifier (COSO) for the classification. This identifier can be used to retrieve tissue and histology information from the classification file.
[7:G]                 GENOMIC_MUTATION_ID          Genomic mutation identifier (COSV) to indicate the definitive position of the variant on the genome. This identifier is trackable and stable between different versions of the release. This identifier can be used to retrieve additional legacy mutation ids from the Cosmic_MutationTracking file.
[8:H]                 LEGACY_MUTATION_ID           Legacy mutation identifier (COSM) or (COSN) that will represent existing COSM or COSN mutation identifiers.
[9:I]                 MUTATION_ID                  An internal mutation identifier to uniquely represent each mutation on a specific transcript on a given assembly build. This identifier can be used to retrieve additional legacy mutation ids from the Cosmic_MutationTracking file.
[10:J]                MUTATION_CDS                 The change that has occurred in the nucleotide sequence. Formatting is identical to the method used for the peptide sequence.
[11:K]                MUTATION_AA                  The change that has occurred in the peptide sequence. Formatting is based on the recommendations made by the Human Genome Variation Society. The description of each type can be found by following the link to the Mutation Overview page.
[12:L]                MUTATION_DESCRIPTION         Types of mutations at the amino acid level. Aggregated sequence ontology terms, for more details see: https://www.ensembl.org/info/genome/variation/prediction/predicted_data.html#consequences
[13:M]                MUTATION_ZYGOSITY            Information on whether the mutation was reported to be homozygous, heterozygous or unknown within the sample.
[14:N]                LOH                          LOH Information on whether the gene was reported to have loss of heterozygosity in the sample: yes, no or unknown.
[15:O]                CHROMOSOME                   The chromosome location of a given targeted screen (1-22, X, Y or MT).
[16:P]                GENOME_START                 The start coordinate of a given targeted screen.
[17:Q]                GENOME_STOP                  The end coordinate of a given targeted screen.
[18:R]                STRAND                       Positive or negative (+/-).
[19:S]                PUBMED_PMID                  The PUBMED ID for the paper that the sample was noted in, linking to pubmed to provide more details of the publication.
[20:T]                COSMIC_STUDY_ID              A unique COSMIC study identifier (COSU) is used to identify a study that have involved this sample.
[21:U]                HGVSP                        Human Genome Variation Society peptide syntax.
[22:V]                HGVSC                        Human Genome Variation Society coding dna sequence syntax (CDS).
[23:W]                HGVSG                        Human Genome Variation Society genomic syntax (3' shifted).
[24:X]                GENOMIC_WT_ALLELE            Genomic Wild type allele sequence.
[25:Y]                GENOMIC_MUT_ALLELE           Genomic mutation allele sequence.
[26:Z]                MUTATION_SOMATIC_STATUS      Information on whether the sample was reported to be Confirmed somatic variant, Reported in another cancer sample as somatic or Variant of unknown origin:
                                                      * Reported in another cancer sample as somatic = when the mutation has been reported as somatic previously but not in current paper
                                                      * Confirmed somatic variant = if the mutation has been confirmed to be somatic in the experiment by sequencing both the tumour and a matched normal from the same patient
                                                      * Variant of unknown origin = When the tumour has been sequenced without a matched normal tissue from the same individual, the somatic status of the variant cannot be assessed
[27:AA]               POSITIVE_SCREEN              Positive result (mutation detected in the sample) 'y' or negative 'n'