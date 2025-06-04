# P4sim Artifact: Simulating Programmable Switches in ns-3

This repository contains the artifact for the paper:

**"P4sim: Simulating programmable switches in ns-3"**  
Accepted at the *2025 International Conference on ns-3 (ICNS3)*.  

## Overview

This artifact allows users to reproduce the simulation results presented in the paper. It provides:

- Source code of `P4sim` as a module integrated into the ns-3 simulator
- Experiment scripts and configuration files to run simulations
- Raw output data and plotting scripts to reproduce key figures and tables from the paper
- Setup instructions for a virtual machine environment or native Ubuntu deployment

## Repository Structure

We will add all the tests for the `example` in p4sim, check dir `examples_test_result`:


| Example Name     | Description                                      | Architecture     |
|------------------|--------------------------------------------------|------------------|
| basic_tunnel [1] | Tunnel with custom header                        | V1model          |
| firewall [2]     | A basic stateful firewall                        | V1model          |
| ipv4_forward     | Basic forwarding based on `ip_dst`               | V1model          |
| load_balance [3] | Load balancing in spine-leaf network             | V1model          |
| p4_basic [4]     | Basic forwarding based on `ip_dst`               | V1model          |
| qos              | Forwarding with priority                         | V1model          |
| simple_pna       | IPv4 forwarding with PNA architecture            | PNA              |
| simple_psa       | IPv4 forwarding with PSA architecture            | PSA              |
| simple_v1model   | IPv4 forwarding with V1model architecture        | V1model          |


```
.
├── Readme.md
├── figures
│   ├── load_balancing.pdf
│   ├── network_simulation_time.pdf
│   ├── network_simulation_time_comparison.pdf
│   └── network_throughput_comparison.pdf
├── plot
│   ├── Readme.md
│   ├── ipv4_forwarding_v1.py
│   ├── ipv4_forwarding_v2.py
│   ├── ipv4_time_usage.py
│   ├── ipv4_time_usage_v1.py
│   ├── read_and_compute_ratio.py
│   └── throughput_lb.py
├── queuing_test
│   ├── Readme.md
│   ├── ...
│   └── queuemodel.png
└── raw_result
    ├── load_balance
    │   └── traffic_data.txt
    ├── pcap_ipv4_forwarding
    │   ├── *.pcap ...
    └── print_ipv4_forwarding
        ├── Readme.md
        ├── ipv4_forward_throughput_mininet_bmv2
        ├── ipv4_forward_throughput_mininet_bmv2_summary
        ├── ipv4_forward_throughput_ns3
        └── ipv4_forward_throughput_p4sim
```

## Requirements and Simulation Environment

- ⭐ Local Deployment (ns-3.39 tested)
- Virtual Machine as Virtual Env
    - ns-3 Version 3.x – 3.35 (tested)
    - ns-3 Version 3.36 – 3.39 (**tested with this paper**)

See [P4Sim: NS-3-Based P4 Simulation Environment](https://github.com/HapCommSys/p4sim/blob/main/doc/vm-env.md) for full setup steps.

## Test and Evaluation

All the evaluation is included in [p4sim/example](https://github.com/HapCommSys/p4sim/tree/main/examples) dir. And also in [ReamMe_Examples](https://github.com/HapCommSys/p4sim/blob/main/doc/examples.md)

The `Evaluation` section of paper:

- Section 5.1: [Script(ns-3)p4-v1model-ipv4-forwarding.cc](https://github.com/HapCommSys/p4sim/blob/main/examples/p4-v1model-ipv4-forwarding.cc), [Script(p4)simple_v1model.p4](https://github.com/HapCommSys/p4sim/tree/main/examples/p4src/simple_v1model), [table_entry_setting_P4_switch](https://github.com/HapCommSys/p4sim/blob/main/examples/p4src/simple_v1model/flowtable_0.txt)

```c++
    // by change `model` to change the simulation approach.
    cmd.AddValue("runnum", "running number in loops", running_number);
    cmd.AddValue("model", "running simulation with p4switch: 0, with ns-3 bridge: 1", model);
    cmd.AddValue("pktSize", "Packet size in bytes (default 1000)", pktSize);
    cmd.AddValue("appDataRate", "Application data rate in bps (default 1Mbps)", appDataRate);
    cmd.AddValue("pcap", "Trace packet pacp [true] or not[false]", enableTracePcap);
```

- Section 5.2: [Script(ns-3)p4-spine-leaf-topo.cc](https://github.com/HapCommSys/p4sim/blob/main/examples/p4-spine-leaf-topo.cc), [Script(p4)load_balance.p4](https://github.com/HapCommSys/p4sim/tree/main/examples/p4src/load_balance), table_entry_setting_P4_switch have 5 files `flowtable_x.txt` (x=0-4) for different P4 switches.

- Section 5.3: [p4-basic-tunnel.cc](https://github.com/HapCommSys/p4sim/blob/main/examples/p4-basic-tunnel.cc), [Script(p4)basic_tunnel.p4](https://github.com/HapCommSys/p4sim/tree/main/examples/p4src/basic_tunnel), table_entry_setting_P4_switch have 3 files `flowtable_x.txt` (x=0-2) for different P4 switches.



PS: Some of the Documents is helped writed with DeepSeek.

## References

PS: Some of the Documents is helped writed with DeepSeek.

- [1] basic_tunnel in [p4lang/tutorials/baisc_tunnel](https://github.com/p4lang/tutorials/tree/master/exercises/basic_tunnel)
- [2] firewall in [p4lang/tutorials/firewall](https://github.com/p4lang/tutorials/tree/master/exercises/firewall)
- [3] load_balance in [p4lang/tutorials/load_balance](https://github.com/p4lang/tutorials/tree/master/exercises/load_balance)
- [4] p4_basic in [p4lang/tutorials/basic](https://github.com/p4lang/tutorials/tree/master/exercises/basic)