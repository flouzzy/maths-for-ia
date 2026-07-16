---
titre: "Exercice 5 : Dérivabilité"
difficulte: "★★★☆☆"
---

# Exercice 5 : Pratique et maîtrise conceptuelle

**Énoncé :**
La règle de l'Hôpital : Soient $f$ et $g$ dérivables au voisinage de $a$, s'annulant en $a$, avec $g'(x) \neq 0$ près de $a$. Montrer que si $\lim_{x \to a} \frac{f'(x)}{g'(x)} = \ell$, alors $\lim_{x \to a} \frac{f(x)}{g(x)} = \ell$.

**Résolution Zéro Ellipse :**
1. La preuve repose sur le Théorème des Accroissements Finis Généralisé (Théorème de Cauchy).
2. Énonçons d'abord le théorème de Cauchy : soient $f,g$ continues sur $[a,b]$ et dérivables sur $]a,b[$, avec $g'$ ne s'annulant pas. Alors il existe $c \in ]a,b[$ tel que $\frac{f(b)-f(a)}{g(b)-g(a)} = \frac{f'(c)}{g'(c)}$.
3. Preuve du th. de Cauchy : On pose $h(x) = f(x) - \lambda g(x)$ avec $\lambda = \frac{f(b)-f(a)}{g(b)-g(a)}$. $h(a) = h(b)$, par Rolle, $\exists c, h'(c) = 0 \implies f'(c) = \lambda g'(c)$.
4. Appliquons ce résultat à notre problème. Pour un $x$ proche de $a$, on applique Cauchy sur le segment $[a, x]$.
5. Puisque $f(a) = 0$ et $g(a) = 0$, le rapport devient : $\frac{f(x)}{g(x)} = \frac{f(x)-f(a)}{g(x)-g(a)} = \frac{f'(c_x)}{g'(c_x)}$.
6. Le point intermédiaire vérifie $c_x \in ]a, x[$ (ou $]x, a[$ si $x < a$). Par les gendarmes, $\lim_{x \to a} c_x = a$.
7. Par composition de limites, la conclusion découle immédiatement. $\blacksquare$
