import pandas as pd

def parse_lammps_dump(filename):
    """
    Parse a LAMMPS dump file into a list of snapshots.
    Each snapshot is a dictionary with:
      - 'timestep': int
      - 'natoms': int
      - 'box': list of (lo, hi) tuples
      - 'atoms': pandas.DataFrame with atom properties
    """
    snapshots = []

    with open(filename, "r") as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        if lines[i].startswith("ITEM: TIMESTEP"):
            timestep = int(lines[i+1].strip())
            i += 2

            assert lines[i].startswith("ITEM: NUMBER OF ATOMS")
            natoms = int(lines[i+1].strip())
            i += 2

            assert lines[i].startswith("ITEM: BOX BOUNDS")
            box = []
            for j in range(3):
                lo, hi = map(float, lines[i+j+1].split())
                box.append((lo, hi))
            i += 4

            assert lines[i].startswith("ITEM: ATOMS")
            columns = lines[i].split()[2:]  # column names after "ITEM: ATOMS"
            i += 1

            atom_data = []
            for j in range(natoms):
                values = lines[i+j].split()
                values = [int(v) if k < 3 else float(v) for k, v in enumerate(values)]  # first 3 cols int
                atom_data.append(values)
            i += natoms

            df = pd.DataFrame(atom_data, columns=columns)

            snapshots.append({
                "timestep": timestep,
                "natoms": natoms,
                "box": box,
                "atoms": df
            })
        else:
            i += 1

    return snapshots
