### Exercice 1 : Inégalité de Young $\bigstar$

**Énoncé :** Démontrer l'inégalité de Young pour $a, b \ge 0$ et $p, q > 1$ conjugués : $ab \le \frac{a^p}{p} + \frac{b^q}{q}$ en utilisant la convexité de la fonction exponentielle.

**Correction Détaillée :**
*Analyse :* La fonction $x \mapsto e^x$ est strictement convexe sur $\mathbb{R}$.
*Résolution pas-à-pas :*
1. Si $a=0$ ou $b=0$, l'inégalité est $0 \le \frac{a^p}{p} + \frac{b^q}{q}$, ce qui est vrai car $a^p \ge 0$ et $b^q \ge 0$. On suppose $a>0, b>0$.
2. On écrit $ab = \exp(\ln(a) + \ln(b)) = \exp(\frac{1}{p}\ln(a^p) + \frac{1}{q}\ln(b^q))$.
3. Comme $\frac{1}{p} + \frac{1}{q} = 1$ et $\frac{1}{p}, \frac{1}{q} \in ]0, 1[$, on peut appliquer la convexité de l'exponentielle aux points $x = \ln(a^p)$ et $y = \ln(b^q)$ avec les poids $\lambda_1 = \frac{1}{p}$ et $\lambda_2 = \frac{1}{q}$.
4. L'inégalité de convexité $\exp(\lambda_1 x + \lambda_2 y) \le \lambda_1 \exp(x) + \lambda_2 \exp(y)$ donne :
   $$\exp\left(\frac{1}{p}\ln(a^p) + \frac{1}{q}\ln(b^q)\right) \le \frac{1}{p}\exp(\ln(a^p)) + \frac{1}{q}\exp(\ln(b^q))$$
5. En simplifiant :
   $$ab \le \frac{1}{p}a^p + \frac{1}{q}b^q$$
