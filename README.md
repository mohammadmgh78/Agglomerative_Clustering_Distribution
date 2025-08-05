# Agglomerative_Clustering_Distribution

The main function to be used is 

cluster_distributions(dist_file, reg=0.5, n_clusters=None, calculate_barycenter=False, stop_threshold=10 ** -9,
                          num_of_iterations=1000, plt_dendrogram=True):
                          
This function performs hierarchical clustering of empirical probability distributions using the regularized Wasserstein distance. It reads a JSON-formatted input file containing a list of distributions, computes pairwise regularized Wasserstein distances between them, and applies agglomerative clustering. It returns two JSON files: One containing the empirical distributions and their corresponding clusters and another containing barycenters of the clusters.  

Function Parameters:
dist_file: JSON file containing the list of distributions. An example of such file is in the test.txt file in src folder. 

reg (float): Entropic regularization parameter for the regularized Wasserstein distance.

n_clusters (int or None): Number of clusters to cut the dendrogram into. If None, the best number based on Silhouette index is chosen automatically.

calculate_barycenter (bool): If True, computes the regularized Wasserstein barycenter of each cluster after clustering.

stop_threshold (float): Convergence threshold for the regularized Wasserstein distance.

num_of_iterations (int): Maximum number of regularized Wasserstein distance iterations per distance computation.

plt_dendrogram (bool): If True, displays the dendrogram for visualization.


