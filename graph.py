import tkinter as tk
from tkinter import messagebox
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def greedy_coloring(self):
        # Assign colors to vertices
        colors = {}
        for vertex in sorted(self.graph.keys()):
            # Initialize available colors for the vertex
            available_colors = set(range(len(self.graph)))

            # Check colors of adjacent vertices and remove them from available colors
            for neighbor in self.graph[vertex]:
                if neighbor in colors:
                    available_colors.discard(colors[neighbor])

            # Assign the smallest available color to the vertex
            color = min(available_colors)
            colors[vertex] = color

        return colors

    def bfs_traversal(self, start):
        if start not in self.graph:
             messagebox.showerror("node not found","Node not found in the graph. Please check your input.")
        else:
            visited = set()
            traversal_order = []

        queue = [start]
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            traversal_order.append(vertex)

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return traversal_order

    def dfs_traversal(self, start):
        if start not in self.graph:
             messagebox.showerror("node not found","Node not found in the graph. Please check your input.")
            
        else:
            visited = set()
            traversal_order = []

        def dfs_util(vertex):
            traversal_order.append(vertex)
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_util(neighbor)

        dfs_util(start)
        return traversal_order

    def draw_colored_graph(self, colors):
        G = nx.Graph()
        for node in self.graph:
            for neighbor in self.graph[node]:
                G.add_edge(node, neighbor)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color=[colors[node] for node in G.nodes()], cmap=plt.cm.rainbow)
        plt.show()

class GraphColoringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Coloring App")

        self.label = tk.Label(root, text="Enter edges (e.g., '0 1' for an edge between vertices 0 and 1):")
        self.label.pack()

        self.edge_entry = tk.Entry(root)
        self.edge_entry.pack()

        self.add_button = tk.Button(root, text="Add Edge", command=self.add_edge)
        self.add_button.pack()

        self.color_button = tk.Button(root, text="Color Graph", command=self.color_graph)
        self.color_button.pack()

        self.bfs_label = tk.Label(root, text="Enter starting vertex for BFS traversal:")
        self.bfs_label.pack()

        self.bfs_entry = tk.Entry(root)
        self.bfs_entry.pack()

        self.bfs_button = tk.Button(root, text="BFS Traversal", command=self.bfs_traversal)
        self.bfs_button.pack()

        self.dfs_label = tk.Label(root, text="Enter starting vertex for DFS traversal:")
        self.dfs_label.pack()

        self.dfs_entry = tk.Entry(root)
        self.dfs_entry.pack()

        self.dfs_button = tk.Button(root, text="DFS Traversal", command=self.dfs_traversal)
        self.dfs_button.pack()

        self.graph = Graph()

    def add_edge(self):
        try:
            u, v = map(int, self.edge_entry.get().split())
            self.graph.addEdge(u, v)
            messagebox.showinfo("Success", "Edge added successfully!")
            self.edge_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def color_graph(self):
        try:
            colors = self.graph.greedy_coloring()
            self.graph.draw_colored_graph(colors)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def bfs_traversal(self):
        try:
            start = int(self.bfs_entry.get())
            traversal_order = self.graph.bfs_traversal(start)
            messagebox.showinfo("BFS Traversal", "Traversal Order: " + str(traversal_order))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def dfs_traversal(self):
        try:
            start = int(self.dfs_entry.get())
            traversal_order = self.graph.dfs_traversal(start)
            messagebox.showinfo("DFS Traversal", "Traversal Order: " + str(traversal_order))
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphColoringApp(root)
    root.mainloop()
