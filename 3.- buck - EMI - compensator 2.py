# -*- coding: utf-8 -*-
from math import pi, log10, sqrt
from control import tf, bode_plot, margin, step_response, nyquist_plot
import matplotlib.pyplot as plt
import numpy as np
L= 10e-6; rL=0.05; C=33e-6;rC=0.1; R=1; Vi= 10; D=0.53;
# Voltage and currents in steady state
Vo=D*Vi/(1 + rL/R); Io= Vo/R; IL=Io
# EMI Filter
Lf= 100e-6; Cf= 10e-6
# PWM modulator gain
kd=1
# PI compensator design
fz=1e3; fp=10e3; Am=0.07; C2=100e-9
R2=1/(2*pi*fz*C2)
C3=1/(2*pi*fp*R2) # assuming C2 >> C3 (~ fp >> fz)
R1=R2/Am          # assuming C2 >> C3 (~ fp >> fz)
# Transfer functions
s = tf('s')
# Impedances definition
Zf= s*Lf/(1 + Lf*Cf*s**2)
ZL= rL + s*L
Zp= R*(1 + s*rC*C)/(1 + s*(R+rC)*C)
# Control-to-output with EMI Filter
Gd=(Vi-D*IL*Zf)*Zp/(ZL+Zp+D**2*Zf)
# Control-to-output without EMI Filter
Gd1=Vi*Zp/(ZL+Zp)
# Compensator
Cp=(1 + R2*C2*s)/( (R1*(C2+C3)*s)*(1 + R2*C2*C3*s/(C2+C3)) )
H=1 # Sensor
# Loop gain with EMI Filter
T=Cp*kd*Gd*H
# Closed-loop Control to output TF with EMI Filter
Gcl=Cp*kd*Gd/(1+T)
# Plot Plant's Bode
# Note that once Hz is true, omega_limits are in Hz
mag, phase, omega = bode_plot(Gd, dB=True, Hz=True, omega_limits=(10,200e3),\
                              omega_num=100, color="red" ) 
mag, phase, omega = bode_plot(Cp, dB=True, Hz=True, omega_limits=(10,200e3),\
                              omega_num=100, color="blue" ) 
mag, phase, omega = bode_plot(T, dB=True, Hz=True, omega_limits=(10,200e3),\
                              omega_num=100, color="green" )    
print("R1(kOhm)= ", R1/1e3)
print("R2(kOhm)= ", R2/1e3)
print("C2(nF)= ", C2/1e-9)
print("C3(nF)= ", C3/1e-9)   
    


'''

# Print a few points
print("F(Hz)               Magnitude(dB)       Phase(deg)")
print("----------------------------------------------------------")
i=20
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=40
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=60
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=80
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)






wmin= -2*pi*100
wmax=  2*pi*100
w =   np.arange(wmin,wmax,10, dtype=np.float)


# EMI Filter
fs= 200e3
fc=fs/40
Cf=10e-6
Lf=1/(4*pi**2*fc**2*Cf)
print("Lf= ", Lf)

'''







