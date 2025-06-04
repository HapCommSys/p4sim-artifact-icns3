# Raw data

We use `*.pcap`, `logging` and `basic print` for tracing the result.

```bash
.
├── Readme.md
├── load_balance
│   └── traffic_data.txt # logging the throughput of targeted P4 switch with ns-3 script
├── pcap_ipv4_forwarding
│   ├── p4-ipv4-forwarding-test-0-0.pcap # I just find that also in my PC, upload that.
│   ├── p4-ipv4-forwarding-test-1-0.pcap
│   ├── p4-ipv4-forwarding-test-1-1.pcap
│   └── p4-ipv4-forwarding-test-2-0.pcap
└── print_ipv4_forwarding
    ├── Readme.md # please check this Readme.md
    ├── ipv4_forward_throughput_mininet_bmv2
    ├── ipv4_forward_throughput_mininet_bmv2_summary
    ├── ipv4_forward_throughput_ns3
    └── ipv4_forward_throughput_p4sim
```