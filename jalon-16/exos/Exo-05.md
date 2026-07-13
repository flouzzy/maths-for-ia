# Exercice 05 : Factorielles et Règle de d'Alembert

## Énoncé
Soit la série de terme général $u_n = \frac{(2n)!}{(n!)^2 4^n}$ pour $n \ge 1$.
Étudier la nature de $\sum u_n$.

## Correction Détaillée
1. **Positivité :**
   Tous les termes sont constitués de factorielles et de puissances d'entiers positifs. $u_n > 0$. On utilise le critère de d'Alembert.

2. **Calcul du rapport $\frac{u_{n+1}}{u_n}$ :**
   $$u_{n+1} = \frac{(2(n+1))!}{((n+1)!)^2 4^{n+1}} = \frac{(2n+2)!}{((n+1)!)^2 4^{n+1}}$$
   $$\frac{u_{n+1}}{u_n} = \frac{(2n+2)!}{((n+1)!)^2 4^{n+1}} \times \frac{(n!)^2 4^n}{(2n)!}$$

3. **Simplifications successives :**
   On décompose les factorielles :
   $(2n+2)! = (2n+2)(2n+1)(2n)!$
   $(n+1)! = (n+1)n! \implies ((n+1)!)^2 = (n+1)^2(n!)^2$
   $4^{n+1} = 4 \times 4^n$

   En réinjectant dans le quotient :
   $$\frac{u_{n+1}}{u_n} = \frac{(2n+2)(2n+1)(2n)!}{(n+1)^2(n!)^2 \times 4 \times 4^n} \times \frac{(n!)^2 4^n}{(2n)!}$$
   Les factorielles et les $4^n$ se simplifient intégralement :
   $$\frac{u_{n+1}}{u_n} = \frac{(2n+2)(2n+1)}{4(n+1)^2}$$
   Or $2n+2 = 2(n+1)$, donc on simplifie par $n+1$ :
   $$\frac{u_{n+1}}{u_n} = \frac{2(n+1)(2n+1)}{4(n+1)^2} = \frac{2(2n+1)}{4(n+1)} = \frac{2n+1}{2n+2}$$

4. **Passage à la limite :**
   $$\lim_{n \to \infty} \frac{u_{n+1}}{u_n} = \lim_{n \to \infty} \frac{2n(1 + \frac{1}{2n})}{2n(1 + \frac{1}{n})} = \frac{2}{2} = 1$$
   La règle de d'Alembert échoue (cas douteux). Il faut une autre méthode.

5. **Utilisation d'un argument alternatif (Suite décroissante) :**
   On a montré que $\frac{u_{n+1}}{u_n} = \frac{2n+1}{2n+2}$.
   Clairement, $2n+1 < 2n+2$, donc $\frac{u_{n+1}}{u_n} < 1$.
   La suite $(u_n)$ est donc strictement décroissante.
   Pour obtenir la convergence, on a besoin de la formule de Stirling pour trouver un équivalent de $(2n)!$ et $(n!)$.
   $$n! \sim \left(\frac{n}{e}\right)^n \sqrt{2\pi n}$$
   $$(2n)! \sim \left(\frac{2n}{e}\right)^{2n} \sqrt{4\pi n}$$
   On injecte dans $u_n$ :
   $$u_n \sim \frac{\left(\frac{2n}{e}\right)^{2n} \sqrt{4\pi n}}{\left(\left(\frac{n}{e}\right)^n \sqrt{2\pi n}\right)^2 4^n}$$
   $$u_n \sim \frac{2^{2n} n^{2n} e^{-2n} \cdot 2\sqrt{\pi n}}{n^{2n} e^{-2n} \cdot 2\pi n \cdot 4^n}$$
   Les puissances de $e$, de $n$ et de $2$ s'annulent ($2^{2n} = 4^n$) :
   $$u_n \sim \frac{2\sqrt{\pi n}}{2\pi n} = \frac{1}{\sqrt{\pi} \sqrt{n}} = \frac{1}{\sqrt{\pi} n^{1/2}}$$
   L'équivalent est une série de Riemann de paramètre $\alpha = 1/2 < 1$. La série est divergente.
