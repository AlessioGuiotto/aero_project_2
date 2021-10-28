#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 15:02:13 2021

@author: alessio
"""

from numpy import pi
import matplotlib.pyplot as plt

def knost_to_ftpersec(speed): #speed is the user input and it is in knots
    return speed * 1.68781
def thrust_required(rho_inf, v_inf, s, cd0_, k, w): #all the inputs for Thurst Required
    cl = 2 * w / (rho_inf * v_inf ** 2 * s)
    return 0.5 * rho_inf * v_inf **2 * s * (cd0_ + k * cl ** 2)

#aircraft parameteres (estimates from the internet) for A321

weight = 200000  # lb
wing_area = 1318  # ft^2
wing_span = 117.416666667  # ft
cd0 = 0.0185
thrust = 66000  # lb of thrust total
aspect_ratio = wing_span**2 / wing_area
e = 0.92
K = 1 / (pi * e * aspect_ratio)
rho_sl = 23.77E-4  # in slugs/ft^3