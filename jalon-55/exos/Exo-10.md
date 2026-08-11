---
uuid: "exo-55-10"
title: "La courbe sinus du topologue (Preuve complète)"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 10 : La courbe sinus du topologue (Preuve complète)

**Énoncé :**
Montrer formellement que l'ensemble $S = A \cup B$ avec $A = \{ (x, \sin(\frac{1}{x})) \mid x \in ]0, 1] \}$ et $B = \{ (0, y) \mid y \in [-1, 1] \}$ est connexe mais n'est pas connexe par arcs.

**Solution :**
1. **Connexité :** L'ensemble $A$ est l'image de l'intervalle $]0, 1]$ par l'application continue $x \mapsto (x, \sin(1/x))$. Comme $]0, 1]$ est connexe, $A$ est connexe.
2. Remarquons que $B$ est exactement l'ensemble des points d'accumulation de $A$ lorsque $x \to 0$. Autrement dit, l'adhérence de $A$ est $\overline{A} = A \cup B = S$.
3. Un résultat du cours affirme que l'adhérence d'un espace connexe est connexe (vu Exercice 2). Donc $S$ est connexe.
4. **Non connexité par arcs :** Raisonnons par l'absurde. Supposons qu'il existe un chemin continu $\gamma : [0, 1] \to S$ tel que $\gamma(0) = (0, 0) \in B$ et $\gamma(1) = (1, \sin(1)) \in A$.
5. Soit $\gamma(t) = (\gamma_1(t), \gamma_2(t))$. Puisque $\gamma(1) \in A$, il existe des points de l'intervalle envoyés dans $A$.
6. L'ensemble $\gamma^{-1}(B)$ est un fermé de $[0, 1]$ car c'est l'image réciproque du fermé $B$. Il contient 0 et est borné. Soit $t_0 = \sup \gamma^{-1}(B)$. On a $\gamma(t_0) \in B$. L'intervalle $]t_0, 1]$ est mappé entièrement dans $A$.
7. Pour $t \in ]t_0, 1]$, $\gamma_1(t) > 0$. De plus, $\gamma_2(t) = \sin(1/\gamma_1(t))$.
8. Comme $\gamma$ est continue, $\lim_{t \to t_0^+} \gamma_1(t) = 0$. Mais lorsque $\gamma_1 \to 0$, la valeur $\sin(1/\gamma_1)$ oscille infiniment entre -1 et 1, donc la limite $\lim_{t \to t_0^+} \gamma_2(t)$ ne peut pas exister, ce qui contredit la continuité de la composante $\gamma_2$ en $t_0$.
9. En conclusion, il n'existe pas de chemin continu reliant $B$ à $A$, $S$ n'est pas connexe par arcs.
