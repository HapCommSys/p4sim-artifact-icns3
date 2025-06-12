import matplotlib.pyplot as plt
import networkx as nx

# Fat-tree parameters for k=6
k = 6
pods = k
agg_per_pod = k // 2
edge_per_pod = k // 2
core_switches = (k // 2) ** 2
aggr_switches = pods * agg_per_pod
edge_switches = pods * edge_per_pod
hosts_per_edge = k // 2
total_hosts = edge_switches * hosts_per_edge

# ID assignment
core_start = 0
aggr_start = core_switches
edge_start = aggr_start + aggr_switches
host_start = edge_start + edge_switches

# Create the graph
G = nx.Graph()

# Add core switches
for i in range(core_switches):
    G.add_node(f'C{i}', layer='core')

# Add aggregation switches and connect to core
for pod in range(pods):
    for i in range(agg_per_pod):
        aggr_id = aggr_start + pod * agg_per_pod + i
        G.add_node(f'A{aggr_id}', layer='aggregation')
        for j in range(k // 2):
            core_id = j * (k // 2) + i
            G.add_edge(f'A{aggr_id}', f'C{core_id}')

# Add edge switches and connect to aggregation
for pod in range(pods):
    for i in range(edge_per_pod):
        edge_id = edge_start + pod * edge_per_pod + i
        G.add_node(f'E{edge_id}', layer='edge')
        for j in range(agg_per_pod):
            aggr_id = aggr_start + pod * agg_per_pod + j
            G.add_edge(f'E{edge_id}', f'A{aggr_id}')

# Add hosts and connect to edge switches
host_id = host_start
for pod in range(pods):
    for i in range(edge_per_pod):
        edge_id = edge_start + pod * edge_per_pod + i
        for h in range(hosts_per_edge):
            G.add_node(f'H{host_id}', layer='host')
            G.add_edge(f'H{host_id}', f'E{edge_id}')
            host_id += 1
# Create a layered layout manually: top-down from Core to Host
layer_map = {'core': 0, 'aggregation': 1, 'edge': 2, 'host': 3}

# Update node attributes with layer info
for node in G.nodes:
    if node.startswith('C'):
        G.nodes[node]['layer'] = layer_map['core']
    elif node.startswith('A'):
        G.nodes[node]['layer'] = layer_map['aggregation']
    elif node.startswith('E'):
        G.nodes[node]['layer'] = layer_map['edge']
    elif node.startswith('H'):
        G.nodes[node]['layer'] = layer_map['host']

# Determine position layout manually
pos = {}
x_offsets = {'core': 0, 'aggregation': 0, 'edge': 0, 'host': 0}
layer_counts = {'core': 0, 'aggregation': 0, 'edge': 0, 'host': 0}

# Assign x-positions to spread nodes in each layer evenly
spacing = 2
for node in sorted(G.nodes):
    layer = G.nodes[node]['layer']
    x = layer_counts[list(layer_map.keys())[layer]] * spacing
    y = -layer  # top-down layout
    pos[node] = (x, y)
    layer_counts[list(layer_map.keys())[layer]] += 1

# Draw the graph
plt.figure(figsize=(18, 12))
nx.draw(G, pos, with_labels=True, node_size=300, font_size=7, node_color="skyblue", edge_color="gray")
plt.title("Fat-Tree Topology (k=6, Top-Down Layout)")
plt.axis('off')
plt.show()

