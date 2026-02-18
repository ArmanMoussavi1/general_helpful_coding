import numpy as np
import matplotlib.pyplot as plt

# Read and parse the data file
def read_msd_data(filename):
    """
    Read MSD data from file
    Format: timestep n_rows
            component_id msd_value  (where 1=x, 2=y, 3=z, 4=total)
            component_id msd_value
            ...
    Returns: time_steps array and dictionary with 'x', 'y', 'z', 'total' MSD arrays
    """
    time_steps = []
    msd_x = []
    msd_y = []
    msd_z = []
    msd_total = []
    
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip comments and empty lines
        if line.startswith('#') or len(line) == 0:
            i += 1
            continue
        
        # Check if this is a timestep line
        parts = line.split()
        if len(parts) == 2:
            try:
                timestep = int(parts[0])
                n_rows = int(parts[1])
                
                time_steps.append(timestep)
                
                # Read the next n_rows lines: component_id msd_value
                msd_values = {}
                for j in range(n_rows):
                    i += 1
                    data_parts = lines[i].strip().split()
                    component_id = int(data_parts[0])
                    msd_value = float(data_parts[1])
                    msd_values[component_id] = msd_value
                
                # Store values by component (1=x, 2=y, 3=z, 4=total)
                msd_x.append(msd_values.get(1, 0.0))
                msd_y.append(msd_values.get(2, 0.0))
                msd_z.append(msd_values.get(3, 0.0))
                msd_total.append(msd_values.get(4, 0.0))
                
            except (ValueError, IndexError) as e:
                print(f"Error parsing line {i}: {e}")
                pass
        
        i += 1
    
    return (np.array(time_steps), 
            {'x': np.array(msd_x), 
             'y': np.array(msd_y), 
             'z': np.array(msd_z), 
             'total': np.array(msd_total)})

# Read the data
filename = 'msd_lj.dat'
time_steps, msd_data = read_msd_data(filename)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot MSD for each component
plt.plot(time_steps, msd_data['x'], 
         marker='o', markersize=3, linewidth=1.5,
         label='MSD X')
plt.plot(time_steps, msd_data['y'], 
         marker='s', markersize=3, linewidth=1.5,
         label='MSD Y')
plt.plot(time_steps, msd_data['z'], 
         marker='^', markersize=3, linewidth=1.5,
         label='MSD Z')

# Plot total MSD
plt.plot(time_steps, msd_data['total'], 
         color='black', linewidth=2.5, linestyle='--',
         label='Total MSD')

# Formatting
plt.xlabel('Time (steps)', fontsize=12)
plt.ylabel('MSD', fontsize=12)
plt.title('Mean Square Displacement vs Time', fontsize=14, fontweight='bold')
plt.legend(fontsize=10)

# plt.xlim(0,5000)
# plt.ylim(0,3)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save the figure
plt.savefig('msd_plot.png', dpi=300, bbox_inches='tight')
print("Figure saved as 'msd_plot.png'")

# Show the plot
plt.show()
