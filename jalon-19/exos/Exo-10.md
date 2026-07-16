---
titre: "Exercice 10 : Dérivabilité"
difficulte: "★★★★★"
---

# Exercice 10 : Pratique et maîtrise conceptuelle

**Énoncé :**
Étude de la dérivée de la fonction de Weierstrass : Soit $f(x) = \sum_{n=0}^{\infty} a^n \cos(b^n \pi x)$ avec $0 < a < 1$ et $b$ entier impair tel que $ab > 1 + \frac{3}{2}\pi$. Démontrer que $f$ est partout continue mais nulle part dérivable.

**Résolution Zéro Ellipse :**
1. La continuité globale est assurée par le théorème de convergence normale. Le terme général est borné par $a^n$. Or $a \in ]0,1[$, donc la série géométrique $\sum a^n$ converge. La somme d'une série normalement convergente de fonctions continues est continue.
2. Fixons un point d'étude arbitraire $x \in \mathbb{R}$.
3. Pour chaque entier $m \in \mathbb{N}$, définissons un incrément scalaire $h_m$ tel que $b^m x = \alpha_m + \epsilon_m$, où $\alpha_m \in \mathbb{Z}$ est l'entier le plus proche de $b^m x$, et $\epsilon_m \in [-1/2, 1/2]$.
4. Posons $h_m = \frac{1 - \epsilon_m}{b^m}$. Notez que $h_m \to 0$ lorsque $m \to \infty$.
5. Analysons le taux d'accroissement partiel pour le terme d'indice $n$ de la série :
   $$ \tau_{n,m} = a^n \frac{\cos(b^n \pi (x+h_m)) - \cos(b^n \pi x)}{h_m} $$
6. Pour la "queue" de la série ($n \geq m$), les hautes fréquences dominent. La différence de phase est $\pi b^{n-m} (1-\epsilon_m)$. Par l'arithmétique modulaire stricte, avec $b$ impair, on extrait un facteur $(-1)^{\alpha_m}$ qui met en évidence une oscillation amplifiée sans annulation. La somme de la queue s'avère minorée en valeur absolue par une constante proportionnelle à $(ab)^m$.
7. Pour la "tête" de la série ($n < m$), les basses fréquences, le théorème des accroissements finis appliqué au cosinus garantit que le taux d'accroissement de chaque harmonique est borné par sa dérivée locale maximale, majorée par $a^n b^n \pi$. La somme géométrique de cette tête est alors majorée par l'intégrale correspondante, approximativement $\frac{\pi (ab)^m}{ab-1}$.
8. Le rapport du taux d'accroissement global est la somme des deux contributions. Par l'inégalité triangulaire inversée :
   $$ \left| \frac{f(x+h_m) - f(x)}{h_m} \right| \geq C_1 (ab)^m - C_2 \frac{\pi (ab)^m}{ab-1} = (ab)^m \left( C_1 - \frac{C_2 \pi}{ab-1} \right) $$
9. La condition fondamentale imposée par Weierstrass, $ab > 1 + \frac{3}{2}\pi$, a été calibrée chirurgicalement pour garantir que la quantité entre parenthèses soit strictement positive (notons-la $K > 0$).
10. La minoration du taux d'accroissement s'écrit alors $| \tau(h_m) | \geq K (ab)^m$.
11. Or, $a \cdot b > 1$ implique que $(ab)^m \to +\infty$ quand $m \to \infty$.
12. Le taux d'accroissement diverge donc vers l'infini le long de la sous-suite $h_m \to 0$. La dérivée, définie comme une limite finie universelle pour tout chemin approchant 0, ne peut exister. L'argument est valide en tout point $x$. $\blacksquare$
