Mes chers étudiants,

Bienvenue à ce jalon de notre exploration. Voici l'exercice 9. La rigueur sera notre guide.

---

# Jalon 142 : Processus de décision de Markov
## Exercice 9/10 : Analyse Mathématique d'un MDP Discret (Difficulté : 9/10)

### Énoncé Rigoureux et Formel
Considérez un Processus de Décision de Markov défini par :
- Un espace d'états fini $\mathcal{S} = \{s_1, s_2, s_3\}$
- Un espace d'actions fini $\mathcal{A} = \{a_1, a_2\}$
- Un facteur d'actualisation $\gamma = 0.9$
- Une matrice de transition $P$ et une fonction de récompense $R$.

Considérons un MDP où la récompense $R(s,a)$ est modifiée en $R'(s,a) = R(s,a) + c$ pour une constante $c$. Montrez que la nouvelle fonction de valeur optimale $V'^*$ est liée à $V^*$ par $V'^*(s) = V^*(s) + \frac{c}{1-\gamma}$.

### Correction Détaillée
1. **Opérateur de Bellman Modifié**
   Soit $T'$ le nouvel opérateur de Bellman :
   $$ (T'V)(s) = \max_a (R(s, a) + c + \gamma \sum_{s'} P(s' | s, a) V(s')) $$
2. **Vérification de la Propriété**
   Vérifions que $V(s) = V^*(s) + \frac{c}{1-\gamma}$ est le point fixe de $T'$ :
   $$ (T'V)(s) = \max_a \left( R(s, a) + c + \gamma \sum_{s'} P(s' | s, a) \left(V^*(s') + \frac{c}{1-\gamma}\right) \right) $$
   Puisque $\sum_{s'} P(s' | s, a) = 1$, le terme constant devient $c + \frac{\gamma c}{1-\gamma} = \frac{c(1-\gamma) + \gamma c}{1-\gamma} = \frac{c}{1-\gamma}$.
3. **Conclusion**
   Ainsi, $(T'V)(s) = \max_a (R(s, a) + \gamma \sum_{s'} P(s' | s, a) V^*(s')) + \frac{c}{1-\gamma} = (TV^*)(s) + \frac{c}{1-\gamma} = V^*(s) + \frac{c}{1-\gamma}$.
   Puisque le point fixe est unique, $V'^*(s) = V^*(s) + \frac{c}{1-\gamma}$.
