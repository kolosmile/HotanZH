"""
Solution for Problem 2: Finned heat transfer surface.

This module calculates:
1. Total heat transfer rate from a 1x1 m² area
2. Fin tip temperature
3. Single fin efficiency
4. Relative heat transfer enhancement compared to unfinned surface
"""

import numpy as np
import os
import sys
import importlib.util

# Dynamic import of the parameters module
current_dir = os.path.dirname(os.path.abspath(__file__))
params_path = os.path.join(current_dir, "parameters.py")

# Import parameters
spec = importlib.util.spec_from_file_location("parameters", params_path)
parameters_module = importlib.util.module_from_spec(spec)
sys.modules["parameters"] = parameters_module
spec.loader.exec_module(parameters_module)

# Get parameters for this problem
params = parameters_module.feladat2_params

def fin_parameter():
    """
    Calculate the fin parameter m.
    """
    h = params['h']
    k = params['k']
    a = params['a']
    
    # Perimeter of the square cross-section
    P = 4 * a
    
    # Cross-sectional area
    A_c = a**2
    
    # Fin parameter m
    m = np.sqrt(h * P / (k * A_c))
    return m

def fin_efficiency():
    """
    Calculate the fin efficiency (with convective tip).
    """
    m = fin_parameter()
    L = params['L']
    h = params['h']
    k = params['k']
    
    # Fin efficiency formula from the document
    num = np.tanh(m * L) + h / (m * k)
    den = 1 + (h / (m * k)) * np.tanh(m * L)
    
    eta = num / den
    return eta

def fin_tip_temperature():
    """
    Calculate the temperature at the fin tip.
    """
    m = fin_parameter()
    L = params['L']
    h = params['h']
    k = params['k']
    
    T_0 = params['T_0']
    T_inf = params['T_inf']
    
    # Fin tip temperature formula from the document
    denominator = np.cosh(m * L) + (h / (m * k)) * np.sinh(m * L)
    T_tip = T_inf + (T_0 - T_inf) / denominator
    
    return T_tip

def total_heat_transfer():
    """
    Calculate the total heat transfer rate from the finned surface (1 m²).
    """
    # Base parameters
    T_0 = params['T_0']
    T_inf = params['T_inf']
    h = params['h']
    n = params['n']  # Number of fins per m²
    a = params['a']
    L = params['L']
    
    # Cross-sectional area of a fin
    A_c = a**2
    
    # Perimeter of the fin
    P = 4 * a
    
    # Total fin surface area (lateral + tip)
    A_f = P * L + A_c
    
    # Fin efficiency
    eta = fin_efficiency()
    
    # Heat transfer from a single fin
    Q_fin = eta * h * A_f * (T_0 - T_inf)
    
    # Area of the base surface not covered by fins
    A_base = 1.0 - n * A_c
    
    # Heat transfer from the base surface
    Q_base = h * A_base * (T_0 - T_inf)
    
    # Total heat transfer
    Q_total = n * Q_fin + Q_base
    
    return Q_total

def relative_enhancement():
    """
    Calculate the relative heat transfer enhancement compared to an unfinned surface.
    """
    # Total heat transfer with fins
    Q_with_fins = total_heat_transfer()
    
    # Heat transfer without fins (only base surface)
    T_0 = params['T_0']
    T_inf = params['T_inf']
    h = params['h']
    
    Q_without_fins = h * 1.0 * (T_0 - T_inf)  # 1 m² surface area
    
    # Relative enhancement
    enhancement = Q_with_fins / Q_without_fins
    
    return enhancement

def solve_problem2():
    """
    Solve all parts of problem 2 and return the results.
    """
    Q_total = total_heat_transfer()
    T_tip = fin_tip_temperature()
    eta = fin_efficiency() * 100  # Convert to percentage
    enhancement = relative_enhancement()
    
    results = {
        'total_heat_transfer': Q_total,
        'fin_tip_temperature': T_tip,
        'fin_efficiency_percent': eta,
        'relative_enhancement': enhancement
    }
    
    return results

if __name__ == "__main__":
    # Test the module
    results = solve_problem2()
    
    print("Problem 2 Results:")
    print(f"Total heat transfer rate: {results['total_heat_transfer']:.2f} W")
    print(f"Fin tip temperature: {results['fin_tip_temperature']:.2f} °C")
    print(f"Single fin efficiency: {results['fin_efficiency_percent']:.2f} %")
    print(f"Relative enhancement: {results['relative_enhancement']:.2f} x")
