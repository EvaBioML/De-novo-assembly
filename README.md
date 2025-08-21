# 🧬 RNA-seq de novo Transcriptome Assembly and Analysis  

This project focuses on **RNA-seq data analysis without a reference genome (de novo transcriptome assembly)**.  
The workflow covers raw data preprocessing, transcriptome assembly, annotation, and downstream analyses such as differential expression and functional enrichment.  

---

## 📂 Analysis Pipeline  

1. **Input Data**  
   - Raw sequence files: `FASTQ.gz`  (paired-end)  

2. **Quality Control (QC)**  
   - Remove adapters and low-quality reads (e.g., **Trimmomatic**)  
   - Assess read quality (e.g., **FastQC**)  

3. **De novo Transcriptome Assembly**  
   - **Trinity** for transcriptome assembly
   - Optimization of transcriptome: **TransDecoder** detected candidate coding regions within transcript 
sequences. **CD-HIT** was used to reduce sequence redundancy with a 100% 
clustering threshold.

4. **Assembly Quality Assessment**  
   - Assembly statistics (**N50, GC content**)  
   - Completeness check using **BUSCO**  

5. **Transcript Quantification**  
   - **RSEM** with Bowtie2 was used to quantify gene and isoform expression 
levels from the RNA-Seq data 

6. **Functional Annotation**  
   - **EggNOG-mapper** 

7. **Differential Expression Analysis (DEA)**  
   - Read count normalization and statistical analysis using **DESeq2**  
   - Identification of differentially expressed genes (DEGs) 

8. **Functional Enrichment Analysis**  
   - GO term enrichment  
   - KEGG pathway enrichment
   - COG (Clusters of Orthologous Groups of proteins)  enrichment
  
---

## 📊 Expected Outputs  
 
- Assembly quality metrics (N50, BUSCO completeness)  
- Gene/transcript expression matrix  
- Differentially expressed gene (DEG) tables  
- Functional annotations (GO / KEGG / COG)  
- Visualizations: MA plots, Functional Enrichment  
