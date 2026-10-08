## Calcul de loi image pour un dé \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
On lance un dé cubique parfaitement équilibré. L'univers est $\Omega = \{1, 2, 3, 4, 5, 6\}$, muni de la tribu $\mathcal{F} = \mathcal{P}(\Omega)$ et de la probabilité uniforme $\mathbb{P}$.
Soit la variable aléatoire $X : \Omega \to \mathbb{R}$ définie par $X(\omega) = (\omega - 3)^2$.
Calculer explicitement la loi de probabilité de $X$ sur $\mathbb{R}$.

**Correction Explicative :**
1. La loi de probabilité de $X$, notée $\mathbb{P}_X$, est la mesure image de $\mathbb{P}$ par l'application $X$. Elle est définie sur $\mathcal{B}(\mathbb{R})$ par $\mathbb{P}_X(B) = \mathbb{P}(X \in B)$.
2. Déterminons d'abord le support de $X$, c'est-à-dire l'ensemble des valeurs qu'elle peut prendre. Nous évaluons $X$ pour chaque issue $\omega \in \Omega$ :
   - Pour $\omega = 1 : X(1) = (1 - 3)^2 = (-2)^2 = 4$
   - Pour $\omega = 2 : X(2) = (2 - 3)^2 = (-1)^2 = 1$
   - Pour $\omega = 3 : X(3) = (3 - 3)^2 = 0^2 = 0$
   - Pour $\omega = 4 : X(4) = (4 - 3)^2 = 1^2 = 1$
   - Pour $\omega = 5 : X(5) = (5 - 3)^2 = 2^2 = 4$
   - Pour $\omega = 6 : X(6) = (6 - 3)^2 = 3^2 = 9$
   Le support de $X$ est donc $S_X = \{0, 1, 4, 9\}$.
3. Comme $X$ est une variable aléatoire discrète, sa loi de probabilité est entièrement caractérisée par les probabilités des singletons $\{x\}$ pour $x \in S_X$. Le dé étant équilibré, la probabilité d'une issue individuelle est $\mathbb{P}(\{\omega\}) = 1/6$.
4. Calculons la probabilité pour chaque valeur du support :
   - Pour $x = 0$ : $\mathbb{P}(X = 0) = \mathbb{P}(\{\omega \in \Omega \mid X(\omega) = 0\}) = \mathbb{P}(\{3\}) = \frac{1}{6}$.
   - Pour $x = 1$ : $\mathbb{P}(X = 1) = \mathbb{P}(\{\omega \in \Omega \mid X(\omega) = 1\}) = \mathbb{P}(\{2, 4\}) = \frac{2}{6} = \frac{1}{3}$.
   - Pour $x = 4$ : $\mathbb{P}(X = 4) = \mathbb{P}(\{\omega \in \Omega \mid X(\omega) = 4\}) = \mathbb{P}(\{1, 5\}) = \frac{2}{6} = \frac{1}{3}$.
   - Pour $x = 9$ : $\mathbb{P}(X = 9) = \mathbb{P}(\{\omega \in \Omega \mid X(\omega) = 9\}) = \mathbb{P}(\{6\}) = \frac{1}{6}$.
5. Vérification de cohérence : La somme des probabilités doit valoir $1$.
   $\sum_{x \in S_X} \mathbb{P}(X = x) = \frac{1}{6} + \frac{2}{6} + \frac{2}{6} + \frac{1}{6} = \frac{6}{6} = 1$. Le calcul est correct.
6. Conclusion : La loi de probabilité $\mathbb{P}_X$ est une mesure de probabilité discrète concentrée sur l'ensemble $\{0, 1, 4, 9\}$, définie par $\mathbb{P}_X = \frac{1}{6}\delta_0 + \frac{1}{3}\delta_1 + \frac{1}{3}\delta_4 + \frac{1}{6}\delta_9$, où $\delta_a$ désigne la mesure de Dirac au point $a$.
