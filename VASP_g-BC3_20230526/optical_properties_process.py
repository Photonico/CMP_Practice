#### Data Process for Optical Propertises
# pylint: disable = C0103, C0114, C0116, C0301, R0914

from optical_properties import extract_opt_vectorized

def optical_properties_process(opt_file_name):
    opt_file_path = f"{opt_file_name}/vasprun.xml"
    results = extract_opt_vectorized(opt_file_path)

    # Extract the nbands value from the file name
    # nbands = opt_file_name.split('_')[-1]

    # Create the dictionary with keys based on the nbands value
    data_dict = {f"{name}": results[i] for i, name in enumerate([
        "nedos",                                        # [0]: NEDOS
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
    ])}
    return data_dict
