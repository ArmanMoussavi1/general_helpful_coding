
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


# System clean-up
## Clean unused packages across all envs
conda clean --packages --yes

## Clean all caches, tarballs, and logs
conda clean --all --yes




# Clean VScode
# You can safely remove:
#   Old bin/<commit_hash> folders except the one matching your current VS Code version.
#   Unneeded extensions inside extensions/.
#   Logs in data/logs/.
# VS Code will automatically re-download what it needs when you reconnect.
# Common cleanup:

rm -rf ~/.vscode-server/bin/*
rm -rf ~/.vscode-server/extensions/*


