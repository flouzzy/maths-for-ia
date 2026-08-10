## Exercice 5 : Distance ultra-métrique \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Une distance $d$ sur $X$ est dite *ultra-métrique* si elle vérifie :
$\forall x,y,z \in X, d(x,z) \le \max(d(x,y), d(y,z))$.
Montrer que dans un tel espace, tout point d'une boule ouverte en est un centre.

**Correction :**
Soit $B(a, r)$ une boule ouverte. Prenons $b \in B(a, r)$. Montrons que $B(b, r) = B(a, r)$.
1. **Montrons $B(b, r) \subset B(a, r)$ :**
   Soit $x \in B(b, r)$. Ainsi $d(b, x) < r$.
   On sait aussi que $b \in B(a, r)$, donc $d(a, b) < r$.
   Par l'inégalité ultra-métrique :
   $d(a, x) \le \max(d(a, b), d(b, x))$.
   Puisque $d(a,b)<r$ et $d(b,x)<r$, leur maximum est strictement inférieur à $r$.
   Donc $d(a,x) < r$, ce qui signifie $x \in B(a, r)$.
2. **Montrons $B(a, r) \subset B(b, r)$ :**
   Par symétrie des rôles, en échangeant $a$ et $b$ (puisque $a \in B(b, r)$ car $d(b, a) = d(a, b) < r$), le même argument s'applique pour montrer l'inclusion réciproque.
Conclusion : $B(b, r) = B(a, r)$. $\blacksquare$
