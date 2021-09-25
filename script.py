import sys
sys.path.extend(['', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/home/rushabh/windows/Users/rusha/Documents/sem7/251/project/gdb-python/gviz/lib/python3.8/site-packages'])

import gdb
import networkx as nx
import matplotlib.pyplot as plt
from utils import StdListToPython

plt.ion()
plt.show()

def bp_handler(event):
    try:
        graph_sym = gdb.lookup_symbol("graph")[0]
        graph_symtab = graph_sym.symtab

        if graph_sym.is_valid() and graph_symtab.is_valid():
            G = nx.Graph()

            num_nodes = int(gdb.parse_and_eval('graph.nodes.size()'))

            print("Graph Size:", num_nodes)
            nodes = []
            for i in range(min(num_nodes, 100)):
                node = gdb.parse_and_eval("graph.nodes[%d]" %i)
                nodes.append(node)

            for node in nodes: G.add_node(int(node['data']))

            for node in nodes:
                children_val = node['children']
                cur_node_label = int(node['data'])
                for child in StdListToPython(children_val).children():
                    child_label = int(child.dereference()['data'])
                    G.add_edge(cur_node_label, child_label) 
            if(len(nodes) > 0):
                plt.gca().clear()
                plt.pause(0.01)
                nx.draw(G, with_labels = True)
                plt.pause(0.01)

    except Exception as e:
        # print(e)
        print("graph object not visible")

def exit_handler(event):
    pass
    # plt.show()

gdb.events.stop.connect(bp_handler)
# gdb.events.exited.conenct(exit_handler)