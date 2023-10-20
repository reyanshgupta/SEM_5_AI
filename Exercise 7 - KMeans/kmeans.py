import numpy as np
import matplotlib.pyplot as plt

def initialize_centroids(data, num_of_centroids):
    indices = np.random.choice(len(data), num_of_centroids, replace=False) #unique indice
    centroids = data[indices] #init random centroids from current data
    return centroids

def assign_to_clusters(data, centroids):
    clusters = {} #key: cluster indices, value: list of data points
    for i in range(len(data)):
        distances = np.sum((data[i] - centroids) ** 2, axis=1)  # Euclidean distance
        cluster_index = np.argmin(distances)  # Assign the data point to the closest centroid
        if cluster_index not in clusters:  # Creating new clusters if not in previous clusters
            clusters[cluster_index] = [] 
        clusters[cluster_index].append(data[i])  # adding the point to the data point list of the cluster
    return clusters

def update_centroids(clusters):
    new_centroids = []
    for cluster in clusters.values():
        new_centroid = np.mean(cluster, axis=0)
        new_centroids.append(new_centroid)
    return np.array(new_centroids)

def kmeans(data, k, max_iterations=100):
    centroids = initialize_centroids(data, k)
    for _ in range(max_iterations):
        clusters = assign_to_clusters(data, centroids)
        new_centroids = update_centroids(clusters)
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    return centroids, clusters

if __name__ == "__main__":
    np.random.seed(0)
    data = np.random.rand(100, 2)  # Generate random data points
    num_of_clusters = int(input("Enter the number of clusters required: "))
    centroids, clusters = kmeans(data, num_of_clusters)
    print("Final centroids: \n", centroids)
    for i, cluster in clusters.items():
        print(f"Cluster {i + 1} has {len(cluster)} points.")
        
    # Plotting the clusters
    for i, cluster in clusters.items():
        cluster = np.array(cluster)
        plt.scatter(cluster[:, 0], cluster[:, 1], label=f"Cluster {i + 1}") #x and y coordinates

    plt.scatter(centroids[:, 0], centroids[:, 1], c='black', marker='x', s=100, label='Centroids')
    plt.title("K-Means Clustering")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.show()