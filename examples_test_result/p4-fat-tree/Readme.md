# fat tree

We run `./ns3 run p4-topo-fattree -- --podnum=6 --pcap=true`. The ns-3 script is in [p4sim/examples/p4-topo-fattree.cc](https://github.com/HapCommSys/p4sim/blob/main/examples/p4-topo-fattree.cc), the P4 scrpit is in [p4sim/examples/p4src/fat-tree/](https://github.com/HapCommSys/p4sim/tree/main/examples/p4src/fat-tree).

```bash
Simulate Running time: 55386ms
Total Running time: 55601ms
Run successfully!
```

![Fattree topo](./Fattree_topo.svg)

1. Generate the network topo based on k (k=6).
2. Create the network based on the topo build in 1.
3. Based on the topo, generate the flow table entries for all the P4 switch.
4. Set the configuration of P4 switch.
5. Set the OnOff application to send the traffic.
6. Start the simulation..

PS: In each run, the topo and flow table may be different.

## network topo

The network topo will be:

| Tier | Quantity | Switch ID Range |
| ----------- | ------ | ------------ |
| Core | 9 | 0 \~ 8 |
| Aggregation | 18 | 9 \~ 26 |
| Edge | 18 | 27 \~ 44 |
| **Total** | **45** | — |


## Detail of the connections


```bash

=========== Switch Port Connection Details ===========
Switch 0 (Node ID: 4) has 6 ports:
  - Port 0 (Device ID: 0) connected to s9_3
  - Port 1 (Device ID: 1) connected to s13_3
  - Port 2 (Device ID: 2) connected to s17_3
  - Port 3 (Device ID: 3) connected to s18_3
  - Port 4 (Device ID: 4) connected to s22_3
  - Port 5 (Device ID: 5) connected to s26_3
Switch 1 (Node ID: 9) has 6 ports:
  - Port 0 (Device ID: 0) connected to s10_3
  - Port 1 (Device ID: 1) connected to s14_3
  - Port 2 (Device ID: 2) connected to s15_3
  - Port 3 (Device ID: 3) connected to s19_3
  - Port 4 (Device ID: 4) connected to s23_3
  - Port 5 (Device ID: 5) connected to s24_3
Switch 2 (Node ID: 14) has 6 ports:
  - Port 0 (Device ID: 0) connected to s11_3
  - Port 1 (Device ID: 1) connected to s12_3
  - Port 2 (Device ID: 2) connected to s16_3
  - Port 3 (Device ID: 3) connected to s20_3
  - Port 4 (Device ID: 4) connected to s21_3
  - Port 5 (Device ID: 5) connected to s25_3
Switch 3 (Node ID: 5) has 6 ports:
  - Port 0 (Device ID: 0) connected to s9_4
  - Port 1 (Device ID: 1) connected to s13_4
  - Port 2 (Device ID: 2) connected to s17_4
  - Port 3 (Device ID: 3) connected to s18_4
  - Port 4 (Device ID: 4) connected to s22_4
  - Port 5 (Device ID: 5) connected to s26_4
Switch 4 (Node ID: 10) has 6 ports:
  - Port 0 (Device ID: 0) connected to s10_4
  - Port 1 (Device ID: 1) connected to s14_4
  - Port 2 (Device ID: 2) connected to s15_4
  - Port 3 (Device ID: 3) connected to s19_4
  - Port 4 (Device ID: 4) connected to s23_4
  - Port 5 (Device ID: 5) connected to s24_4
Switch 5 (Node ID: 6) has 6 ports:
  - Port 0 (Device ID: 0) connected to s9_5
  - Port 1 (Device ID: 1) connected to s13_5
  - Port 2 (Device ID: 2) connected to s17_5
  - Port 3 (Device ID: 3) connected to s18_5
  - Port 4 (Device ID: 4) connected to s22_5
  - Port 5 (Device ID: 5) connected to s26_5
Switch 6 (Node ID: 11) has 6 ports:
  - Port 0 (Device ID: 0) connected to s10_5
  - Port 1 (Device ID: 1) connected to s14_5
  - Port 2 (Device ID: 2) connected to s15_5
  - Port 3 (Device ID: 3) connected to s19_5
  - Port 4 (Device ID: 4) connected to s23_5
  - Port 5 (Device ID: 5) connected to s24_5
Switch 7 (Node ID: 12) has 6 ports:
  - Port 0 (Device ID: 0) connected to s10_6
  - Port 1 (Device ID: 1) connected to s14_6
  - Port 2 (Device ID: 2) connected to s15_6
  - Port 3 (Device ID: 3) connected to s19_6
  - Port 4 (Device ID: 4) connected to s23_6
  - Port 5 (Device ID: 5) connected to s24_6
Switch 8 (Node ID: 7) has 6 ports:
  - Port 0 (Device ID: 0) connected to s9_6
  - Port 1 (Device ID: 1) connected to s13_6
  - Port 2 (Device ID: 2) connected to s17_6
  - Port 3 (Device ID: 3) connected to s18_6
  - Port 4 (Device ID: 4) connected to s22_6
  - Port 5 (Device ID: 5) connected to s26_6
Switch 9 (Node ID: 0) has 7 ports:
  - Port 0 (Device ID: 0) connected to s27_0
  - Port 1 (Device ID: 1) connected to s28_0
  - Port 2 (Device ID: 2) connected to s29_0
  - Port 3 (Device ID: 3) connected to s0_0
  - Port 4 (Device ID: 4) connected to s3_0
  - Port 5 (Device ID: 5) connected to s5_0
  - Port 6 (Device ID: 6) connected to s8_0
Switch 10 (Node ID: 8) has 7 ports:
  - Port 0 (Device ID: 0) connected to s27_1
  - Port 1 (Device ID: 1) connected to s28_1
  - Port 2 (Device ID: 2) connected to s29_1
  - Port 3 (Device ID: 3) connected to s1_0
  - Port 4 (Device ID: 4) connected to s4_0
  - Port 5 (Device ID: 5) connected to s6_0
  - Port 6 (Device ID: 6) connected to s7_0
Switch 11 (Node ID: 13) has 4 ports:
  - Port 0 (Device ID: 0) connected to s27_2
  - Port 1 (Device ID: 1) connected to s28_2
  - Port 2 (Device ID: 2) connected to s29_2
  - Port 3 (Device ID: 3) connected to s2_0
Switch 12 (Node ID: 15) has 4 ports:
  - Port 0 (Device ID: 0) connected to s30_0
  - Port 1 (Device ID: 1) connected to s31_0
  - Port 2 (Device ID: 2) connected to s32_0
  - Port 3 (Device ID: 3) connected to s2_1
Switch 13 (Node ID: 19) has 7 ports:
  - Port 0 (Device ID: 0) connected to s30_1
  - Port 1 (Device ID: 1) connected to s31_1
  - Port 2 (Device ID: 2) connected to s32_1
  - Port 3 (Device ID: 3) connected to s0_1
  - Port 4 (Device ID: 4) connected to s3_1
  - Port 5 (Device ID: 5) connected to s5_1
  - Port 6 (Device ID: 6) connected to s8_1
Switch 14 (Node ID: 20) has 7 ports:
  - Port 0 (Device ID: 0) connected to s30_2
  - Port 1 (Device ID: 1) connected to s31_2
  - Port 2 (Device ID: 2) connected to s32_2
  - Port 3 (Device ID: 3) connected to s1_1
  - Port 4 (Device ID: 4) connected to s4_1
  - Port 5 (Device ID: 5) connected to s6_1
  - Port 6 (Device ID: 6) connected to s7_1
Switch 15 (Node ID: 21) has 7 ports:
  - Port 0 (Device ID: 0) connected to s33_0
  - Port 1 (Device ID: 1) connected to s34_0
  - Port 2 (Device ID: 2) connected to s35_0
  - Port 3 (Device ID: 3) connected to s1_2
  - Port 4 (Device ID: 4) connected to s4_2
  - Port 5 (Device ID: 5) connected to s6_2
  - Port 6 (Device ID: 6) connected to s7_2
Switch 16 (Node ID: 25) has 4 ports:
  - Port 0 (Device ID: 0) connected to s33_1
  - Port 1 (Device ID: 1) connected to s34_1
  - Port 2 (Device ID: 2) connected to s35_1
  - Port 3 (Device ID: 3) connected to s2_2
Switch 17 (Node ID: 26) has 7 ports:
  - Port 0 (Device ID: 0) connected to s33_2
  - Port 1 (Device ID: 1) connected to s34_2
  - Port 2 (Device ID: 2) connected to s35_2
  - Port 3 (Device ID: 3) connected to s0_2
  - Port 4 (Device ID: 4) connected to s3_2
  - Port 5 (Device ID: 5) connected to s5_2
  - Port 6 (Device ID: 6) connected to s8_2
Switch 18 (Node ID: 27) has 7 ports:
  - Port 0 (Device ID: 0) connected to s36_0
  - Port 1 (Device ID: 1) connected to s37_0
  - Port 2 (Device ID: 2) connected to s38_0
  - Port 3 (Device ID: 3) connected to s0_3
  - Port 4 (Device ID: 4) connected to s3_3
  - Port 5 (Device ID: 5) connected to s5_3
  - Port 6 (Device ID: 6) connected to s8_3
Switch 19 (Node ID: 31) has 7 ports:
  - Port 0 (Device ID: 0) connected to s36_1
  - Port 1 (Device ID: 1) connected to s37_1
  - Port 2 (Device ID: 2) connected to s38_1
  - Port 3 (Device ID: 3) connected to s1_3
  - Port 4 (Device ID: 4) connected to s4_3
  - Port 5 (Device ID: 5) connected to s6_3
  - Port 6 (Device ID: 6) connected to s7_3
Switch 20 (Node ID: 32) has 4 ports:
  - Port 0 (Device ID: 0) connected to s36_2
  - Port 1 (Device ID: 1) connected to s37_2
  - Port 2 (Device ID: 2) connected to s38_2
  - Port 3 (Device ID: 3) connected to s2_3
Switch 21 (Node ID: 33) has 4 ports:
  - Port 0 (Device ID: 0) connected to s39_0
  - Port 1 (Device ID: 1) connected to s40_0
  - Port 2 (Device ID: 2) connected to s41_0
  - Port 3 (Device ID: 3) connected to s2_4
Switch 22 (Node ID: 37) has 7 ports:
  - Port 0 (Device ID: 0) connected to s39_1
  - Port 1 (Device ID: 1) connected to s40_1
  - Port 2 (Device ID: 2) connected to s41_1
  - Port 3 (Device ID: 3) connected to s0_4
  - Port 4 (Device ID: 4) connected to s3_4
  - Port 5 (Device ID: 5) connected to s5_4
  - Port 6 (Device ID: 6) connected to s8_4
Switch 23 (Node ID: 38) has 7 ports:
  - Port 0 (Device ID: 0) connected to s39_2
  - Port 1 (Device ID: 1) connected to s40_2
  - Port 2 (Device ID: 2) connected to s41_2
  - Port 3 (Device ID: 3) connected to s1_4
  - Port 4 (Device ID: 4) connected to s4_4
  - Port 5 (Device ID: 5) connected to s6_4
  - Port 6 (Device ID: 6) connected to s7_4
Switch 24 (Node ID: 39) has 7 ports:
  - Port 0 (Device ID: 0) connected to s42_0
  - Port 1 (Device ID: 1) connected to s43_0
  - Port 2 (Device ID: 2) connected to s44_0
  - Port 3 (Device ID: 3) connected to s1_5
  - Port 4 (Device ID: 4) connected to s4_5
  - Port 5 (Device ID: 5) connected to s6_5
  - Port 6 (Device ID: 6) connected to s7_5
Switch 25 (Node ID: 43) has 4 ports:
  - Port 0 (Device ID: 0) connected to s42_1
  - Port 1 (Device ID: 1) connected to s43_1
  - Port 2 (Device ID: 2) connected to s44_1
  - Port 3 (Device ID: 3) connected to s2_5
Switch 26 (Node ID: 44) has 7 ports:
  - Port 0 (Device ID: 0) connected to s42_2
  - Port 1 (Device ID: 1) connected to s43_2
  - Port 2 (Device ID: 2) connected to s44_2
  - Port 3 (Device ID: 3) connected to s0_5
  - Port 4 (Device ID: 4) connected to s3_5
  - Port 5 (Device ID: 5) connected to s5_5
  - Port 6 (Device ID: 6) connected to s8_5
Switch 27 (Node ID: 1) has 6 ports:
  - Port 0 (Device ID: 0) connected to s9_0
  - Port 1 (Device ID: 1) connected to s10_0
  - Port 2 (Device ID: 2) connected to s11_0
  - Port 3 (Device ID: 3) connected to h0
  - Port 4 (Device ID: 4) connected to h1
  - Port 5 (Device ID: 5) connected to h2
Switch 28 (Node ID: 2) has 6 ports:
  - Port 0 (Device ID: 0) connected to s9_1
  - Port 1 (Device ID: 1) connected to s10_1
  - Port 2 (Device ID: 2) connected to s11_1
  - Port 3 (Device ID: 3) connected to h3
  - Port 4 (Device ID: 4) connected to h4
  - Port 5 (Device ID: 5) connected to h5
Switch 29 (Node ID: 3) has 6 ports:
  - Port 0 (Device ID: 0) connected to s9_2
  - Port 1 (Device ID: 1) connected to s10_2
  - Port 2 (Device ID: 2) connected to s11_2
  - Port 3 (Device ID: 3) connected to h6
  - Port 4 (Device ID: 4) connected to h7
  - Port 5 (Device ID: 5) connected to h8
Switch 30 (Node ID: 16) has 6 ports:
  - Port 0 (Device ID: 0) connected to s12_0
  - Port 1 (Device ID: 1) connected to s13_0
  - Port 2 (Device ID: 2) connected to s14_0
  - Port 3 (Device ID: 3) connected to h9
  - Port 4 (Device ID: 4) connected to h10
  - Port 5 (Device ID: 5) connected to h11
Switch 31 (Node ID: 17) has 6 ports:
  - Port 0 (Device ID: 0) connected to s12_1
  - Port 1 (Device ID: 1) connected to s13_1
  - Port 2 (Device ID: 2) connected to s14_1
  - Port 3 (Device ID: 3) connected to h12
  - Port 4 (Device ID: 4) connected to h13
  - Port 5 (Device ID: 5) connected to h14
Switch 32 (Node ID: 18) has 6 ports:
  - Port 0 (Device ID: 0) connected to s12_2
  - Port 1 (Device ID: 1) connected to s13_2
  - Port 2 (Device ID: 2) connected to s14_2
  - Port 3 (Device ID: 3) connected to h15
  - Port 4 (Device ID: 4) connected to h16
  - Port 5 (Device ID: 5) connected to h17
Switch 33 (Node ID: 22) has 6 ports:
  - Port 0 (Device ID: 0) connected to s15_0
  - Port 1 (Device ID: 1) connected to s16_0
  - Port 2 (Device ID: 2) connected to s17_0
  - Port 3 (Device ID: 3) connected to h18
  - Port 4 (Device ID: 4) connected to h19
  - Port 5 (Device ID: 5) connected to h20
Switch 34 (Node ID: 23) has 6 ports:
  - Port 0 (Device ID: 0) connected to s15_1
  - Port 1 (Device ID: 1) connected to s16_1
  - Port 2 (Device ID: 2) connected to s17_1
  - Port 3 (Device ID: 3) connected to h21
  - Port 4 (Device ID: 4) connected to h22
  - Port 5 (Device ID: 5) connected to h23
Switch 35 (Node ID: 24) has 6 ports:
  - Port 0 (Device ID: 0) connected to s15_2
  - Port 1 (Device ID: 1) connected to s16_2
  - Port 2 (Device ID: 2) connected to s17_2
  - Port 3 (Device ID: 3) connected to h24
  - Port 4 (Device ID: 4) connected to h25
  - Port 5 (Device ID: 5) connected to h26
Switch 36 (Node ID: 28) has 6 ports:
  - Port 0 (Device ID: 0) connected to s18_0
  - Port 1 (Device ID: 1) connected to s19_0
  - Port 2 (Device ID: 2) connected to s20_0
  - Port 3 (Device ID: 3) connected to h27
  - Port 4 (Device ID: 4) connected to h28
  - Port 5 (Device ID: 5) connected to h29
Switch 37 (Node ID: 29) has 6 ports:
  - Port 0 (Device ID: 0) connected to s18_1
  - Port 1 (Device ID: 1) connected to s19_1
  - Port 2 (Device ID: 2) connected to s20_1
  - Port 3 (Device ID: 3) connected to h30
  - Port 4 (Device ID: 4) connected to h31
  - Port 5 (Device ID: 5) connected to h32
Switch 38 (Node ID: 30) has 6 ports:
  - Port 0 (Device ID: 0) connected to s18_2
  - Port 1 (Device ID: 1) connected to s19_2
  - Port 2 (Device ID: 2) connected to s20_2
  - Port 3 (Device ID: 3) connected to h33
  - Port 4 (Device ID: 4) connected to h34
  - Port 5 (Device ID: 5) connected to h35
Switch 39 (Node ID: 34) has 6 ports:
  - Port 0 (Device ID: 0) connected to s21_0
  - Port 1 (Device ID: 1) connected to s22_0
  - Port 2 (Device ID: 2) connected to s23_0
  - Port 3 (Device ID: 3) connected to h36
  - Port 4 (Device ID: 4) connected to h37
  - Port 5 (Device ID: 5) connected to h38
Switch 40 (Node ID: 35) has 6 ports:
  - Port 0 (Device ID: 0) connected to s21_1
  - Port 1 (Device ID: 1) connected to s22_1
  - Port 2 (Device ID: 2) connected to s23_1
  - Port 3 (Device ID: 3) connected to h39
  - Port 4 (Device ID: 4) connected to h40
  - Port 5 (Device ID: 5) connected to h41
Switch 41 (Node ID: 36) has 6 ports:
  - Port 0 (Device ID: 0) connected to s21_2
  - Port 1 (Device ID: 1) connected to s22_2
  - Port 2 (Device ID: 2) connected to s23_2
  - Port 3 (Device ID: 3) connected to h42
  - Port 4 (Device ID: 4) connected to h43
  - Port 5 (Device ID: 5) connected to h44
Switch 42 (Node ID: 40) has 6 ports:
  - Port 0 (Device ID: 0) connected to s24_0
  - Port 1 (Device ID: 1) connected to s25_0
  - Port 2 (Device ID: 2) connected to s26_0
  - Port 3 (Device ID: 3) connected to h45
  - Port 4 (Device ID: 4) connected to h46
  - Port 5 (Device ID: 5) connected to h47
Switch 43 (Node ID: 41) has 6 ports:
  - Port 0 (Device ID: 0) connected to s24_1
  - Port 1 (Device ID: 1) connected to s25_1
  - Port 2 (Device ID: 2) connected to s26_1
  - Port 3 (Device ID: 3) connected to h48
  - Port 4 (Device ID: 4) connected to h49
  - Port 5 (Device ID: 5) connected to h50
Switch 44 (Node ID: 42) has 6 ports:
  - Port 0 (Device ID: 0) connected to s24_2
  - Port 1 (Device ID: 1) connected to s25_2
  - Port 2 (Device ID: 2) connected to s26_2
  - Port 3 (Device ID: 3) connected to h51
  - Port 4 (Device ID: 4) connected to h52
  - Port 5 (Device ID: 5) connected to h53

=========== Host Connection Details ===========
Host 45 (Node ID: 45) connected to Switch 27 at Port 3
Host 46 (Node ID: 46) connected to Switch 27 at Port 4
Host 47 (Node ID: 47) connected to Switch 27 at Port 5
Host 48 (Node ID: 48) connected to Switch 28 at Port 3
Host 49 (Node ID: 49) connected to Switch 28 at Port 4
Host 50 (Node ID: 50) connected to Switch 28 at Port 5
Host 51 (Node ID: 51) connected to Switch 29 at Port 3
Host 52 (Node ID: 52) connected to Switch 29 at Port 4
Host 53 (Node ID: 53) connected to Switch 29 at Port 5
Host 54 (Node ID: 54) connected to Switch 30 at Port 3
Host 55 (Node ID: 55) connected to Switch 30 at Port 4
Host 56 (Node ID: 56) connected to Switch 30 at Port 5
Host 57 (Node ID: 57) connected to Switch 31 at Port 3
Host 58 (Node ID: 58) connected to Switch 31 at Port 4
Host 59 (Node ID: 59) connected to Switch 31 at Port 5
Host 60 (Node ID: 60) connected to Switch 32 at Port 3
Host 61 (Node ID: 61) connected to Switch 32 at Port 4
Host 62 (Node ID: 62) connected to Switch 32 at Port 5
Host 63 (Node ID: 63) connected to Switch 33 at Port 3
Host 64 (Node ID: 64) connected to Switch 33 at Port 4
Host 65 (Node ID: 65) connected to Switch 33 at Port 5
Host 66 (Node ID: 66) connected to Switch 34 at Port 3
Host 67 (Node ID: 67) connected to Switch 34 at Port 4
Host 68 (Node ID: 68) connected to Switch 34 at Port 5
Host 69 (Node ID: 69) connected to Switch 35 at Port 3
Host 70 (Node ID: 70) connected to Switch 35 at Port 4
Host 71 (Node ID: 71) connected to Switch 35 at Port 5
Host 72 (Node ID: 72) connected to Switch 36 at Port 3
Host 73 (Node ID: 73) connected to Switch 36 at Port 4
Host 74 (Node ID: 74) connected to Switch 36 at Port 5
Host 75 (Node ID: 75) connected to Switch 37 at Port 3
Host 76 (Node ID: 76) connected to Switch 37 at Port 4
Host 77 (Node ID: 77) connected to Switch 37 at Port 5
Host 78 (Node ID: 78) connected to Switch 38 at Port 3
Host 79 (Node ID: 79) connected to Switch 38 at Port 4
Host 80 (Node ID: 80) connected to Switch 38 at Port 5
Host 81 (Node ID: 81) connected to Switch 39 at Port 3
Host 82 (Node ID: 82) connected to Switch 39 at Port 4
Host 83 (Node ID: 83) connected to Switch 39 at Port 5
Host 84 (Node ID: 84) connected to Switch 40 at Port 3
Host 85 (Node ID: 85) connected to Switch 40 at Port 4
Host 86 (Node ID: 86) connected to Switch 40 at Port 5
Host 87 (Node ID: 87) connected to Switch 41 at Port 3
Host 88 (Node ID: 88) connected to Switch 41 at Port 4
Host 89 (Node ID: 89) connected to Switch 41 at Port 5
Host 90 (Node ID: 90) connected to Switch 42 at Port 3
Host 91 (Node ID: 91) connected to Switch 42 at Port 4
Host 92 (Node ID: 92) connected to Switch 42 at Port 5
Host 93 (Node ID: 93) connected to Switch 43 at Port 3
Host 94 (Node ID: 94) connected to Switch 43 at Port 4
Host 95 (Node ID: 95) connected to Switch 43 at Port 5
Host 96 (Node ID: 96) connected to Switch 44 at Port 3
Host 97 (Node ID: 97) connected to Switch 44 at Port 4
Host 98 (Node ID: 98) connected to Switch 44 at Port 5
```