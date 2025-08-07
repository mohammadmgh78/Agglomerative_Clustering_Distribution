The code for paper titled **"An Agglomerative Clustering Algorithm for Simulation Output Distributions Using Regularized Wasserstein Distance"**, accepted in the *INFORMS Journal on Data Science*.
The preprint is available on [arXiv:2407.12100](https://arxiv.org/abs/2407.12100).  
This link will be updated once the final published version becomes available.

Each folder in this repository serves a specific purpose:

- **`code/`**  
  Contains all the code used to perform the analysis in the paper.  
  Refer to the **Code Instruction** section for further usage details.

- **`data/`**  
  Includes the data files used by the code. These files may be overwritten when simulations are re-run.

- **`data_backup/`**  
  Stores the original data files used in the experiments of the paper.  
  This folder acts as a backup: running the simulation code will overwrite files only in the `data/` folder, not here.

- **`distclust/`**  
  Contains the source code of the `distclust` Python package.  
  This package implements the clustering algorithm for empirical distributions.  
  Refer to the module's internal documentation for implementation details.
