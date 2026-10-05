# Exercice 7 : Valeur Principale de Cauchy (Introduction)

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

**Énoncé :**
On définit l'action de $vp(1/x)$ sur $\phi \in \mathcal{D}(\mathbb{R})$ par :
$$ \langle vp(1/x), \phi \rangle = \lim_{\epsilon \to 0^+} \left( \int_{-\infty}^{-\epsilon} \frac{\phi(x)}{x} dx + \int_{\epsilon}^{+\infty} \frac{\phi(x)}{x} dx \right) $$
Montrer que cette limite existe bien et qu'elle définit une distribution sur $\mathbb{R}$.

**Correction Détaillée :**
1. **Existence de la limite :**
   Par symétrie, $\int_{-R}^{-\epsilon} \frac{1}{x} dx + \int_{\epsilon}^R \frac{1}{x} dx = 0$.
   Donc $\int_{-\infty}^{-\epsilon} \frac{\phi(x)}{x} dx + \int_{\epsilon}^{+\infty} \frac{\phi(x)}{x} dx = \int_{|x| \ge \epsilon} \frac{\phi(x) - \phi(0)}{x} dx + \phi(0) \int_{|x| \ge \epsilon} \frac{1}{x} dx$.
   Le deuxième terme s'annule par symétrie pour des bornes infinies (puisque le support est borné, prenons un $R$ tel que $\text{supp}(\phi) \subset [-R, R]$).
   On a donc $\int_{|x| \ge \epsilon} \frac{\phi(x)}{x} dx = \int_{|x| \ge \epsilon, |x| \le R} \frac{\phi(x) - \phi(0)}{x} dx$.
   Or, d'après l'inégalité des accroissements finis, $\left| \frac{\phi(x) - \phi(0)}{x} \right| \le \sup_{t \in [-R,R]} |\phi'(t)| = \|\phi'\|_\infty$.
   La fonction $x \mapsto \frac{\phi(x) - \phi(0)}{x}$ (prolongée par $\phi'(0)$ en 0) est continue, donc intégrable sur $[-R, R]$.
   La limite quand $\epsilon \to 0$ existe bien.
2. **Linéarité et Continuité :**
   La linéarité est évidente. Pour la continuité, si $\phi_n \to 0$ dans $\mathcal{D}(\mathbb{R})$, il existe un compact $K=[-R, R]$ contenant tous les supports.
   $|\langle vp(1/x), \phi_n \rangle| \le \int_{-R}^R |\frac{\phi_n(x) - \phi_n(0)}{x}| dx \le \int_{-R}^R \|\phi_n'\|_\infty dx = 2R \|\phi_n'\|_\infty$.
   Comme $\phi_n \to 0$ dans $\mathcal{D}(\mathbb{R})$, on a $\|\phi_n'\|_\infty \to 0$.
   Ainsi, $\langle vp(1/x), \phi_n \rangle \to 0$. $vp(1/x)$ est bien une distribution.
