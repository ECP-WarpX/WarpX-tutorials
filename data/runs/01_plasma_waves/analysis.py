#!/usr/bin/env python3


# This simulates a 1D periodic plasma wave.
# The electric field in the simulation is given (in theory) by:
# $$ E_z = \epsilon \,\frac{m_e c^2 k_z}{q_e}\sin(k_z z)\sin( \omega_p t)$$
import os
import re
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

import numpy as np
from scipy.constants import c, e, epsilon_0, m_e


from openpmd_viewer import OpenPMDTimeSeries


series = OpenPMDTimeSeries('diags/openpmd')

# Parameters (these parameters must match the parameters in `inputs.multi.rt`)
epsilon = 0.01
n = 4.0e24
n_osc_z = 2
zmin = -20e-6
zmax = 20.0e-6
Nz = 128

# Wave vector of the wave
kz = 2.0 * np.pi * n_osc_z / (zmax - zmin)
# Plasma frequency
wp = np.sqrt((n * e**2) / (m_e * epsilon_0))

k = {"Ez": kz}
cos = {"Ez": (1, 1, 0)}


def get_contribution(is_cos, k):
    du = (zmax - zmin) / Nz
    u = zmin + du * (0.5 + np.arange(Nz))
    if is_cos == 1:
        return np.cos(k * u)
    else:
        return np.sin(k * u)


def get_theoretical_field(field, t):
    amplitude = epsilon * (m_e * c**2 * k[field]) / e * np.sin(wp * t)
    cos_flag = cos[field]
    z_contribution = get_contribution(cos_flag[2], kz)

    E = amplitude * z_contribution

    return E


# Check the validity of the fields
iterations = series.iterations
error_rel = 0

for t in iterations: 
    E_sim, info = series.get_field('E', coord='z', iteration=t)
    E_th = get_theoretical_field('Ez', t)
    max_error = abs(E_sim - E_th).max() / abs(E_th).max()
    print("%s: Max error: %.2e" % ("Ez", max_error))
    error_rel = max(error_rel, max_error)



# Plot the last field from the loop (Ez at iteration 80)

fig, ax = plt.subplots(1,1,figsize=(8,6), dpi=300)

ax.plot(E_sim, label='simulation')
ax.set_title("Ez, last iteration")
ax.plot(E_th, label='theory')

plt.tight_layout()
plt.savefig("langmuir_multi_1d_analysis.png")

tolerance_rel = 0.05

print("error_rel    : " + str(error_rel))
print("tolerance_rel: " + str(tolerance_rel))

#assert error_rel < tolerance_rel
