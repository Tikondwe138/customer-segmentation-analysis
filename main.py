import pandas as pd
import numpy as np
from src.preprocessing import preprocess_data
from src.clustering import find_optimal_k, perform_kmeans
from src.visualization import plot_clusters, plot_silhouette_scores

def main():
    # Load the dataset
    df = pd.read_csv("data/customer_data.csv")  # Make sure the file exists

    # Preprocess the data
    X_scaled, df_cleaned = preprocess_data(df)

    print(f"Data shape after scaling: {X_scaled.shape}")
    print(f"Contains NaNs: {np.isnan(X_scaled).any()}")

    # Determine the optimal number of clusters
    best_k, scores = find_optimal_k(X_scaled, max_k=10)
    print(f"Optimal number of clusters: {best_k}")

    # Visualize silhouette scores
    plot_silhouette_scores(scores)

    # Run K-Means clustering
    model, labels = perform_kmeans(X_scaled, best_k)

    # Visualize the clusters
    plot_clusters(X_scaled, labels)

    # Save clustered results
    df_cleaned["Cluster"] = labels
    df_cleaned.to_csv("reports/clustered_customers.csv", index=False)
    print("Clustered data saved to reports/clustered_customers.csv")

if __name__ == "__main__":
    main()
