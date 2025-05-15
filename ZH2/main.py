"""
Main program to run solutions for all three heat transfer problems.
"""

import os
import sys

# Add the parent directory to sys.path to help with imports
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# Import solutions
try:
    from solutions.feladat1 import solve_problem1
    from solutions.feladat2 import solve_problem2
    from solutions.feladat3 import solve_problem3
except ImportError:
    print("Error importing solution modules. Check file paths and directory structure.")

def print_header(text):
    """Print a formatted header."""
    print("\n" + "=" * 80)
    print(f" {text} ".center(80, "="))
    print("=" * 80 + "\n")

def present_results(results, units):
    """Present results in a formatted way with proper units."""
    # Find the longest key name for alignment
    max_len = max(len(key.replace('_', ' ').title()) for key in results.keys())
    
    # Print each result with its unit
    for key, value in results.items():
        # Format the value with appropriate precision
        if isinstance(value, float):
            if value < 0.1:
                formatted_value = f"{value:.4f}"
            else:
                formatted_value = f"{value:.2f}"
        else:
            formatted_value = str(value)
        
        # Add the unit if available
        if key in units:
            formatted_value += f" {units[key]}"
        
        # Create a nicer display name
        display_name = key.replace('_', ' ').title()
        
        # Print aligned result
        print(f"{display_name.ljust(max_len)} : {formatted_value}")

def main():
    """Main function to run all solutions."""
    print_header("Heat Transfer Problem Solutions")
    
    # Problem 1: Two-layer wall with heat generation
    print_header("Problem 1: Two-layer Wall with Heat Generation")
    results_1 = solve_problem1()
    units_1 = {
        'heat_flux': 'W/m²',
        'interface_temperature': '°C',
        'surface_temperature': '°C',
        'required_heat_transfer_coefficient': 'W/(m²·K)'
    }
    present_results(results_1, units_1)
    
    # Problem 2: Finned heat transfer surface
    print_header("Problem 2: Finned Heat Transfer Surface")
    results_2 = solve_problem2()
    units_2 = {
        'total_heat_transfer': 'W',
        'fin_tip_temperature': '°C',
        'fin_efficiency_percent': '%',
        'relative_enhancement': 'x'  # times
    }
    present_results(results_2, units_2)
    
    # Problem 3: Cooling brass balls in water
    print_header("Problem 3: Cooling Brass Balls in Water")
    results_3 = solve_problem3()
    units_3 = {
        'biot_number': '',  # dimensionless
        'final_temperature': '°C',
        'required_cooling_power': 'W'
    }
    present_results(results_3, units_3)
    
    print("\nAll problems solved successfully!\n")

if __name__ == "__main__":
    main()
    
    print("\nAll problems solved successfully!\n")

if __name__ == "__main__":
    main()
