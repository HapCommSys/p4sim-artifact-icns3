# Tutorial: Generating Paper Figures

This directory contains all Python scripts used to generate the figures in the paper. This tutorial explains what each script does, what data it needs, and how to run it.

---

## Directory Structure

```
plot/
├── Readme.md
├── ipv4_forwarding_v1.py       # Figure 4 — throughput comparison (used in paper)
├── ipv4_forwarding_v2.py       # Figure 4 — alternate style using brokenaxes (deprecated)
├── ipv4_time_usage.py          # Figure 5 — simulation time, uniform x-axis style
├── ipv4_time_usage_v1.py       # Figure 5 — simulation time, broken x-axis style (used in paper)
├── read_and_compute_ratio.py   # Helper — compute path ratios from traffic_data.txt
└── throughput_lb.py            # Figure 7 — load balancing throughput
```

---

## Dependencies

Install required Python packages before running any script:

```bash
pip install numpy matplotlib brokenaxes
```

> `brokenaxes` is only needed for `ipv4_forwarding_v2.py` (deprecated). All other scripts use standard `matplotlib`.

---

## Figure 4 — Network Throughput Comparison

**Script:** `ipv4_forwarding_v1.py`
**Output:** `network_throughput_comparison.pdf`

This figure compares the measured network throughput of three simulators — **Mininet**, **p4sim**, and **ns-3** — across a range of input bandwidths from 1 Mbps to 10,000 Mbps.

The plot uses a **broken x-axis** to show both the low-bandwidth range (1–100 Mbps) and the high-bandwidth range (1,000–10,000 Mbps) in a single figure, with a logarithmic y-axis.

**Data source:** Hard-coded arrays inside the script (no external file needed).

**Run:**

```bash
python3 ipv4_forwarding_v1.py
```

> **Note:** `ipv4_forwarding_v2.py` generates the same figure using the `brokenaxes` library. It is **not used in the paper** and kept only for reference.

---

## Figure 5 — Simulation Execution Time

**Script:** `ipv4_time_usage_v1.py`
**Output:** `network_simulation_time_comparison.pdf`

This figure compares the **wall-clock execution time** of p4sim and ns-3 across the same bandwidth range as Figure 4. It uses a broken x-axis (left: 1–100 Mbps, right: 1,000–10,000 Mbps) and a logarithmic y-axis. Time values are stored in milliseconds and converted to seconds for display.

**Data source:** Hard-coded arrays inside the script (no external file needed).

**Run:**

```bash
python3 ipv4_time_usage_v1.py
```

> **Note:** `ipv4_time_usage.py` is an alternate version that plots the same data with a uniform (non-broken) x-axis. It produces `network_simulation_time.pdf` and can be useful for a simpler view of the same results.

---

## Figure 7 — Load Balancing Throughput

**Script:** `throughput_lb.py`
**Output:** `load_balancing.pdf`

This figure shows how traffic is distributed across two paths (Path A and Path B) under a load balancer. It combines:

- A **line plot** for total input traffic and received traffic
- A **stacked bar chart** for per-path traffic (Path A and Path B)
- A **dashed reference line** at 50% of the input traffic, indicating ideal equal-split load balancing

All traffic values are read from `traffic_data.txt` in Mbps and converted to Gbps for display.

**Data source:** `traffic_data.txt` (must be in the same directory)

Expected format — 5 space-separated columns per row:

```
<time>  <input_Mbps>  <pathA_Mbps>  <pathB_Mbps>  <received_Mbps>
```

**Run:**

```bash
python3 throughput_lb.py
```

---

## Helper — Compute Path Traffic Ratio

**Script:** `read_and_compute_ratio.py`
**Output:** printed to console (no file generated)

This utility script reads `traffic_data.txt` and computes the ratio between Path A traffic (column 3) and Path B traffic (column 4) for each time step. It then prints each ratio and the average across all steps.

Use this to verify that load balancing is distributing traffic evenly before plotting Figure 7.

**Run:**

```bash
python3 read_and_compute_ratio.py
```

---

## Quick Reference

| Script | Figure | Output File | Data Source |
|--------|--------|-------------|-------------|
| `ipv4_forwarding_v1.py` | Figure 4 | `network_throughput_comparison.pdf` | Hard-coded |
| `ipv4_forwarding_v2.py` | Figure 4 (deprecated) | `network_throughput_brokenaxes.pdf` | Hard-coded |
| `ipv4_time_usage_v1.py` | Figure 5 | `network_simulation_time_comparison.pdf` | Hard-coded |
| `ipv4_time_usage.py` | Figure 5 (alt style) | `network_simulation_time.pdf` | Hard-coded |
| `throughput_lb.py` | Figure 7 | `load_balancing.pdf` | `traffic_data.txt` |
| `read_and_compute_ratio.py` | — | Console output | `traffic_data.txt` |
