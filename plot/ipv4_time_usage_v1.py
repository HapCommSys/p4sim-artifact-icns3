import numpy as np
import matplotlib.pyplot as plt

# Set global font size
font_size = 15

# Transmit Rate & Link Rate (Unit: Mbps)
bandwidths = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000, 10000]

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

# Split x-axis range
x1 = bandwidths[:11]   # 1 - 100
x2 = bandwidths[11:]   # 1000 - 10000

fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(8, 5), gridspec_kw={'width_ratios': [3, 1]})
fig.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.15, wspace=0.1)

# Set y-axis to logarithmic scale
ax1.set_yscale("log")
ax2.set_yscale("log")

# Plot P4 Simulator execution time scatter points
ax1.scatter(x1, measured_time_p4sim[:11], label="P4sim", marker='x', color='#B85450', s=100)
ax2.scatter(x2, measured_time_p4sim[11:], marker='x', color='#B85450', s=100)

# Plot ns3 execution time scatter points
ax1.scatter(x1, measured_time_ns3[:11], label="ns-3", marker='o', color='#527cb4')
ax2.scatter(x2, measured_time_ns3[11:], marker='o', color='#527cb4')

# Set x-axis limits
ax1.set_xlim(0, 105)
ax2.set_xlim(500, 11000)

# Remove some spines to create a broken axis effect
ax1.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)

# Add x-axis ticks (scientific notation)
ax1.set_xticks(x1)
ax2.set_xticks(x2)

ax1.set_xticklabels([str(x) for x in x1], fontsize=font_size)
ax2.set_xticklabels([r"$10^3$", r"$10^4$"], fontsize=font_size)

# ----- Adjustable slope & gap for broken axis -----
dx = 0.005  # Control x-axis slope
dy = 0.02   # Control y-axis slope (dy > dx makes the angle steeper)
delta_y = 0.04  # Control the gap between the two slanted lines

line_width = 1.8
kwargs = dict(transform=fig.transFigure, color='black', linewidth=line_width, clip_on=False)

# Get Figure coordinates
x1_fig, y_base = ax1.transAxes.transform((1, 0))
x1_fig /= fig.bbox.width
y_base /= fig.bbox.height
y_top = ax1.transAxes.transform((1, 1))[1] / fig.bbox.height

x2_fig = ax2.transAxes.transform((0, 0))[0] / fig.bbox.width

# Draw left side (right axis broken)
ax1.plot([x1_fig - dx, x1_fig + dx], [y_base - dy, y_base + dy], **kwargs)
# ax1.plot([x1_fig - dx, x1_fig + dx], [y_base - dy + delta_y, y_base + dy + delta_y], **kwargs)

ax1.plot([x1_fig - dx, x1_fig + dx], [y_top - dy, y_top + dy], **kwargs)
# ax1.plot([x1_fig - dx, x1_fig + dx], [y_top - dy - delta_y, y_top + dy - delta_y], **kwargs)

# Draw right side (left axis broken)
ax2.plot([x2_fig - dx, x2_fig + dx], [y_base - dy, y_base + dy], **kwargs)
# ax2.plot([x2_fig - dx, x2_fig + dx], [y_base - dy + delta_y, y_base + dy + delta_y], **kwargs)

ax2.plot([x2_fig - dx, x2_fig + dx], [y_top - dy, y_top + dy], **kwargs)
# ax2.plot([x2_fig - dx, x2_fig + dx], [y_top - dy - delta_y, y_top + dy - delta_y], **kwargs)
# ---------------------------------------


# Axis labels and titles
# ax1.set_xlabel("Input Traffic Throughput (Mbps)", fontsize=font_size)
ax1.tick_params(axis='y', labelsize=font_size)  # Adjust the y-axis tick label size for ax1
ax1.set_ylabel("Wall-Clock Time (s)", fontsize=font_size)

# Add grid
ax1.grid(True, which="both", linestyle="--", linewidth=0.5)
ax2.grid(True, which="both", linestyle="--", linewidth=0.5)

# Add legend to the upper left corner
ax1.legend(fontsize=font_size, loc="upper left")
fig.text(0.5, 0.05, "Input Throughput (Mbps)", fontsize=font_size, ha='center')
# Add global y-axis label (centered) for the entire figure
# fig.text(0.02, 0.5, "Simulation Execution Time (s)", fontsize=font_size, ha='center', va='center', rotation=90)
# Save PDF
pdf_filename = "network_simulation_time_comparison.pdf"
plt.savefig(pdf_filename, format="pdf")

plt.show()
