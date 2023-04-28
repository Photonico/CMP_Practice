#!/bin/csh
#PBS -N BC3Practice
#PBS -q defaultQ
#PBS -j oe
#PBS -l select=1:ncpus=12:mpiprocs=12:mem=30GB
#PBS -l walltime=48:00:00
#PBS -m a
#PBS -M luke.niu@sydney.edu.au

cd "$PBS_O_WORKDIR"

module purge
module load pbspro-intelmpi 
module load compiler-rt mpi mkl
set VASP=~/VASP544/bin/vasp_std

BIN=~/VASP544/bin/vasp_std

rm WAVECAR SUMMARY.fcc
for i in 3.4 3.5 3.6 3.7 3.8 3.9 4.0 4.1 4.2 4.3 ; do
cat >POSCAR <<!
fcc:
    $i
    0.5 0.5 0.0
    0.0 0.5 0.5
    0.5 0.0 0.5
    1
    cartesian
    0 0 0
!
echo "a= $i" ; mpirun -np 12 $BIN
E=`awk '/F=/ {print $0}' OSZICAR` ; echo $i $E  >>SUMMARY.fcc
done
cat SUMMARY.fcc
