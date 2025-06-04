# Implementing A Basic Stateful Firewall

**PS**: This example is taken from [`tutorials/exercises/firewall/`](https://github.com/p4lang/tutorials/tree/master/exercises/firewall) and simulated in ns-3 p4sim.

# Introduction

The objective of this exercise is to write a P4 program that implements a simple stateful firewall. To do this, we will use a bloom filter. This exercise builds upon the basic exercise so be sure to complete that one before trying this one.

We will use the pod-topology for this exercise, which consists of four hosts connected to four switches, which are wired up as they would be in a single pod of a fat tree topology.

![topology](./firewall-topo.png)

Switch s1 will be configured with a P4 program that implements a simple stateful firewall (firewall.p4), the rest of the switches will run the basic IPv4 router program (basic.p4) from the previous exercise.

The firewall on s1 should have the following functionality:

Hosts h1 and h2 are on the internal network and can always connect to one another.
Hosts h1 and h2 can freely connect to h3 and h4 on the external network.
Hosts h3 and h4 can only reply to connections once they have been established from either h1 or h2, but cannot initiate new connections to hosts on the internal network.
Note: This stateful firewall is implemented 100% in the dataplane using a simple bloom filter. Thus there is some probability of hash collisions that would let unwanted flows to pass through.

Our P4 program will be written for the V1Model architecture implemented on P4.org's bmv2 software switch. The architecture file for the V1Model can be found at: /usr/local/share/p4c/p4include/v1model.p4. This file desribes the interfaces of the P4 programmable elements in the architecture, the supported externs, as well as the architecture's standard metadata fields. We encourage you to take a look at it.


# Run

`./ns3 run p4-firewall` the scripts is in [p4sim/examples/p4-firewall.cc](https://github.com/HapCommSys/p4sim/blob/main/examples/p4-firewall.cc), and the P4 scripts is in [p4sim/examples/p4src/firewall](https://github.com/HapCommSys/p4sim/tree/main/examples/p4src/firewall). 

We using three flows for testing the connection. 
In this simulation setup, we designed a testbed to evaluate the behavior of a stateful firewall under multiple concurrent flows using ns-3.
Three application flows are configured:

- A TCP stream from host h0 to host h3 on port 9093, simulating a typical client-server connection.
- A UDP stream from h3 to h0 on port 9200, representing a bidirectional communication pattern.
- Another UDP stream from h1 to h0 on port 9003, simulating a second client communicating with the server.

Both TCP and UDP traffic are included to test how the firewall handles different transport protocols.
The firewall is expected to maintain state for TCP connections and track UDP flows based on 5-tuples (source/destination IP and port, protocol).
The `OnOffHelper` is used to generate constant bitrate traffic, while `PacketSinkHelper` is used to collect received packets.
`PCAP tracing` is enabled to capture and analyze packet-level activity.
This setup allows us to evaluate how effectively the stateful firewall identifies and permits or blocks traffic based on established connection states and flow consistency.

# Result

```bash
(p4dev-python-venv) p4@p4:~/workdir/ns-3-dev-git$ ./ns3 run p4-firewall
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
Simulate Running time: 7466ms
Total Running time: 7510ms
Run successfully!
```