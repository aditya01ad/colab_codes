"""
Common utility functions for practice notebooks.
"""
import numpy as np
import matplotlib.pyplot as plt


def print_matrix(M, name="Matrix"):
    """Pretty-print a matrix with its name."""
    print(f"\n{name}:")
    print(np.round(M, 4))


def plot_graph(G, title="Graph"):
    """Draw a networkx graph."""
    import networkx as nx
    plt.figure(figsize=(6, 4))
    nx.draw(G, with_labels=True, node_color='lightblue',
            node_size=500, font_size=12)
    plt.title(title)
    plt.show()


def spectrum(A):
    """Return sorted eigenvalues of a symmetric matrix."""
    return np.sort(np.linalg.eigvalsh(A))
