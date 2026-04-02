import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def plot_tau_hat_vs_theta(
    theta_values,
    tau_hat_values,
    output_dir: Path,
):
    """
    Plot estimated treatment effect (tau_hat) against collider strength (theta)
    for OLS under linear collider setting.

    Args:
        theta_values (list or array): List of theta values.
        tau_hat_values (list or array): Corresponding OLS estimates.
        output_dir (Path): Directory to save plot.
    """

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    theta_values = np.asarray(theta_values)
    tau_hat_values = np.asarray(tau_hat_values)

    plt.figure(figsize=(8, 5))

    # OLS line
    plt.plot(
        theta_values,
        tau_hat_values,
        marker="o",
        label="OLS",
    )

    # True treatment effect line (tau = 1.0 from your DGP)
    plt.axhline(
        y=1.0,
        linestyle="--",
        linewidth=2,
        label="True Effect (tau = 1.0)",
    )

    plt.xlabel("Theta")
    plt.ylabel("tau_hat")
    plt.title("Effect of Linear Collider on OLS Estimates")

    plt.legend()
    plt.grid(alpha=0.3)

    fname = "ols_linear_collider_tau_hat_vs_theta.png"
    plt.savefig(output_dir / fname, dpi=200, bbox_inches="tight")
    plt.close()

    print(f"Saved: {fname}")