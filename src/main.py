from TreeFriendlyDGP import TreeFriendlyDGP
from ols import OLSEstimator
from plotting import plot_tau_hat_vs_theta
from pathlib import Path

def main():
    print("MAIN IS RUNNING")
def run_single_simulation(theta, seed=42):
    """
    Executes a single simulation and returns tau_hat.
    """

    dgp = TreeFriendlyDGP(
        n_features=4,
        theta=theta,
        include_linear_collider=True
    )

    D, Y, W = dgp.sample(n_obs=1000, seed=seed)

    estimator = OLSEstimator()
    estimator.fit(D, Y, W)

    tau_hat = estimator.tau_hat

    return tau_hat


def main():
    theta_grid = [0.0, 0.2, 0.5, 1.0]

    tau_hat_list = []

    print("Running OLS simulations under linear collider...\n")

    for theta in theta_grid:
        tau_hat = run_single_simulation(theta)

        tau_hat_list.append(tau_hat)

        print(f"Theta = {theta:.1f} | tau_hat = {tau_hat:.4f}")

    # Plot results
    plot_tau_hat_vs_theta(
        theta_values=theta_grid,
        tau_hat_values=tau_hat_list,
        output_dir=Path("results")
    )


if __name__ == "__main__":
    main()