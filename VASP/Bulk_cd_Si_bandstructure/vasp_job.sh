#!/bin/csh
#PBS -N Bulk_cd_Si_bandstructure
#PBS -q defaultQ
#PBS -j oe
#PBS -l select=1:ncpus=12:mpiprocs=12:mem=30GB
#PBS -l walltime=48:00:00
#PBS -m a
#PBS -M luke.niu@sydney.edu.au

cp ../Bulk_cd_Si_DOS/CHGCAR

cd "$PBS_O_WORKDIR"

module purge
module load pbspro-intelmpi 
module load compiler-rt mpi mkl
set VASP=~/VASP544/bin/vasp_std

mpirun -np 12 $VASP > vasp.out
