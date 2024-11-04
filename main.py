from spectral_lines import get_spectral_lines
from atmospheric_parameters import get_uncertainty_atmospheric
from signal_to_noise_ratio_changes import get_uncertainty_signal
from pseudocontinuum_displacements import get_uncertainty_pseudocontinuum



temperatura = input("Temperature: ")
elemento = input("Element: ")
teff = input("Teff: ")
logg = input("Logg: ")
metalicidade = input("[Fe/H]: ")
xi = input("ξ: ")
sinal_ruido = input("SNR: ")
deslocamento_num = input("%: ")



print(get_spectral_lines(int(temperatura)))
print(get_uncertainty_atmospheric(int(temperatura), str(teff), str(logg), str(metalicidade), str(xi), str(elemento)))
print(get_uncertainty_signal(int(temperatura), int(sinal_ruido), str(elemento)))
print(get_uncertainty_pseudocontinuum(int(temperatura), float(deslocamento_num), elemento))


