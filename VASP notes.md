# VASP note

## Prepration

+ Install VASP, add environment variable: `export PATH="~/VASP544/bin:$PATH"`  
+ Install Python package `py4vasp`: `pip install py4vasp`  

## Input files

+ `INCAR`: The calculation information

+ `KPOINTS`: K-points information

+ `POSCAR`: Check the file with Vesta

+ `POTCAR`: Contains the pseudopotential for each atomic species used in the calculation

  + Move POTCAR for one element: `POTCAR`: `mv pot/Ni/POTCAR /headnode2/lniu6305/OCM_Practice/VASP/Bulk_fcc_Ni`

## Output files

+ `OUTCAR`: This is the main output file of VASP, containing extensive information about the calculation, such as energies, forces, stresses, and convergence information. The OUTCAR file is typically the first step in analyzing VASP calculation results.

+ `OSZICAR`: This file contains convergence information for the self-consistent field (SCF) process and structural optimization process. It displays the energy changes for each electronic and ionic step.

+ `CONTCAR`: This file contains the lattice constants and atomic positions at the end of the calculation. If structural optimization or molecular dynamics simulations were performed, the CONTCAR file contains the optimized structure or the final step of the simulation.

+ `DOSCAR`: If the calculation of the density of states (DOS) was set up in the calculation, the DOSCAR file contains information on the total and partial electronic density of states.

+ `EIGENVAL`: This file contains the band structure information of the system, i.e., the energy eigenvalues of the Kohn-Sham orbitals. You can use this file to plot the band structure.

+ `XDATCAR`: If molecular dynamics simulations were performed, the XDATCAR file contains the atomic position information for each time step during the simulation.

+ `CHG` and `CHGCAR`: These files contain information about the electronic charge density. The CHG file is the charge density file for a single SCF step, while the CHGCAR file contains the charge density at the end of the self-consistent field calculation. These files are typically used for analyzing and visualizing charge density distribution.

+ `WAVECAR:` This file contains the wavefunction information of the system. It is typically used when subsequent calculations (such as band unfolding) need to start from the current calculation.

## Run code

+ Script parameters in USYD Physics department cluster
  + Host name of cluster is `headnode.physics.usyd.edu.au`
  + See PDF file guide; PBS system as Artemis (similar job script; but csh shell, and need mpiprocs)
  + `defaultQ`: for all Physics users; available nodes are:
    + 1-15 31-35 (12cores, 31GB mem, name of queue: `hippocrates`)
    + 21-23 (32cores, 188GB mem, name of queue: `yossarian`)
    + 41-45 (16cores, 125GB mem, name of queue: `cmt`)
  + Check the running information:
    + `qload` shows summary of resource availability
    + `qstat` shows jobs running
  + job submission script example below and in `<project_name>/vasp_job.sh`
  + How to use: `qsub vasp_job.sh`
  + More information: [USYD](http://www.physics.usyd.edu.au/computing/)

## Data analysis and demonstration

+ With the package `py4vasp`
