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
```

Create a virtual environment for WarpX and install the dependencies. 


```bash markdown-code-runner
conda create -n warpx -c conda-forge blaspp boost ccache cmake compilers git "heffte=*=mpi_mpich*" 
lapackpp "openpmd-api=*=mpi_mpich*" openpmd-viewer python make numpy pandas scipy yt 
"fftw=*=mpi_mpich*" pkg-config matplotlib mamba mpich mpi4py ninja pip virtualenv
conda activate warpx
```

Create a virtual environment for WarpX and install the dependencies. 
```bash markdown-code-runner
conda create -n warpx -c conda-forge blaspp boost ccache cmake compilers git "heffte=*=mpi_mpich*" 
lapackpp "openpmd-api=*=mpi_mpich*" openpmd-viewer python make numpy pandas scipy yt 
"fftw=*=mpi_mpich*" pkg-config matplotlib mamba mpich mpi4py ninja pip virtualenv
conda activate warpx
```


## Build WarpX

Get the source code
~~~
git clone https://github.com/ECP-WarpX/WarpX.git $HOME/src/warpx
cd $HOME/src/warpx
~~~
{: .language-bash}
Configure the build
~~~
cmake -S . -B build
~~~
{: .language-bash}

When configuring, you can pass different flags that enble or disable various options.  
For example: `cmake -S . -B build -DWarpX_DIMS=1 -DCMAKE_BUILD_TYPE=Debug`
will compile the code in 1D geometry and in debug mode.  
You can find the list of the build options and their default values 
[here](https://warpx.readthedocs.io/en/latest/install/cmake.html#build-options).  
For these tutorials, we compile in 1D, 2D, 3D and enable FFT calculations.
~~~
cmake -S . -B build -DWarpX_DIMS="1;2;3" -DWarpX_FFT=ON
~~~
{: .language-bash}
Finally, compile!
~~~
cmake --build build -j 4
~~~
{: .language-bash}
The executables will appear in `build/bin/`.


{% include links.md %}
