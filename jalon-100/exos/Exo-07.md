# Exercice 7 : Opérateurs sur l'espace des fonctions holomorphes
$\bigstar\bigstar\bigstar\bigstar\star$
**Énoncé :**
Soit $H(\mathbb{D})$ l'espace des fonctions holomorphes sur le disque unité ouvert $\mathbb{D}$, muni de la topologie de la convergence uniforme sur les compacts (c'est un espace de Fréchet).
Soit $T_n : H(\mathbb{D}) \to \mathbb{C}$ des formes linéaires continues telles que, pour tout $f \in H(\mathbb{D})$, $\sup_n |T_n(f)| < \infty$.
Démontrer qu'il existe un compact $K \subset \mathbb{D}$ et une constante $C > 0$ tels que pour tout $n$ et tout $f$, $|T_n(f)| \le C \sup_{z \in K} |f(z)|$.

**Correction :**
1. Le théorème de Banach-Steinhaus s'étend aux espaces de Fréchet. En effet, la démonstration via le théorème de Baire ne requiert que la complétude et la structure d'espace métrique. $H(\mathbb{D})$ étant complet, Baire s'applique.
2. Posons $X_k = \{ f \in H(\mathbb{D}) \mid \forall n, |T_n(f)| \le k \}$.
   Comme dans la preuve classique, $X_k$ est fermé et l'union des $X_k$ recouvre $H(\mathbb{D})$.
   Par Baire, l'un des $X_N$ contient une boule ouverte.
3. Une base de voisinages de $0$ dans $H(\mathbb{D})$ est donnée par $V(K, \epsilon) = \{f \in H(\mathbb{D}) \mid \sup_K |f| < \epsilon\}$ pour $K$ compact de $\mathbb{D}$.
   L'existence d'une boule implique l'existence d'un compact $K$, de $r > 0$ et de $f_0 \in H(\mathbb{D})$ tels que
   $f_0 + V(K, r) \subset X_N$.
4. Par symétrie et linéarité (cf. cours), on obtient que pour tout $g \in V(K, r)$, on a $|T_n(g)| \le 2N$ pour tout $n$.
5. Pour toute fonction $f \in H(\mathbb{D})$ non nulle, posons $M = \sup_{z \in K} |f(z)|$.
   Alors $g = \frac{r}{2M} f \in V(K, r)$.
   Donc $|T_n(g)| \le 2N$, soit $\frac{r}{2M} |T_n(f)| \le 2N$.
   En posant $C = \frac{4N}{r}$, on a bien $|T_n(f)| \le C \sup_{z \in K} |f(z)|$.