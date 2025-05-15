"""
Solution for Problem 3: Cooling brass balls in water.

This module calculates:
1. Biot number (dimensionless boundary condition criterion)
2. Average temperature of a ball at the end of cooling
3. Required cooling power to maintain water at constant temperature
"""

import numpy as np
import math
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
params = parameters_module.feladat3_params

def biot_number():
    """
    Calculate the Biot number to determine if lumped capacitance model is valid.
    """
    # Parameters
    h = params['h']
    d = params['d']
    k = params['k']
    
    # Characteristic length for a sphere: L_c = V/A = r/3 = d/6
    L_c = d / 6
    
    # Biot number calculation
    Bi = (h * L_c) / k
    
    return Bi

def dimensionless_temperature(tau):
    """
    Calculate the dimensionless temperature at time tau.
    """
    # Parameters
    h = params['h']
    rho = params['rho']
    c = params['c']
    d = params['d']
    
    # Dimensionless temperature formula from lumped model
    theta_star = math.exp(-(6 * h * tau) / (rho * c * d))
    
    return theta_star

def average_temperature_at_end():
    """
    Calculate the average temperature of a ball at the end of cooling period.
    """
    # Parameters
    T_0 = params['T_0']
    T_inf = params['T_inf']
    tau = params['tau']
    
    # Dimensionless temperature at the end of cooling
    theta_star = dimensionless_temperature(tau)
    
    # Final average temperature
    T_final = T_inf + (T_0 - T_inf) * theta_star
    
    return T_final

def ball_mass():
    """
    Calculate the mass of a single ball.
    """
    # Parameters
    rho = params['rho']
    d = params['d']
    
    # Volume of a sphere
    V = (math.pi * d**3) / 6
    
    # Mass
    m = rho * V
    
    return m

def heat_released_per_ball():
    """
    Calculate the heat released by a single ball during cooling.
    """
    # Parameters
    T_0 = params['T_0']
    T_inf = params['T_inf']
    tau = params['tau']
    
    # Mass of a ball
    m = ball_mass()
    
    # Specific heat capacity
    c = params['c']
    
    # Dimensionless temperature at the end of cooling
    theta_star = dimensionless_temperature(tau)
    
    # Heat released by one ball
    Q_1 = m * c * (T_0 - T_inf) * (1 - theta_star)
    
    return Q_1

def required_cooling_power():
    """
    Calculate the required cooling power to maintain water at constant temperature.
    """
    # Parameters
    n = params['n']  # Balls per minute
    
    # Heat released per ball
    Q_1 = heat_released_per_ball()
    
    # Power required to maintain water temperature constant
    # Conversion from balls/minute to balls/second: n/60
    P = (n / 60) * Q_1
    
    return P

def solve_problem3():
    """
    Solve all parts of problem 3 and return the results.
    """
    Bi = biot_number()
    T_final = average_temperature_at_end()
    P = required_cooling_power()
    
    results = {
        'biot_number': Bi,
        'final_temperature': T_final,
        'required_cooling_power': P
    }
    
    return results

if __name__ == "__main__":
    # Test the module
    results = solve_problem3()
    
    print("Problem 3 Results:")
    print(f"Biot number: {results['biot_number']:.4f}")
    print(f"Final ball temperature: {results['final_temperature']:.2f} °C")
    print(f"Required cooling power: {results['required_cooling_power']:.2f} W")
