# Tutorial: Spine-Leaf Load Balancing

This example simulates ECMP (Equal-Cost Multi-Path) load balancing across a spine-leaf data center topology. It corresponds to **Section 5.2** of the paper and produces the data for **Figure 7**.

---

## Topology

```
         [Spine 4]         [Spine 5]       ← Two equal-cost spine switches
           /    \           /    \
     [Leaf 2]──────────────[Leaf 3]         ← Aggregation/leaf switches
       / | \                 / | \
   [h0][h1][h2]         [h3][h4][h5]        ← End hosts
```

**6 hosts, 6 P4 switches** (2 leaf + 2 spine + 2 aggregation = 6 total)

**Link capacities:**
- Host ↔ Leaf: 10 Gbps, 1 ms delay
- Leaf ↔ Spine / Spine ↔ Leaf: 40 Gbps, 0.5 ms delay

---

## Scripts

| File | Description |
|------|-------------|
| [`p4-spine-leaf-topo.cc`](https://github.com/HapCommSys/p4sim/blob/main/examples/p4-spine-leaf-topo.cc) | ns-3 simulation script |
| [`load_balance.p4`](https://github.com/HapCommSys/p4sim/tree/main/examples/p4src/load_balance) | P4 load balancing program |
| `flowtable_0.txt` – `flowtable_5.txt` | Per-switch flow table entries |

---

## How to Run

```bash
./ns3 run p4-spine-leaf-topo
```

### Key parameters (edit in the script)

```cpp
double client_stop_time = client_start_time + 10;   // 10-second simulation
std::string appDataRate = "1Mbps";                  // Per-flow rate (100 flows × 1 Mbps = 100 Mbps total)

// Switch processing rate — must be >= total pps required
p4SwitchHelper.SetDeviceAttribute("SwitchRate", UintegerValue(13000));

uint16_t servPortStart = 9900;   // 100 UDP flows on ports 9900–10000
uint16_t servPortEnd   = 10000;
```

> PCAP files are not captured in this test because 100 flows × 10 seconds would produce very large files.

---

## Reading the Output

The simulation prints per-second throughput at four key monitoring points:

```
Time: 5s | Throughput (Mbps) - Switch0(Rx): 56.67, Switch2(Rx): 28.89, Switch3(Rx): 27.76, Switch5(Tx): 56.67
```

| Column | Meaning |
|--------|---------|
| `Switch0(Rx)` | Total traffic entering the destination leaf switch |
| `Switch2(Rx)` | Traffic routed via Spine 4 (Path A) |
| `Switch3(Rx)` | Traffic routed via Spine 5 (Path B) |
| `Switch5(Tx)` | Total traffic leaving the source leaf switch |

**Load balance check:** `Switch2(Rx) ≈ Switch3(Rx) ≈ Switch0(Rx) / 2`

In the captured output above (t=5s): Path A = 28.89 Mbps, Path B = 27.76 Mbps → ratio ≈ 1.04, which is near-perfect 50/50 split.

---

## Analyzing Load Balance Ratio

```bash
cd raw_result/load_balance
python3 ../../plot/read_and_compute_ratio.py
```

This reads `traffic_data.txt` and prints the Path A / Path B ratio for each time step, then the overall average. A ratio close to 1.0 indicates balanced load distribution.

---

## Generating Figure 7

```bash
cd raw_result/load_balance
python3 ../../plot/throughput_lb.py
# Output: load_balancing.pdf
```

The figure shows:
- Total input and received traffic as line plots
- Per-path (Path A and Path B) traffic as a stacked bar chart
- A dashed reference line at 50% of input (ideal equal split)

---

## Full Captured Console Output

<details>
<summary>Click to expand full simulation output</summary>

```bash
(p4dev-python-venv) p4@p4:~/workdir/ns-3-dev-git$ ./ns3 run p4-spine-leaf-topo
*** Reading topology from file: .../load_balance/topo.txt with format: P2PTopo
*** Host number: 6, Switch number: 6

Switch 0 (Node ID: 1) has 5 ports:
  - Port 0 connected to h0
  - Port 1 connected to h1
  - Port 2 connected to h2
  - Port 3 connected to s2_0
  - Port 4 connected to s3_0
Switch 1 (Node ID: 5) has 5 ports:
  - Port 0 connected to h3
  - Port 1 connected to h4
  - Port 2 connected to h5
  - Port 3 connected to s2_3
  - Port 4 connected to s3_3
Switch 2 (Node ID: 8) has 4 ports: [spine switch — connects s0 and s1]
Switch 3 (Node ID: 11) has 4 ports: [spine switch — connects s0 and s1]
Switch 4 (Node ID: 9) has 2 ports: [aggregation]
Switch 5 (Node ID: 10) has 2 ports: [aggregation]

Running simulation...
P4 switch 1 thrift port: 9090
P4 switch 2 thrift port: 9091
...
Time:  5s | Switch0(Rx):  56.67, Switch2(Rx): 28.89, Switch3(Rx): 27.76, Switch5(Tx):  56.67
Time:  6s | Switch0(Rx):  49.18, Switch2(Rx): 24.68, Switch3(Rx): 23.72, Switch5(Tx):  48.35
Time:  7s | Switch0(Rx): 104.20, Switch2(Rx): 53.14, Switch3(Rx): 51.06, Switch5(Tx): 104.20
Time:  8s | Switch0(Rx):  65.02, Switch2(Rx): 33.56, Switch3(Rx): 32.24, Switch5(Tx):  65.85
Time: 10s | Switch0(Rx):  87.53, Switch2(Rx): 44.59, Switch3(Rx): 42.86, Switch5(Tx):  87.39
Time: 11s | Switch0(Rx):  39.18, Switch2(Rx): 19.81, Switch3(Rx): 19.01, Switch5(Tx):  38.82
Time: 12s | Switch0(Rx):  55.02, Switch2(Rx): 28.28, Switch3(Rx): 27.17, Switch5(Tx):  55.51
Time: 13s | Switch0(Rx):  52.52, Switch2(Rx): 26.57, Switch3(Rx): 25.53, Switch5(Tx):  52.04
Simulate Running time: 109972ms
Total Running time: 110030ms
Run successfully!
```

</details>

---

## Connection to Paper

| Paper section | Figure | Description |
|--------------|--------|-------------|
| Section 5.2 — Load Balancing | Figure 7 | Per-path throughput showing ~50/50 ECMP distribution |
