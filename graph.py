import matplotlib.pyplot as plt
import networkx as nx


def visualize_graph(G):
    """Drawing graph"""

    nx.draw_networkx(G)
    plt.show()


def coloring(node, color):
    """Coloring each edge"""

    for neighbor in G.neighbors(node):
       color_of_neighbor = colors_of_nodes.get(neighbor, None)
       if color_of_neighbor == color:
          return False
    return True

def get_color_for_node(node):
    """Adding color to each node"""

    for color in colors:
       if coloring(node, color):
          return color

def main():
    """Printing result and visualizing graph"""
    
    for node in G.nodes():
        colors_of_nodes[node] = get_color_for_node(node)
    print(colors_of_nodes)
    visualize_graph(G)

G = nx.Graph()

colors = ['Red', 'Blue', 'Green', 'Yellow']

G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])
G.add_edges_from([(1, 5), (1, 3), (1, 2), (1, 4), (4, 5), (3, 6), (6, 2), (6, 7), (7, 8)])
colors_of_nodes={}

main()