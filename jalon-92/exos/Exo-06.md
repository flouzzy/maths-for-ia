# Exercice 6 : Loi forte et fonction génératrice des moments \quad $\bigstar\bigstar\bigstar\star\star$

Soit $(X_n)_{n \geq 1}$ une suite de variables aléatoires I.I.D. de loi normale standard $\mathcal{N}(0,1)$.
1. Montrer que pour tout $t \in \mathbb{R}$, $\mathbb{E}[\exp(t X_1)] = \exp(t^2/2)$.
2. On pose $Y_n = \frac{1}{n} \sum_{i=1}^n \exp(t X_i)$. Vers quelle limite $Y_n$ converge-t-elle presque sûrement ?
3. En déduire la limite presque sûre de $\ln(Y_n)$.

**Correction :**
1. Calculons l'espérance de $\exp(tX_1)$ :
$$\mathbb{E}[e^{tX_1}] = \int_{-\infty}^{\infty} e^{tx} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} \exp\left( -\frac{1}{2} (x^2 - 2tx) \right) dx$$
En complétant le carré, $x^2 - 2tx = (x-t)^2 - t^2$, d'où :
$$\mathbb{E}[e^{tX_1}] = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} \exp\left( -\frac{1}{2} (x-t)^2 \right) \exp(t^2/2) dx = \exp(t^2/2) \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-(x-t)^2/2} dx$$
L'intégrale restante est celle d'une densité de loi normale $\mathcal{N}(t, 1)$, elle vaut donc 1. Ainsi, $\mathbb{E}[e^{tX_1}] = e^{t^2/2}$.
2. Fixons $t \in \mathbb{R}$. Soit $Z_i = \exp(tX_i)$. Les $X_i$ étant I.I.D., les $Z_i$ le sont aussi. De plus, $\mathbb{E}[Z_1] = \exp(t^2/2) < \infty$. D'après la LFGN, la moyenne empirique $Y_n = \frac{1}{n} \sum_{i=1}^n Z_i$ converge presque sûrement vers $\mathbb{E}[Z_1]$. Donc $Y_n \xrightarrow{p.s.} \exp(t^2/2)$.
3. La fonction $\ln$ est continue sur $]0, +\infty[$. Puisque $Y_n \xrightarrow{p.s.} \exp(t^2/2)$ qui est strictement positif, on peut composer les limites : $\ln(Y_n) \xrightarrow{p.s.} \ln(\exp(t^2/2)) = \frac{t^2}{2}$.
