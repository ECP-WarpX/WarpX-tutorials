---
title: Setup
---
  
  
Welcome to the WarpX tutorials!  
Here you can find a guide on how to set up your system to be able to run and analyze WarpX simulations.  
Let's roll 💃🕺. 


## Install the dependencies 

We use Conda, that work on most opertive system (Windows, macOS, Linux).  
As a first step get [Conda](https://docs.conda.io/en/latest/) and configure it with `libmamba`.  


```bash markdown-code-runner
conda update -y -n base conda
conda install -y -n base conda-libmamba-solver
conda config --set solver libmamba
conda config --set auto_activate_base false
```  



{% include links.md %}
