## Fonction de répartition d'une variable discrète \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $X$ une variable aléatoire réelle discrète dont la loi est donnée par $\mathbb{P}(X = -1) = 0.2$, $\mathbb{P}(X = 0) = 0.5$ et $\mathbb{P}(X = 2) = 0.3$.
Expliciter analytiquement et tracer l'allure de sa fonction de répartition $F_X$.

**Correction Explicative :**
1. La fonction de répartition $F_X : \mathbb{R} \to [0, 1]$ d'une variable aléatoire $X$ est définie par $F_X(x) = \mathbb{P}(X \leq x)$.
2. Pour une variable discrète, la fonction de répartition est une fonction constante par morceaux, dite en escalier, qui présente des sauts aux points de discontinuité correspondant aux valeurs du support. L'amplitude d'un saut en un point $a$ est exactement égale à $\mathbb{P}(X = a)$.
3. Analysons $F_X(x)$ sur les différents intervalles formés par les points du support $S_X = \{-1, 0, 2\}$ :
   - Intervalle $]-\infty, -1[$ :
     Si $x < -1$, alors il n'y a aucune valeur possible de $X$ qui soit inférieure ou égale à $x$. L'événement $\{X \leq x\}$ est impossible.
     Donc, $F_X(x) = \mathbb{P}(\emptyset) = 0$.
   - Intervalle $[-1, 0[$ :
     Si $-1 \leq x < 0$, la seule valeur de $X$ satisfaisant la condition est $-1$.
     Donc, $F_X(x) = \mathbb{P}(X = -1) = 0.2$.
   - Intervalle $[0, 2[$ :
     Si $0 \leq x < 2$, les valeurs de $X$ satisfaisant la condition sont $-1$ et $0$. Ces événements étant disjoints, on additionne leurs probabilités.
     Donc, $F_X(x) = \mathbb{P}(X = -1) + \mathbb{P}(X = 0) = 0.2 + 0.5 = 0.7$.
   - Intervalle $[2, +\infty[$ :
     Si $x \geq 2$, toutes les valeurs possibles de $X$ satisfont la condition. L'événement $\{X \leq x\}$ est l'événement certain.
     Donc, $F_X(x) = \mathbb{P}(X = -1) + \mathbb{P}(X = 0) + \mathbb{P}(X = 2) = 0.2 + 0.5 + 0.3 = 1$.
4. Récapitulatif analytique :
   $$F_X(x) = \begin{cases}
   0 & \text{si } x < -1 \\
   0.2 & \text{si } -1 \leq x < 0 \\
   0.7 & \text{si } 0 \leq x < 2 \\
   1 & \text{si } x \geq 2
   \end{cases}$$
5. Propriétés caractéristiques :
   On vérifie aisément que $F_X$ est une fonction croissante, qu'elle tend vers $0$ en $-\infty$ et vers $1$ en $+\infty$. De plus, on observe qu'elle est continue à droite en tout point. Par exemple, au point de saut $x=0$, $\lim_{x \to 0^+} F_X(x) = 0.7 = F_X(0)$, alors que $\lim_{x \to 0^-} F_X(x) = 0.2$.
