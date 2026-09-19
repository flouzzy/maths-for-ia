### Exercice 3 : Moyenne arithmético-géométrique via Jensen $\bigstar\bigstar$

**Énoncé :** Soient $x_1, \dots, x_n > 0$. En utilisant l'inégalité de Jensen, montrer que $(x_1 x_2 \dots x_n)^{1/n} \le \frac{x_1 + \dots + x_n}{n}$.

**Correction Détaillée :**
*Analyse :* On doit choisir une fonction convexe bien adaptée aux produits et sommes, typiquement $-\ln$.
*Résolution pas-à-pas :*
1. La fonction $f(x) = -\ln(x)$ est de classe $C^2$ sur $\mathbb{R}_+^*$ avec $f''(x) = 1/x^2 > 0$. Elle est donc strictement convexe.
2. Considérons l'espace de probabilité $\{1, \dots, n\}$ muni de la mesure uniforme $P(i) = 1/n$.
3. La variable aléatoire $X$ prend la valeur $x_i$ avec probabilité $1/n$.
4. L'inégalité de Jensen stipule que $f(\mathbb{E}[X]) \le \mathbb{E}[f(X)]$, soit :
   $$-\ln\left(\frac{1}{n}\sum_{i=1}^n x_i\right) \le \frac{1}{n}\sum_{i=1}^n -\ln(x_i)$$
5. On simplifie le membre de droite :
   $$\frac{1}{n}\sum_{i=1}^n -\ln(x_i) = -\frac{1}{n}\ln\left(\prod_{i=1}^n x_i\right) = -\ln\left(\left(\prod_{i=1}^n x_i\right)^{1/n}\right)$$
6. On a donc $-\ln(\frac{1}{n}\sum x_i) \le -\ln((\prod x_i)^{1/n})$. En multipliant par $-1$ (ce qui inverse l'inégalité) :
   $$\ln\left(\frac{1}{n}\sum_{i=1}^n x_i\right) \ge \ln\left(\left(\prod_{i=1}^n x_i\right)^{1/n}\right)$$
7. La fonction exponentielle étant strictement croissante, on l'applique aux deux membres pour obtenir le résultat.
