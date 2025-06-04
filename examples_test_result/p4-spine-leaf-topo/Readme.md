# How to test and get the result

## The paper result

Run `./ns3 run p4-spine-leaf-topo` with script [`p4sim/examples/p4-spine-leaf-topo.cc`](https://github.com/HapCommSys/p4sim/blob/main/examples/p4-spine-leaf-topo.cc) will get the result.

## The parameter we use for quick test

```bash
# Here we use 100 UDP flows each 1Mbps as a quick test
# Change that in scripts:

double client_stop_time = client_start_time + 10; // Total 10s
std::string appDataRate = "1Mbps"; // Default application data rate

p4SwitchHelper.SetDeviceAttribute("SwitchRate", UintegerValue(13000)); // Switch processing rate should always >= pps need for simulation

uint16_t servPortStart = 9900; // UDP port 9900 to 10000 total 10 flows
uint16_t servPortEnd = 10000;
```

The results will be like:

```bash
(p4dev-python-venv) p4@p4:~/workdir/ns-3-dev-git$ ./ns3 run p4-spine-leaf-topo 
[  0%] Building CXX object contrib/p4sim/examples/CMakeFiles/p4-spine-leaf-topo.dir/p4-spine-leaf-topo.cc.o
[  0%] Linking CXX executable ns3.39-p4-spine-leaf-topo-debug
*** Reading topology from file: /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/load_balance/topo.txt with format: P2PTopo
*** Host number: 6, Switch number: 6
DataRate: 10Gbps
Delay: 1ms
*** Link from host 6 to  switch0 with data rate 10Gbps and delay 1ms
DataRate: 10Gbps
Delay: 1ms
*** Link from host 7 to  switch0 with data rate 10Gbps and delay 1ms
DataRate: 10Gbps
Delay: 1ms
*** Link from host 8 to  switch0 with data rate 10Gbps and delay 1ms
DataRate: 10Gbps
Delay: 1ms
*** Link from host 9 to  switch1 with data rate 10Gbps and delay 1ms
DataRate: 10Gbps
Delay: 1ms
*** Link from host 10 to  switch1 with data rate 10Gbps and delay 1ms
DataRate: 10Gbps
Delay: 1ms
*** Link from host 11 to  switch1 with data rate 10Gbps and delay 1ms
DataRate: 40Gbps
Delay: 0.5ms
*** Link from  switch 0 to  switch 2 with data rate 40Gbps and delay 0.5ms
DataRate: 40Gbps
Delay: 0.5ms
*** Link from  switch 2 to  switch 4 with data rate 40Gbps and delay 0.5ms
DataRate: 40Gbps
Delay: 0.5ms
*** Link from  switch 2 to  switch 5 with data rate 40Gbps and delay 0.5ms
DataRate: 40Gbps
Delay: 0.5ms
*** Link from  switch 2 to  switch 1 with data rate 40Gbps and delay 0.5ms
DataRate: 40Gbps
Delay: 0.5ms
*** Link from  switch 0 to  switch 3 with data rate 40Gbps and delay 0.5ms
DataRate: 40Gbps
Delay: 0.5ms
*** Link from  switch 4 to  switch 3 with data rate 40Gbps and delay 0.5ms
DataRate: 40Gbps
Delay: 0.5ms
*** Link from  switch 5 to  switch 3 with data rate 40Gbps and delay 0.5ms
DataRate: 40Gbps
Delay: 0.5ms
*** Link from  switch 1 to  switch 3 with data rate 40Gbps and delay 0.5ms

=========== Switch Port Connection Details ===========
Switch 0 (Node ID: 1) has 5 ports:
  - Port 0 (Device ID: 0) connected to h0
  - Port 1 (Device ID: 1) connected to h1
  - Port 2 (Device ID: 2) connected to h2
  - Port 3 (Device ID: 3) connected to s2_0
  - Port 4 (Device ID: 4) connected to s3_0
Switch 1 (Node ID: 5) has 5 ports:
  - Port 0 (Device ID: 0) connected to h3
  - Port 1 (Device ID: 1) connected to h4
  - Port 2 (Device ID: 2) connected to h5
  - Port 3 (Device ID: 3) connected to s2_3
  - Port 4 (Device ID: 4) connected to s3_3
Switch 2 (Node ID: 8) has 4 ports:
  - Port 0 (Device ID: 0) connected to s0_3
  - Port 1 (Device ID: 1) connected to s4_0
  - Port 2 (Device ID: 2) connected to s5_0
  - Port 3 (Device ID: 3) connected to s1_3
Switch 3 (Node ID: 11) has 4 ports:
  - Port 0 (Device ID: 0) connected to s0_4
  - Port 1 (Device ID: 1) connected to s4_1
  - Port 2 (Device ID: 2) connected to s5_1
  - Port 3 (Device ID: 3) connected to s1_4
Switch 4 (Node ID: 9) has 2 ports:
  - Port 0 (Device ID: 0) connected to s2_1
  - Port 1 (Device ID: 1) connected to s3_1
Switch 5 (Node ID: 10) has 2 ports:
  - Port 0 (Device ID: 0) connected to s2_2
  - Port 1 (Device ID: 1) connected to s3_2

=========== Host Connection Details ===========
Host 6 (Node ID: 0) connected to Switch 0 at Port 0
Host 7 (Node ID: 2) connected to Switch 0 at Port 1
Host 8 (Node ID: 3) connected to Switch 0 at Port 2
Host 9 (Node ID: 4) connected to Switch 1 at Port 0
Host 10 (Node ID: 6) connected to Switch 1 at Port 1
Host 11 (Node ID: 7) connected to Switch 1 at Port 2
Node IP and MAC addresses:
Node 0: IP = 10.1.1.1, MAC = 00:00:00:00:00:01
Node 0: IP = 0x0a010101, MAC = 0x000000000001
Node 1: IP = 10.1.1.2, MAC = 00:00:00:00:00:03
Node 1: IP = 0x0a010102, MAC = 0x000000000003
Node 2: IP = 10.1.1.3, MAC = 00:00:00:00:00:05
Node 2: IP = 0x0a010103, MAC = 0x000000000005
Node 3: IP = 10.1.1.4, MAC = 00:00:00:00:00:07
Node 3: IP = 0x0a010104, MAC = 0x000000000007
Node 4: IP = 10.1.1.5, MAC = 00:00:00:00:00:09
Node 4: IP = 0x0a010105, MAC = 0x000000000009
Node 5: IP = 10.1.1.6, MAC = 00:00:00:00:00:0b
Node 5: IP = 0x0a010106, MAC = 0x00000000000b

=========== Switch Port IP and MAC Addresses ===========
Switch 0 Interface Details:
  - Port 0 | MAC: 00:00:00:00:00:02 | IP: 0.0.0.0
  - Port 1 | MAC: 00:00:00:00:00:04 | IP: 0.0.0.0
  - Port 2 | MAC: 00:00:00:00:00:06 | IP: 0.0.0.0
  - Port 3 | MAC: 00:00:00:00:00:0d | IP: 0.0.0.0
  - Port 4 | MAC: 00:00:00:00:00:15 | IP: 0.0.0.0
Switch 1 Interface Details:
  - Port 0 | MAC: 00:00:00:00:00:08 | IP: 0.0.0.0
  - Port 1 | MAC: 00:00:00:00:00:0a | IP: 0.0.0.0
  - Port 2 | MAC: 00:00:00:00:00:0c | IP: 0.0.0.0
  - Port 3 | MAC: 00:00:00:00:00:14 | IP: 0.0.0.0
  - Port 4 | MAC: 00:00:00:00:00:1b | IP: 0.0.0.0
Switch 2 Interface Details:
  - Port 0 | MAC: 00:00:00:00:00:0e | IP: 0.0.0.0
  - Port 1 | MAC: 00:00:00:00:00:0f | IP: 0.0.0.0
  - Port 2 | MAC: 00:00:00:00:00:11 | IP: 0.0.0.0
  - Port 3 | MAC: 00:00:00:00:00:13 | IP: 0.0.0.0
Switch 3 Interface Details:
  - Port 0 | MAC: 00:00:00:00:00:16 | IP: 0.0.0.0
  - Port 1 | MAC: 00:00:00:00:00:18 | IP: 0.0.0.0
  - Port 2 | MAC: 00:00:00:00:00:1a | IP: 0.0.0.0
  - Port 3 | MAC: 00:00:00:00:00:1c | IP: 0.0.0.0
Switch 4 Interface Details:
  - Port 0 | MAC: 00:00:00:00:00:10 | IP: 0.0.0.0
  - Port 1 | MAC: 00:00:00:00:00:17 | IP: 0.0.0.0
Switch 5 Interface Details:
  - Port 0 | MAC: 00:00:00:00:00:12 | IP: 0.0.0.0
  - Port 1 | MAC: 00:00:00:00:00:19 | IP: 0.0.0.0
*** P4 switch configuration: /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/load_balance/load_balance.json, 
 /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/load_balance/flowtable_0.txt for switch 0
*** P4 switch configuration: /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/load_balance/load_balance.json, 
 /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/load_balance/flowtable_1.txt for switch 1
*** P4 switch configuration: /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/load_balance/load_balance.json, 
 /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/load_balance/flowtable_2.txt for switch 2
*** P4 switch configuration: /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/load_balance/load_balance.json, 
 /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/load_balance/flowtable_3.txt for switch 3
*** P4 switch configuration: /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/load_balance/load_balance.json, 
 /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/load_balance/flowtable_4.txt for switch 4
*** P4 switch configuration: /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/load_balance/load_balance.json, 
 /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/load_balance/flowtable_5.txt for switch 5
TraceConnectWithoutContext for switch 0.
TraceConnectWithoutContext for switch 2.
TraceConnectWithoutContext for switch 3.
TraceConnectWithoutContext for switch 5.
Running simulation...
P4 switch 1 thrift port: 9090
P4 switch 2 thrift port: 9091
P4 switch 3 thrift port: 9092
P4 switch 4 thrift port: 9093
P4 switch 5 thrift port: 9094
P4 switch 6 thrift port: 9095
Time: 1s | Throughput (Mbps) - Switch0(Rx): 0, Switch2(Rx): 0, Switch3(Rx): 0, Switch5(Tx): 0
Time: 2s | Throughput (Mbps) - Switch0(Rx): 0, Switch2(Rx): 0, Switch3(Rx): 0, Switch5(Tx): 0
Time: 3s | Throughput (Mbps) - Switch0(Rx): 0, Switch2(Rx): 0, Switch3(Rx): 0, Switch5(Tx): 0
Time: 4s | Throughput (Mbps) - Switch0(Rx): 0, Switch2(Rx): 0, Switch3(Rx): 0, Switch5(Tx): 0
Time: 5s | Throughput (Mbps) - Switch0(Rx): 56.6681, Switch2(Rx): 28.8926, Switch3(Rx): 27.7589, Switch5(Tx): 56.6681
Time: 6s | Throughput (Mbps) - Switch0(Rx): 49.1824, Switch2(Rx): 24.6829, Switch3(Rx): 23.7243, Switch5(Tx): 48.3488
Time: 7s | Throughput (Mbps) - Switch0(Rx): 104.2, Switch2(Rx): 53.142, Switch3(Rx): 51.058, Switch5(Tx): 104.2
Time: 8s | Throughput (Mbps) - Switch0(Rx): 65.0208, Switch2(Rx): 33.5607, Switch3(Rx): 32.2353, Switch5(Tx): 65.8544
Time: 9s | Throughput (Mbps) - Switch0(Rx): 0, Switch2(Rx): 0, Switch3(Rx): 0, Switch5(Tx): 0
Time: 10s | Throughput (Mbps) - Switch0(Rx): 87.528, Switch2(Rx): 44.5893, Switch3(Rx): 42.8637, Switch5(Tx): 87.3946
Time: 11s | Throughput (Mbps) - Switch0(Rx): 39.1792, Switch2(Rx): 19.8063, Switch3(Rx): 19.0144, Switch5(Tx): 38.8208
Time: 12s | Throughput (Mbps) - Switch0(Rx): 55.0176, Switch2(Rx): 28.284, Switch3(Rx): 27.167, Switch5(Tx): 55.5094
Time: 13s | Throughput (Mbps) - Switch0(Rx): 52.5168, Switch2(Rx): 26.5668, Switch3(Rx): 25.5332, Switch5(Tx): 52.0416
Time: 14s | Throughput (Mbps) - Switch0(Rx): 0, Switch2(Rx): 0.216736, Switch3(Rx): 0.200064, Switch5(Tx): 0.475152
Time: 15s | Throughput (Mbps) - Switch0(Rx): 0, Switch2(Rx): 0, Switch3(Rx): 0, Switch5(Tx): 0
Time: 16s | Throughput (Mbps) - Switch0(Rx): 0, Switch2(Rx): 0, Switch3(Rx): 0, Switch5(Tx): 0
Time: 17s | Throughput (Mbps) - Switch0(Rx): 0, Switch2(Rx): 0, Switch3(Rx): 0, Switch5(Tx): 0
Time: 18s | Throughput (Mbps) - Switch0(Rx): 0, Switch2(Rx): 0, Switch3(Rx): 0, Switch5(Tx): 0
Time: 19s | Throughput (Mbps) - Switch0(Rx): 0, Switch2(Rx): 0, Switch3(Rx): 0, Switch5(Tx): 0
Time: 20s | Throughput (Mbps) - Switch0(Rx): 0, Switch2(Rx): 0, Switch3(Rx): 0, Switch5(Tx): 0
Time: 21s | Throughput (Mbps) - Switch0(Rx): 0, Switch2(Rx): 0, Switch3(Rx): 0, Switch5(Tx): 0
Time: 22s | Throughput (Mbps) - Switch0(Rx): 0, Switch2(Rx): 0, Switch3(Rx): 0, Switch5(Tx): 0
Simulate Running time: 109972ms
Total Running time: 110030ms
Run successfully!
(p4dev-python-venv) p4@p4:~/workdir/ns-3-dev-git$
```

Because the large `*.pcap` files, so this test we didn't record the `*.pcap` files.