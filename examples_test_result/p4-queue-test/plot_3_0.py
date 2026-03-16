import dpkt
import pandas as pd
import matplotlib.pyplot as plt

# ======= Global data and function examples (keep the same structure as your original) =======
font_size = 20

# buffer data to plot
input_pkts_pps = [0, 1497, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 1500, 0]
Egress_pps =     [0, 1197, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 999]
egress_buffer_p_3 = [0, 299, 599, 899, 998, 998, 998, 998, 998, 998, 998, 0]
egress_buffer_p_1 = [0]*12
egress_buffer_p_2 = [0]*12
time = [i for i in range(0, 12)]

def parse_pcap_latency(file_path, direction):
    """Use dpkt to parse the pcap file and extract the UDP traffic and IPv4 ID of the specified port"""
    with open(file_path, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        data = []
        for timestamp, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                if isinstance(ip.data, dpkt.udp.UDP):
                    udp = ip.data
                    dest_port = udp.dport
                    ipv4_id = ip.id
                    if dest_port in [2000, 3000, 4000]:
                        data.append([timestamp, dest_port, ipv4_id, direction])
    return pd.DataFrame(data, columns=['timestamp', 'port', 'ipv4_id', 'direction'])

def compute_latency(df_A, df_B):
    """Calculate the latency for the same IPv4 ID and average latency in seconds"""
    # Merge
    df_merged = pd.merge(df_A, df_B, on=['ipv4_id', 'port'], suffixes=('_A', '_B'))
    df_merged['latency'] = df_merged['timestamp_B'] - df_merged['timestamp_A']
    
    # Calculate the average delay per second
    df_merged['time'] = df_merged['timestamp_B'].apply(lambda x: int(x + 0.5)) # Round to the nearest second
    avg_latency_per_second = df_merged.groupby(['time', 'port'])['latency'].mean().unstack(fill_value=0)
    
    # print(avg_latency_per_second)

    return df_merged[['timestamp_B', 'port', 'latency']], avg_latency_per_second

def parse_pcap_pps(file_path):
    """Use dpkt to parse the pcap file and extract the UDP traffic for packet count"""
    with open(file_path, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        data = []
        for timestamp, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)
            if isinstance(eth.data, dpkt.ip.IP):
                ip = eth.data
                if isinstance(ip.data, dpkt.udp.UDP):
                    udp = ip.data
                    dest_port = udp.dport
                    if dest_port in [2000, 3000, 4000]:
                        data.append([timestamp, dest_port])
    return pd.DataFrame(data, columns=['timestamp', 'port'])

def compute_packet_count(df):
    """Calculate the packet count per second"""
    # df['time'] = df['timestamp'].apply(lambda x: int(x + 0.5))  # Round to the nearest second
    df['time'] = df['timestamp'].apply(lambda x: int(x+1))  # Round to the nearest second

    packet_count_per_second = df.groupby(['time', 'port']).size().unstack(fill_value=0)
    # Calculate the total packet count
    packet_count_per_second['Total'] = packet_count_per_second.sum(axis=1)

    # Ensure the last second's data is included
    if not df.empty:
        max_time = df['time'].max()
        if max_time not in packet_count_per_second.index:
            packet_count_per_second.loc[max_time] = 0
    
    return packet_count_per_second

# ======= Plotting function =======
# This function will plot the buffer, packet count, and latency in a single figure with 3 subplots
# Each subplot will have its own y-axis and title, and they will be arranged in a single column with 3 rows.
# The first subplot will show the buffer occupancy, the second will show the packet count, and the third will show the latency.
# The x-axis will be the time in seconds, and the y-axis will be the respective values for each subplot.
def plot_all_in_one():
    """Plot buffer, packet count, and latency in a single figure with 3 subplots"""
    pcap_A = "p4-queue-test-0-0.pcap"
    pcap_B = "p4-queue-test-2-0.pcap"

    # For latency, we need to parse the pcap files
    df_A_latency = parse_pcap_latency(pcap_A, 'A')
    df_B_latency = parse_pcap_latency(pcap_B, 'B')
    # Calculate latency
    latency_df, avg_latency_per_second = compute_latency(df_A_latency, df_B_latency)
    max_time_latency = int(latency_df['timestamp_B'].max()) if not latency_df.empty else 0

    # print("max_time_latency: ", max_time_latency)

    time_range_latency = list(range(0, max_time_latency + 2)) # we add 2 seconds to make sure the last second is included (0-21s)
    # print ("time_range_latency: ", time_range_latency)
    # avg_latency_per_second = avg_latency_per_second.reindex(time_range_latency, fill_value=0)

    # For pps, we need to parse the pcap files
    df_A_pps = parse_pcap_pps(pcap_A)
    df_B_pps = parse_pcap_pps(pcap_B)
    packet_A = compute_packet_count(df_A_pps)
    packet_B = compute_packet_count(df_B_pps)

    packet_A.to_csv("packet_A.csv")
    packet_B.to_csv("packet_B.csv")

    max_time_pps = max(packet_A.index.max(), packet_B.index.max()) if not (packet_A.empty or packet_B.empty) else 0
    print("max_time_pps: ", max_time_pps)

    time_range_pps = list(range(0, max_time_pps + 1))
    packet_A = packet_A.reindex(time_range_pps, fill_value=0)
    packet_B = packet_B.reindex(time_range_pps, fill_value=0)
    
    # 2) Create a figure and set 1 column and 3 rows through subplots + gridspec_kw

    # Create a figure and set 1 column and 3 rows through subplots + gridspec_kw
    fig, axes = plt.subplots(
        3, 1,
        figsize=(15, 13),  # You can adjust the overall width and height
        gridspec_kw={'height_ratios': [0.8, 0.8, 0.4]}  # The 1,1,0.4 here is the relative height ratio, adjustable
    )


    # plt.rcParams.update({'xtick.labelsize': font_size, 'ytick.labelsize': font_size})

    # To prevent overlapping of subplots, enable tight layout
    plt.tight_layout(h_pad=3)  # You can adjust h_pad to control the vertical spacing between subplots

    # 1) First subplot: buffer plotting
    ax1 = axes[0]
    ax1.plot(time, input_pkts_pps, label="Total input rate", linestyle='-', marker='o')
    ax1.plot(time, Egress_pps, label="Dequeue rate", linestyle='-', marker='s')
    ax1.plot(time, egress_buffer_p_3, label="Queue len (TX 3)", linestyle='--', marker='^')
    ax1.plot(time, egress_buffer_p_1, label="Queue len (TX 2)", linestyle='--', marker='d')
    ax1.plot(time, egress_buffer_p_2, label="Queue len (TX 1)", linestyle='--', marker='x')


    ax1.set_xlim(0, 12) # Unify the X-axis range
    # ax1.set_xlabel("Time (s)", fontsize=font_size)
    ax1.set_ylabel("Packets Count [pps]", fontsize=font_size)
    ax1.set_title("(A) Virtual Queue Occupancy", fontsize=font_size)
    ax1.grid(True)
    ax1.tick_params(axis='both', labelsize=font_size)
    
    # Place the legend on the right
    ax1.legend(fontsize=font_size, bbox_to_anchor=(1.05, 0.5), loc='center left')

    # 2) Second subplot: packet count plotting
    ax2 = axes[1]

    print("packet_A: ", packet_A)

    ax2.plot(time_range_pps, packet_A[2000], label='TX flow 1', linestyle='-')
    ax2.plot(time_range_pps, packet_A[3000], label='TX flow 2', linestyle='-')
    ax2.plot(time_range_pps, packet_A[4000], label='TX flow 3', linestyle='-')
    ax2.plot(time_range_pps, packet_A['Total'], label='TX sum', linestyle='-')

    print("packet_B: ", packet_B)

    ax2.plot(time_range_pps, packet_B[2000], label='RX flow 1', linestyle='--', marker='o')
    ax2.plot(time_range_pps, packet_B[3000], label='RX flow 2', linestyle='--', marker='D')
    ax2.plot(time_range_pps, packet_B[4000], label='RX flow 3', linestyle='--', marker='^')
    ax2.plot(time_range_pps, packet_B['Total'], label='RX sum', linestyle='--', marker='s')

    ax2.set_xlim(0, 12)
    # ax2.set_xlabel('Time (s)', fontsize=font_size)
    ax2.set_ylabel('Packet Count [pps]',  fontsize=font_size)
    ax2.set_title("(B) Throughput", fontsize=font_size)
    ax2.grid(True)
    ax2.tick_params(axis='both', labelsize=font_size)

    # Place the legend on the right
    ax2.legend(fontsize=font_size, bbox_to_anchor=(1.05, 0.5), loc='center left')

    # 3) Third subplot: latency plotting
    ax3 = axes[2]
    if not avg_latency_per_second.empty:
        ax3.plot(time_range_latency, avg_latency_per_second[2000], label=f'Flow 1')
        ax3.plot(time_range_latency, avg_latency_per_second[3000], label=f'Flow 2')
        ax3.plot(time_range_latency, avg_latency_per_second[4000], label=f'Flow 3')

        print("avg_latency_per_second: ", avg_latency_per_second)

    ax3.set_xlim(0, 12)
    ax3.set_xlabel('Time [s]', fontsize=font_size)
    ax3.set_ylabel('E2E Latency [s]', fontsize=font_size)
    ax3.set_title("(C) End-to-End Latency", fontsize=font_size)
    ax3.set_ylim(0, 4)
    # log scale for y-axis
    # ax3.set_yscale('log')
    ax3.grid(True)
    ax3.tick_params(axis='both', labelsize=font_size)
    ax3.legend(fontsize=font_size, bbox_to_anchor=(1.05, 0.5), loc='center left')

    # plt.rcParams.update({'xtick.labelsize': font_size, 'ytick.labelsize': font_size})
    plt.subplots_adjust(left=0.1, right=0.75, bottom=0.07, top=0.93)
    plt.savefig("QueueModel.pdf", format='pdf')
    plt.show()

if __name__ == "__main__":
    plot_all_in_one()
