# Exercice 2 : Distribution régulière et locale intégrabilité

**Difficulté :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Montrer que la fonction $f(x) = \frac{1}{\sqrt{|x|}}$ définit une distribution régulière sur $\mathbb{R}$, c'est-à-dire que $f \in L^1_{loc}(\mathbb{R})$. Calculer l'action de $T_f$ sur une fonction test paire.

**Correction Détaillée :**
1. **Intégrabilité locale :**
   La fonction $f$ est continue sur $\mathbb{R}^*$. La seule singularité est en $x=0$. Nous devons vérifier que $f$ est intégrable au voisinage de 0.
   L'intégrale sur $[0, a]$ (pour $a>0$) est $\int_0^a x^{-1/2} dx = \left[ 2x^{1/2} \right]_0^a = 2\sqrt{a}$.
   L'intégrale est finie. Par symétrie, l'intégrale sur $[-a, 0]$ est aussi $2\sqrt{a}$.
   Ainsi, pour tout segment $[c, d]$, $f$ est intégrable. Donc $f \in L^1_{loc}(\mathbb{R})$, et $T_f$ est bien une distribution.

2. **Action sur une fonction test paire :**
   Soit $\phi \in \mathcal{D}(\mathbb{R})$ une fonction paire (i.e., $\phi(-x) = \phi(x)$).
   $$ \langle T_f, \phi \rangle = \int_{-\infty}^{+\infty} \frac{1}{\sqrt{|x|}} \phi(x) dx $$
   Comme $f$ est paire et $\phi$ est paire, le produit $f \phi$ est pair. On peut donc restreindre l'intégrale à $\mathbb{R}^+$ et multiplier par 2 :
   $$ \langle T_f, \phi \rangle = 2 \int_0^{+\infty} \frac{\phi(x)}{\sqrt{x}} dx $$
   Cette intégrale est bien définie car $\phi$ est bornée et à support compact, et l'intégrale converge en 0.
