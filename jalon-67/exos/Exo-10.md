# Exercice 10 : Un contre-exemple abstrait et la restriction du TCM aux réels
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

### Énoncé

Soit l'espace mesuré $(\mathbb{N}, \mathcal{P}(\mathbb{N}), \mu)$ où $\mu$ est la mesure de comptage. Considérons la suite de fonctions $f_n: \mathbb{N} \to \mathbb{R}$ définie par $f_n(k) = 1$ si $k \ge n$, et $f_n(k) = 0$ si $k < n$. Cette suite converge ponctuellement. Évaluer $\lim_n \int f_n$ et $\int \lim_n f_n$. Expliquer mathématiquement le paradoxe au regard du TCM.

---
### Correction détaillée

1. Étudions la convergence ponctuelle de $(f_n)$. Soit un entier $k$ fixé. Dès que $n > k$, $f_n(k) = 0$. Donc la suite $(f_n(k))$ devient stationnaire et constante égale à 0. La limite ponctuelle est donc la fonction identiquement nulle : $f(k) = 0$ pour tout $k \in \mathbb{N}$.
2. Calculons l'intégrale de la limite : l'intégrale de la fonction nulle par rapport à la mesure de comptage est 0. Donc $\int_{\mathbb{N}} \lim_{n} f_n \, d\mu = 0$.
3. Évaluons l'intégrale de $f_n$ pour un $n$ fixé.
   $$\int_{\mathbb{N}} f_n \, d\mu = \sum_{k=0}^{+\infty} f_n(k) = \sum_{k=n}^{+\infty} 1 = +\infty$$
   Pour tout $n$, l'intégrale est infinie, donc la limite des intégrales est $+\infty$.
4. Nous constatons un échec dramatique : $+\infty = \lim_n \int f_n \neq \int \lim_n f_n = 0$.
5. Expliquons le paradoxe. Pourquoi le Théorème de Convergence Monotone ne s'applique-t-il pas ?
   - Les fonctions $f_n$ sont-elles mesurables et positives ? Oui, à valeurs dans $\{0, 1\}$.
   - La suite est-elle croissante ? Soit $k$ fixé. Pour $n \le k$, $f_n(k) = 1$. Pour $n > k$, $f_n(k) = 0$. La suite des valeurs passe de 1 à 0. La suite de fonctions est donc **strictement décroissante** ($f_1 \ge f_2 \ge f_3 \ge \dots$).
6. Le TCM classique requiert une suite *croissante*. L'analogue pour les suites *décroissantes* (voir Exercice 6) exige impérativement que la première fonction $f_1$ ait une intégrale finie pour éviter la forme indéterminée "$\infty - \infty$".
   Or ici, l'intégrale de $f_1$ (et de tout $f_n$) est infinie. Le théorème de convergence monotone pour les suites décroissantes ne s'applique donc pas. L'espace mathématique est préservé de toute incohérence par l'élégance de cette restriction théorique.
