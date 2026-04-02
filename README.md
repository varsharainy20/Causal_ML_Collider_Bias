# Collider Bias in OLS: A Simulation Study

This project demonstrates how conditioning on a linear collider biases treatment effect estimates obtained using Ordinary Least Squares (OLS).

## Overview

We simulate data using a structured data-generating process (TreeFriendlyDGP) and introduce a linear collider into the covariates. The goal is to study how increasing collider strength (theta) affects the estimated treatment effect (tau_hat).

## Methodology

- Simulated data with nonlinear confounding
- Linear collider added to covariates
- OLS used to estimate treatment effects
- Estimates evaluated across different values of theta

## Key Result

As collider strength increases, OLS estimates (tau_hat) deviate from the true treatment effect (tau = 1.0), illustrating collider bias.

## Project Structure
