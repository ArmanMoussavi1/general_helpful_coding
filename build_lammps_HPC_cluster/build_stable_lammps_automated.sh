#!/bin/bash
# Written by Arman Moussavi
# Last updated: 09-04-2025

# Clone the stable branch of the LAMMPS repository into a directory named "lammps_stable"
git clone -b stable https://github.com/lammps/lammps.git lammps_stable

# Navigate into the cloned repository
cd lammps_stable/ 

# Create a build directory inside the LAMMPS directory and navigate into it
mkdir build && cd build/

# Purge all loaded modules to avoid conflicts
module purge

# Load required modules for compiling LAMMPS (make require newer versions of cmake)
module load gcc/10.2.0 mpi/openmpi-4.1.1-gcc.10.2.0 cmake/3.22.4

# Run CMake to configure the LAMMPS build  
    # Edit package options below as needed to include/exclude specific features
    # Remove unnecessary packages to optimize compilation time and reduce memory usage
cmake -D CMAKE_C_COMPILER=$(which mpicc) \
      -D CMAKE_CXX_COMPILER=$(which mpicxx) \
      -D CMAKE_CXX_STANDARD=17 \
      -D PKG_DPD-BASIC=yes \
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
      ../cmake  # Specify the source directory for CMake configuration


# Simple Build
cmake ../cmake \
  -D CMAKE_C_COMPILER=$(which mpicc) \
  -D CMAKE_CXX_COMPILER=$(which mpicxx) \
  -D CMAKE_CXX_STANDARD=17 \
  -D BUILD_MPI=yes \
  -D PKG_X11=no     # disable GUI



# Compile and install LAMMPS using 4 parallel threads
make -j4 install


# NOTE: To run LAMMPS after installation, ensure that the correct modules are loaded:
# module load gcc/10.2.0 mpi/openmpi-4.1.1-gcc.10.2.0 cmake/3.22.4



# Example command to run LAMMPS with 4 MPI processes:
# mpirun -np 4 <path_to_lammps_stable>/build/lmp -i input_script.in
#
# Replace `<path_to_lammps_stable>` with the path where LAMMPS was cloned/built
# Replace `input_script.in` with the LAMMPS input file for your simulation
# Adjust the number of MPI processes (`-np 4`) based on available resources
