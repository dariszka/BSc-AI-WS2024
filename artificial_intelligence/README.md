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

---

# A3 - Game-Playing and Reinforcement Learning

### Overview
This assignment focuses on implementing game-playing strategies and reinforcement learning algorithms to optimize decision-making. The key tasks involve creating Minimax and Alpha-Beta pruning agents, as well as a Q-Learning agent, demonstrating core techniques in search optimization and reinforcement learning for intelligent decision-making.

### Key Tasks

- **Minimax Algorithm**
  - Implemented the basic Minimax algorithm for adversarial games to evaluate moves by simulating all possible outcomes.
  - Ensured correct terminal node evaluation and optimal move selection.

- **Alpha-Beta Pruning**
  - Enhanced the Minimax algorithm with Alpha-Beta pruning to improve efficiency by reducing node expansions.
  - Tested the implementation in a simulated game environment, validating optimality.

- **Q-Learning**
  - Developed a Q-Learning agent to learn optimal policies through exploration (epsilon-greedy) and exploitation.
  - Applied the Bellman equation for iterative Q-value updates and visualized the resulting policies and value functions.

---

# A4 - Decision Trees and Reinforcement Learning

### Overview
This assignment focuses on implementing decision trees for classification tasks The key objectives involve building a Decision Tree classifier from scratch using the ID3 algorithm and testing its performance.

### Key Tasks

- **Decision Tree Classifier**
  - Implemented the ID3 algorithm to construct a Decision Tree for binary classification problems.
  - Developed functions to identify optimal splits, and recursively create tree nodes.
  - Debugged and validated the tree-building process through visualizations and textual representations of splits.

- **Prediction Using Decision Trees**
  - Designed a recursive traversal method for predicting labels of unseen samples based on the trained Decision Tree.
  - Ensured accurate handling of leaf nodes and efficient traversal through decision splits.

---

# A5 - Bayesian Networks and Probabilistic Inference

### Overview
This assignment focuses on understanding and implementing Bayesian Networks for probabilistic reasoning. The key objectives involve building a Bayesian Network, performing inference tasks using the Chain Rule, and calculating probabilities of events.

### Key Tasks

- **Defining Bayesian Networks**
  - Constructed a Bayesian Network with random variables, parent-child relationships, and Conditional Probability Tables (CPTs).
  - Encoded dependencies between variables using Directed Acyclic Graphs (DAGs) to represent conditional independence.

- **Recursive Event Probability Calculation**
  - Implemented a recursive function to compute probabilities of events by summing over missing variables.
  - Applied the Chain Rule to calculate the joint probability of atomic events.
  - Designed helper functions for handling partial events and extending assignments to missing variables.
  - Computed joint probabilities of events and normalized results using the inference-by-enumeration approach.
