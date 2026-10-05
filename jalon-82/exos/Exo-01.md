# Exercice 1 : Distributions et Fonctions Tests

**Difficulté :** $\bigstar\star\star\star\star$

**Énoncé :**
Montrer que la fonction $\phi(x) = \begin{cases} e^{-1/x} & \text{si } x > 0 \\ 0 & \text{si } x \le 0 \end{cases}$ est de classe $\mathcal{C}^\infty$ sur $\mathbb{R}$. Cette propriété est cruciale pour construire les fonctions tests de $\mathcal{D}(\mathbb{R})$. Évaluer ensuite $\langle \delta_0, \phi \rangle$.

**Correction Détaillée :**
1. **Régularité sur $\mathbb{R}^*$ :**
   Pour $x < 0$, $\phi(x) = 0$, donc $\phi$ est indéfiniment dérivable sur $]-\infty, 0[$ et toutes ses dérivées y sont nulles.
   Pour $x > 0$, $\phi(x) = e^{-1/x}$. Par composition de fonctions $\mathcal{C}^\infty$ sur $]0, +\infty[$, $\phi$ y est $\mathcal{C}^\infty$. On peut montrer par récurrence que pour tout $n \in \mathbb{N}^*$, il existe un polynôme $P_n$ tel que $\phi^{(n)}(x) = \frac{P_n(x)}{x^{2n}} e^{-1/x}$ pour $x > 0$.

2. **Régularité en $x=0$ :**
   Nous devons montrer que toutes les dérivées à droite de $\phi$ en 0 existent et valent 0.
   - **Continuité en 0 :** $\lim_{x \to 0^+} e^{-1/x} = \lim_{X \to +\infty} e^{-X} = 0 = \phi(0)$. Donc $\phi$ est continue.
   - **Dérivabilité en 0 :** Le taux d'accroissement est $\frac{\phi(x) - \phi(0)}{x} = \frac{e^{-1/x}}{x}$. Posons $X = 1/x$. La limite lorsque $x \to 0^+$ est $\lim_{X \to +\infty} X e^{-X} = 0$ par croissances comparées. Donc $\phi'(0) = 0$.
   - **Récurrence :** Supposons $\phi^{(n)}(0) = 0$. Le taux d'accroissement de $\phi^{(n)}$ en 0 est $\frac{\phi^{(n)}(x)}{x} = \frac{P_n(x)}{x^{2n+1}} e^{-1/x}$. La limite en $0^+$ correspond à $\lim_{X \to +\infty} X^{2n+1} P_n(1/X) e^{-X}$. Comme $X^{2n+1} P_n(1/X)$ est une fonction polynomiale en $X$, l'exponentielle l'emporte et la limite est $0$. Ainsi, $\phi^{(n+1)}(0) = 0$.
   Par récurrence, $\phi$ est $\mathcal{C}^\infty$ sur $\mathbb{R}$.

3. **Évaluation :**
   La distribution de Dirac en $0$ évaluée en $\phi$ donne $\langle \delta_0, \phi \rangle = \phi(0) = 0$.
