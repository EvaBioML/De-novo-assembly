conda activate rna-assembly
#修剪
/path/trinity_out_dir --trimmomatic --quality_trimming_params "ILLUMINACLIP:/path/anaconda3/envs/rnaseq/share/trimmomatic/adapters/TruSeq3-PE.fa:2:30:10 SLIDINGWINDOW:4:5 LEADING:20 TRAILING:3 MINLEN:25"



#改格式
zcat *R2.trimmed.P.fastq.gz| gzip > right_merged.R2.fq.gz
zcat *R1.trimmed.P.fastq.gz| gzip > left_merged.R1.fq.gz

#組裝
${TRINITY_HOME}/Trinity --seqType fq --max_memory 50G \
              --left left_merged.R1.fq.gz \
              --right right_merged.R2.fq.gz \
              --SS_lib_type RF \
              --CPU 10

#TransDecoder
TransDecoder.LongOrfs -t Trinity.fasta
#grep -c '>' Trinity.fasta.transdecoder.pep(看蛋白質)

#注釋
emapper.py -i longest_orfs.pep --output longest_orfs_eggnog -m diamond --pfam_realign realign --cpu 6 --data_dir EggNOG --target_taxa ???
hmmscan --cpu 6 --domtblout pfam.domtblout /eggnog-mapper-2.1.12/data/pfam/Pfam-A.hmm /Trinity.fasta.transdecoder_dir/longest_orfs.pep 
TransDecoder.Predict -t Trinity.fasta --retain_blastp_hits longest_orfs_eggnog.emapper.hits --retain_pfam_hits pfam.domtblout --single_best_only

#去除短片段
cd-hit -i Trinity.fasta.transdecoder.pep -o longest_orfs_100_identity.pep -c 1.00 -sc 1 -M 0 -d 0 -T 6

#確認品質
busco -m transcriptome -i Trinity.fasta -l ??? -o busco -c 20

#N10~N50
$TRINITY_HOME/util/misc/get_longest_isoform_seq_per_trinity_gene.pl Trinity.fasta > long.txt

#定量
$TRINITY_HOME/util/align_and_estimate_abundance.pl --transcripts longest_orfs_100_identity.cds --seqType fq --samples_file sample.txt --est_method RSEM --aln_method bowtie2 --prep_reference --output_dir
$TRINITY_HOME/Analysis/DifferentialExpression/PtR --matrix all_isoforms.isoform.counts.matrix --samples QC_Samples_and_Biological_Replicates/sample.txt --log2 --CPM --min_rowSums 10 --compare_replicates
$TRINITY_HOME/Analysis/DifferentialExpression/PtR --matrix all_isoforms.isoform.counts.matrix --samples QC_Samples_and_Biological_Replicates/sample.txt --log2 --CPM --min_rowSums 10 --sample_cor_matrix
$TRINITY_HOME/Analysis/DifferentialExpression/PtR \
          --matrix Trinity_trans.counts.matrix \
          --min_rowSums 10 \
          -s samples.txt --log2 --CPM --sample_cor_matrix
  
$TRINITY_HOME/Analysis/DifferentialExpression/analyze_diff_expr.pl --matrix all_isoforms.isoform.TMM.EXPR.matrix -P 1e-3 -C 2
