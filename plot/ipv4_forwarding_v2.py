from brokenaxes import brokenaxes
import matplotlib.pyplot as plt
import numpy as np

# Data preparation
bandwidths = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000, 10000]
measured_throughput_mininet = [0.97407, 9.09, 16.78, 27.50, 37.03, 41.57, 40.50, 
                                40.87, 42.95, 42.23, 42.71, 39.52, np.nan]
measured_throughput_p4sim = [1.02762, 10.0268, 20.0268, 30.0268, 40.0267, 50.0267, 
                             60.0269, 70.0272, 80.0267, 90.0276, 100.027, 945.205, 9557.97]
measured_throughput_ns3 = [0.971146, 9.47754, 18.9293, 28.3811, 37.8328, 47.2845, 
                           56.7365, 66.1887, 75.6398, 85.0929, 94.5434, 945.206, 9467.48]

mininet = [max(x, 0.01) for x in measured_throughput_mininet]
p4sim = [max(x, 0.01) for x in measured_throughput_p4sim]
ns3 = [max(x, 0.01) for x in measured_throughput_ns3]

# Broken axis settings
fig = plt.figure(figsize=(9, 5))
bax = brokenaxes(xlims=((0, 110), (900, 11000)), hspace=.05, yscale='log')

bax.scatter(bandwidths, mininet, label="Mininet", marker='d', color='#dba614')
bax.scatter(bandwidths, p4sim, label="p4sim", marker='x', color='#B85450', s=100)
bax.scatter(bandwidths, ns3, label="ns-3", marker='o', color='#527cb4')
bax.set_ylabel("Output Throughput (Mbps)", fontsize=15)
bax.set_xlabel("Input Throughput (Mbps)", fontsize=15)
bax.legend(loc='upper left', fontsize=13)

plt.tight_layout()
plt.savefig("network_throughput_brokenaxes.pdf")
plt.show()
