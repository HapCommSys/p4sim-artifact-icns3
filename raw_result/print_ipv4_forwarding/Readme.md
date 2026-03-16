# IPv4 Forwarding Throughput Results

Raw throughput measurement results for IPv4 forwarding, comparing Mininet/BMv2 and ns-3 (bridge and P4 switch). These files are the data source for **Figure 4** and **Figure 5** in the paper.

---

## Directory Structure

```bash
print_ipv4_forwarding/
├── Readme.md
├── ipv4_forward_throughput_mininet_bmv2         # Raw iperf UDP output from Mininet + BMv2 (all runs)
├── ipv4_forward_throughput_mininet_bmv2_summary # One throughput value per bandwidth point (Mininet + BMv2)
├── ipv4_forward_throughput_ns3                  # Throughput + simulation time from ns-3 bridge
└── ipv4_forward_throughput_p4sim                # Throughput + simulation time from ns-3 P4sim
```

---

## File Formats

### `ipv4_forward_throughput_mininet_bmv2_summary`

One measured throughput value per line, in `Mbits/sec`, for input rates:
1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000 Mbps.

Note: Mininet/BMv2 is CPU-bound and saturates at ~40 Mbps regardless of the configured rate.

### `ipv4_forward_throughput_ns3` / `ipv4_forward_throughput_p4sim`

These files contain the raw console output from ns-3 runs across all bandwidth points. Each run includes:
- Build log header (waf output — can be ignored)
- Simulation results block with TX/RX throughput and wall-clock time

To extract the numbers for plotting, the Python scripts in `../../plot/` read these files directly (or use hard-coded data derived from them).

---

## How to Regenerate This Data

### p4sim and ns-3 bridge

```bash
# Sweep bandwidth points with P4 switch (model=0) and ns-3 bridge (model=1)
for rate in 1 10 20 30 40 50 100 1000 5000 10000; do
  ./ns3 run "p4-v1model-ipv4-forwarding --model=0 --appDataRate=${rate}Mbps --pktSize=1000" >> raw_result/print_ipv4_forwarding/ipv4_forward_throughput_p4sim
  ./ns3 run "p4-v1model-ipv4-forwarding --model=1 --appDataRate=${rate}Mbps --pktSize=1000" >> raw_result/print_ipv4_forwarding/ipv4_forward_throughput_ns3
done
```

### Mininet + BMv2

Run on a Mininet host using iperf UDP:

```bash
# On Mininet host h1 (sender):
iperf -u -c <h2_ip> -b <rate>M -t 10

# On Mininet host h2 (receiver):
iperf -u -s
```

Collect the reported throughput from the receiver side and append to `ipv4_forward_throughput_mininet_bmv2_summary`.

---

## Generate Paper Figures from This Data

```bash
cd ../../plot
python3 ipv4_forwarding_v1.py    # → network_throughput_comparison.pdf (Figure 4)
python3 ipv4_time_usage_v1.py    # → network_simulation_time_comparison.pdf (Figure 5)
```