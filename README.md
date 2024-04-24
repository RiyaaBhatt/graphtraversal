**Graph Coloring and Traversal Application**

This application is designed to provide a visual representation of graph coloring and traversal algorithms using Python's tkinter for the GUI, networkx for graph manipulation, and matplotlib for graph visualization.

### Features:

1. **Graph Creation:**
   - Add edges to create an undirected graph.
   - Edges are inputted as pairs of vertices (e.g., '0 1' for an edge between vertices 0 and 1).

2. **Graph Coloring:**
   - Apply a greedy coloring algorithm to color the graph.
   - Each vertex is assigned a color such that no two adjacent vertices have the same color.

3. **Graph Traversal:**
   - Perform Breadth-First Search (BFS) traversal starting from a specified vertex.
   - Perform Depth-First Search (DFS) traversal starting from a specified vertex.

### How to Use:

1. **Adding Edges:**
   - Enter the desired edges in the format 'u v' and click "Add Edge" to create the graph.

2. **Coloring Graph:**
   - After adding edges, click "Color Graph" to apply the greedy coloring algorithm and visualize the colored graph.

3. **BFS Traversal:**
   - Enter the starting vertex for BFS traversal and click "BFS Traversal" to see the traversal order.

4. **DFS Traversal:**
   - Enter the starting vertex for DFS traversal and click "DFS Traversal" to see the traversal order.

### How to Run:

1. Clone the repository to your local machine.
2. Make sure you have Python installed (version 3.6 or higher).
3. Install the required libraries
4. Run the application using `python graph.py`.

### Additional Notes:

- The graph is displayed using matplotlib's pyplot, and the traversal order is shown in message boxes.
- Error messages are displayed if invalid input or operations occur.

Enjoy exploring graph coloring and traversal with this interactive application!
