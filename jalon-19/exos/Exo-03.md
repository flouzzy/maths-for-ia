---
titre: "Exercice 3 : Dérivabilité"
difficulte: "★★☆☆☆"
---

# Exercice 3 : Pratique et maîtrise conceptuelle

**Énoncé :**
Soit $f : \mathbb{R} \to \mathbb{R}$ dérivable telle que $\lim_{x \to +\infty} f(x) = \ell$ et $\lim_{x \to +\infty} f'(x) = m$. Montrer rigoureusement que $m = 0$.

**Résolution Zéro Ellipse :**
1. La fonction $f$ possède une asymptote horizontale d'ordonnée $\ell$ en l'infini. Intuitivement, sa pente (sa dérivée) doit nécessairement s'annuler, faute de quoi la fonction divergerait. Formalisons ce fait avec le TAF.
2. Soit $x \in \mathbb{R}$. La fonction $f$ satisfait les conditions du Théorème des Accroissements Finis sur l'intervalle $[x, x+1]$ (elle est continue et dérivable sur $\mathbb{R}$).
3. Il existe donc un réel $c_x \in ]x, x+1[$ tel que :
   $$ f(x+1) - f(x) = f'(c_x)((x+1) - x) = f'(c_x) $$
4. Étudions le comportement à la limite lorsque $x$ tend vers $+\infty$.
5. Par hypothèse, $\lim_{x \to +\infty} f(x) = \ell$. Par suite, $\lim_{x \to +\infty} f(x+1) = \ell$ par composition des limites avec la translation temporelle.
6. Le membre de gauche de l'équation de l'étape 3 converge donc :
   $$ \lim_{x \to +\infty} (f(x+1) - f(x)) = \ell - \ell = 0 $$
7. Analysons le membre de droite. Puisque $c_x \in ]x, x+1[$, nous avons la double inégalité $x < c_x < x+1$.
8. Par le théorème d'encadrement, lorsque $x \to +\infty$, le paramètre intermédiaire $c_x$ tend inexorablement vers $+\infty$.
9. Par composition de limite, sachant par hypothèse que $\lim_{t \to +\infty} f'(t) = m$, nous déduisons :
   $$ \lim_{x \to +\infty} f'(c_x) = m $$
10. Par unicité de la limite, en identifiant les limites des deux membres de l'égalité de l'étape 3, nous concluons irréfutablement : $0 = m$. $\blacksquare$
