### Exercice 10 : L'Approximation Universelle et le NTK (Niveau X/ENS) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
En Intelligence Artificielle, on étudie une suite de réseaux de neurones $f_n(x) = \frac{1}{\sqrt{n}} \sum_{i=1}^n a_i \sigma(w_i x)$ sur un compact $K$. Si les trajectoires des paramètres lors de l'entraînement par descente de gradient garantissent que la famille $(f_n(x, t))$ (où $t$ est le temps continu) a des dérivées par rapport au temps uniformément bornées indépendamment de $n$, prouver en utilisant Arzelà-Ascoli qu'il existe une dynamique limite pour une sous-suite de $n$.

**Correction :**
Ceci est une esquisse rigoureuse des arguments type "Mean Field" ou NTK.
Soit l'espace des fonctions $f_n(t, \cdot) : K \to \mathbb{R}$, vu comme une application de $t \in [0, T]$ vers l'espace de Banach $E = \mathcal{C}(K)$ muni de $\| \cdot \|_\infty$.
L'hypothèse indique que $\|\partial_t f_n(t, \cdot)\|_\infty \le C$.
Par intégration, $f_n$ est $C$-lipschitzienne en temps : $\|f_n(t_1, \cdot) - f_n(t_2, \cdot)\|_\infty \le C |t_1 - t_2|$.
La famille d'applications $(t \mapsto f_n(t, \cdot))_{n \ge 1}$ est donc **équicontinue** de $[0, T]$ vers $E$.
Pour un $t$ fixé, l'ensemble $A_t = \{f_n(t, \cdot) \mid n \ge 1\}$ doit être précompact dans $E$.
Si on ajoute la régularité spatiale (les $\sigma$ lisses impliquent les $f_n$ spatialement équicontinues), un double argument d'Ascoli (en espace puis en temps) montre que $A_t$ est précompact.
Par le théorème d'Arzelà-Ascoli à valeurs dans un espace de Banach, la famille $(f_n)_{n}$ est précompacte. Il existe une sous-suite qui converge uniformément en temps et en espace vers une dynamique limite continue $f(t, x)$. Ceci fonde l'analyse théorique moderne du Deep Learning.
