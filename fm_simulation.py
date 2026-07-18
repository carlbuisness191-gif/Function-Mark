import numpy as np

def classical_energy(r):
    """The old equation that crashes at the center."""
    # Avoid exact zero division error in python, but watch it explode
    return 1.0 / np.maximum(r, 1e-15)

def function_mark_energy(r, k=2.0):
    """The equation filtered by Function Mark (FM).
    Uses the Heat-Kernel filter to suppress the infinity as r approaches 0.
    """
    # e^(-1 / (r^2 * k^2)) acts as the custom Mark Heat-Kernel Filter
    filter_dampener = np.exp(-1.0 / (np.maximum(r, 1e-15)**2 * k**2))
    return (1.0 / np.maximum(r, 1e-15)) * filter_dampener

# Test values approaching the center (r = 0)
radius_points = [1.0, 0.5, 0.1, 0.01, 0.001, 0.0]

print("--- FUNCTION MARK (FM) SIMULATION RESULTS ---")
print(f"{'Distance (r)':<15} | {'Old Energy Result':<20} | {'Function Mark (FM) Result':<25}")
print("-" * 68)

for r in radius_points:
    old_res = classical_energy(r)
    fm_res = function_mark_energy(r)
    
    # Format infinity string for exact zero
    old_str = "INFINITY (CRASH)" if r == 0.0 else f"{old_res:.2f}"
    fm_str = f"{fm_res:.6f} (FINITE)"
    
    print(f"{r:<15} | {old_str:<20} | {fm_str:<25}")
