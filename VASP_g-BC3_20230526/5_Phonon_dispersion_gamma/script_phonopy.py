""" Script for Phonon Dispersion """

import subprocess

BASH_COMMAND = "phonopy -d --dim 8 8 1 --pa auto -c POSCAR-unitcell"

subprocess.run(BASH_COMMAND, shell=True, check=True)
