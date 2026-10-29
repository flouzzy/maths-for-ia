# Exercice 02 : Loi Exponentielle et Moments
Difficulté : $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $X$ suivant une loi exponentielle de paramètre $\lambda > 0$.
1. Calculer sa fonction caractéristique $\phi_X(t)$.
2. En déduire l'espérance $\mathbb{E}[X]$ et la variance $\text{Var}(X)$ en dérivant $\phi_X(t)$.

**Correction pas à pas :**
1. La densité est $f_X(x) = \lambda e^{-\lambda x} \mathbf{1}_{[0, +\infty[}(x)$.
2. $\phi_X(t) = \int_{0}^{+\infty} e^{itx} \lambda e^{-\lambda x} dx = \lambda \int_{0}^{+\infty} e^{(it - \lambda)x} dx$.
3. L'intégrale d'une exponentielle complexe convergente est directe :
   $\phi_X(t) = \lambda \left[ \frac{e^{(it - \lambda)x}}{it - \lambda} \right]_{0}^{+\infty}$.
   Comme $\lambda > 0$, $|e^{(it - \lambda)x}| = e^{-\lambda x} \to 0$ quand $x \to +\infty$.
   Donc $\phi_X(t) = 0 - \lambda \frac{1}{it - \lambda} = \frac{\lambda}{\lambda - it}$.
4. Pour les moments, on utilise $\mathbb{E}[X^k] = \frac{\phi_X^{(k)}(0)}{i^k}$.
   Calculons la dérivée première :
   $\phi'_X(t) = \frac{d}{dt}\left(\lambda(\lambda - it)^{-1}\right) = \lambda (-1)(-i)(\lambda - it)^{-2} = \frac{i\lambda}{(\lambda - it)^2}$.
5. En $t = 0$ : $\phi'_X(0) = \frac{i\lambda}{\lambda^2} = \frac{i}{\lambda}$.
   Or $\phi'_X(0) = i\mathbb{E}[X]$, d'où $\mathbb{E}[X] = \frac{1}{\lambda}$.
6. Calculons la dérivée seconde :
   $\phi''_X(t) = i\lambda \frac{d}{dt}\left((\lambda - it)^{-2}\right) = i\lambda (-2)(-i)(\lambda - it)^{-3} = \frac{-2\lambda}{(\lambda - it)^3}$.
7. En $t = 0$ : $\phi''_X(0) = \frac{-2\lambda}{\lambda^3} = \frac{-2}{\lambda^2}$.
   Or $\phi''_X(0) = i^2 \mathbb{E}[X^2] = -\mathbb{E}[X^2]$, d'où $\mathbb{E}[X^2] = \frac{2}{\lambda^2}$.
8. La variance est $\text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2}$.
