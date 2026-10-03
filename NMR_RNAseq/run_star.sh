#!/bin/sh 
#SBATCH --job-name=STAR
#SBATCH --account=43070_203920
#SBATCH --partition=compute
#SBATCH --cpus-per-task=20
#SBATCH --time=24:00:00


module load bioconda
conda activate STAR_env

INPUT=/storage/atedder/trimmed_data
OUTPUT=/storage/atedder/STAR_mapped
GENOME=/storage/atedder/NMR_genome/star/GCF_053883595.1_H.glaber_assembly_v1.0_genomic


for r1 in ${INPUT}/*_R1_001_trim_paired_.fastq.gz
   do
   name=$(basename ${r1} _R1_001_trim_paired_.fastq.gz)
   echo $name
   mkdir -p ${OUTPUT}/${name}
   STAR \
    --runThreadN ${SLURM_CPUS_PER_TASK} \
    --genomeDir ${GENOME} \
    --readFilesIn ${INPUT}/${name}_R1_001_trim_paired_.fastq.gz ${INPUT}/${name}_R2_001_trim_paired_.fastq.gz \
    --readFilesCommand zcat \
    --outFileNamePrefix ${OUTPUT}/${name}/ \
    --twopassMode Basic \
    --outSAMtype BAM SortedByCoordinate \
    --quantMode GeneCounts
done
