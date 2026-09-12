# Exercice 4 : Additivité dénombrable sur les mesurables

**Difficulté :** $\bigstar\bigstar\star\star\star$

Soit $(E_n)_{n \in \mathbb{N}}$ une suite d'ensembles Lebesgue-mesurables disjoints. Démontrer par récurrence que pour tout $N$, $\lambda\left(\bigcup_{n=1}^N E_n\right) = \sum_{n=1}^N \lambda(E_n)$.

**Correction Détaillée :**
Pour $N=1$, c'est trivial.
Supposons la propriété vraie au rang $N-1$.
Posons $S_{N-1} = \bigcup_{n=1}^{N-1} E_n$. Soit $A$ un ensemble test. Puisque $E_N$ est mesurable, on utilise le critère de Carathéodory avec l'ensemble test $S_{N-1} \cup E_N$ :
$$\lambda(S_{N-1} \cup E_N) = \lambda((S_{N-1} \cup E_N) \cap E_N) + \lambda((S_{N-1} \cup E_N) \setminus E_N)$$
Comme les ensembles sont disjoints, $(S_{N-1} \cup E_N) \cap E_N = E_N$ et $(S_{N-1} \cup E_N) \setminus E_N = S_{N-1}$.
Ainsi, $\lambda(S_{N-1} \cup E_N) = \lambda(E_N) + \lambda(S_{N-1})$.
Par hypothèse de récurrence, $\lambda(S_{N-1}) = \sum_{n=1}^{N-1} \lambda(E_n)$, d'où le résultat au rang $N$.
