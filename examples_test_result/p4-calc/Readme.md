# Tutorial: P4 Calculator in ns-3 (p4sim)

This tutorial walks you through a simple P4-based calculator running inside an ns-3 simulation using the p4sim module. The switch performs arithmetic directly in the data plane — no control plane needed.

> This example mirrors the [calc exercise](https://github.com/p4lang/tutorials/tree/master/exercises/calc) from [p4lang/tutorials](https://github.com/p4lang/tutorials), adapted for ns-3 + p4sim.

---

## Topology

The simulation uses a minimal 2-host, 1-switch topology:

```
[ h0 ] <────> [ Switch 0 ] ──── [ h1 ]
```

- **h0** sends a calculator packet to the switch
- **Switch 0** is P4-programmable; it reads the packet, performs the operation, writes the result, and sends the packet back to h0
- **h1** does not receive the packet — the switch reflects it back to the sender

| Node | IP Address | MAC Address       |
|------|------------|-------------------|
| h0   | 10.1.1.1   | 00:00:00:00:00:01 |
| h1   | 10.1.1.2   | 00:00:00:00:00:03 |

Both links are 1000 Mbps with 0.1 ms delay.

---

## Custom Packet Header Format

The calculator uses a custom Ethernet payload identified by **EtherType 0x1234**. The header layout is:

```
 0               1               2               3
 +---------------+---------------+---------------+---------------+
 |      'P'      |      '4'      |    Version    |      Op       |
 +---------------+---------------+---------------+---------------+
 |                          Operand A                            |
 +---------------+---------------+---------------+---------------+
 |                          Operand B                            |
 +---------------+---------------+---------------+---------------+
 |                           Result                              |
 +---------------+---------------+---------------+---------------+
```

| Field     | Size    | Description                              |
|-----------|---------|------------------------------------------|
| `P`       | 8 bits  | ASCII `'P'` (0x50) — magic byte          |
| `4`       | 8 bits  | ASCII `'4'` (0x34) — magic byte          |
| `Version` | 8 bits  | Protocol version, currently `0x01`       |
| `Op`      | 8 bits  | Operation code (see table below)         |
| `Operand A` | 32 bits | First operand                          |
| `Operand B` | 32 bits | Second operand                         |
| `Result`  | 32 bits | Written by the switch, returned to host  |

### Supported Operations

| Op Code | Symbol | Operation                  |
|---------|--------|----------------------------|
| `0x2b`  | `+`    | Result = Operand A + Operand B |
| `0x2d`  | `-`    | Result = Operand A - Operand B |
| `0x26`  | `&`    | Result = Operand A & Operand B |
| `0x7c`  | `\|`   | Result = Operand A \| Operand B |
| `0x5e`  | `^`    | Result = Operand A ^ Operand B |

---

## How the Switch Works (Data Plane Logic)

The P4 program on the switch does the following for every incoming packet:

1. **Parse** — check for EtherType `0x1234` and extract the calculator header
2. **Match** — identify the requested operation from the `Op` field
3. **Execute** — compute the result and write it into the `Result` field
4. **Reflect** — swap source and destination MAC addresses, then send the packet back out the ingress port

There is no control plane or table entries required — everything is handled by the P4 match-action pipeline.

---

## Running the Example

Make sure you are in the ns-3 root directory and your P4 development environment is activated:

```bash
cd ~/ns3.39
source p4dev-python-venv/bin/activate   # activate the virtual environment
```

Run the simulation:

```bash
./ns3 run p4-calc
```

### Expected Output

```
*** Reading topology from file: /home/mm/ns3.39/contrib/p4sim/examples/p4src/calc/topo.txt with format: CsmaTopo
Host 1 Port 0 Link to Switch 0 Port 0 | DataRate: 1000Mbps, Delay: 0.1ms
Host 2 Port 0 Link to Switch 0 Port 1 | DataRate: 1000Mbps, Delay: 0.1ms
*** Host number: 2, Switch number: 1
*** Link from host 1 to  switch0 with data rate 1000Mbps and delay 0.1ms
*** Link from host 2 to  switch0 with data rate 1000Mbps and delay 0.1ms
Node IP and MAC addresses:
Node 0: IP = 10.1.1.1, MAC = 00:00:00:00:00:01
Node 1: IP = 10.1.1.2, MAC = 00:00:00:00:00:03
*** P4 switch configuration: /home/mm/ns3.39/contrib/p4sim/examples/p4src/calc/calc.json,
 /home/mm/ns3.39/contrib/p4sim/examples/p4src/calc/flowtable_0.txt
P4 switch 1 thrift port: 9090
P4Calc RX : op = 0x 2b opA=1 opB=2 result=3
```

### Reading the Result

The last line is the key output:

```
P4Calc RX : op = 0x2b  opA=1  opB=2  result=3
```

| Field    | Value  | Meaning             |
|----------|--------|---------------------|
| `op`     | `0x2b` | Addition (`+`)      |
| `opA`    | `1`    | First operand       |
| `opB`    | `2`    | Second operand      |
| `result` | `3`    | 1 + 2 = 3, correct! |

The switch successfully computed `1 + 2 = 3` in the data plane and returned the result to h0.

---

## Key Files

| File | Description |
|------|-------------|
| `examples/p4src/calc/calc.p4` | P4 program defining the parser, match-action pipeline, and deparser |
| `examples/p4src/calc/calc.json` | Compiled P4 program loaded onto the switch at simulation start |
| `examples/p4src/calc/flowtable_0.txt` | Flow table entries for switch 0 (empty — no entries needed) |
| `examples/p4src/calc/topo.txt` | Topology description file (hosts, switches, links) |

---

## Next Steps

- Modify `calc.p4` to add support for more operations (e.g., multiplication via repeated addition)
- Extend the topology to include multiple switches and observe how packets are routed
- Try the [p4-basic-example](../p4-basic-example/) to see standard IPv4 forwarding in p4sim
