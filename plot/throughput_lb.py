
import matplotlib.pyplot as plt
import numpy as np

# Set global font size
font_size = 14

# Read data from file
def read_data(filename):
    data = np.loadtxt(filename)
    time = data[:, 0]  # First column: time
    input_traffic = data[:, 1] / 1000  # Second column: Input Traffic (converted to Gbps)
    path_a = data[:, 2] / 1000  # Third column: Path A Traffic (Gbps)
    path_b = data[:, 3] / 1000  # Fourth column: Path B Traffic (Gbps)
    received_traffic = data[:, 4] / 1000  # Fifth column: Received Traffic (Gbps)

    length = len(time)
    time = np.linspace(0, length - 1, length)  # Re-generate time series
    
    return time, input_traffic, path_a, path_b, received_traffic

def plot_traffic(time, input_traffic, path_a, path_b, received_traffic):
    fig, ax = plt.subplots(figsize=(8, 5))  # Adjust the figure size as needed

    # Adjust the layout to prevent overlap
    fig.subplots_adjust(left=0.15, right=0.95, top=0.95, bottom=0.15)  

    # Set the font size for the entire plot
    plt.rcParams.update({'xtick.labelsize': font_size, 'ytick.labelsize': font_size})  

    # Plot Input Traffic and Received Traffic
    ax.plot(time, input_traffic, label='Input Traffic', linestyle='-', marker='o', color='#B85450', linewidth=2)
    ax.plot(time, received_traffic, label='Received Traffic', linestyle=':', marker='d', color='#f9c776', linewidth=2)

    # Stacked bar chart for Path A and Path B
    ax.bar(time, path_a, width=0.6, label='Path A', alpha=0.9, color="#d1e2ef")
    ax.bar(time, path_b, width=0.6, bottom=path_a, label='Path B', alpha=0.9, color='#7fa9cd')

    # Add 50% input traffic reference line
    input_half = input_traffic / 2
    ax.plot(time, input_half, label='50% Input Traffic', linestyle='--', color='gray', linewidth=2)

    ax.tick_params(axis='x', labelsize=font_size)  # Adjust the x-axis tick label size
    ax.tick_params(axis='y', labelsize=font_size)  # Adjust the y-axis tick label size

    # Set labels to ensure they apply to `ax` instead of `plt`
    ax.set_xlabel('Simulation Time (s)', fontsize=font_size)
    ax.set_ylabel('Traffic Throughput (Gbps)', fontsize=font_size)

    # Unify legend position and font size
    ax.legend(loc='lower right', fontsize=font_size)

    # Add grid
    ax.grid(True)

    # Disable `tight_layout()` to keep the two plots consistent
    # plt.tight_layout()

    # Save PDF without using bbox_inches="tight"
    output_pdf = "load_balancing.pdf"
    plt.savefig(output_pdf, format='pdf')

    plt.show()


if __name__ == "__main__":
    filename = "traffic_data.txt"  # Replace with your actual file name
    time, input_traffic, path_a, path_b, received_traffic = read_data(filename)
    plot_traffic(time, input_traffic, path_a, path_b, received_traffic)
    
