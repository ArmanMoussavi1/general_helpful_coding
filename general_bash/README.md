

# Quick Reference Guide for Linux/Conda/VS Code

This document provides a concise reference for common Linux, conda, and VS Code commands for managing environments, files, and development setups.

## Table of Contents
- [Conda Environment Management](#conda-environment-management)
- [File and Directory Management](#file-and-directory-management)
- [System Maintenance](#system-maintenance)
- [VS Code Cleanup](#vs-code-cleanup)
- [Basic Linux Commands](#basic-linux-commands)

## Conda Environment Management

### Create a Conda Environment
Create a new conda environment with a specified name.
```bash
module load python/anaconda3.6
conda create --name env_name
```

### Activate a Conda Environment
Switch to the specified conda environment.
```bash
source activate env_name
```

### Deactivate a Conda Environment
Exit the current conda environment.
```bash
conda deactivate
```

### List All Conda Environments
Display all available conda environments.
```bash
conda env list
```

### Install a Package in an Environment
Install a specific package in the active environment.
```bash
conda install package_name
```

### Remove a Conda Environment
Delete a specified conda environment.
```bash
conda env remove --name env_name
```

## File and Directory Management

### Create a Compressed Archive
Compress a directory into a `.tar.gz` archive.
```bash
tar -czvf archive_name.tar.gz /path/to/your_directory/
```

### Extract a Compressed Archive
Decompress and extract a `.tar.gz` archive.
```bash
tar -xzvf archive_name.tar.gz
```

### List Directory Sizes
Show the size of all directories in the current directory (human-readable, depth=1).
```bash
du -hd1
```

### Move a Directory
Move a directory from one location to another.
```bash
mv source_directory destination_directory
```

### Copy a Directory
Copy a directory and its contents to another location.
```bash
cp -r source_directory destination_directory
```

### Remove a Directory
Delete a directory and its contents (use with caution).
```bash
rm -rf directory_name
```

## System Maintenance

### Reload `.bashrc`
Refresh the shell configuration to apply changes in `.bashrc`.
```bash
source ~/.bashrc
```

### Clean Unused Conda Packages
Remove unused packages across all conda environments.
```bash
conda clean --packages --yes
```

### Clean All Conda Caches

First — see what would be deleted and how much space you'd save
```bash
conda clean --all --dry-run
```

Remove all caches, tarballs, and logs from conda.
```bash
conda clean --all --yes
```

### Check Disk Usage
Display disk usage statistics for the current filesystem.
```bash
df -h
```

## VS Code Cleanup

### Clean VS Code Server Files
Remove old VS Code server binaries and extensions (safe, as VS Code re-downloads needed files).
```bash
rm -rf ~/.vscode-server/bin/*
rm -rf ~/.vscode-server/extensions/*
```

### Clean VS Code Logs
Remove VS Code log files to free up space.
```bash
rm -rf ~/.vscode-server/data/logs/*
```

### Notes on VS Code Cleanup
- Only remove `bin/<commit_hash>` folders that do not match your current VS Code version.
- Extensions in `extensions/` can be safely removed if unneeded; VS Code will re-download them as required.

## Basic Linux Commands

### List Files and Directories
List files and directories in the current directory (with details).
```bash
ls -l
```

### Change Directory
Navigate to a specified directory.
```bash
cd /path/to/directory
```

### Print Working Directory
Display the current working directory.
```bash
pwd
```

### View File Contents
Display the contents of a file.
```bash
cat filename
```

### Create a File
Create an empty file or update the timestamp of an existing file.
```bash
touch filename
```

### Check Running Processes
List currently running processes.
```bash
ps aux
```

### Monitor System Resources
Display real-time system resource usage (CPU, memory, etc.).
```bash
top
```

### Find Files
Search for files matching a pattern in a directory.
```bash
find /path/to/directory -name "pattern"
```

