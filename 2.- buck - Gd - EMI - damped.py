# -*- coding: utf-8 -*-
from math import pi, log10, sqrt
from control import tf, bode_plot, margin, step_response, nyquist_plot
import matplotlib.pyplot as plt
import numpy as np
L= 10e-6; rL=0.05; C=33e-6;rC=0.1; R=1; Vi=10; D=0.53;
# Voltage and currents in steady state
Vo=D*Vi/(1 + rL/R); Io= Vo/R; IL=Io
# EMI Filter
Lf= 100e-6; Cf= 10e-6; Cf1=1000e-6; Rf=1
# Transfer functions
s = tf('s')
# Impedances definition
Zf= s*Lf/(1 + Lf*Cf*s**2) # undamped EMI filter
Zf1= 1/( 1/(s*Lf) + s*Cf + s*Cf1/(1+Rf*Cf1*s) ) # damped EMI filter
ZL= rL + s*L
Zp= R*(1 + s*rC*C)/(1 + s*(R+rC)*C)
# Control-to-output with undamped EMI Filter
Gd=(Vi-D*IL*Zf)*Zp/(ZL+Zp+D**2*Zf)
# Control-to-output with damped EMI Filter
Gd1=(Vi-D*IL*Zf1)*Zp/(ZL+Zp+D**2*Zf1)
# Control-to-output without EMI Filter
Gd2=Vi*Zp/(ZL+Zp)
# Plot Plant's Bode
# Note that once Hz is true, omega_limits are in Hz
mag, phase, omega = bode_plot(Gd, dB=True, Hz=True, omega_limits=(10,200e3),\
                              omega_num=100, color="blue" )

mag, phase, omega = bode_plot(Gd1, dB=True, Hz=True, omega_limits=(10,200e3),\
                              omega_num=100, color="green" )    

mag, phase, omega = bode_plot(Gd2, dB=True, Hz=True, omega_limits=(10,200e3),\
                              omega_num=100, color="red" ) 







