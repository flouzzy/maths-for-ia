### Exercice 5 : Inégalité de Hölder généralisée (3 fonctions) $\bigstar\bigstar\bigstar$

**Énoncé :** Soient $p, q, r \in [1, +\infty]$ tels que $\frac{1}{p} + \frac{1}{q} + \frac{1}{r} = 1$. Montrer que pour $f \in L^p, g \in L^q, h \in L^r$, on a $\|fgh\|_1 \le \|f\|_p \|g\|_q \|h\|_r$.

**Correction Détaillée :**
*Analyse :* L'idée est d'appliquer Hölder de manière récursive en groupant deux fonctions.
*Résolution pas-à-pas :*
1. Considérons la fonction $gh$. Nous cherchons un exposant $s$ tel que $gh \in L^s$ pour utiliser Hölder avec $f \in L^p$.
2. L'exposant conjugué de $p$ est $s$ tel que $\frac{1}{p} + \frac{1}{s} = 1$. Donc $\frac{1}{s} = 1 - \frac{1}{p} = \frac{1}{q} + \frac{1}{r}$.
3. Par Hölder sur $f$ et $gh$ avec les exposants $p$ et $s$ :
   $$\int |f(gh)| \le \|f\|_p \|gh\|_s = \|f\|_p \left( \int |g|^s |h|^s \right)^{1/s}$$
4. Il reste à majorer $\|gh\|_s = (\int |g|^s |h|^s)^{1/s}$. On applique à nouveau Hölder à l'intégrale $\int |g|^s |h|^s$.
5. Cherchons des exposants $u, v$ conjugués ($\frac{1}{u} + \frac{1}{v} = 1$) tels que $|g|^s \in L^u$ et $|h|^s \in L^v$. Il faut $su = q$ et $sv = r$.
6. Vérifions si $u = q/s$ et $v = r/s$ sont conjugués : $\frac{1}{u} + \frac{1}{v} = \frac{s}{q} + \frac{s}{r} = s(\frac{1}{q} + \frac{1}{r}) = s(\frac{1}{s}) = 1$. Oui.
7. On applique Hölder avec $u, v$ :
   $$\int |g|^s |h|^s \le \left(\int (|g|^s)^u\right)^{1/u} \left(\int (|h|^s)^v\right)^{1/v} = \left(\int |g|^q\right)^{s/q} \left(\int |h|^r\right)^{s/r}$$
8. En élevant à la puissance $1/s$ :
   $$\|gh\|_s \le \left( \int |g|^q \right)^{1/q} \left( \int |h|^r \right)^{1/r} = \|g\|_q \|h\|_r$$
9. En combinant avec l'étape 3 : $\|fgh\|_1 \le \|f\|_p \|g\|_q \|h\|_r$.
