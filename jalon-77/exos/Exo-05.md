# Exercice 5 : Invariance par translation

**Niveau :** \bigstar\bigstar\bigstar\star\star

**Énoncé :**
Soit $f \in L^p(\mathbb{R})$ avec $1 \le p < +\infty$. On définit la fonction translatée $\tau_h f(x) = f(x - h)$.
Montrer que l'application $h \mapsto \tau_h f$ est continue de $\mathbb{R}$ dans $L^p(\mathbb{R})$, c'est-à-dire que $\lim_{h \to 0} \|\tau_h f - f\|_p = 0$.

**Correction Détaillée :**
1. **Cas d'une fonction continue à support compact :**
   Supposons d'abord que $g \in \mathcal{C}_c(\mathbb{R})$. Soit $K$ un compact contenant le support de $g$.
   Puisque $g$ est continue à support compact, elle est uniformément continue (Théorème de Heine).
   Pour tout $\varepsilon > 0$, il existe $\delta > 0$ tel que $|h| \le \delta \implies \sup_x |g(x-h) - g(x)| \le \varepsilon$.
   Pour $|h| \le 1$, le support de $g(x-h) - g(x)$ est contenu dans un compact $K'$ fixe (de mesure finie $M$).
   Alors $\|\tau_h g - g\|_p^p \le \int_{K'} \varepsilon^p dx = \varepsilon^p M$.
   Donc $\lim_{h \to 0} \|\tau_h g - g\|_p = 0$.

2. **Densité pour le cas général :**
   Soit $f \in L^p(\mathbb{R})$ et $\varepsilon > 0$.
   Par densité de $\mathcal{C}_c(\mathbb{R})$, il existe $g \in \mathcal{C}_c(\mathbb{R})$ telle que $\|f - g\|_p \le \frac{\varepsilon}{3}$.
   L'invariance de la mesure de Lebesgue par translation garantit que $\|\tau_h(f - g)\|_p = \|f - g\|_p \le \frac{\varepsilon}{3}$.

3. **Inégalité triangulaire (Minkowski) :**
   $\|\tau_h f - f\|_p \le \|\tau_h f - \tau_h g\|_p + \|\tau_h g - g\|_p + \|g - f\|_p$.
   $\|\tau_h f - f\|_p \le \frac{\varepsilon}{3} + \|\tau_h g - g\|_p + \frac{\varepsilon}{3}$.
   D'après l'étape 1, il existe $\delta > 0$ tel que pour $|h| \le \delta$, $\|\tau_h g - g\|_p \le \frac{\varepsilon}{3}$.
   Ainsi, pour $|h| \le \delta$, $\|\tau_h f - f\|_p \le \varepsilon$.
   La continuité des translations est démontrée.
