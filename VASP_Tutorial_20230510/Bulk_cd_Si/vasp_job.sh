#!/bin/csh
#PBS -N Bulk_cd_Si
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
set BIN=~/VASP544/bin/vasp_std

rm -f WAVECAR SUMMARY.fcc

foreach i (5.2 5.3 5.4 5.5 5.6 5.7 5.8)
cat > POSCAR << END
cd:
    $i
    0.0 0.5 0.5
    0.5 0.0 0.5
    0.5 0.5 0.0
    2
Direct
    -0.125  -0.125  -0.125
    0.125   0.125   0.125
END
echo "a= $i"
mpirun -np 12 $BIN
set E=`awk '/F=/ {print $0}' OSZICAR` ; echo $i $E  >> SUMMARY.fcc
end

cat SUMMARY.fcc
