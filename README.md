# Function Mark (FM)

**Function Mark (FM)** is a universal mathematical functional integral template designed to systematically regulate and eliminate ultraviolet divergences (infinities) from arbitrary field theory equations. 

Unlike specific physical theories (such as string theory or loop quantum gravity), **FM operates purely as a mathematical framework and computational tool**. Researchers can plug their target equations directly into the FM engine, which dynamically suppresses mathematical singularities before division-by-zero errors can crash the calculation.

---

## 🧮 Mathematical Definition

The universal framework of Function Mark is defined by the following functional integral:

$$ \mathbf{FM}[\mathcal{L}_{\text{Target}}, \mu] = \int \prod_{i} \mathcal{D}[\Phi_i] \exp \left( \frac{i}{\hbar} \int d^D x \sqrt{-g} \left[ \int_{k=\mu}^{\infty} \frac{dk}{k} \, \mathcal{R}_k \, \mathbf{Tr} \left( e^{- \frac{\mathbf{\Delta}_{\text{Target}}}{k^2}} \right) + \mathcal{L}_{\text{Target}} \right] \right) $$

### Variable Glossary:
* **$\mathbf{FM}$**: The overarching Function Mark engine.
* **$\mathcal{L}_{\text{Target}}$**: The user's input Lagrangian equation (e.g., Einstein gravity, Maxwell electromagnetism, Navier-Stokes fluids).
* **$\mathbf{\Delta}_{\text{Target}}$**: The **Mark Operator** (the characteristic differential operator extracted automatically from the input equation).
* **$e^{- \frac{\mathbf{\Delta}_{\text{Target}}}{k^2}}$**: The **Mark Heat-Kernel Filter**. This serves as the core shielding mechanism, acting as an exponential dampener that intercepts infinities at ultra-short distances ($r \to 0$).
* **$\mu$**: The user-defined scale slider, allowing calculations to shift smoothly from macroscopic views ($\mu \to 0$) to microscopic quantum scales ($\mu \to \infty$).

---

## 🛠️ How It Works (Operational Architecture)

1. **Input:** The user feeds an infinity-prone equation ($\mathcal{L}_{\text{Target}}$) into the framework.
2. **Isolate:** The system isolates the field changes using the Mark Operator ($\mathbf{\Delta}$).
3. **Regulate:** The Heat-Kernel filter applies a running scale ($k$). If a calculation tries to divide by zero, the exponent drops the infinity straight to a clean, maximum finite limit (the Planck scale).
4. **Output:** A regularized, calculable mathematical prediction that is fully compatible with quantum mechanics.

---

## 📜 Academic Citation & Origins
Function Mark is built by synthesizing foundational concepts from **Functional Renormalization Group (FRG)** mathematics and the **Exact Renormalization Group Equation (ERGE)** historically pioneered by Christof Wetterich (1993) and Martin Reuter (1996). It provides a unified, highly adaptable template for modern quantum cosmology and high-energy physics research.

## 🤝 Contributing
Contributions, equations tests, and code implementations are welcome! Please fork this repository, plug your target Lagrangian into the template, and open a Pull Request with your findings.
