The package can be installed using 

```python
pip install --index-url https://pypi.org/simple/ --no-deps distclust==0.0.3
```

## Main function
```python
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
```

## Description
This function performs hierarchical (agglomerative) clustering of empirical probability distributions using the *regularized (entropic) Wasserstein* distance.  
It takes a JSON-formatted string that encodes a list of distributions, computes all pairwise regularized Wasserstein distances, and then performs agglomerative clustering.

- Returns one JSON string with each distribution and its assigned cluster.
- If `calculate_barycenter=True`, it also computes barycenters of each cluster and returns a second JSON string with the barycenters.

---

Function parameters\\

- **`dist_file`** *(str)*: A JSON-formatted string containing a dictionary of distributions.  
  Each key in the dictionary is a **distribution ID**, mapped to another dictionary with the keys:
  - `"id"`: The identifier of the distribution.
  - `"data_points"`: A list of tuples representing the data points.  
  An example format is provided in [`src/JSON_test.txt`](src/JSON_test.txt).

- **`reg`** *(float)*: Entropic regularization parameter for the Wasserstein distance.
- **`n_clusters`** *(int or None)*: Number of clusters. If `None`, the function chooses the number using the silhouette index.
- **`calculate_barycenter`** *(bool)*: If `True`, compute a regularized Wasserstein barycenter for each cluster. If `False`, only clustering results are returned.
- **`stop_threshold`** *(float)*: Convergence threshold for the Sinkhorn iterations.
- **`num_of_iterations`** *(int)*: Maximum number of Sinkhorn iterations per distance computation.
- **`plt_dendrogram`** *(bool)*: If `True`, save and show the dendrogram plot.
- **`sup_barycenter`** *(int)*: Number of support points used for barycenter computation.
- **`t0`** *(float)*: Base step size for the mass (`a`-vector) update in barycenter computation.
- **`theta`** *(float)*: Relaxation parameter for the support (`X`) update in barycenter computation.

---

Returns\\

If `calculate_barycenter=False`:
- **`json_inputs`** *(str)*: JSON with distributions and their cluster labels.

If `calculate_barycenter=True`:
- **`json_inputs`** *(str)*: JSON with distributions and their cluster labels.
- **`json_barycenters`** *(str)*: JSON with cluster barycenters (supports and probabilities).


We also provide the following functions that might be useful to some users:
## Other Functions in `distclust`

These are the primary functions used for simulation output clustering, optimal transport computation, and barycenter calculation.

1. **`density_calc`** – Compute empirical probability masses.  
2. **`density_calc_list`** – Batch probability mass computation.  
3. **`fill_ot_distance`** – Compute and store OT distances between all systems.  
4. **`calculate_OT_cost`** – Entropic OT via Sinkhorn.  
5. **`plot_dendrogram`** – Dendrogram visualization.  
6. **`silhouette_score_agglomerative`** – Choose number of clusters.  
7. **`find_barycenter`** – Compute Wasserstein barycenter.  
8. **`calculate_OT_cost_bary`** – OT computation for barycenter step.  
