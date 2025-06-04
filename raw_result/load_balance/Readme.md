# tracing

The result is in `traffic_data.txt`, we tracing the `switch 0 port 0` as the input data, `switch 2 port 0` as the Path A input data,
`switch 3 port 0` as the Path B input data, `switch 1 port 0` as the receiver side data.

The switch number marked may different with the `switchNodes[0]` id in that `switchNodes`.

```c++
    // Add call back for netdevice we want to trace
    Ptr<NetDevice> netDevice0 = switchNodes[0].switchDevices.Get(0); // switch 0 port 0
    Ptr<CustomP2PNetDevice> customNetDevice0 = DynamicCast<CustomP2PNetDevice>(netDevice0);
    if (customNetDevice0)
    {
        NS_LOG_INFO("TraceConnectWithoutContext for switch 0.");
        customNetDevice0->TraceConnectWithoutContext("MacRx", MakeCallback(&RxCallback_switch_0));
    }

    Ptr<NetDevice> netDevice = switchNodes[2].switchDevices.Get(0); // switch 2 port 0
    Ptr<CustomP2PNetDevice> customNetDevice = DynamicCast<CustomP2PNetDevice>(netDevice);
    if (customNetDevice)
    {
        NS_LOG_INFO("TraceConnectWithoutContext for switch 2.");
        customNetDevice->TraceConnectWithoutContext("MacRx", MakeCallback(&RxCallback_switch_2));
    }

    Ptr<NetDevice> netDevice2 = switchNodes[3].switchDevices.Get(0); // switch 3 port 0
    Ptr<CustomP2PNetDevice> customNetDevice2 = DynamicCast<CustomP2PNetDevice>(netDevice2);
    if (customNetDevice2)
    {
        NS_LOG_INFO("TraceConnectWithoutContext for switch 3.");
        customNetDevice2->TraceConnectWithoutContext("MacRx", MakeCallback(&RxCallback_switch_3));
    }

    Ptr<NetDevice> netDevice5 = switchNodes[1].switchDevices.Get(0); // switch 1 port 0
    Ptr<CustomP2PNetDevice> customNetDevice5 = DynamicCast<CustomP2PNetDevice>(netDevice5);
    if (customNetDevice5)
    {
        NS_LOG_INFO("TraceConnectWithoutContext for switch 5.");
        customNetDevice5->TraceConnectWithoutContext("MacTx", MakeCallback(&TxCallback_switch_5));
    }

```