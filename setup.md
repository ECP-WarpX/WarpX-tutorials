---
title: Setup
---

Welcome to the WarpX tutorials!  
Here you can find a guide on how to set up your system to be able to run and analyze WarpX simulations.  
Let's roll 💃🕺. 


## Install the dependencies

We use Conda, that work on most opertive system (Windows, macOS, Linux).  
As a first step get [Conda](https://docs.conda.io/en/latest/) and configure it with `libmamba`.  

```bash
conda update -y -n base conda
conda install -y -n base conda-libmamba-solver
conda config --set solver libmamba
conda config --set auto_activate_base false
```

Create a virtual environment for WarpX and install the dependencies. 

```bash
conda create -n warpx -c conda-forge blaspp boost ccache cmake compilers git "heffte=*=mpi_mpich*" lapackpp "openpmd-api=*=mpi_mpich*" openpmd-viewer python make numpy pandas scipy yt "fftw=*=mpi_mpich*" pkg-config matplotlib mamba mpich mpi4py ninja pip virtualenv
```

Activate your WarpX environment to make all the dependencies accessible. 

```bash
conda activate warpx
```


## Set up your working directory 

Open a terminal in your machine.  
For Windows users, we recommend installing [Windows Subsystem for Linux (WSL)](https://ubuntu.com/desktop/wsl), to have access to a full Ubuntu terminal environment.  

Create and/or move to a working directory of your choice.  
Throughout the tutorials we will assume that the working directory is `$HOME/warpx-tutorials`. 

```bash
mkdir $HOME/warpx-tutorials
cd $HOME/warpx-tutorials
```

Download in this folder the material (input files and analysis scripts) 
that will be used in the tutorials. 

```bash 
DOWNLOAD SOMEHOW THE RUNS DIRECTORY
```


## Build WarpX

Get WarpX's source code and move into the cloned folder:  

```bash
git clone https://github.com/ECP-WarpX/WarpX.git warpx
cd warpx
```
Configure the build in a directory called `build`.
When configuring, you can pass different flags that enble or disable various options.  
For example: `cmake -S . -B build -DWarpX_DIMS=1 -DCMAKE_BUILD_TYPE=Debug`
will compile the code in 1D geometry and in debug mode.  
You can find the list of the build options and their default values 
[here](https://warpx.readthedocs.io/en/latest/install/cmake.html#build-options).  
For these tutorials, we compile in 1D, 2D, 3D and enable FFT calculations.

```bash
cmake -S . -B build -DWarpX_DIMS="1;2;3" -DWarpX_FFT=ON
```

Finally, compile!

```bash
cmake --build build -j 4 
```

The `-j 4` options executes the compilation on 4 processes in parallel.

The executables will appear in `build/bin/` as `warpx.<DIMS>d.MPI.OMP.DP.PDP.OPMD.FFT.EB.QED`. 
You will also find `warpx.<DIMS>d` files, which are symbolic links to the executables with a shorter name. 


## Run WarpX 

To test that everything works fine, we run a first toy case.  


```bash  
mpirun -np 1 warpx/build/bin/warpx.3d inputs.txt
```



{% include links.md %}
