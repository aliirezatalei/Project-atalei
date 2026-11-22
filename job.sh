#!/bin/bash
#SBATCH --job-name=project-hpc-atalei
#SBATCH --time=00:02:00
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=500M
#SBATCH --output=%x-%j.out
#SBATCH --account=def-sponsor00

module load python/3.11.5

virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --no-index --upgrade pip
pip install --no-index asteval

python Project-HPC-atalei.py
