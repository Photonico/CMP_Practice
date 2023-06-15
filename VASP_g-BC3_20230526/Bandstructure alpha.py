# Plot 2D matter bandstructure
import matplotlib.pyplot as plt
from pymatgen.electronic_structure.plotter import BSPlotter
from pymatgen.io.vasp import Vasprun
from pymatgen.io.vasp.inputs import Kpoints

vasp_run = Vasprun("3_Bandstructure_gamma/vasprun.xml", parse_potcar_file=False)
kpoints_file = "3_Bandstructure_gamma/KPOINTS"
kpoints = Kpoints.from_file(kpoints_file)

bandstructure = vasp_run.get_band_structure(kpoints_filename=kpoints_file, line_mode=True)

plotter = BSPlotter(bandstructure)
plot_data = plotter.bs_plot_data()

# Plot
params = {"text.usetex": False, "font.family": "serif", "mathtext.fontset": "cm", "axes.titlesize": 16, "axes.labelsize": 14, "figure.facecolor": "w"}
plt.rcParams.update(params)

plotter.get_plot(ylim=(-6, 6))

ax = plt.gca()
ax.figure.set_dpi(160)
ax.figure.set_size_inches(6.4,4.8)

ax.set_title("bandstructure for g-BC3",fontsize=params['axes.titlesize'])
ax.set_xlabel(r"Wave Vector", fontsize=params['axes.labelsize'])
ax.set_ylabel(r"Relative Energies ($E-E_\mathrm{F}$) in eV", fontsize=params['axes.labelsize'])
ax.tick_params(axis='both', labelsize=params['axes.labelsize'],direction='in')

plt.show()
