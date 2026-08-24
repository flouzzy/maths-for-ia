# Exercice 5 : Mesure de Dirac et translation \quad $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $\delta_2$ la mesure de Dirac concentrée en $x=2$ sur $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$. Calculer $\int_\mathbb{R} x^3 \, d\delta_2(x)$.

**Correction :**
Rappelons la définition de l'intégrale par rapport à une mesure de Dirac.
1. Pour toute fonction mesurable positive $g$, $\int_X g \, d\delta_a = g(a)$.
2. Ici, la fonction à intégrer est $g(x) = x^3$, qui est bien mesurable (car continue) et positive sur le support effectif.
3. Attention, $g(x)$ n'est pas positive sur tout $\mathbb{R}$, mais on peut scinder : $\int_\mathbb{R} x^3 \, d\delta_2 = \int_{\mathbb{R}^+} x^3 \, d\delta_2 + \int_{\mathbb{R}^-} x^3 \, d\delta_2$.
4. Pour la partie négative, le support est $\mathbb{R}^-$, or $\delta_2(\mathbb{R}^-) = 0$, donc l'intégrale est nulle.
5. Pour la partie positive, $g(2) = 2^3 = 8$. Donc $\int_\mathbb{R} x^3 \, d\delta_2(x) = 8$.
