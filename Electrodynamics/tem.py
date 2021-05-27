import numpy as np
import pandas as pd

# Parameters
driver_frequency = 10 * 10e9  # GHz
a, b = 3, 2  # cms

c = 3 * 10e8
driver_wavelength = 100 * c / driver_frequency
if b > a:
    a, b = b, a

frequency_1 = 100 * c / (2 * a)
frequency_2 = 100 * c / (2 * b)

set_1 = [n * frequency_1 for n in range(1, 4)]
set_2 = [n * frequency_2 for n in range(1, 4)]

possible_modes = []
possible_frequencies = []

for x in set_1:
    if x < driver_frequency:
        ans = str(set_1.index(x) + 1) + "0"
        possible_modes.append(ans)
        possible_frequencies.append(x)

for x in set_2:
    if x < driver_frequency:
        ans = "0" + str(set_2.index(x) + 1)
        possible_modes.append(ans)
        possible_frequencies.append(x)

rms_array = [[set_1[i], set_2[i]] for i in range(len(set_1))]
rms = [np.sqrt(np.mean(np.square(x))) for x in rms_array]

for x in rms:
    if x < driver_frequency:
        ans = str(rms.index(x) + 1) + str(rms.index(x) + 1)
        possible_modes.append(ans)
        possible_frequencies.append(x)

possible_wavelengths = [100 * c / f for f in possible_frequencies]
possible_frequencies = [f / 10e9 for f in possible_frequencies]
guide_wavelength = [driver_wavelength / np.sqrt(1 - (driver_wavelength / x) ** 2) for x in possible_wavelengths]

data = {"Modes": possible_modes, 'cutoff freq': possible_frequencies, "cutoff wavelength": possible_wavelengths,
        "Guide λ": guide_wavelength}
df = pd.DataFrame(data)
df.index += 1
# printing
print('Driver frequency     :', driver_frequency / 10e9, '  GHz')
print('Driver wavelength    :', driver_wavelength, 'cm')
print('Possible modes       :', *possible_modes, '\n')
print(df)
