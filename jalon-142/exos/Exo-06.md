Mes chers étudiants,

Bienvenue à ce jalon de notre exploration. Voici l'exercice 6. La rigueur sera notre guide.

---

# Jalon 142 : Processus de décision de Markov
## Exercice 6/10 : Analyse Mathématique d'un MDP Discret (Difficulté : 6/10)

### Énoncé Rigoureux et Formel
Considérez un Processus de Décision de Markov défini par :
- Un espace d'états fini $\mathcal{S} = \{s_1, s_2, s_3\}$
- Un espace d'actions fini $\mathcal{A} = \{a_1, a_2\}$
- Un facteur d'actualisation $\gamma = 0.8$
- Une matrice de transition $P$ et une fonction de récompense $R$.

Démontrez que l'opérateur de Bellman $T$ est une contraction stricte, et déduisez-en que la suite $V_{k+1} = T(V_k)$ converge.

### Correction Détaillée
1. **Contraction de Bellman**
   La définition de $T$ donne $(TV)(s) = \max_a (R(s, a) + \gamma \sum_{s'} P(s' | s, a) V(s'))$.
   L'application du maximum et de la valeur absolue nous permet de borner :
   $$ \|TU - TV\|_\infty \le \gamma \|U - V\|_\infty $$
2. **Convergence**
   La contraction stricte de rapport $\gamma < 1$ assure l'existence d'un unique point fixe $V^*$ par le Théorème de Banach.
   La suite $V_{k}$ vérifie $\|V_k - V^*\|_\infty \le \gamma^k \|V_0 - V^*\|_\infty$.
   Comme $\lim_{k\to\infty} \gamma^k = 0$, $V_k$ converge vers $V^*$.
