from math import pi, sqrt
import urllib.parse

# From
# [1] LCL Filter Design and Performance Analysis for Grid-Interconnected Systems | https://www.researchgate.net/file.PostFileLoader.html?id=57e9474893553b66371b212c&assetKey=AS%3A410599377915905%401474905928458
# [2] Control and Filter Design of Single Phase Grid-Connected Inverter for PV applications | https://www.researchgate.net/publication/326294725_Control_and_Filter_Design_of_Single_Phase_Grid-Connected_Inverter_for_PV_applications
# [3] Optimal design of LCL filter in grid connected inverters | https://www.researchgate.net/publication/331565579_Optimal_design_of_LCL_filter_in_grid_connected_inverters
# also interesting:
# https://www.researchgate.net/publication/370894026_An_Evolutionary_Annealing-Simplex_Method_for_Inductance_Value_Selection_for_LCL_Filters
# https://www.researchgate.net/publication/301481213_Design_of_LCL_and_LLCL_Filters_for_Single-Phase_Grid_Connected_Converters
# An LCL-Filter Design with Optimum Total Inductance and Capacitance | https://arrow.tudublin.ie/cgi/viewcontent.cgi?article=1311&context=engscheleart2

# The above papers reference a master thesis
# (V. H. Prasad, "Average current mode control of a voltage source inverter connected to the grid:
# Application to different filter cells," Virginia Tech, 1997.)
# which is available here: https://vtechworks.lib.vt.edu/handle/10919/36578 (chapter 2 show the derivation of the equations)

# parameters
V_g = 230
f_g = 50
f_sw = 124_000
P_r = 400
V_bus = 400

# target grid ripple current (typ. 2%)
deltaI_grid = 0.02

# inverter-side inductor ripple current (typ. 10%)
deltaI_inv = 0.50

# maximum current
I_max = sqrt(2) * P_r / V_g

# attenuation factor - the capacity of attenuating harmonic content (typ. 20%)
ka = deltaI_grid / deltaI_inv

# maximum power factor variation seen by grid (max 5%)
x = 0.045

print("Parameters:")
print(f"  Grid voltage (RMS):         {V_g} V")
print(f"  Grid frequency:             {f_g} Hz")
print(f"  Switching frequency:        {f_sw // 1000} kHz")
print(f"  Rated power:                {P_r} W")
print(f"  Bus voltage:                {V_bus} V")

print("\nCalculation:")
print(f"  grid ripple current (ΔIg):  {deltaI_grid*100}%")
print(f"  inverter ripple current:    {deltaI_inv*100}%")
print(f"  Attenuation factor (ka):    {ka:.6}")
print(f"  Maximum current:            {I_max:.6} A")
print(f"  ∆IL_max:                    {I_max*deltaI_inv*1e3:.6} mA")

# angular frequency
w_g = 2 * pi * f_g
w_sw = 2 * pi * f_sw

# base impedance and capacitance
Z_b = V_g**2 / P_r
C_b = 1 / (Z_b * w_g)

# filter capacitance (5% reactive power)
C_f = x * C_b

# inverter-side filter inductance
# by [1], [2]
L_i = V_bus / (6 * f_sw * I_max * deltaI_inv)

# grid-side inductance
# by [1]
L_g = (1 + sqrt(1 / ka**2)) / (C_f * w_sw**2)
# by [2]
L_max = 0.1 * Z_b / w_g
L_g_max = L_max - L_i
# by [3] with r = L_i / (L_i + L_g) = 0.75
L_g_r = L_i * (1 / 0.75 - 1)

# resonant frequency
w_res = sqrt((L_i + L_g_r) / (L_i * L_g_r * C_f))
f_res = w_res / (2 * pi)
valid = (f_res > 10 * f_g) & (f_res < 0.5 * f_sw)

# damping resistor
R_f = 1 / (3 * w_res * C_f)

# print results
print("\nResults [1], [2], [3]:")
print(f"  Filter capacitance:         {C_f*1e6:.6} uF")
print(f"  Inverter-side inductance:   {L_i*1e3:.6} mH")
print(f"  Grid-side inductance:")
print(f"    [1] ka = {ka:.3}:             {L_g*1e6:.6} uH")
print(f"    [2] max:                  {L_g_max*1e3:.6} mH")
print(f"    [3] r = 0.75:             {L_g_r*1e6:.6} uH")
print(
    f"  Resonant frequency:         {f_res/1000:.6} kHz ({'ok' if valid else 'out of range'})"
)
print(f"  Damping resistor:           {R_f:.6} Ohm")

# actual values
L_i = 600e-6
L_g_r = 110e-6
C_f = 1e-6
# resonant frequency
w_res = sqrt((L_i + L_g_r) / (L_i * L_g_r * C_f))
f_res = w_res / (2 * pi)
valid = (f_res > 10 * f_g) & (f_res < 0.5 * f_sw)

# damping resistor
R_f = 1 / (3 * w_res * C_f)
# print results
print("\nActual values:")
print(f"  Filter capacitance:         {C_f*1e6:.6} uF")
print(f"  Inverter-side inductance:   {L_i*1e6:.6} uH")
print(f"  Grid-side inductance:       {L_g_r*1e6:.6} uH")
print(
    f"  Resonant frequency:         {f_res/1000:.6} kHz ({'ok' if valid else 'out of range'})"
)
print(f"  Damping resistor:           {R_f:.6} Ohm")
