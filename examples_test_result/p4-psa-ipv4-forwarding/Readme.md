# p4-v1model-ipv4-forwarding

Test with script [p4-psa-ipv4-forwarding.cc](https://github.com/HapCommSys/p4sim/blob/main/examples/p4-psa-ipv4-forwarding.cc) and script [simple_psa](https://github.com/HapCommSys/p4sim/tree/main/examples/p4src/simple_psa)

```bash
(p4dev-python-venv) p4@p4:~/workdir/ns-3-dev-git$ ./ns3 run p4-psa-ipv4-forwarding
*** Reading topology from file: /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/simple_psa/topo.txt with format: CsmaTopo
*** Host number: 2, Switch number: 1
Node IP and MAC addresses:
Node 0: IP = 10.1.1.1, MAC = 00:00:00:00:00:01
Node 0: IP = 0x0a010101, MAC = 0x000000000001
Node 1: IP = 10.1.1.2, MAC = 00:00:00:00:00:03
Node 1: IP = 0x0a010102, MAC = 0x000000000003
Using P4switch model
*** P4 switch configuration: /home/p4/workdir/ns-3-dev-git/contrib/p4sim/examples/p4src/simple_psa/simple_psa.json, 
Running simulation...
P4 switch 1 thrift port: 9090
Simulate Running time: 873ms
Total Running time: 911ms
Run successfully!
client_start_time: 3.02667client_stop_time: 5.99733sink_start_time: 3.03001sink_stop_time: 5.99801
======================================
Final Simulation Results:
Total Transmitted Bytes: 1114000 bytes in time 2.97067
Total Received Bytes: 1113000 bytes in time 2.968
Final Transmitted Throughput: 3 Mbps
Final Received Throughput: 3 Mbps
======================================
(p4dev-python-venv) p4@p4:~/workdir/ns-3-dev-git$ 
```