Mes chers étudiants,

Bienvenue à ce jalon de notre exploration. Voici l'exercice 07. La rigueur sera notre guide.

---

# Jalon 142 : Processus de décision de Markov
## Exercice 07/10 : Évaluation d'une Politique dans un Environnement Linéaire Quadratique (Difficulté : 07/10)

### Énoncé Rigoureux et Formel
Considérons le système dynamique linéaire déterministe suivant sur $\mathbb{R}$:
$$ s_{t+1} = a s_t + b u_t $$
où $s_t \in \mathbb{R}$ est l'état, $u_t \in \mathbb{R}$ est l'action, et $a,b$ sont des constantes réelles ($b \neq 0$).

Le coût (récompense négative) à chaque étape est quadratique :
$$ R(s_t, u_t) = -(q s_t^2 + r u_t^2) $$
avec $q > 0$ et $r > 0$. Le facteur d'escompte est $\gamma \in (0,1)$.

Soit la politique linéaire proportionnelle $\pi(s) = -k s$ pour une constante $k$.
Déterminez analytiquement la fonction de valeur $V^\pi(s)$ associée à cette politique sous la forme $V^\pi(s) = -P s^2$, et exprimez la constante $P > 0$ en fonction de $a, b, q, r, k, \gamma$.

### Correction Détaillée
1. **Équation de Bellman pour l'évaluation de politique**
   La fonction de valeur $V^\pi(s)$ vérifie l'équation d'évaluation de politique :
   $$ V^\pi(s) = R(s, \pi(s)) + \gamma V^\pi(s_{t+1}) $$
   où $s_{t+1} = a s + b \pi(s) = a s - b k s = (a - b k) s$.

2. **Substitution de la forme postulée**
   Nous cherchons une solution de la forme $V^\pi(s) = -P s^2$.
   Substituons cela dans l'équation de Bellman :
   $$ -P s^2 = -(q s^2 + r (-k s)^2) + \gamma (-P (s_{t+1})^2) $$
   $$ -P s^2 = -q s^2 - r k^2 s^2 - \gamma P ((a - b k) s)^2 $$

3. **Identification des coefficients**
   En factorisant $s^2$ (qui est non nul pour $s \neq 0$), nous obtenons l'équation pour $P$ :
   $$ -P = -q - r k^2 - \gamma P (a - b k)^2 $$
   $$ P = q + r k^2 + \gamma P (a - b k)^2 $$

4. **Résolution pour P**
   Regroupons les termes en $P$ :
   $$ P - \gamma P (a - b k)^2 = q + r k^2 $$
   $$ P \left( 1 - \gamma (a - b k)^2 \right) = q + r k^2 $$

   Pour que $P$ soit bien définie (et positive), il faut que $1 - \gamma (a - b k)^2 > 0$, c'est-à-dire que la politique stabilise suffisamment le système pour que les coûts escomptés convergent. Sous cette condition :
   $$ P = \frac{q + r k^2}{1 - \gamma (a - b k)^2} $$

5. **Conclusion**
   La fonction de valeur associée à la politique linéaire $\pi(s) = -ks$ est bien quadratique, donnée par $V^\pi(s) = -P s^2$, avec la constante $P$ identifiée rigoureusement comme calculée ci-dessus. Ce résultat fondamental est à la base de la théorie du contrôle optimal Linear-Quadratic Regulator (LQR).
