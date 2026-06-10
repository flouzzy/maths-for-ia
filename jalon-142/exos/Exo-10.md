Mes chers étudiants,

Bienvenue à ce jalon de notre exploration. Voici l'exercice 10. La rigueur sera notre guide.

---

# Jalon 142 : Processus de décision de Markov
## Exercice 10/10 : Analyse Mathématique d'un MDP Discret (Difficulté : 10/10)

### Énoncé Rigoureux et Formel
Considérez un Processus de Décision de Markov défini par :
- Un espace d'états fini $\mathcal{S} = \{s_1, s_2, s_3\}$
- Un espace d'actions fini $\mathcal{A} = \{a_1, a_2\}$
- Un facteur d'actualisation $\gamma = 0.8$
- Une matrice de transition $P$ et une fonction de récompense $R$.

Soit une politique $\pi$. Prouvez que l'opérateur $T^\pi$ défini par $(T^\pi V)(s) = R(s, \pi(s)) + \gamma \sum_{s'} P(s'|s, \pi(s)) V(s')$ est également une contraction.

### Correction Détaillée
1. **Évaluation de l'opérateur**
   Soient $U, V \in \mathcal{B}(\mathcal{S})$. La différence donne :
   $$ (T^\pi U)(s) - (T^\pi V)(s) = \gamma \sum_{s'} P(s'|s, \pi(s)) (U(s') - V(s')) $$
2. **Majoration et Contraction**
   La valeur absolue de cette différence est bornée par la norme infinie :
   $$ |(T^\pi U)(s) - (T^\pi V)(s)| \le \gamma \sum_{s'} P(s'|s, \pi(s)) \|U - V\|_\infty = \gamma \|U - V\|_\infty $$
   Ceci est valable pour tout $s$, donc en passant au supremum :
   $$ \|T^\pi U - T^\pi V\|_\infty \le \gamma \|U - V\|_\infty $$
   $T^\pi$ est bien une contraction de rapport $\gamma$.
