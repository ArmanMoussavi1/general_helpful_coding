#!/bin/bash

How to Set Up and Use Aliases in Bash

Aliases in Bash are shortcuts for longer commands that you use frequently. You can define them in your Bash configuration files, such as ~/.bashrc or ~/.bash_profile, so that they are available every time you open a new terminal session.


Step 1: Open Your Bash Configuration File
    To define aliases that persist across terminal sessions, you need to edit your Bash configuration file.

    1. Open your terminal.
    2. Open the ~/.bashrc file (or ~/.bash_profile on some systems) in a text editor. For example, using nano:
       nano ~/.bashrc


Step 2: Define Aliases
    In the configuration file, you can define aliases by using the alias command. Here is an example of how to define an alias:

        alias g="git"


Step 3: Save and Close the File
    After adding the aliases, save the file and exit the text editor.

    - In nano, press `CTRL + O` to save, then `CTRL + X` to exit.


Step 4: Apply the Changes
    To apply the changes, run the following command to reload the configuration file:

       source ~/.bashrc


Step 5: Test the Aliases
    Once the configuration is reloaded, you can test the aliases by simply typing the alias name in the terminal:

    - To run the `g` command, type:
      g



#########################
HELPFUL ALIASES
#########################

# On HPC clusters:
sqme Alias:
    This alias runs the squeue command for the user amp4121 and formats the output with specific columns.

    alias sqme="squeue -u amp4121 --format='%.18i %.9P %.64j %.8u %.2t %.10M %.9l %.6D %R'"

sacct Alias:
    This alias runs the sacct command with a custom format.

    alias sacct="sacct --format='JobID,JobName%50,Partition,Account,AllocCPUS,State,ExitCode'"