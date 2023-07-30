# Importiamo le librerie necessarie
import numpy as np
from scipy.optimize import linprog

# Dati iniziali
# Coefficienti della funzione obiettivo (da massimizzare) - Efficienza dei cristalli di potenza
c = [-200, -300, -150, -400, -100]

# Vincoli - Quantità disponibile di ciascun cristallo di potenza
A = np.array([
    [1, 0, 0, 0, 0],  # Vincolo per il cristallo A
    [0, 1, 0, 0, 0],  # Vincolo per il cristallo B
    [0, 0, 1, 0, 0],  # Vincolo per il cristallo C
    [0, 0, 0, 1, 0],  # Vincolo per il cristallo D
    [0, 0, 0, 0, 1],  # Vincolo per il cristallo E
])

# B = [Q_A, Q_B, Q_C, Q_D, Q_E] - Quantità disponibile di ciascun cristallo
b = [10, 15, 5, 20, 5]

# Limiti per le variabili (quantità di ciascun cristallo da utilizzare)
# Le quantità devono essere maggiori o uguali a 0
x_bounds = (0, None)

# Risoluzione del problema di ottimizzazione utilizzando il simplesso primale
result_primale = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='simplex')

# Estrazione dei risultati dalla soluzione ottenuta
# Combinazione ottimale dei cristalli di potenza
combinazione_cristalli_primale = result_primale.x

# Efficienza massima raggiunta dal "Generator X"
efficienza_massima_primale = -result_primale.fun

# Costo totale di produzione per la combinazione ottimale
costo_totale_primale = np.dot(combinazione_cristalli_primale, np.array(c))

# Stampa dei risultati
print("Risultati ottenuti dalla risoluzione del problema di ottimizzazione:")
print("Combinazione ottimale di cristalli di potenza (Primale):", combinazione_cristalli_primale)
print("Efficienza massima raggiunta (Primale):", efficienza_massima_primale)
print("Costo totale di produzione (Primale):", costo_totale_primale)

