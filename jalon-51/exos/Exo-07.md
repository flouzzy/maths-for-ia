---
title: "Exercice 7 : Distance ultramétrique et triangles isocèles"
---

### Exercice 7 : Distance ultramétrique et triangles isocèles \quad $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
Une distance $d$ sur un ensemble $X$ est dite ultramétrique si elle vérifie l'inégalité forte :
$$d(x, z) \le \max(d(x, y), d(y, z))$$
Démontrer que dans un tel espace métrique, tout triangle est isocèle, c'est-à-dire que pour tout triplet de points $(x, y, z)$, au moins deux des distances sont égales, et la troisième est inférieure ou égale.

**Correction Détaillée :**
Soient $x, y, z \in X$. Il y a trois distances : $d(x, y)$, $d(y, z)$ et $d(x, z)$.
Supposons par l'absurde que ces trois distances soient distinctes. Quitte à permuter les points, nous pouvons les ordonner strictement. Supposons sans perte de généralité que :
$$d(x, z) < d(x, y) < d(y, z)$$
Appliquons l'inégalité ultramétrique au couple $(y, z)$ en introduisant le point $x$ :
$$d(y, z) \le \max(d(y, x), d(x, z))$$
Puisque la distance est symétrique, $d(y, x) = d(x, y)$. L'inégalité devient :
$$d(y, z) \le \max(d(x, y), d(x, z))$$
Or, par notre hypothèse d'ordre strict, le maximum de l'ensemble $\{d(x, y), d(x, z)\}$ est précisément $d(x, y)$ (car $d(x, z) < d(x, y)$).
Nous obtenons donc l'inégalité :
$$d(y, z) \le d(x, y)$$
Cependant, ceci est en contradiction flagrante avec notre hypothèse initiale selon laquelle $d(x, y) < d(y, z)$.
L'hypothèse que les trois distances sont distinctes est donc fausse.
Par conséquent, au moins deux des distances doivent être égales. Le 'triangle' formé par ces trois points possède donc au moins deux 'côtés' de même 'longueur', justifiant l'appellation de triangle isocèle. De plus, la démonstration montre que les deux plus grandes distances doivent être égales.
