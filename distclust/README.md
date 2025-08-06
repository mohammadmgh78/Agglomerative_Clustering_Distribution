Function Reference: cluster_distributions
Main function
python
Copy
Edit
cluster_distributions(
    dist_file,
    reg=0.5,
    n_clusters=None,
    calculate_barycenter=False,
    stop_threshold=1e-9,
    num_of_iterations=1000,
    plt_dendrogram=True,
    sup_barycenter=100,
    t0=0.005,
    theta=0.005
)
What it does
This function performs hierarchical (agglomerative) clustering of empirical probability distributions using the regularized (entropic) Wasserstein distance.
It takes a JSON-formatted string that encodes a list of distributions, computes all pairwise regularized Wasserstein distances, and then applies agglomerative clustering.

Returns one JSON string with each distribution and its assigned cluster.

If calculate_barycenter=True, it also computes barycenters for each cluster and returns a second JSON string with those barycenters.

Parameters
dist_file (str) – JSON string containing the list of distributions. An example format is in src/JSON_test.txt.

reg (float) – Entropic regularization parameter for the Wasserstein distance. Default is 0.5.

n_clusters (int or None) – Number of clusters. If None, the function chooses the number using the silhouette index.

calculate_barycenter (bool) – If True, compute a regularized Wasserstein barycenter for each cluster. If False, only clustering results are returned.

stop_threshold (float) – Convergence threshold for the Sinkhorn iterations.

num_of_iterations (int) – Maximum number of Sinkhorn iterations per distance computation.

plt_dendrogram (bool) – If True, save and show the dendrogram plot.

sup_barycenter (int) – Number of support points used for barycenter computation.

t0 (float) – Base step size for the mass (a-vector) update in barycenter computation.

theta (float) – Relaxation parameter for the support (X) update in barycenter computation.

Returns
If calculate_barycenter=False:

json_inputs (str) – JSON with distributions and their cluster labels.

If calculate_barycenter=True:

json_inputs (str) – JSON with distributions and their cluster labels.

json_barycenters (str) – JSON with cluster barycenters (supports and probabilities).
