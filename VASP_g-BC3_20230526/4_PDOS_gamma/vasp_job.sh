#!/bin/csh
#PBS -N BC3_PDOS_gamma
#PBS -q cmt
#PBS -j oe
#PBS -l select=1:ncpus=12:mpiprocs=12:mem=30GB
#PBS -l walltime=48:00:00
#PBS -m a
#PBS -M luke.niu@sydney.edu.au

# Calculating bandstructure need initial density of charges
# cp ../<>/CHGCAR

cd "$PBS_O_WORKDIR"

module purge
module load pbspro-intelmpi 
module load compiler-rt mpi mkl
set VASP=~/VASP544/bin/vasp_std
set BIN=~/VASP544/bin/vasp_std

mpirun -np 12 $VASP > vasp.out
