# Exercice 2 : Inégalité de Hoeffding
**Énoncé :** Soient $X_1, \dots, X_n$ des variables aléatoires indépendantes telles que $X_i \in [0, 1]$ presque sûrement. Démontrer l'inégalité de Hoeffding pour $S_n = \sum_{i=1}^n X_i$.
**Correction Détaillée :**
* *Analyse de l'énoncé :* Montrer la borne $P(S_n - \mathbb{E}[S_n] \ge t) \le \exp(-2 t^2 / n)$.
* *Résolution pas-à-pas :*
Soit $\lambda > 0$. Par l'inégalité de Markov sur $e^{\lambda (S_n - \mathbb{E}[S_n])}$ :
$$P(S_n - \mathbb{E}[S_n] \ge t) = P(e^{\lambda (S_n - \mathbb{E}[S_n])} \ge e^{\lambda t}) \le e^{-\lambda t} \mathbb{E}[e^{\lambda (S_n - \mathbb{E}[S_n])}]$$
Par indépendance des $X_i$ :
$$\mathbb{E}[e^{\lambda (S_n - \mathbb{E}[S_n])}] = \prod_{i=1}^n \mathbb{E}[e^{\lambda (X_i - \mathbb{E}[X_i])}]$$
D'après le lemme de Hoeffding, pour toute variable $Y$ telle que $a \le Y \le b$ presque sûrement avec $\mathbb{E}[Y]=0$, on a $\mathbb{E}[e^{\lambda Y}] \le \exp(\frac{\lambda^2 (b-a)^2}{8})$.
Ici, $Y_i = X_i - \mathbb{E}[X_i] \in [-\mathbb{E}[X_i], 1-\mathbb{E}[X_i]]$, l'amplitude est $b-a = 1 - 0 = 1$.
Donc $\mathbb{E}[e^{\lambda Y_i}] \le \exp(\frac{\lambda^2}{8})$.
En multipliant ces $n$ inégalités :
$$\prod_{i=1}^n \mathbb{E}[e^{\lambda Y_i}] \le \prod_{i=1}^n e^{\lambda^2 / 8} = e^{n \lambda^2 / 8}$$
Ainsi :
$$P(S_n - \mathbb{E}[S_n] \ge t) \le e^{-\lambda t} e^{n \lambda^2 / 8} = \exp\left(-\lambda t + \frac{n \lambda^2}{8}\right)$$
Pour minimiser cette borne, dérivons par rapport à $\lambda$ : $\frac{d}{d\lambda} (-\lambda t + \frac{n \lambda^2}{8}) = -t + \frac{n \lambda}{4} = 0 \implies \lambda = \frac{4t}{n}$.
En substituant cette valeur optimale :
$$\exp\left(-\frac{4t}{n} t + \frac{n}{8} \left(\frac{4t}{n}\right)^2\right) = \exp\left(-\frac{4t^2}{n} + \frac{16nt^2}{8n^2}\right) = \exp\left(-\frac{4t^2}{n} + \frac{2t^2}{n}\right) = \exp\left(-\frac{2t^2}{n}\right)$$
La preuve est complète. $\blacksquare$
