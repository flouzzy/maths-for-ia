# Exercice 2 : Distribution associée à la fonction échelon de Heaviside
Difficulté : $\bigstar\star\star\star\star$

**Énoncé :**
La fonction de Heaviside est définie par $H(x) = 1$ si $x > 0$ et $H(x) = 0$ si $x \le 0$.
Montrez rigoureusement que $H$ est localement intégrable et donnez l'expression explicite de l'action de la distribution régulière associée $T_H$ sur une fonction test $\varphi \in \mathcal{D}(\mathbb{R})$. L'intervalle d'intégration final ne doit plus contenir les infinis.

**Correction Détaillée :**
1. **Vérification de l'intégrabilité locale :**
   Une fonction $f$ est dans $L^1_{loc}(\mathbb{R})$ si pour tout intervalle compact $[a, b]$, l'intégrale $\int_a^b |f(x)|dx$ est finie.
   Pour tout intervalle compact $[a, b]$, $|H(x)| \le 1$.
   Donc, $\int_a^b |H(x)|dx \le \int_a^b 1 dx = b - a < +\infty$.
   La fonction de Heaviside est bien localement intégrable.

2. **Action de la distribution régulière associée :**
   Puisque $H \in L^1_{loc}(\mathbb{R})$, elle définit une distribution régulière $T_H$ dont l'action sur une fonction test $\varphi \in \mathcal{D}(\mathbb{R})$ est donnée par :
   $$\langle T_H, \varphi \rangle = \int_{-\infty}^{+\infty} H(x)\varphi(x) dx$$

3. **Simplification de l'intégrale :**
   En utilisant la définition de $H(x)$, nous pouvons découper l'intégrale en deux domaines :
   $$\langle T_H, \varphi \rangle = \int_{-\infty}^{0} 0 \cdot \varphi(x) dx + \int_{0}^{+\infty} 1 \cdot \varphi(x) dx$$
   L'intégrale sur $]-\infty, 0]$ est nulle. Il reste :
   $$\langle T_H, \varphi \rangle = \int_{0}^{+\infty} \varphi(x) dx$$

4. **Prise en compte du support compact :**
   Puisque $\varphi \in \mathcal{D}(\mathbb{R})$, son support est compact. Il existe donc un réel $R > 0$ tel que $\varphi(x) = 0$ pour $x > R$.
   L'intégrale devient formellement une intégrale sur un segment borné :
   $$\langle T_H, \varphi \rangle = \int_{0}^{R} \varphi(x) dx$$
   Ce résultat montre que l'action de $T_H$ équivaut à intégrer la fonction test sur le demi-axe positif.
