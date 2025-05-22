import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

def plot_clusters(data, labels):
    """
    Reduces high-dimensional data to 2D using PCA
    and plots it with cluster labels.
    """
    pca = PCA(n_components=2)
    reduced_data = pca.fit_transform(data)

    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        x=reduced_data[:, 0],
        y=reduced_data[:, 1],
        hue=labels,
        palette='tab10'
    )
    plt.title("Customer Segments (PCA)")
    plt.xlabel("PCA 1")
    plt.ylabel("PCA 2")
    plt.legend(title="Cluster")
    plt.tight_layout()
    plt.show()


def plot_silhouette_scores(score_dict):
    """
    Plots silhouette scores against number of clusters.
    Accepts a dictionary of {k: score}.
    """
    ks = list(score_dict.keys())
    sil_scores = list(score_dict.values())

    plt.figure(figsize=(7, 4))
    plt.plot(ks, sil_scores, marker='o')
    plt.title("Silhouette Scores by Cluster Count")
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Silhouette Score")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
