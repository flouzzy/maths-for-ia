# Fausse intégrale impropre (Prolongement par continuité)

**Difficulté :** $\star\star\star$

**Énoncé :**
Étudier la nature de l'intégrale :
$$ M = \int_0^1 \frac{\sin(t)}{t} dt $$

**Correction Zéro Ellipse :**
1. **Typage de l'intégrande :** Soit $f(t) = \frac{\sin(t)}{t}$. La fonction $f$ est continue sur $]0, 1]$. Le point $t=0$ pose a priori problème car le dénominateur s'annule, ce qui en fait formellement une intégrale généralisée en 0.
2. **Analyse de la singularité en 0 :** Étudions la limite de $f(t)$ lorsque $t$ tend vers 0.
   Il s'agit d'une limite de référence fondamentale en analyse, issue du taux d'accroissement de la fonction sinus en 0 :
   $$ \lim_{t \to 0} \frac{\sin(t)}{t} = \lim_{t \to 0} \frac{\sin(t) - \sin(0)}{t - 0} = \cos(0) = 1 $$
3. **Prolongement par continuité :** La fonction $f$ admet une limite finie (qui vaut 1) en $t=0$. On peut donc définir une nouvelle fonction $\tilde{f}$ sur le segment fermé $[0, 1]$ telle que :
   - $\tilde{f}(t) = \frac{\sin(t)}{t}$ si $t \in ]0, 1]$
   - $\tilde{f}(0) = 1$
   Cette fonction $\tilde{f}$ est continue sur le segment fermé et borné $[0, 1]$.
4. **Conclusion :** L'intégrale $\int_0^1 \tilde{f}(t) dt$ est une intégrale de Riemann tout à fait classique (propre). L'intégrale $M$ est ce qu'on appelle une "fausse intégrale impropre". Elle converge trivialement car l'aire sous la courbe d'une fonction continue sur un segment est toujours finie.
