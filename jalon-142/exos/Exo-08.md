Mes chers étudiants,

Bienvenue à ce jalon de notre exploration. Voici l'exercice 8. La rigueur sera notre guide.

---

# Jalon 142 : Processus de décision de Markov
## Exercice 8/10 : Analyse Mathématique d'un MDP Discret (Difficulté : 8/10)

### Énoncé Rigoureux et Formel
Considérez un Processus de Décision de Markov défini par :
- Un espace d'états fini $\mathcal{S} = \{s_1, s_2, s_3\}$
- Un espace d'actions fini $\mathcal{A} = \{a_1, a_2\}$
- Un facteur d'actualisation $\gamma = 0.8$
- Une matrice de transition $P$ et une fonction de récompense $R$.

Montrez que la distance entre $V_k$ et $V^*$ est bornée par $\frac{\gamma^k}{1-\gamma} \|V_1 - V_0\|_\infty$.

### Correction Détaillée
1. **Majoration par la différence initiale**
   On sait que $\|V_{k+1} - V_k\|_\infty = \|T(V_k) - T(V_{k-1})\|_\infty \le \gamma \|V_k - V_{k-1}\|_\infty$.
   Par récurrence, $\|V_{k+1} - V_k\|_\infty \le \gamma^k \|V_1 - V_0\|_\infty$.
2. **Série Télescopique**
   Pour tout $m > k$, $\|V_m - V_k\|_\infty \le \sum_{j=k}^{m-1} \|V_{j+1} - V_j\|_\infty \le \sum_{j=k}^{m-1} \gamma^j \|V_1 - V_0\|_\infty$.
3. **Passage à la limite**
   En faisant tendre $m$ vers l'infini, on obtient la série géométrique :
   $$ \|V^* - V_k\|_\infty \le \sum_{j=k}^\infty \gamma^j \|V_1 - V_0\|_\infty = \gamma^k \sum_{j=0}^\infty \gamma^j \|V_1 - V_0\|_\infty = \frac{\gamma^k}{1-\gamma} \|V_1 - V_0\|_\infty $$
