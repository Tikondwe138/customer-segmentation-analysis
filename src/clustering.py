from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def find_optimal_k(data, max_k=10):
    """
    Determines the optimal number of clusters (k) using silhouette score.
    Automatically caps max_k to n_samples - 1 to avoid errors.
    Returns the best k and a dictionary of k:silhouette_score values.
    """
    n_samples = len(data)
    if n_samples < 3:
        raise ValueError("At least 3 samples are required to perform clustering.")

    # Prevent invalid silhouette calculations
    max_k = min(max_k, n_samples - 1)

    scores = {}
    for k in range(2, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        labels = kmeans.fit_predict(data)

        # Skip if all points are assigned to one cluster
        if len(set(labels)) < 2:
            print(f"Skipped k={k}: Only one cluster found.")
            continue

        score = silhouette_score(data, labels)
        scores[k] = score
        print(f"k={k}, Silhouette Score={score:.4f}")

    if not scores:
        raise ValueError("No valid clustering configuration found. Check the dataset.")

    best_k = max(scores, key=scores.get)
    return best_k, scores


def perform_kmeans(data, n_clusters):
    """
    Performs KMeans clustering with a specified number of clusters.
    Returns the trained model and cluster labels.
    """
    if n_clusters < 2 or n_clusters >= len(data):
        raise ValueError(f"Invalid number of clusters: {n_clusters}. "
                         f"Must be between 2 and {len(data) - 1}.")

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(data)
    return kmeans, labels
