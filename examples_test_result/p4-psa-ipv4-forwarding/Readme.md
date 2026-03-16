# Tutorial: IPv4 Forwarding with PSA Architecture

This example demonstrates IPv4 forwarding through a P4 switch using the **PSA (Portable Switch Architecture)**. The topology and traffic pattern are identical to the V1model forwarding example, making it easy to compare the two P4 architectures side-by-side.

---

## Topology

```
[ Host 0 (10.1.1.1) ] ──── [ P4 Switch (PSA) ] ──── [ Host 1 (10.1.1.2) ]
```

- 2 hosts, 1 P4 switch
- Link type: CSMA
- Traffic: UDP OnOff from Host 0 → Host 1

---

## Scripts

| File | Description |
|------|-------------|
| [`p4-psa-ipv4-forwarding.cc`](https://github.com/HapCommSys/p4sim/blob/main/examples/p4-psa-ipv4-forwarding.cc) | ns-3 simulation script |
| [`simple_psa.p4`](https://github.com/HapCommSys/p4sim/tree/main/examples/p4src/simple_psa) | P4 program (PSA architecture) |

> Note: Unlike the V1model example, the PSA switch loads the flow table entries from within the JSON pipeline configuration rather than a separate `flowtable_X.txt` file.

---

## How to Run

```bash
./ns3 run p4-psa-ipv4-forwarding
```

---

## Captured Output

```bash
(p4dev-python-venv) p4@p4:~/workdir/ns-3-dev-git$ ./ns3 run p4-psa-ipv4-forwarding
*** Reading topology from file: .../simple_psa/topo.txt with format: CsmaTopo
*** Host number: 2, Switch number: 1
Node IP and MAC addresses:
Node 0: IP = 10.1.1.1, MAC = 00:00:00:00:00:01
Node 1: IP = 10.1.1.2, MAC = 00:00:00:00:00:03
Using P4switch model
*** P4 switch configuration: .../simple_psa/simple_psa.json,
Running simulation...
P4 switch 1 thrift port: 9090
Simulate Running time: 873ms
Total Running time: 911ms
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

---

## Comparison: PSA vs V1model

| Metric | V1model | PSA |
|--------|---------|-----|
| Simulate Running time | 1834 ms | 873 ms |
| TX Throughput | 3 Mbps | 3 Mbps |
| RX Throughput | 3 Mbps | 3 Mbps |
| Packet loss | ~1 packet | ~1 packet |

Both architectures achieve the same forwarding correctness. The PSA run is faster in wall-clock time for this small scenario. The difference grows at higher bandwidth — see Figure 5 in the paper.

---

## PCAP Files (in this directory)

| File | Interface | Description |
|------|-----------|-------------|
| `p4-psa-ipv4-forwarding-0-0.pcap` | Host 0 NIC | All packets sent by Host 0 |
| `p4-psa-ipv4-forwarding-1-0.pcap` | Switch port 0 | Packets entering the switch |
| `p4-psa-ipv4-forwarding-1-1.pcap` | Switch port 1 | Packets leaving the switch |
| `p4-psa-ipv4-forwarding-2-0.pcap` | Host 1 NIC | All packets received by Host 1 |
