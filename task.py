import sympy
from typing import Dict

# Controlla il file readme.md per i dettagli su ciascun sub-task

def calcola_derivata(espressione: str, variabile: str) -> sympy.Expr:
    """Sub-task 1: Calcolare una Derivata."""
    try:
        # Crea il simbolo
        var = sympy.Symbol(variabile)

        # Converte la stringa in espressione simbolica
        expr = sympy.sympify(espressione)

        # Calcola la derivata
        derivata = sympy.diff(expr, var)

        return derivata

    except Exception as e:
            raise ValueError(f"Errore nel calcolo della derivata: {e}")
    pass

def calcola_integrale_definito(espressione: str, variabile: str, estremo_inf: float, estremo_sup: float) -> sympy.Expr:
    """Sub-task 2: Calcolare un Integrale Definito."""
    try:
        # Variabile simbolica
        var = sympy.Symbol(variabile)

        # Parsing espressione
        expr = sympy.sympify(espressione)

        # Conversione degli estremi in oggetti SymPy
        a = sympy.sympify(estremo_inf)
        b = sympy.sympify(estremo_sup)

        # Calcolo dell'integrale definito
        risultato = sympy.integrate(expr, (var, a, b))

        return risultato

    except Exception as e:
            raise ValueError(f"Errore nel calcolo dell'integrale: {e}")

    pass

def calcola_limite(espressione: str, variabile: str, punto: str) -> sympy.Expr:
    """Sub-task 3: Calcolare un Limite."""
    try:
        # Variabile simbolica
        var = sympy.Symbol(variabile)

        # Parsing espressione e punto
        expr = sympy.sympify(espressione)
        pt = sympy.sympify(punto)

        # Calcolo limite
        risultato = sympy.limit(expr, var, pt)

        return risultato

    except Exception as e:
            raise ValueError(f"Errore nel calcolo del limite: {e}")
    pass

def calcola_polinomio_taylor(espressione: str, variabile: str, punto: float, ordine: int) -> sympy.Expr:
    """Sub-task 4: Calcolare una Serie di Taylor."""
    try:
        # Variabile simbolica
        var = sympy.Symbol(variabile)

        # Parsing espressione e punto
        expr = sympy.sympify(espressione)
        pt = sympy.sympify(punto)

        # Serie di Taylor (include O-grande)
        serie = sympy.series(expr, var, pt, ordine + 1)

        # Rimuove il termine O(...)
        polinomio = serie.removeO()

        return polinomio

    except Exception as e:
            raise ValueError(f"Errore nel calcolo del polinomio di Taylor: {e}")
    pass

def risolvi_sistema_lineare(eq1: str, eq2: str, var1: str, var2: str) -> Dict[sympy.Symbol, sympy.Expr]:
    """Sub-task 5: Risolvere un Sistema Lineare."""
    pass

def main():
    print("Sub-task 1:", calcola_derivata("x**3 + 2*x", "x"))
    print("Sub-task 2:", calcola_integrale_definito("x**2", "x", 0, 3))
    print("Sub-task 3:", calcola_limite("sin(x)/x", "x", "0"))
    print("Sub-task 4:", calcola_polinomio_taylor("exp(x)", "x", 0.0, 4))
    print("Sub-task 5:", risolvi_sistema_lineare("x + y - 3", "x - y - 1", "x", "y"))

if __name__ == "__main__":
    main()
