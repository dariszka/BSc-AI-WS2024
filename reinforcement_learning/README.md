## **Assignment 1 - k-Armed Bandit Problems**

#### Overview
This assignment focuses on implementing and optimizing algorithms to solve **k-Armed Bandit problems**, with an emphasis on performance analysis and efficient exploration strategies.

#### Key Tasks

- **Algorithm Implementation**: Developed and tested strategies like Epsilon-Greedy, Gradient Bandit, Upper Confidence Bound (UCB), Incremental Sample Average Method (ISAM).
- **Exploration Tuning**: Experimented with different exploration techniques, refining the balance between exploring new options and exploiting known rewards.
- **Performance Benchmarking**: Compared the effectiveness of the algorithms through performance metrics, visualizing their outcomes and impact on cumulative rewards.
- **Efficient Computation**: Utilized SciPy and NumPy for efficient operations, ensuring smooth and scalable implementation of the algorithms.

---

## **Assignment 2 - Dynamic Programming**

#### Overview
This assignment focuses on implementing and analyzing dynamic programming algorithms for solving **Markov Decision Processes (MDPs)**, emphasizing policy evaluation, improvement, and iteration techniques.

#### Key Tasks

- **Policy Evaluation and Improvement**: Implemented iterative policy evaluation and policy improvement algorithms to compute and refine policies for MDPs.
- **Value Iteration**: Developed the value iteration algorithm to derive optimal policies and value functions using dynamic programming principles.
- **Action-Value Estimation**: Derived and implemented action-value function update rules for evaluating state-action pairs under different policies.
- **Performance Analysis**: Benchmarked the algorithms and visualized results to understand convergence properties and improvements in policy quality.
- **Efficient Implementation**: Leveraged NumPy for matrix-based operations to ensure computational efficiency and scalability across tasks.

---

## **Assignment 3 - Monte Carlo Methods**

### Overview
This assignment explores Monte Carlo (MC) methods for solving reinforcement learning problems, focusing on key algorithms for policy evaluation and control in model-free environments. These methods are applied to the Blackjack and Fishlake environments to analyze performance and differences from Dynamic Programming (DP) techniques.

### Key Tasks

- **First-Visit Monte Carlo Policy Evaluation:**
  - Implemented to compute the value function for a given policy by averaging returns from the first visit to each state in sampled episodes.
  - Applied to the Blackjack environment to evaluate its performance and convergence properties.

- **Every-Visit Monte Carlo Policy Evaluation:**
  - Developed to update the value function using the average of all returns for each state encountered during an episode.
  - Compared with first-visit MC to understand differences in convergence and variance.

- **Monte Carlo On-Policy Control with ε-Soft Policies:**
  - Implemented to derive near-optimal policies by iteratively improving state-action values using sampled episodes.
  - Used ε-greedy exploration to balance exploration and exploitation while refining the policy for Blackjack and Fishlake environments.

---

## **Assignment 4 - Temporal Difference Learning**

### Overview
This assignment focuses on **Temporal Difference (TD) methods** for policy evaluation and control, highlighting key algorithms such as TD(0), SARSA, Q-Learning, and Expected SARSA. These methods are applied to the **CliffWalking environment** to demonstrate their learning behaviors, convergence properties, and differences in policy outcomes.


### Key Tasks

- **TD(0) Policy Evaluation**:
  - Implemented TD(0) to evaluate a given policy by incrementally updating the value function using bootstrapping.
  - Demonstrated the method's efficiency as a model-free approach without requiring complete episodes.

- **SARSA (On-Policy Control)**:
  - Developed the SARSA algorithm to compute state-action values and derive a near-optimal policy.
  - Illustrated its risk-averse behavior in the CliffWalking environment, where the learned policy avoids the cliff by accounting for the exploratory behavior.

- **Q-Learning (Off-Policy Control)**:
  - Implemented Q-Learning as an off-policy control algorithm that updates \( Q \)-values based on the greedy target policy.
  - Observed its risk-neutral behavior, prioritizing the shortest path to the goal, even at the risk of falling off the cliff.

- **Expected SARSA**:
  - Implemented Expected SARSA, which combines the benefits of SARSA and Q-Learning by using the expected value over actions under an epsilon-greedy policy.
  - Compared on-policy and off-policy variants to analyze their impact on policy learning and convergence.

---
