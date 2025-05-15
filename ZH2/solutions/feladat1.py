"""
Solution for Problem 1: Two-layer wall with heat generation.

This module calculates:
1. Heat flux from the wall surface
2. Temperature at the interface between layers
3. Temperature at the outer surface of the wall
4. Required heat transfer coefficient
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
params = parameters_module.feladat1_params

def heat_flux():
    """
    Calculate the heat flux from the wall.
    """
    # Since the inner surface is perfectly insulated,
    # all heat generated in layer A flows outward
    q = params['q_V'] * params['s_A']
    return q

def interface_temperature():
    """
    Calculate the temperature at the interface between layers A and B.
    """
    # Temperature distribution in layer A is parabolic
    T_max = params['T_max']
    q_V = params['q_V']
    s_A = params['s_A']
    lambda_A = params['lambda_A']
    
    # Temperature drop across layer A
    delta_T_A = (q_V * s_A**2) / (2 * lambda_A)
    
    # Interface temperature
    T_interface = T_max - delta_T_A
    return T_interface

def surface_temperature():
    """
    Calculate the temperature at the outer surface of layer B.
    """
    # Get interface temperature
    T_interface = interface_temperature()
    
    # Heat flux
    q = heat_flux()
    
    # Temperature drop across layer B (linear distribution)
    s_B = params['s_B']
    lambda_B = params['lambda_B']
    delta_T_B = (q * s_B) / lambda_B
    
    # Surface temperature
    T_surface = T_interface - delta_T_B
    return T_surface

def required_heat_transfer_coefficient():
    """
    Calculate the required heat transfer coefficient to maintain
    the maximum temperature below 145°C.
    """
    # Heat flux
    q = heat_flux()
    
    # Surface temperature
    T_surface = surface_temperature()
    
    # Water temperature
    T_water = params['T_water']
    
    # Required heat transfer coefficient from q = alpha * (T_surface - T_water)
    alpha = q / (T_surface - T_water)
    return alpha

def solve_problem1():
    """
    Solve all parts of problem 1 and return the results.
    """
    q = heat_flux()
    T_interface = interface_temperature()
    T_surface = surface_temperature()
    alpha = required_heat_transfer_coefficient()
    
    results = {
        'heat_flux': q,
        'interface_temperature': T_interface,
        'surface_temperature': T_surface,
        'required_heat_transfer_coefficient': alpha
    }
    
    return results

if __name__ == "__main__":
    # Test the module
    results = solve_problem1()
    
    print("Problem 1 Results:")
    print(f"Heat flux: {results['heat_flux']:.2f} W/m²")
    print(f"Interface temperature: {results['interface_temperature']:.2f} °C")
    print(f"Surface temperature: {results['surface_temperature']:.2f} °C")
    print(f"Required heat transfer coefficient: {results['required_heat_transfer_coefficient']:.2f} W/(m²·K)")
