# Exercice 2 : Inégalité de Hoeffding pour une fonction indicatrice
**Énoncé :** Soit $\mathcal{Z} = \mathbb{R}$, une probabilité $\mathcal{P}$ de fonction de répartition $F(t) = \mathcal{P}(Z \le t)$, et la fonction $h_t(z) = \mathbb{I}_{z \le t}$ pour un réel $t$ fixé. En utilisant l'inégalité de Hoeffding, démontrer une borne supérieure sur la probabilité que l'écart absolu entre la fonction de répartition empirique $F_n(t)$ et la fonction de répartition réelle $F(t)$ dépasse un certain $\epsilon > 0$.

**Correction Détaillée :**
* *Analyse de l'énoncé :* On se place en un point fixé $t \in \mathbb{R}$. La variable aléatoire d'intérêt est $Y_i = h_t(Z_i) = \mathbb{I}_{Z_i \le t}$. C'est une variable de Bernoulli.
* *Résolution pas-à-pas :*
  1. Les variables $Y_i$ sont indépendantes et identiquement distribuées, car les $Z_i$ le le sont.
  2. L'espérance de $Y_i$ est $\mathbb{E}[Y_i] = \mathbb{P}(Z_i \le t) = F(t)$.
  3. Les variables $Y_i$ prennent leurs valeurs dans l'intervalle borné $[0, 1]$. Donc $Y_i \in [a, b]$ avec $a=0$ et $b=1$.
  4. La fonction de répartition empirique est la moyenne empirique des $Y_i$ :
     $$F_n(t) = \frac{1}{n} \sum_{i=1}^n Y_i$$
  5. L'inégalité de Hoeffding stipule que pour des variables aléatoires indépendantes $X_1, \dots, X_n$ prenant leurs valeurs dans $[a_i, b_i]$, la moyenne empirique $\bar{X} = \frac{1}{n} \sum X_i$ vérifie :
     $$\mathbb{P}(|\bar{X} - \mathbb{E}[\bar{X}]| \ge \epsilon) \le 2 \exp\left( -\frac{2 n^2 \epsilon^2}{\sum_{i=1}^n (b_i - a_i)^2} \right)$$
  6. En appliquant Hoeffding à nos variables $Y_i$ avec $\bar{X} = F_n(t)$ et $\mathbb{E}[\bar{X}] = F(t)$ :
     $$\mathbb{P}(|F_n(t) - F(t)| \ge \epsilon) \le 2 \exp\left( -\frac{2 n^2 \epsilon^2}{n (1 - 0)^2} \right)$$
  7. Simplification finale :
     $$\mathbb{P}(|F_n(t) - F(t)| \ge \epsilon) \le 2 \exp(-2 n \epsilon^2)$$
     Cette borne montre une décroissance exponentiellement rapide de la probabilité d'un grand écart, mais pour un unique point $t$.
