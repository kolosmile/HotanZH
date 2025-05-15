"""
Parameters file for all three heat transfer problems.
This file contains all the input data needed for calculations.
"""

# Feladat 1 - Two-layer wall with heat generation
feladat1_params = {
    # Volumetric heat generation [W/m³]
    'q_V': 1.3e6,
    # Layer A thickness [m]
    's_A': 55e-3,
    # Layer B thickness [m]
    's_B': 10e-3,
    # Layer A thermal conductivity [W/(m·K)]
    'lambda_A': 85,
    # Layer B thermal conductivity [W/(m·K)]
    'lambda_B': 145,
    # Water temperature [°C]
    'T_water': 25,
    # Maximum allowed temperature [°C]
    'T_max': 145
}

# Feladat 2 - Finned heat transfer surface
feladat2_params = {
    # Surface temperature [°C]
    'T_0': 60,
    # Air temperature [°C]
    'T_inf': 22,
    # Convective heat transfer coefficient [W/(m²·K)]
    'h': 30,
    # Fin length [m]
    'L': 25e-3,
    # Fin square cross-section side [m] (value to be provided)
    'a': 4e-3,  # Example value, replace with actual value from diagram
    # Thermal conductivity of duralumin [W/(m·K)]
    'k': 165,   # Segédletből
    # Number of fins per 1 m² base surface
    'n': 2500   # Example value, replace with actual value
}

# Feladat 3 - Cooling brass balls in water
feladat3_params = {
    # Ball diameter [m]
    'd': 43e-3,
    # Initial temperature [°C]
    'T_0': 134,
    # Water temperature [°C]
    'T_inf': 38,
    # Convective heat transfer coefficient [W/(m²·K)]
    'h': 240,
    # Thermal conductivity [W/(m·K)]
    'k': 131,
    # Density [kg/m³]
    'rho': 8384,
    # Specific heat capacity [J/(kg·K)]
    'c': 380,
    # Immersion time [s]
    'tau': 120,
    # Balls per minute
    'n': 107
}
