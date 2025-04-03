#!/bin/bash
# Written by Arman Moussavi
# Last updated: 04-03-2025

# Clone the stable branch of the LAMMPS repository into a directory named "lammps_stable"
git clone -b stable https://github.com/lammps/lammps.git lammps_stable

# Navigate into the cloned repository
cd lammps_stable/ 

# Create a build directory inside the LAMMPS directory and navigate into it
mkdir build && cd build/

# Purge all loaded modules to avoid conflicts
module purge

# Load required modules for compiling LAMMPS
# module load cmake/3.15.4 mpi/openmpi-4.1.1-gcc.10.2.0 gcc/11.2.0 hdf5/1.10.8-openmpi-3.1.3-gcc-8.4.0 

module load gcc/10.4.0-gcc-4.8.5 hdf5/1.10.7-openmpi-intel-2021.4.0 git/2.37.2 intel-oneapi-mkl/2023.1.0-intel-2021.4.0 mpi/openmpi-4.1.6rc2-intel-2021.4.0 cmake/3.26.3-intel-2021.4.0 intel-oneapi-compilers/2021.4.0-gcc-10.4.0 ffmpeg/4.2.2-intel-19.0.5.281 fftw/3.3.4-openmpi-4.0.5-intel-19.0.5.281

# Run CMake to configure the LAMMPS build  
    # Edit package options below as needed to include/exclude specific features
    # Remove unnecessary packages to optimize compilation time and reduce memory usage
cmake -D PKG_DPD-BASIC=yes \
      -D PKG_EXTRA-FIX=yes \
      -D PKG_GRANULAR=yes \
      -D PKG_MOLECULE=yes \
      -D PKG_CLASS2=yes \
      -D PKG_EXTRA-PAIR=yes \
      -D PKG_KSPACE=yes \
      -D PKG_BROWNIAN=yes \
      -D PKG_RIGID=yes \
      -D PKG_MC=yes \
      -D BUILD_MPI=yes \
      -D PKG_USER-SMD=yes \
      -D PKG_USER-MISC=yes \
      -D DOWNLOAD_EIGEN3=yes \
      -D PKG_MANYBODY=yes \
      -D PKG_INTEL=yes
      -D PKG_USER-COLVARS=yes \
      -DCMAKE_C_COMPILER=gcc \
      -DCMAKE_CXX_COMPILER=g++ \
      -DCMAKE_Fortran_COMPILER=gfortran \
      -D FFT=MKL
      ../cmake  # Specify the source directory for CMake configuration

# Compile and install LAMMPS using 4 parallel threads
make -j4 install


# NOTE: To run LAMMPS after installation, ensure that the correct modules are loaded:
# module load gcc/10.4.0-gcc-4.8.5 hdf5/1.10.7-openmpi-intel-2021.4.0 git/2.37.2 intel-oneapi-mkl/2023.1.0-intel-2021.4.0 mpi/openmpi-4.1.6rc2-intel-2021.4.0 cmake/3.26.3-intel-2021.4.0 intel-oneapi-compilers/2021.4.0-gcc-10.4.0 ffmpeg/4.2.2-intel-19.0.5.281 fftw/3.3.4-openmpi-4.0.5-intel-19.0.5.281


# Example command to run LAMMPS with 4 MPI processes:
# mpirun -np 4 <path_to_lammps_stable>/build/lmp -i input_script.in
#
# Replace `<path_to_lammps_stable>` with the path where LAMMPS was cloned/built
# Replace `input_script.in` with the LAMMPS input file for your simulation
# Adjust the number of MPI processes (`-np 4`) based on available resources
