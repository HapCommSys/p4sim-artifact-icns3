def read_and_compute_ratios(file_path):
    ratios = []
    with open(file_path, 'r') as f:
        for line in f:
            if not line.strip():
                continue
            parts = line.strip().split()
            if len(parts) < 4:
                continue
            try:
                col3 = float(parts[2])
                col4 = float(parts[3])
                if col4 != 0:
                    ratio = col3 / col4
                    ratios.append(ratio)  # just store the ratio
            except ValueError:
                continue
    return ratios

# Example usage
file_path = "traffic_data.txt"
ratios = read_and_compute_ratios(file_path)

# Print each ratio
for i, r in enumerate(ratios):
    print(f"Line {i+1}: Ratio (Col3 / Col4) = {r:.4f}")

# Compute and print average
if ratios:
    avg_ratio = sum(ratios) / len(ratios)
    print(f"\nAverage Ratio (Col3 / Col4): {avg_ratio:.4f}")
else:
    print("No valid ratios to compute.")
