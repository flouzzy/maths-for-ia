# Exercice 10 : Limite d'un oscillateur rapide (Lemme de Riemann-Lebesgue tempéré)
Difficulté : $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Soit $\lambda \in \mathbb{R}^*$. On définit la distribution régulière $T_\lambda$ associée à la fonction oscillante $f_\lambda(x) = \sin(\lambda x)$.
Montrez que lorsque la fréquence spatiale $|\lambda| \to +\infty$, la suite de distributions $(T_\lambda)$ converge vers la distribution nulle $0$ dans $\mathcal{D}'(\mathbb{R})$.
*Indication : Écrivez l'action de $T_\lambda$ sur une fonction test $\varphi$, puis effectuez une intégration par parties pour faire apparaître un terme en $1/\lambda$ avant de passer à la limite.*

**Correction Détaillée :**
1. **Action de l'oscillateur rapide :**
   Soit $\varphi \in \mathcal{D}(\mathbb{R})$ une fonction test de support inclus dans un compact $[a, b]$.
   L'action de la distribution régulière est :
   $$ \langle T_\lambda, \varphi \rangle = \int_{-\infty}^{+\infty} \sin(\lambda x)\varphi(x) dx = \int_{a}^{b} \sin(\lambda x)\varphi(x) dx $$
   Notre but est de montrer que cette intégrale tend vers 0 quand $|\lambda| \to +\infty$.

2. **Stratégie de l'intégration par parties :**
   L'intuition physique est qu'une oscillation extrêmement rapide et de moyenne nulle, intégrée contre une fonction "lente", voit ses aires positives et négatives s'annuler presque parfaitement. Mathématiquement, c'est l'intégration par parties qui révèle ce phénomène de moyennage à zéro.
   On pose : $u(x) = \varphi(x) \implies u'(x) = \varphi'(x)$
   Et : $v'(x) = \sin(\lambda x) \implies v(x) = -\frac{\cos(\lambda x)}{\lambda}$

   En appliquant la formule d'intégration par parties sur l'intervalle $[a, b]$ :
   $$ \int_{a}^{b} \sin(\lambda x)\varphi(x) dx = \left[ -\frac{\cos(\lambda x)}{\lambda} \varphi(x) \right]_a^b - \int_{a}^{b} \left( -\frac{\cos(\lambda x)}{\lambda} \right) \varphi'(x) dx $$

3. **Évaluation du terme de bord :**
   Par hypothèse, la fonction test s'annule en dehors de $[a,b]$, et par continuité, $\varphi(a) = \varphi(b) = 0$.
   Donc le terme entre crochets est strictement nul :
   $$ \left[ -\frac{\cos(\lambda x)}{\lambda} \varphi(x) \right]_a^b = -\frac{\cos(\lambda b)}{\lambda}\cdot 0 - \left( -\frac{\cos(\lambda a)}{\lambda}\cdot 0 \right) = 0 $$

4. **Majoration du terme intégral :**
   Il reste l'intégrale :
   $$ \langle T_\lambda, \varphi \rangle = \frac{1}{\lambda} \int_{a}^{b} \cos(\lambda x) \varphi'(x) dx $$
   On applique l'inégalité triangulaire pour l'intégrale afin de majorer la valeur absolue :
   $$ |\langle T_\lambda, \varphi \rangle| = \frac{1}{|\lambda|} \left| \int_{a}^{b} \cos(\lambda x) \varphi'(x) dx \right| \le \frac{1}{|\lambda|} \int_{a}^{b} |\cos(\lambda x)| |\varphi'(x)| dx $$
   Comme la fonction cosinus est bornée par 1 :
   $$ |\langle T_\lambda, \varphi \rangle| \le \frac{1}{|\lambda|} \int_{a}^{b} |\varphi'(x)| dx $$

5. **Passage à la limite :**
   La fonction $\varphi'$ est continue et intégrable sur le segment compact $[a, b]$. L'intégrale $M = \int_a^b |\varphi'(x)| dx$ est un nombre fini fixe, complètement indépendant de $\lambda$.
   On obtient donc la majoration finale :
   $$ |\langle T_\lambda, \varphi \rangle| \le \frac{M}{|\lambda|} $$
   Lorsque $|\lambda| \to +\infty$, la quantité $M/|\lambda|$ tend de manière évidente vers 0.
   Par le théorème des gendarmes :
   $$ \lim_{|\lambda| \to +\infty} \langle T_\lambda, \varphi \rangle = 0 $$
   L'égalité est vraie pour toute fonction test. La distribution converge donc vers la distribution identiquement nulle.
