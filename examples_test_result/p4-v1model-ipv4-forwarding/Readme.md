# Tutorial: IPv4 Forwarding with V1model Architecture

This example runs a host-to-host UDP forwarding simulation through a single P4 switch using the **V1model** architecture. It is the baseline benchmark used in **Section 5.1** of the paper to compare throughput and simulation time across p4sim, ns-3 bridge, and Mininet/BMv2.

---

## Topology

```
[ Host 0 (10.1.1.1) ] ──── [ P4 Switch (V1model) ] ──── [ Host 1 (10.1.1.2) ]
```

- 2 hosts, 1 P4 switch
- Link type: CSMA
- Traffic: UDP OnOff from Host 0 → Host 1

---

## Scripts

| File | Description |
|------|-------------|
| [`p4-v1model-ipv4-forwarding.cc`](https://github.com/HapCommSys/p4sim/blob/main/examples/p4-v1model-ipv4-forwarding.cc) | ns-3 simulation script |
| [`simple_v1model.p4`](https://github.com/HapCommSys/p4sim/tree/main/examples/p4src/simple_v1model) | P4 program (V1model architecture) |
| [`flowtable_0.txt`](https://github.com/HapCommSys/p4sim/blob/main/examples/p4src/simple_v1model/flowtable_0.txt) | Static flow table entries for the switch |

---

## How to Run

```bash
# Basic run (default: 1 Mbps, P4 switch)
./ns3 run p4-v1model-ipv4-forwarding

# With explicit options
./ns3 run "p4-v1model-ipv4-forwarding --model=0 --pktSize=1000 --appDataRate=10Mbps --pcap=true"
```

### Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `model` | `0` | `0` = P4 switch, `1` = ns-3 bridge device |
| `pktSize` | `1000` | Packet size in bytes |
| `appDataRate` | `1Mbps` | Application sending rate (e.g., `100Mbps`, `1Gbps`) |
| `pcap` | `false` | Enable PCAP trace files |
| `runnum` | `1` | Run index for scripted parameter sweeps |

To reproduce the paper benchmark (Section 5.1), sweep `appDataRate` from 1 Mbps to 10,000 Mbps with both `--model=0` (p4sim) and `--model=1` (ns-3 bridge) and record the reported throughput and wall-clock time.

---

## Captured Output

```bash
(p4dev-python-venv) p4@p4:~/workdir/ns-3-dev-git$ ./ns3 run p4-v1model-ipv4-forwarding
[  0%] Building CXX object contrib/p4sim/CMakeFiles/libp4sim-obj.dir/model/p4-core-v1model.cc.o
[  0%] Linking CXX shared library ../../lib/libns3.39-p4sim-debug.so
[  0%] Building CXX object contrib/p4sim/examples/CMakeFiles/p4-v1model-ipv4-forwarding.dir/p4-v1model-ipv4-forwarding.cc.o
[  0%] Linking CXX executable ns3.39-p4-v1model-ipv4-forwarding-debug
*** Reading topology from file: .../simple_v1model/topo.txt with format: CsmaTopo
*** Host number: 2, Switch number: 1
Node IP and MAC addresses:
Node 0: IP = 10.1.1.1, MAC = 00:00:00:00:00:01
Node 1: IP = 10.1.1.2, MAC = 00:00:00:00:00:03
*** P4 switch configuration: .../simple_v1model/simple_v1model.json, .../flowtable_0.txt
Running simulation...
P4 switch 1 thrift port: 9090
Simulate Running time: 1834ms
Total Running time: 1872ms
Run successfully!
client_start_time: 3.02667  client_stop_time: 5.99733
sink_start_time:   3.03001  sink_stop_time:   5.99801
======================================
Final Simulation Results:
Total Transmitted Bytes: 1114000 bytes in time 2.97067
Total Received Bytes:    1113000 bytes in time 2.968
Final Transmitted Throughput: 3 Mbps
Final Received Throughput:    3 Mbps
======================================
```

### Reading the output

| Field | Meaning |
|-------|---------|
| `Simulate Running time` | Wall-clock time for the ns-3 event loop — used in **Figure 5** |
| `Total Running time` | Includes setup and teardown overhead |
| `Final Received Throughput` | Application-layer throughput — used in **Figure 4** |

Near-zero packet loss (1 packet in this run = 0.09%) is expected and acceptable.

---

## PCAP Files (in this directory)

| File | Interface | Description |
|------|-----------|-------------|
| `p4-v1model-ipv4-forwarding-0-0.pcap` | Host 0 NIC | All packets sent by Host 0 |
| `p4-v1model-ipv4-forwarding-1-0.pcap` | Switch port 0 | Packets entering the switch from Host 0 |
| `p4-v1model-ipv4-forwarding-1-1.pcap` | Switch port 1 | Packets leaving the switch toward Host 1 |
| `p4-v1model-ipv4-forwarding-2-0.pcap` | Host 1 NIC | All packets received by Host 1 |

Open any PCAP in Wireshark to inspect the IPv4/UDP headers and verify forwarding correctness.

---

## Connection to Paper

| Paper section | Figure | How to reproduce |
|--------------|--------|-----------------|
| Section 5.1 — IPv4 Forwarding | Figure 4 (throughput) | `python3 plot/ipv4_forwarding_v1.py` |
| Section 5.1 — IPv4 Forwarding | Figure 5 (simulation time) | `python3 plot/ipv4_time_usage_v1.py` |
