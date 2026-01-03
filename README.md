# n-Queens
AI Homework - 2025-2026

# N-Queens Problem Solver: A* Search vs CSP

This project implements and compares different algorithmic approaches to solve the **N-Queens Puzzle**. It evaluates the performance of **Informed Search (A*)** using different heuristics against a **Constraint Satisfaction Problem (CSP)** model.

## Features
- **A* Search**: Implementation of the A* algorithm with state-space exploration.
- **Heuristics Comparison**: 
  - *Simple*: Basic depth-based estimation.
  - *Advanced*: Includes **Look-ahead Pruning** to detect dead-ends early.
- **CSP Solver**: Uses the `python-constraint` library for a declarative approach.
- **Visualization**: Generates performance graphs and a graphical representation of the chessboard solution.

## Project Structure
- `main.py`: The main script to run benchmarks and generate plots.
- `n_queens.py`: Problem logic (rules, state transitions, safety checks).
- `astar_solver.py`: The A* search algorithm implementation.
- `heuristics.py`: Heuristic functions used by the A* solver.
- `csp_solver.py`: Integration with the CSP library.
- `requirements.txt`: Necessary Python packages.

## Installation & Usage

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

2. **Run the simulation**:
   ```bash
   python main.py

## Results and Outputs
After execution, a folder named `Outputs/` will be created containing the following files:

- **`execution_time.png`**: A graph comparing the execution times (on a log scale) for A* (Simple), A* (Advanced), and the CSP Solver.
- **`nodes_expanded.png`**: A chart showing the search complexity by comparing the number of nodes expanded by the two A* heuristics.
- **`solution_nqueens.png`**: A visual representation of the chessboard showing the solution found for the largest value of $N$ tested.

## Algorithms Overview

### A* Heuristics
A* search performance heavily relies on the quality of the heuristic function ($h$):
*   **Simple Heuristic**: A basic depth-based approach that calculates the number of queens remaining to be placed.
*   **Advanced Heuristic**: Implements **Look-ahead Pruning**. It checks the remaining columns to see if they still contain legal moves. If a future column is found to be completely blocked by existing queens, the heuristic returns `infinity`, allowing the algorithm to prune the entire branch immediately.

### CSP Approach
The **Constraint Satisfaction Problem** solver uses a declarative approach:
*   **Variables**: Each column is a variable.
*   **Domains**: Each variable can take a value from $0$ to $N-1$ (representing the row).
*   **Constraints**: Specific rules are added to ensure that no two queens share the same row or any diagonal (the "AllDifferent" and diagonal absolute difference constraints).
  

