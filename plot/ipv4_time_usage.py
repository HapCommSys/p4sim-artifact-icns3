import numpy as np
import matplotlib.pyplot as plt

# Set global font size
font_size = 14

# Transmit Rate & Link Rate (Unit: Mbps)
bandwidths = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000, 10000]

# Generate a uniformly distributed x-axis
x_uniform = np.linspace(1, len(bandwidths), len(bandwidths))

# Simulation execution time (unit: ms)
measured_time_p4sim = [
    5401, 7228, 8518, 11710, 12124, 15211, 15332, 17881, 19430, 21006, 22201, 189805, 1747683,
]

measured_time_ns3 = [
    90, 648, 1247, 1859, 2473, 3028, 3696, 4262, 4907, 5461, 5995, 59861, 589413,
]

# Convert time from ms to seconds
measured_time_p4sim = [t / 1000 for t in measured_time_p4sim]
measured_time_ns3 = [t / 1000 for t in measured_time_ns3]

# Create a graph
fig, ax = plt.subplots(figsize=(8, 5))
fig.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.15)  # Adjust the margins

# Set y-axis to logarithmic scale
plt.yscale("log")

# Plot P4 Simulator execution time curve
plt.plot(x_uniform, measured_time_p4sim, label="p4sim Execution Time", linestyle='-', marker='o', color='#B85450', linewidth=2)

# Plot ns3 execution time curve
plt.plot(x_uniform, measured_time_ns3, label="ns-3 Execution Time", linestyle='--', marker='s', color='#527cb4', linewidth=2)

# Set x-axis ticks (keep uniform distribution but format large values)
formatted_xticks = [r"$10^3$" if x == 1000 else
                    r"$10^4$" if x == 10000 else str(x)
                    for x in bandwidths]

plt.xticks(x_uniform, formatted_xticks, fontsize=font_size)

# Axis labels
plt.xlabel("Input Traffic Throughput (Mbps)", fontsize=font_size)
plt.ylabel("Simulation Execution Time (s)", fontsize=font_size)

# Add grid
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Add legend
plt.legend(fontsize=font_size)

# Save as PDF
pdf_filename = "network_simulation_time.pdf"
plt.savefig(pdf_filename, format="pdf")

# Show the chart
plt.show()
