# basic example

/**
 * This example is same with "basic exerciese" in p4lang/tutorials
 * URL: https://github.com/p4lang/tutorials/tree/master/exercises/basic
 * The P4 program implements basic ipv4 forwarding, also with ARP.
 *
 *          ┌──────────┐              ┌──────────┐
 *          │ Switch 2 \\            /│ Switch 3 │
 *          └─────┬────┘  \        // └──────┬───┘
 *                │         \    /           │
 *                │           /              │
 *          ┌─────┴────┐   /   \      ┌──────┴───┐
 *          │ Switch 0 //         \ \ │ Switch 1 │
 *      ┌───┼          │             \\          ┼────┐
 *      │   └────────┬─┘              └┬─────────┘    │
 *  ┌───┼────┐     ┌─┴──────┐    ┌─────┼──┐     ┌─────┼──┐
 *  │ host 4 │     │ host 5 │    │ host 6 │     │ host 7 │
 *  └────────┘     └────────┘    └────────┘     └────────┘
 */

Script [`p4sim/examples/p4-basic-example.cc`](https://github.com/HapCommSys/p4sim/blob/main/examples/p4-basic-example.cc), P4 Script [basic](https://github.com/HapCommSys/p4sim/tree/main/examples/p4src/p4_basic)

Run with `./ns3 run p4-basic-example`

```bash
(p4dev-python-venv) p4@p4:~/workdir/ns-3-dev-git$ ./ns3 run p4-basic-example
[  0%] Building CXX object contrib/p4sim/examples/CMakeFiles/p4-basic-example.dir/p4-basic-example.cc.o
[  0%] Linking CXX executable ns3.39-p4-basic-example-debug
*** Reading topology from file: /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/p4_basic/topo.txt with format: CsmaTopo
Host 4 Port 0 Link to Switch 0 Port 0 | DataRate: 1000Mbps, Delay: 0.1ms
Host 5 Port 0 Link to Switch 0 Port 1 | DataRate: 1000Mbps, Delay: 0.1ms
Host 6 Port 0 Link to Switch 1 Port 0 | DataRate: 1000Mbps, Delay: 0.1ms
Host 7 Port 0 Link to Switch 1 Port 1 | DataRate: 1000Mbps, Delay: 0.1ms
Switch 0 Port 2 Link to Switch 2 Port 0 | DataRate: 1000Mbps, Delay: 0.1ms
Switch 0 Port 3 Link to Switch 3 Port 0 | DataRate: 1000Mbps, Delay: 0.1ms
Switch 1 Port 2 Link to Switch 2 Port 1 | DataRate: 1000Mbps, Delay: 0.1ms
Switch 1 Port 3 Link to Switch 3 Port 1 | DataRate: 1000Mbps, Delay: 0.1ms
*** Host number: 4, Switch number: 4
*** Link from host 4 to  switch0 with data rate 1000Mbps and delay 0.1ms
*** Link from host 5 to  switch0 with data rate 1000Mbps and delay 0.1ms
*** Link from host 6 to  switch1 with data rate 1000Mbps and delay 0.1ms
*** Link from host 7 to  switch1 with data rate 1000Mbps and delay 0.1ms
*** Link from  switch 0 to  switch 2 with data rate 1000Mbps and delay 0.1ms
*** Link from  switch 0 to  switch 3 with data rate 1000Mbps and delay 0.1ms
*** Link from  switch 1 to  switch 2 with data rate 1000Mbps and delay 0.1ms
*** Link from  switch 1 to  switch 3 with data rate 1000Mbps and delay 0.1ms
Node IP and MAC addresses:
Node 0: IP = 10.1.1.1, MAC = 00:00:00:00:00:01
Node 0: IP = 0x0a010101, MAC = 0x000000000001
Node 1: IP = 10.1.1.2, MAC = 00:00:00:00:00:03
Node 1: IP = 0x0a010102, MAC = 0x000000000003
Node 2: IP = 10.1.1.3, MAC = 00:00:00:00:00:05
Node 2: IP = 0x0a010103, MAC = 0x000000000005
Node 3: IP = 10.1.1.4, MAC = 00:00:00:00:00:07
Node 3: IP = 0x0a010104, MAC = 0x000000000007
*** P4 switch configuration: /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/p4_basic/p4_basic.json, 
 /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/p4_basic/flowtable_0.txt
*** P4 switch configuration: /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/p4_basic/p4_basic.json, 
 /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/p4_basic/flowtable_1.txt
*** P4 switch configuration: /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/p4_basic/p4_basic.json, 
 /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/p4_basic/flowtable_2.txt
*** P4 switch configuration: /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/p4_basic/p4_basic.json, 
 /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/p4_basic/flowtable_3.txt
Running simulation...
P4 switch 1 thrift port: 9090
P4 switch 2 thrift port: 9091
P4 switch 3 thrift port: 9092
P4 switch 4 thrift port: 9093
Simulate Running time: 6142ms
Total Running time: 6188ms
Run successfully!
client_start_time: 3.02667client_stop_time: 5.99733sink_start_time: 3.04311sink_stop_time: 6.00011
======================================
Final Simulation Results:
Total Transmitted Bytes: 1114000 bytes in time 2.97067
Total Received Bytes: 1109000 bytes in time 2.957
Final Transmitted Throughput: 3 Mbps
Final Received Throughput: 3.00034 Mbps
======================================
```