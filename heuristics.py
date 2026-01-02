# heuristics.py
def h_simple(state, problem):
    """Simple Heuristic (Depth-Based)"""
    return problem.n - len(state)

def h_advanced(state, problem):
    """
    Advanced Heuristic: Look-ahead Pruning.
    È ammissibile perché restituisce h_simple, MA restituisce infinito 
    se rileva che una colonna futura non può contenere regine.
    """
    n = problem.n
    current_col = len(state)
    h_base = n - current_col # Questo è h* (il minimo costo reale)

    # Look-ahead: controlliamo le colonne rimaste
    for col in range(current_col, n):
        has_legal_move = False
        for row in range(n):
            if problem.is_safe(state, col, row):
                has_legal_move = True
                break
        
        # Se una colonna futura non ha righe sicure, questo ramo è un vicolo cieco
        if not has_legal_move:
            return float('inf') # Potatura immediata (Pruning)

    return h_base
