import networkx as nx
import matplotlib.pyplot as plt
import time

start_time = time.time()

g = nx.read_edgelist("files_result/users.csv",
                     delimiter="|",
                     encoding="utf-8",
                     create_using=nx.DiGraph())

print(nx.info(g))
print("="*20)

base_centrality = nx.degree_centrality(g)
sorted_degree_centrality = sorted(base_centrality, key=base_centrality.get, reverse=True)

for c in sorted_degree_centrality[:15]:
    print(f"node: {c}")
    print(f"centrality {base_centrality[c]:.4f}")

print("="*20)

for i in range(3):
    print(f"out: {g.out_degree(sorted_degree_centrality[i])}")
    print(f"in: {g.in_degree(sorted_degree_centrality[i])}")
