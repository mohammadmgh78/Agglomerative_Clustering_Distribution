Each folder in this repository serves a specific purpose:

- **`code/`**  
  Contains all the code used to generate the dataset.  
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
