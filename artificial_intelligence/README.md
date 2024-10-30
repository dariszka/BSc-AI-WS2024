# A1 - Uninformed Search Algorithms

### Overview
This assignment focuses on the implementation and analysis of various uninformed search algorithms for problem-solving, applied to a maze-solving task. 

### Key Tasks

- **Breadth-First Search (BFS)**
  - Implemented BFS to explore all possible paths, level by level, ensuring the shortest path is found.

- **Uniform Cost Search (UCS)**
  - Used a priority queue to explore nodes based on path cost, ensuring the least-cost path is found.

- **Depth-First Search (DFS)**
  - Implemented DFS using a stack to explore as deeply as possible before backtracking.
  - Compared DFS with BFS to understand their performance in different maze configurations.

- **Depth-Limited Depth-First Search (DLDFS)**
  - Introduced a depth limit to DFS, preventing it from going beyond a specified depth.
  - Implemented a recursive approach to handle depth limits.

- **Iterative Deepening Depth-First Search (IDS)**
  - Combined the strengths of DFS and BFS by incrementally increasing the depth limit in each iteration.
  - Ensured optimality while avoiding the memory limitations of BFS.

---

# A2 - Heuristic Search Algorithms

### Overview
This assignment involves implementing and analyzing heuristic-based search algorithms to solve a maze navigation problem efficiently. The focus is on using heuristic functions to guide the search, optimizing the pathfinding process with informed techniques.

### Key Tasks

- **Greedy Best-First Search (GBFS)**
  - Implemented GBFS using heuristic values to prioritize nodes expected to be closest to the goal.
  - Analyzed the effectiveness of each heuristic in guiding the search directly toward the goal without guaranteeing the shortest path.

- **A\*-Search (A\*)**
  - Designed A\* to combine path cost with heuristic estimates, ensuring both optimality and efficiency in finding the least-cost path to the goal.
  - Compared cumulative path cost versus action cost in computing the best path, validating that cumulative cost yields the most reliable results for A\*.
  - Implemented `f = g + h` calculations, where `g` is the path cost and `h` is the heuristic estimate, enabling the algorithm to balance exploration and goal proximity.

- **Heuristic Functions**
  - Implemented and tested various heuristic functions tailored to the maze problem:
    - **City Block (Manhattan) Distance** for grid-based distance estimation.
    - **Euclidean Distance** for direct-line distance.
    - **Chebyshev Distance** for cases allowing diagonal movement.

