## USYD Physical cluster script

Reference: <http://www.physics.usyd.edu.au/computing/>

+ Host name of cluster is <headnode.physics.usyd.edu.au>

+ see PDF file guide; PBS system as Artemis (similar job script; but `csh` shell, and need `mpiprocs`).

+ `defaultQ`: for all Physics users, available nodes are:
  + `1-15`, `31-35`: 12 cores, 31 GB mem, name of queue: `hippocrates`;
  + `21-23`: 32 cores, 188 GB mem, name of queue: `yossarian`;
  + `41-45`: 16 cores, 125 GB mem, name of queue: `cmt`;

+ `qload` shows summary of resource availability;

+ `qstat` shows jobs running;

+ job submission script example below and in `DATA/vasp_job.sh`:
  + How to use: `qsub vasp_job.sh`

```csh
cd "$PBS_O_WORKDIR"

module unload pbspro
module load pbspro-intelmpi
module load compiler-rt mpi mkl

#!/bin/csh
#PBS -N test
#PBS -q defaultQ
#PBS -j oe
#PBS -l select=2:ncpus=12:mpiprocs=12:mem=30GB
#PBS -l walltime=01:00:00
#PBS -m a
#PBS -M luke.niu@sydney.edu.au

cd "$PBS_O_WORKDIR"

module purge
module load pbspro-intelmpi compiler-rt mpi mkl
set VASP=~/vasp.5.4.4/bin/vasp_std

mpirun -np 24 $VASP > vasp.out
```
