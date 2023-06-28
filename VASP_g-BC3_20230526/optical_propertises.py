#### Declarations of process functions for Optical Propertises
# pylint: disable = C0103, C0114, C0116, C0301, R0914

### Necessary packages invoking
import xml.etree.ElementTree as ET
import numpy as np

### Physical constants
hbar = 4.135667662e-15
c_vacuum = 2.99792458e8

### Extract optical propertises from vasprun.xml
def extract_opt_vectorized(file_path):
    ## Analysis vasprun.xml file
    tree = ET.parse(file_path)
    root = tree.getroot()
    data_label = "dielectricfunction"

    ## Extract NEDOS
    nedos_element = root.find(".//i[@name='NEDOS']")
    nedos = int(nedos_element.text.strip())

    ## Loop variables
    # Define prefixes:
        # e_ for Density-Density (Charge density response)
        # c_ for Current-Current (Current response)
    prefixes = ["e_", "c_"]
    # Initialize a dictionary to store dynamic variables
    data = {}

    ## Extract imaginary part of Density-Density and Current-Current
    imag_path = f".//{data_label}/imag/array/set"
    imag_elements = root.findall(imag_path)
    for loop_index, imag_element in enumerate(imag_elements[0:2]):
        # Select prefix based on the loop index
        prefix = prefixes[loop_index]
        # Initialize columns as lists
        columns = ["energy_imag_col",
                   "xx_imag_col", "yy_imag_col", "zz_imag_col", "xy_imag_col", "yz_imag_col", "zx_imag_col"]
        for col in columns:
            data[prefix + col] = []
        # Append data to lists
        for imag_index in imag_element.findall("r"):
            imag_values = list(map(float, imag_index.text.split()))
            for value_index, col in enumerate(columns):
                data[prefix + col].append(imag_values[value_index])
        # Convert lists to numpy arrays
        for col in columns:
            data[prefix + col] = np.array(data[prefix + col])

    ## Extract real part of Density-Density and Current-Current
    real_path = f".//{data_label}/real/array/set"
    real_elements = root.findall(real_path)
    for loop_index, real_element in enumerate(real_elements[0:2]):
        # Select prefix based on the loop index
        prefix = prefixes[loop_index]
        # Initialize columns as lists
        columns = ["energy_real_col",
                   "xx_real_col", "yy_real_col", "zz_real_col", "xy_real_col", "yz_real_col", "zx_real_col"]
        for col in columns:
            data[prefix + col] = []
        # Append data to lists
        for real_index in real_element.findall("r"):
            real_values = list(map(float, real_index.text.split()))
            for value_index, col in enumerate(columns):
                data[prefix + col].append(real_values[value_index])
        # Convert lists to numpy arrays
        for col in columns:
            data[prefix + col] = np.array(data[prefix + col])

    ## Extract Fermi energy
    efermi_element = root.find(".//dos/i[@name='efermi']")
    fermi_energy = float(efermi_element.text.strip())

    ## Extract Conductivity
    conductivity_path = ".//conductivity[@comment='spin=1']/array/set"
    conductivity_set_element = tree.find(conductivity_path)
    # Initialize columns as lists
    columns = ["conductivity_energy",
               "conductivity_xx", "conductivity_yy", "conductivity_zz", "conductivity_xy", "conductivity_yz", "conductivity_zx"]
    # Initialize dictionary
    conductivity_data = {col: [] for col in columns}
    for conductivity_index in conductivity_set_element.findall("r"):
        values = list(map(float, conductivity_index.text.split()))
        conductivity_data["conductivity_energy"].append(values[0])
        conductivity_data["conductivity_xx"].append(values[1])
        conductivity_data["conductivity_yy"].append(values[2])
        conductivity_data["conductivity_zz"].append(values[3])
        conductivity_data["conductivity_xy"].append(values[4])
        conductivity_data["conductivity_yz"].append(values[5])
        conductivity_data["conductivity_zx"].append(values[6])

    ## Extract DOS
    dos_path = ".//dos/total/array/set/set[@comment='spin 1']"
    dos_set_element = tree.find(dos_path)
    # Initialize columns as lists
    columns = ["dos_energy", "total_dos", "integrated_dos"]
    # Initialize dictionary
    dos_data = {col: [] for col in columns}
    for dos_index in dos_set_element.findall("r"):
        values = list(map(float, dos_index.text.split()))
        dos_data["dos_energy"].append(values[0])
        dos_data["total_dos"].append(values[1])
        dos_data["integrated_dos"].append(values[2])

    return (nedos,                                      #  [0]: NEDOS
            data["e_energy_imag_col"],                  #  [1]: imaginary part of energy of Density-Density
            data["e_xx_imag_col"],                      #  [2]: imaginary part of xx direction of Density-Density
            data["e_yy_imag_col"],                      #  [3]: imaginary part of yy direction of Density-Density
            data["e_zz_imag_col"],                      #  [4]: imaginary part of zz direction of Density-Density
            data["e_xy_imag_col"],                      #  [5]: imaginary part of xy direction of Density-Density
            data["e_yz_imag_col"],                      #  [6]: imaginary part of yz direction of Density-Density
            data["e_zx_imag_col"],                      #  [7]: imaginary part of zx direction of Density-Density
            data["c_energy_imag_col"],                  #  [8]: imaginary part of energy of Current-Current
            data["c_xx_imag_col"],                      #  [9]: imaginary part of xx direction of Current-Current
            data["c_yy_imag_col"],                      # [10]: imaginary part of yy direction of Current-Current
            data["c_zz_imag_col"],                      # [11]: imaginary part of zz direction of Current-Current
            data["c_xy_imag_col"],                      # [12]: imaginary part of xy direction of Current-Current
            data["c_yz_imag_col"],                      # [13]: imaginary part of yz direction of Current-Current
            data["c_zx_imag_col"],                      # [14]: imaginary part of zx direction of Current-Current
            data["e_energy_real_col"],                  # [15]: real part of energy of Density-Density
            data["e_xx_real_col"],                      # [16]: real part of xx direction of Density-Density
            data["e_yy_real_col"],                      # [17]: real part of yy direction of Density-Density
            data["e_zz_real_col"],                      # [18]: real part of zz direction of Density-Density
            data["e_xy_real_col"],                      # [19]: real part of xy direction of Density-Density
            data["e_yz_real_col"],                      # [20]: real part of yz direction of Density-Density
            data["e_zx_real_col"],                      # [21]: real part of zx direction of Density-Density
            data["c_energy_real_col"],                  # [22]: real part of energy of Current-Current
            data["c_xx_real_col"],                      # [23]: real part of xx direction of Current-Current
            data["c_yy_real_col"],                      # [24]: real part of yy direction of Current-Current
            data["c_zz_real_col"],                      # [25]: real part of zz direction of Current-Current
            data["c_xy_real_col"],                      # [26]: real part of xy direction of Current-Current
            data["c_yz_real_col"],                      # [27]: real part of yz direction of Current-Current
            data["c_zx_real_col"],                      # [28]: real part of zx direction of Current-Current
            data_label,                                 # [29]: data label
            fermi_energy,                               # [30]: system Fermi energy
            conductivity_data["conductivity_energy"],   # [31]: energy of conductivity
            conductivity_data["conductivity_xx"],       # [32]: xx direction of conductivity
            conductivity_data["conductivity_yy"],       # [33]: yy direction of conductivity
            conductivity_data["conductivity_zz"],       # [34]: zz direction of conductivity
            conductivity_data["conductivity_xy"],       # [35]: xy direction of conductivity
            conductivity_data["conductivity_yz"],       # [36]: yz direction of conductivity
            conductivity_data["conductivity_zx"],       # [37]: zx direction of conductivity
            dos_data["dos_energy"],                     # [38]: energy list of DOS
            dos_data["total_dos"],                      # [39]: total DOS
            dos_data["integrated_dos"],                 # [40]: integrated DOS
            )

##### Data Process
def process_optical_properties(opt_file_name):
    opt_file_path = f"{opt_file_name}/vasprun.xml"
    results = extract_opt_vectorized(opt_file_path)

    globals().update({f"{name}_{opt_file_name.split('_')[-1]}": results[i] for i, name in enumerate([
        "nedos",                                       # [0]: NEDOS
        "density_imag_energy",                          # [1]: imaginary part of energy of Density-Density
        "density_imag_xx",                              # [2]: imaginary part of xx direction of Density-Density
        "density_imag_yy",                              # [3]: imaginary part of yy direction of Density-Density
        "density_imag_zz",                              # [4]: imaginary part of zz direction of Density-Density
        "density_imag_xy",                              # [5]: imaginary part of xy direction of Density-Density
        "density_imag_yz",                              # [6]: imaginary part of yz direction of Density-Density
        "density_imag_zx",                              # [7]: imaginary part of zx direction of Density-Density
        "current_imag_energy",                          # [8]: imaginary part of energy of Current-Current
        "current_imag_xx",                              # [9]: imaginary part of xx direction of Current-Current
        "current_imag_yy",                              # [10]: imaginary part of yy direction of Current-Current
        "current_imag_zz",                              # [11]: imaginary part of zz direction of Current-Current
        "current_imag_xy",                              # [12]: imaginary part of xy direction of Current-Current
        "current_imag_yz",                              # [13]: imaginary part of yz direction of Current-Current
        "current_imag_zx",                              # [14]: imaginary part of zx direction of Current-Current
        "density_real_energy",                          # [15]: real part of energy of Density-Density
        "density_real_xx",                              # [16]: real part of xx direction of Density-Density
        "density_real_yy",                              # [17]: real part of yy direction of Density-Density
        "density_real_zz",                              # [18]: real part of zz direction of Density-Density
        "density_real_xy",                              # [19]: real part of xy direction of Density-Density
        "density_real_yz",                              # [20]: real part of yz direction of Density-Density
        "density_real_zx",                              # [21]: real part of zx direction of Density-Density
        "current_real_energy",                          # [22]: real part of energy of Current-Current
        "current_real_xx",                              # [23]: real part of xx direction of Current-Current
        "current_real_yy",                              # [24]: real part of yy direction of Current-Current
        "current_real_zz",                              # [25]: real part of zz direction of Current-Current
        "current_real_xy",                              # [26]: real part of xy direction of Current-Current
        "current_real_yz",                              # [27]: real part of yz direction of Current-Current
        "current_real_zx",                              # [28]: real part of zx direction of Current-Current
        "data_label",                                   # [29]: data label
        "fermi_energy",                                 # [30]: system Fermi energy
        "conductivity_energy",                          # [31]: energy of conductivity
        "conductivity_xx",                              # [32]: xx direction of conductivity
        "conductivity_yy",                              # [33]: yy direction of conductivity
        "conductivity_zz",                              # [34]: zz direction of conductivity
        "conductivity_xy",                              # [35]: xy direction of conductivity
        "conductivity_yz",                              # [36]: yz direction of conductivity
        "conductivity_zx",                              # [37]: zx direction of conductivity
        "dos_energy",                                   # [38]: energy list of DOS
        "total_dos",                                    # [39]: total DOS
        "integrated_dos"                                # [40]: integrated DOS
    ])})
