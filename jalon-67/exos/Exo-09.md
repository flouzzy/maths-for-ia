# Exercice 9 : Contre-exemple : fonctions non positives \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

Donner un exemple de suite de fonctions $(f_n)$ **croissante** qui converge vers $0$, telle que $\lim \int f_n \neq \int \lim f_n$, et expliquer pourquoi le TCM ne s'applique pas.

**Solution Détaillée :**
1. Considérons $X = \mathbb{R}$ muni de la mesure de Lebesgue.
2. Posons $f_n(x) = -\frac{1}{n} \mathbf{1}_{]0, n]}(x)$.
3. Pour tout $x \in \mathbb{R}$ et $n \ge 1$, on a $f_n(x) \le 0$.
   La suite $(f_n)$ est croissante : en effet, $-1/n \le -1/(n+1)$. Pour $x \in ]0, n]$, $f_n(x) = -1/n \le -1/(n+1) = f_{n+1}(x)$. Pour $x > n$, $f_n(x) = 0 \le 0 = f_{n+1}(x)$.
4. La limite simple de $f_n(x)$ est $f(x) = 0$ pour tout $x$.
5. Calculons les intégrales :
   $$ \int_{\mathbb{R}} f_n(x) dx = -\frac{1}{n} \times n = -1 $$
6. La limite des intégrales est $\lim_{n \to \infty} (-1) = -1$.
7. Or l'intégrale de la limite est $\int_{\mathbb{R}} 0 dx = 0$.
8. On a bien $-1 \neq 0$.
9. **Explication :** Le théorème de convergence monotone (Beppo Levi) exige de manière stricte que les fonctions soient **positives** (à valeurs dans $[0, +\infty]$). Ici, les $f_n$ sont négatives, la condition de positivité est violée, entraînant la défaillance du théorème.
