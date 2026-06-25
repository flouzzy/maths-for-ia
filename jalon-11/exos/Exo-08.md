# Exercice 8: Orthogonalité croisée (Difficulté 4/5)
## Énoncé
Soient $F_1, F_2$ deux sous-espaces de $E$. Montrer que $(F_1 + F_2)^\perp = F_1^\perp \cap F_2^\perp$.

## Correction détaillée
1. **Étape 1 :** Soit $\phi \in (F_1 + F_2)^\perp$. Alors pour tout $x \in F_1 + F_2, \phi(x)=0$.
   En particulier, pour tout $x_1 \in F_1$, $\phi(x_1)=0$ (car $F_1 \subset F_1+F_2$), donc $\phi \in F_1^\perp$.
   De même $\phi \in F_2^\perp$. Ainsi $(F_1 + F_2)^\perp \subset F_1^\perp \cap F_2^\perp$.
2. **Étape 2 :** Réciproquement, soit $\phi \in F_1^\perp \cap F_2^\perp$. Pour tout $x \in F_1+F_2$, on peut écrire $x = x_1 + x_2$ avec $x_1 \in F_1, x_2 \in F_2$.
3. **Étape 3 :** On a par linéarité $\phi(x) = \phi(x_1+x_2) = \phi(x_1) + \phi(x_2)$.
4. **Étape 4 :** Puisque $\phi \in F_1^\perp$, $\phi(x_1)=0$. Puisque $\phi \in F_2^\perp$, $\phi(x_2)=0$. Donc $\phi(x) = 0 + 0 = 0$. Ainsi $\phi \in (F_1+F_2)^\perp$. On a l'inclusion réciproque.
5. **Conclusion:** Par double inclusion, l'égalité $(F_1 + F_2)^\perp = F_1^\perp \cap F_2^\perp$ est strictement démontrée.
