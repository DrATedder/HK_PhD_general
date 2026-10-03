#!/bin/sh 
#SBATCH --job-name=STAR_index
#SBATCH --account=43070_203920
#SBATCH --partition=compute
#SBATCH --cpus-per-task=20
#SBATCH --time=10:00:00

module load bioconda
conda activate STAR_env

STAR \
    --runMode genomeGenerate \
    --runThreadN ${SLURM_CPUS_PER_TASK} \
    --genomeDir /storage/atedder/NMR_genome/star/GCF_053883595.1_H.glaber_assembly_v1.0_genomic \
    --genomeFastaFiles /storage/atedder/NMR_genome/genome/GCF_053883595.1_H.glaber_assembly_v1.0_genomic.fna \
    --sjdbGTFfile /storage/atedder/NMR_genome/annotation/genomic.gtf \
    --sjdbOverhang 149
