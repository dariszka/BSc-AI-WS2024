# **Assignment 1 - AVL Tree Implementation**

### Overview
Implemented an **AVL tree**, a self-balancing binary search tree, focusing on maintaining balance during dynamic insertions and deletions.

### Key Tasks
- **Node Management**: Added, removed, and searched nodes while ensuring the AVL tree properties were maintained.
- **Balance Maintenance**:
  - Calculated and updated heights of nodes after modifications.
  - Restructured subtrees dynamically using single and double rotations to restore balance.
- **Auxiliary Functions**: Developed helper methods for parent-child reassignments and tree traversal to facilitate efficient operations.

---

# **Assignment 2 - Chaining Hash Set**

### Overview
Implemented a **chaining hash set**, focusing on efficient key storage and collision handling using linked lists.

### Key Tasks
- **Hash Function**: Calculated hash codes using modulo division to map keys to table indices.
- **Collision Resolution**: Managed linked lists in buckets to handle collisions effectively.
- **Core Operations**: Developed methods for insertion, search, deletion, and clearing the table.
- **Table Representation**: Created a function to display the hash table and its contents in a readable format.

---

# **Assignment 3 - Dijkstra's Algorithm and Shortest Paths**

### Overview
Developed a **graph representation and navigation system** with support for finding the shortest paths and distances between nodes using Dijkstra's algorithm.

### Key Tasks
- **Shortest Path Calculation**: Utilized Dijkstra's algorithm to compute the shortest paths and distances from a given node to all others.
- **Core Methods**:
  - `get_shortest_path`: Retrieves the shortest path between two nodes, including intermediate steps.
  - `get_shortest_distances`: Returns the shortest distance to each node from a given start node.
  - `reachable`: Checks whether a path exists between two nodes.
- **Graph Testing**: Validated graph operations using a predefined map (e.g., campus locations).

---

# **Assignment 4 - Ford-Fulkerson Algorithm for Maximum Flow**

### Overview
Implemented the **Ford-Fulkerson algorithm** to compute the **maximum flow** in a flow network using augmenting paths and a residual graph with support for **dynamic residual graph updates** for augmenting path-based flow calculations.


### Key Tasks
- **Maximum Flow Calculation**:
  - Designed a class-based implementation to perform flow augmentations iteratively.
  - Computed the maximum flow from a source node to a sink node using a BFS-based approach.
  
- **Core Methods**:
  - `ff_step`: Executes a single augmentation step, updating:
    - `latest_augmenting_path`: Tracks the augmenting path found in the current iteration.
    - `current_flow`: Updates cumulative flows in the network, tracking forward and reverse flows.
    - `residual_graph`: Reflects available capacities after each augmentation.
  - `ford_fulkerson`: Iteratively calls `ff_step` until no further augmenting path is found, returning the **maximum flow**.
  - `bfs`: Performs Breadth-First Search to find augmenting paths in the residual graph.
