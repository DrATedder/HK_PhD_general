#!/bin/sh 
#SBATCH --job-name=Trimmomatic
#SBATCH --account=43070_203920
#SBATCH --partition=compute
#SBATCH --cpus-per-task=20
#SBATCH --time=10:00:00


module load anvio

INPUT=/storage/atedder/RAW_data
OUTPUT=/storage/atedder/trimmed_data
ADAPTERS=/storage/atedder/adapters.fa

for r1 in ${INPUT}/*_R1_001.fastq.gz
   do
   name=$(basename ${r1} _R1_001.fastq.gz)
   echo $name
   anvio trimmomatic PE -threads ${SLURM_CPUS_PER_TASK} ${INPUT}/${name}_R1_001.fastq.gz ${INPUT}/${name}_R2_001.fastq.gz ${OUTPUT}/${name}_R1_001_trim_paired_.fastq.gz ${OUTPUT}/${name}_R1_001_trim_unpaired_.fastq.gz ${OUTPUT}/${name}_R2_001_trim_paired_.fastq.gz ${OUTPUT}/${name}_R2_001_trim_unpaired_.fastq.gz ILLUMINACLIP:${ADAPTERS}:2:30:10:2:True LEADING:3 TRAILING:3 MINLEN:110
done

anvio fastqc -o /storage/atedder/post_trim_fastqc_output -t ${SLURM_CPUS_PER_TASK} ${OUTPUT}/*.fastq.gz
