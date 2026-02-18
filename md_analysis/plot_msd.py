import numpy as np
import matplotlib.pyplot as plt
import argparse

# Read and parse the data file
def read_msd_data(filename):
    """
    Read MSD data from file
    Supports two formats:
    
    Format 1 (simple): timestep msd_value
    
    Format 2 (multi-component): 
            timestep n_rows
            component_id msd_value  (where 1=x, 2=y, 3=z, 4=total)
            ...
    
    Returns: time_steps array and dictionary with available components
    """
    time_steps = []
    msd_data = {}
    
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    i = 0
    format_type = None  # Will be detected from first data line
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip comments and empty lines
        if line.startswith('#') or len(line) == 0:
            i += 1
            continue
        
        # Parse data line
        parts = line.split()
        if len(parts) >= 2:
            try:
                timestep = int(parts[0])
                
                # Detect format from first data line
                if format_type is None:
                    if len(parts) == 2:
                        # Check if second value is int (n_rows) or float (msd_value)
                        try:
                            int(parts[1])
                            format_type = 'multi-component'
                        except ValueError:
                            format_type = 'simple'
                    else:
                        format_type = 'simple'
                
                time_steps.append(timestep)
                
                if format_type == 'simple':
                    # Format: timestep msd_value
                    msd_value = float(parts[1])
                    if 'total' not in msd_data:
                        msd_data['total'] = []
                    msd_data['total'].append(msd_value)
                    
                elif format_type == 'multi-component':
                    # Format: timestep n_rows
                    n_rows = int(parts[1])
                    msd_values = {}
                    
                    # Read the next n_rows lines: component_id msd_value
                    for j in range(n_rows):
                        i += 1
                        data_parts = lines[i].strip().split()
                        component_id = int(data_parts[0])
                        msd_value = float(data_parts[1])
                        msd_values[component_id] = msd_value
                    
                    # Store values by component (1=x, 2=y, 3=z, 4=total)
                    component_map = {1: 'x', 2: 'y', 3: 'z', 4: 'total'}
                    for comp_id, comp_name in component_map.items():
                        if comp_name not in msd_data:
                            msd_data[comp_name] = []
                        msd_data[comp_name].append(msd_values.get(comp_id, 0.0))
                
            except (ValueError, IndexError) as e:
                print(f"Error parsing line {i}: {e}")
                pass
        
        i += 1
    
    # Convert lists to numpy arrays
    for key in msd_data:
        msd_data[key] = np.array(msd_data[key])
    
    return (np.array(time_steps), msd_data)

# Parse command line arguments
parser = argparse.ArgumentParser(description='Plot Mean Square Displacement (MSD) data')
parser.add_argument('-f', '--file', type=str, default='msd_lj.dat',
                    help='Input data file (default: msd_lj.dat)')
parser.add_argument('-c', '--components', type=str, nargs='+', 
                    help='MSD components to plot (e.g., x y z total). If not specified, all available components are plotted.')
parser.add_argument('-o', '--output', type=str, default='msd_plot.png',
                    help='Output figure filename (default: msd_plot.png)')

args = parser.parse_args()

# Read the data
time_steps, msd_data = read_msd_data(args.file)

# Determine which components to plot
available_components = list(msd_data.keys())
if args.components:
    # Filter to requested components that are available
    components_to_plot = [c for c in args.components if c in available_components]
    if not components_to_plot:
        print(f"Warning: None of the requested components {args.components} are available.")
        print(f"Available components: {available_components}")
        components_to_plot = available_components
else:
    components_to_plot = available_components

print(f"Plotting components: {components_to_plot}")

# Create the plot
plt.figure(figsize=(10, 6))

# Define plot styles for each component
plot_styles = {
    'x': {'marker': 'o', 'markersize': 3, 'linewidth': 1.5, 'label': 'MSD X'},
    'y': {'marker': 's', 'markersize': 3, 'linewidth': 1.5, 'label': 'MSD Y'},
    'z': {'marker': '^', 'markersize': 3, 'linewidth': 1.5, 'label': 'MSD Z'},
    'total': {'color': 'black', 'linewidth': 2.5, 'linestyle': '--', 'label': 'Total MSD'}
}

# Plot selected components
for component in components_to_plot:
    plt.plot(time_steps, msd_data[component], **plot_styles[component])

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
plt.savefig(args.output, dpi=300, bbox_inches='tight')
print(f"Figure saved as '{args.output}'")

# Show the plot
plt.show()
