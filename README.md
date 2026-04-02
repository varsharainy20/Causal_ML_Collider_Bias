# Collider Bias in OLS: A Simulation Study

This project investigates how conditioning on a **collider variable** distorts causal effect estimation using Ordinary Least Squares (OLS). It is part of a broader research project on collider bias in causal machine learning methods conducted at the University of Bonn.
---

## Project Context

The group project studies how **including colliders in the control set** affects:

* bias in treatment effect estimation
* coverage of confidence intervals
* spurious heterogeneity in machine learning models

While the full project evaluates **Double Machine Learning (DML)** and **Causal Forests**, this repository focuses on a **clean, interpretable baseline: OLS under collider bias**.

---

##  My Contribution

This repository contains my **individual implementation and analysis**, specifically:

* Implementation of **OLS estimator with robust standard errors**
* Integration with a **Tree-Friendly Data Generating Process (DGP)**

  * adapted and partially modified from the group framework
* Design and simulation of a **linear collider mechanism**
* Systematic evaluation of how collider strength (θ) affects:

  * estimated treatment effect (`tau_hat`)
  * bias relative to true effect (`tau`)
* Visualization of results for interpretability

---

## Methodology

We simulate data using a structured DGP and introduce a **linear collider**:

* True causal model:

  * Treatment effect: `τ = 1.0`
* Collider construction:

  * Depends on both treatment (D) and outcome (Y)
* Key parameter:

  * **θ (theta)** controls collider strength
  * θ ∈ {0.0, 0.2, 0.5, 1.0}

We then estimate:

* **Naive OLS (with collider included as control)**

---

## Pipeline

The simulation pipeline is structured as follows:

1. **Data Generation (`dgp.py`)**

   * Generates covariates (X), treatment (D), and outcome (Y)
   * Applies nonlinear confounding structure
   * Adds linear collider based on θ

2. **Estimation (`ols.py`)**

   * Fits OLS regression:

     ```
     Y ~ D + W (+ collider)
     ```
   * Computes:

     * `tau_hat`
     * standard errors (`se_hat`)
     * confidence intervals (`ci`)

3. **Simulation Runner (`main.py`)**

   * Loops over different θ values
   * Stores estimated treatment effects

4. **Visualization (`plotting.py`)**

   * Plots:

     * `tau_hat` vs `theta`
   * Compares against true effect (`τ = 1.0`)

---

##  Key Result

As collider strength increases:

* OLS estimates (`tau_hat`) **systematically deviate** from the true effect
* Bias increases with θ
* Even a correctly specified linear model becomes **causally invalid**

This illustrates **collider bias**: conditioning on a collider induces a spurious relationship between treatment and outcome.

---

## Project Structure

```
.
├── src/
│   ├── main.py          # Runs simulations
│   ├── dgp.py           # Data generating process (modified)
│   ├── ols.py           # OLS estimator
│   ├── plotting.py      # Visualization
│
├── results/             # Generated plots
├── README.md
└── .gitignore
```

---

##  How to Run
To run the code, you need Python 3.11.9.

1. Clone this folder.

2. Install the required packages:

 pip install -r requirements.txt
