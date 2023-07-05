from math import pi, sqrt

# From
# https://www.researchgate.net/publication/370894026_An_Evolutionary_Annealing-Simplex_Method_for_Inductance_Value_Selection_for_LCL_Filters
# https://www.researchgate.net/publication/354054424_A_MATLAB_script_for_automatic_LCL_filter_design_deltawye
# both referencing
# LCL Filter Design and Performance Analysis for Grid-Interconnected Systems
# https://www.researchgate.net/file.PostFileLoader.html?id=57e9474893553b66371b212c&assetKey=AS%3A410599377915905%401474905928458
# which itself references
# https://www.researchgate.net/publication/261527213_LCL_filter_design_and_performance_analysis_for_small_wind_turbine_systems

# also interesting: https://www.researchgate.net/publication/301481213_Design_of_LCL_and_LLCL_Filters_for_Single-Phase_Grid_Connected_Converters

# parameters
V_g = 230
f_g = 50
f_sw = 124_000
P_r = 400
V_bus = 400

# attenuation factor - the capacity of attenuating harmonic content
ka = 0.2
# ripple current - that is 10% of maximum current
deltaI = 0.1
# maximum current
I_max = sqrt(2) * P_r / V_g
# maximum power factor variation seen by grid
x = 0.05


print("Parameters:")
print(f"  Grid voltage (RMS):      {V_g} V")
print(f"  Grid frequency:          {f_g} Hz")
print(f"  Switching frequency:     {f_sw // 1000} kHz")
print(f"  Rated power:             {P_r} W")
print(f"  Bus voltage:             {V_bus} V")


# base impedance and capacitance
Z_b = V_g**2 / P_r
C_b = 1 / (2 * pi * f_g * Z_b)

# filter capacitance (5% reactive power)
C_f = x * C_b

# inverter-side filter inductance
L_i = V_bus / (6 * f_sw * deltaI * I_max)

# grid-side inductance
L_max = 0.1 * Z_b / (2 * pi * f_g)
print(f"  Maximum inductance:      {L_max*1e3:.6} mH")
L_g = L_max - L_i
L_g_alt = (sqrt(1 / ka**2) + 1) / (C_f * (2 * pi * f_sw) ** 2)
L_g_alt2 = (sqrt(1 / (ka**2)) + 1) / ((deltaI / x) * C_b * f_sw**2)

L_g_yt = (0.1 * V_g**2) / (P_r * 2 * pi * f_g) - L_i

# resonant frequency
f_res = 1 / (2 * pi) * sqrt((L_i + L_g_alt) / (L_i * L_g_alt * C_f))
w_res = 2 * pi * f_res
valid = (f_res > 10 * f_g) & (f_res < 0.5 * f_sw)

# damping resistor
R_f = 1 / (3 * w_res * C_f)

# print results
print("Results:")
print(f"  Filter capacitance:       {C_f*1e6:.6} uF")
print(f"  inverter-side inductance: {L_i*1e3:.6} mH")
print(f"  grid-side inductance:     {L_g*1e3:.6} mH")
print(f"  grid-side inductance:     {L_g_alt*1e6:.6} uH")
print(f"  grid-side inductance:     {L_g_alt2*1e6:.6} uH")
print(f"  grid-side inductance:     {L_g_yt*1e3:.6} mH")
print(
    f"  Resonant frequency:       {f_res/1000:.6} kHz ({'ok' if valid else 'out of range'})"
)
print(f"  Damping resistor:         {R_f:.6} Ohm")
