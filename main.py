# main.py
import matplotlib.pyplot as plt
import numpy as np
import os
from n_queens import NQueensProblem
from astar_solver import astar_search
from heuristics import h_simple, h_advanced
from csp_solver import solve_nqueens_csp

# Creazione cartella di output
OUTPUT_DIR = "Outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_board(state, n, filename="solution_nqueens.png"):
    if state is None:
        return
    
    if isinstance(state, dict):
        state = [state[i] for i in range(n)]

    fig, ax = plt.subplots(figsize=(6, 6))
    board = np.zeros((n, n))
    board[1::2, ::2] = 1
    board[::2, 1::2] = 1
    
    ax.imshow(board, cmap='gray', alpha=0.15)
    
    for col, row in enumerate(state):
        ax.text(col, row, u'♛', fontsize=30, ha='center', va='center', color='darkred')
    
    ax.set_xticks(np.arange(-0.5, n, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, n, 1), minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=1)
    
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_title(f"Visual Solution for N={n} (A*)", fontsize=14, pad=20)
    
    full_path = os.path.join(OUTPUT_DIR, filename)
    plt.tight_layout()
    plt.savefig(full_path)
    plt.close()
    print(f"-> Scacchiera salvata in: '{full_path}'")

def run_suite():
    ns = [4, 6, 8, 10, 12, 13, 14]
    results = {"sim": [], "adv": [], "csp": [], "nodes_sim": [], "nodes_adv": []}

    print(f"{'N':<4} | {'A*(Sim) [s]':<12} | {'A*(Adv) [s]':<12} | {'CSP [s]':<12}")
    print("-" * 50)

    last_solution, last_n = None, 0

    for n in ns:
        prob = NQueensProblem(n)
        
        # A* Simple
        res_sim = astar_search(prob, h_simple)
        results["sim"].append(res_sim['time'])
        results["nodes_sim"].append(res_sim['nodes_expanded'])
        
        # A* Advanced (Pruning)
        res_adv = astar_search(prob, h_advanced)
        results["adv"].append(res_adv['time'])
        results["nodes_adv"].append(res_adv['nodes_expanded'])
        
        # CSP
        res_csp = solve_nqueens_csp(n)
        results["csp"].append(res_csp['time'])

        print(f"{n:<4} | {res_sim['time']:12.5f} | {res_adv['time']:12.5f} | {res_csp['time']:12.5f}")
        
        last_solution, last_n = res_sim['solution'], n

    # Plot Tempi
    plt.figure(figsize=(8, 6))
    plt.plot(ns, results["sim"], 'b-o', label='A* (Simple H)')
    plt.plot(ns, results["adv"], 'g-^', label='A* (Advanced H)')
    plt.plot(ns, results["csp"], 'r-s', label='CSP Solver')
    plt.yscale('log')
    plt.title("Execution Time (Log Scale)")
    plt.xlabel("N")
    plt.ylabel("Seconds")
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.3)
    plt.savefig(os.path.join(OUTPUT_DIR, 'execution_time.png'))

    # Plot Nodi
    plt.figure(figsize=(8, 6))
    plt.plot(ns, results["nodes_sim"], 'b-o', label='Nodes A* (Simple)')
    plt.plot(ns, results["nodes_adv"], 'g-^', label='Nodes A* (Advanced)')
    plt.title("Search Complexity: Nodes Expanded")
    plt.xlabel("N")
    plt.ylabel("Number of Nodes")
    plt.legend()
    plt.grid(True, ls="-", alpha=0.3)
    plt.savefig(os.path.join(OUTPUT_DIR, 'nodes_expanded.png'))

    plot_board(last_solution, last_n, "solution_nqueens.png")
    print(f"\nSuite completata. Controlla la cartella '{OUTPUT_DIR}' per i risultati.")

if __name__ == "__main__":
    run_suite()
