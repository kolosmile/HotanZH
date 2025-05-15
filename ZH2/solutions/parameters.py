"""
Parameters file for all three heat transfer problems.
This file contains all the input data needed for calculations.
"""

# Feladat 1 - Two-layer wall with heat generation
feladat1_params = {
    # Volumetric heat generation [W/m³]
    'q_V': 1.6e6,
    # Layer A thickness [m]
    's_A': 60e-3,
    # Layer B thickness [m]
    's_B': 25e-3,
    # Layer A thermal conductivity [W/(m·K)]
    'lambda_A': 70,
    # Layer B thermal conductivity [W/(m·K)]
    'lambda_B': 140,
    # Water temperature [°C]
    'T_water': 40,
    # Maximum allowed temperature [°C]
    'T_max': 145
}

# Feladat 2 - Finned heat transfer surface
feladat2_params = {
    # Surface temperature [°C]
    'T_0': 86,
    # Air temperature [°C]
    'T_inf': 21,
    # Convective heat transfer coefficient [W/(m²·K)]
    'h': 30,
    # Fin length [m]
    'L': 17e-3,
    # Fin square cross-section side [m] (value to be provided)
    'a': 3e-3,  # Example value, replace with actual value from diagram
    # Thermal conductivity of duralumin [W/(m·K)]
    'k': 200,   # Example value, replace with actual value
    # Number of fins per 1 m² base surface
    'n': 1000   # Example value, replace with actual value
}

# Feladat 3 - Cooling brass balls in water
feladat3_params = {
    # Ball diameter [m]
    'd': 47e-3,
    # Initial temperature [°C]
    'T_0': 132,
    # Water temperature [°C]
    'T_inf': 55,
    # Convective heat transfer coefficient [W/(m²·K)]
    'h': 240,
    # Thermal conductivity [W/(m·K)]
    'k': 132,
    # Density [kg/m³]
    'rho': 8167,
    # Specific heat capacity [J/(kg·K)]
    'c': 379,
    # Immersion time [s]
    'tau': 120,
    # Balls per minute
    'n': 132
}
