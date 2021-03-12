import networkx as nx
import matplotlib.pyplot as plt
import time

start_time = time.time()

g = nx.read_edgelist("files_result/users.csv",
                     delimiter="|",
                     encoding="utf-8",
                     create_using=nx.DiGraph())

print(nx.info(g))
# Type: DiGraph
# Number of nodes: 1214394
# Number of edges: 4819766
# Average in degree:   3.9689
# Average out degree:   3.9689
# ====================
print("="*20)

base_centrality = nx.degree_centrality(g)
sorted_degree_centrality = sorted(base_centrality, key=base_centrality.get, reverse=True)

for c in sorted_degree_centrality[:15]:
    print(f"node: {c}")
    print(f"centrality {base_centrality[c]:.4f}")

# node: youtube
# centrality 0.0241
# node: koffboy
# centrality 0.0177
# node: 5umm
# centrality 0.0146
# node: russiamoscow
# centrality 0.0081
# node: drunktwi
# centrality 0.0074
# node: podslyshano
# centrality 0.0072
# node: wordtri
# centrality 0.0067
# node: samantadarko
# centrality 0.0065
# node: today_okay
# centrality 0.0065
# node: lentaruofficial
# centrality 0.0062
# node: ktvsktvs
# centrality 0.0056
# node: artem_klyushin
# centrality 0.0053
# node: euromaidan
# centrality 0.0052
# node: rianru
# centrality 0.0050
# node: palnom6
# centrality 0.0050
# ====================

print("="*20)

for i in range(3):
    print(f"out: {g.out_degree(sorted_degree_centrality[i])}")
    print(f"in: {g.in_degree(sorted_degree_centrality[i])}")

# out: 0
# in: 29275
# out: 8
# in: 21479
# out: 0
# in: 17735