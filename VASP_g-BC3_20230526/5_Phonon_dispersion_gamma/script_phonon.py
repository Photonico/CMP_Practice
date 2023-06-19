""" Script for Phonon Dispersion """

import subprocess

bash_command = "phonopy -d --dim 2 2 2 --pa auto -c POSCAR-unitcell"

subprocess.run(bash_command, shell=True)
