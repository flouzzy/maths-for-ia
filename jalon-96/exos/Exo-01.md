# Exercice 1 : Calcul élémentaire d'entropie

$\bigstar\star\star\star\star$


Soit une source émettant les symboles $\{A, B, C, D\}$ avec les probabilités $p(A)=0,5$, $p(B)=0,25$, $p(C)=0,125$, $p(D)=0,125$.

**1.** Calculer l'entropie de Shannon $H(P)$ de cette source en base 2 (en bits).
**2.** Vérifier que cette valeur respecte la borne supérieure pour un alphabet de taille 4.

**Correction :**

**1.** Par définition, l'entropie de Shannon discrète en base 2 est :
$$H(P) = - \sum_{x \in \mathcal{X}} p(x) \log_2 p(x)$$
Calculons chaque terme :
Pour A : $-0,5 \log_2(0,5) = -0,5 \times (-1) = 0,5$
Pour B : $-0,25 \log_2(0,25) = -0,25 \times (-2) = 0,5$
Pour C : $-0,125 \log_2(0,125) = -0,125 \times (-3) = 0,375$
Pour D : $-0,125 \log_2(0,125) = -0,125 \times (-3) = 0,375$
En sommant :
$$H(P) = 0,5 + 0,5 + 0,375 + 0,375 = 1,75 \text{ bits}.$$

**2.** La borne supérieure de l'entropie pour un alphabet de taille $N=4$ est atteinte pour la distribution uniforme, valant $\log_2(4) = 2$ bits.
Nous avons bien $H(P) = 1,75 \le 2$.
