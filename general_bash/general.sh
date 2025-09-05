
# Create a conda environment
module load python/anaconda3.6
conda create --name env_name
source activate env_name


# Create a compressed archive of a directory using tar and gzip
tar -czvf archive_name.tar.gz /path/to/your_directory/

# List size of all directories in current directory
du -hd1


# Reload .bashrc
source ~/.bashrc
