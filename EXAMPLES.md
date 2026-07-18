# Function Mark (FM) Examples

This document demonstrates how to use the **Function Mark (FM)** template to resolve a real infinity problem in physics: the self-energy of a point-charge particle (the classical electron radius crisis).

## The Problem: Classical Infinity
In standard electrodynamics, the energy $E$ of an electric field at a distance $r$ from a point charge is given by Coulomb's Law:
$$ \mathcal{L}_{\text{Target}} \propto \frac{1}{r} $$

As you calculate the energy closer and closer to the exact center of the particle ($r \to 0$), the equation divides by zero, resulting in:
$$ E = \infty $$
This mathematical crash is called an **ultraviolet divergence**.

---

## The Solution: Processing via Function Mark
When we feed this broken equation into **Function Mark**, the engine isolates the spatial changes using the **Mark Operator ($\mathbf{\Delta}$)** and applies the **Heat-Kernel Filter**:

$$ \mathbf{FM}[\mathcal{L}_{\text{Target}}] \implies \int d^D x \left[ \frac{1}{r} \cdot e^{-\frac{\mathbf{\Delta}}{k^2}} \right] $$

As the calculation approaches the center ($r \to 0$), the running scale ($k$) increases. The negative exponent in the Heat-Kernel filter drops the infinite spike down to zero, capping the maximum allowable energy at a clean, finite limit (the Planck Energy).

* **Old Physics Result:** Energy = Infinity (System Crash)
* **Function Mark Result:** Energy = $E_{\text{Planck}}$ (Stable and Calculable)
