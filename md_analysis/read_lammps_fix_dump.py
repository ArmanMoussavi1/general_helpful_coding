
import numpy as np
from typing import Dict, List, Tuple

def read_lammps_fix_dump(filename: str) -> Dict[int, np.ndarray]:
    """
    Read LAMMPS fix autocorrelation dump file.
    
    Parameters:
    -----------
    filename : str
        Path to the LAMMPS dump file
    
    Returns:
    --------
    dict
        Dictionary where keys are timesteps and values are numpy arrays
        with columns: [Index, TimeDelta, Ncount, Autocorrelation]
    
    Example:
    --------
    >>> data = read_lammps_fix_dump('vacf_np.dat')
    >>> timesteps = list(data.keys())
    >>> print(f"Available timesteps: {timesteps}")
    >>> print(f"Data at timestep 0:\n{data[0]}")
    """
    data = {}
    current_timestep = None
    current_data = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            
            # Skip empty lines and comment lines starting with #
            if not line or line.startswith('#'):
                continue
            
            parts = line.split()
            
            # Check if this is a timestep header (2 values: timestep and n_windows)
            if len(parts) == 2:
                # Save previous timestep data if it exists
                if current_timestep is not None and current_data:
                    data[current_timestep] = np.array(current_data)
                
                # Start new timestep
                current_timestep = int(parts[0])
                current_data = []
            
            # Otherwise it's data (4 values: index, timedelta, ncount, autocorr)
            elif len(parts) == 4:
                current_data.append([float(x) for x in parts])
    
    # Don't forget to save the last timestep
    if current_timestep is not None and current_data:
        data[current_timestep] = np.array(current_data)
    
    return data





# Example usage
if __name__ == "__main__":
    # Replace np.loadtxt with this function
    filepath = 'vacf.dat'
    data = read_lammps_fix_dump(filepath)
    
    print(f"Number of timesteps: {len(data)}")
    print(f"Available timesteps: {list(data.keys())}")
    
