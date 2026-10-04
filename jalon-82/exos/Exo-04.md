# Exercice 4 : Convergence d'une suite de fonctions vers la masse de Dirac
Difficulté : $\bigstar\bigstar\star\star\star$

**Énoncé :**
Pour tout entier $n \ge 1$, on définit la fonction (noyau gaussien) :
$$ f_n(x) = \frac{n}{\sqrt{\pi}} e^{-n^2 x^2} $$
On note $T_n$ la distribution régulière associée à $f_n$. Montrez que la suite de distributions $(T_n)_{n \ge 1}$ converge vers la distribution de Dirac $\delta_0$ au sens des distributions.
*Indication : On rappelle que $\int_{-\infty}^{+\infty} e^{-u^2}du = \sqrt{\pi}$. Utilisez le changement de variable $u = nx$ pour la démonstration.*

**Correction Détaillée :**
1. **Définition de la convergence au sens des distributions :**
   Il faut montrer que pour toute fonction test $\varphi \in \mathcal{D}(\mathbb{R})$, la suite numérique réelle $\langle T_n, \varphi \rangle$ converge vers $\langle \delta_0, \varphi \rangle = \varphi(0)$ quand $n \to +\infty$.

2. **Écriture de l'action de $T_n$ :**
   Par définition d'une distribution régulière, nous avons :
   $$ \langle T_n, \varphi \rangle = \int_{-\infty}^{+\infty} f_n(x)\varphi(x) dx = \int_{-\infty}^{+\infty} \frac{n}{\sqrt{\pi}} e^{-n^2 x^2} \varphi(x) dx $$

3. **Changement de variable :**
   Posons $u = nx$. Alors $dx = \frac{du}{n}$. Les bornes d'intégration restent inchangées.
   $$ \langle T_n, \varphi \rangle = \int_{-\infty}^{+\infty} \frac{n}{\sqrt{\pi}} e^{-u^2} \varphi\left(\frac{u}{n}\right) \frac{du}{n} = \int_{-\infty}^{+\infty} \frac{1}{\sqrt{\pi}} e^{-u^2} \varphi\left(\frac{u}{n}\right) du $$

4. **Passage à la limite sous l'intégrale (Théorème de Convergence Dominée) :**
   Considérons la suite de fonctions $g_n(u) = \frac{1}{\sqrt{\pi}} e^{-u^2} \varphi\left(\frac{u}{n}\right)$.
   *   **Convergence ponctuelle :** Pour tout $u$ fixé, comme $\varphi$ est continue, $\lim_{n\to\infty} \varphi\left(\frac{u}{n}\right) = \varphi(0)$. Ainsi, $g_n(u) \to \frac{1}{\sqrt{\pi}} e^{-u^2} \varphi(0)$ ponctuellement.
   *   **Domination :** La fonction test $\varphi$ est à support compact, donc elle est bornée sur $\mathbb{R}$. Posons $M = \sup_{x \in \mathbb{R}} |\varphi(x)|$.
       Pour tout $n$ et tout $u$, on a :
       $$ |g_n(u)| \le \frac{M}{\sqrt{\pi}} e^{-u^2} $$
       La fonction majorante $u \mapsto \frac{M}{\sqrt{\pi}} e^{-u^2}$ est indépendante de $n$ et intégrable sur $\mathbb{R}$.

5. **Conclusion :**
   Par le théorème de la convergence dominée de Lebesgue, nous pouvons inverser la limite et l'intégrale :
   $$ \lim_{n \to +\infty} \langle T_n, \varphi \rangle = \int_{-\infty}^{+\infty} \lim_{n \to +\infty} g_n(u) du = \int_{-\infty}^{+\infty} \frac{1}{\sqrt{\pi}} e^{-u^2} \varphi(0) du $$
   Comme $\varphi(0)$ est une constante, on la sort de l'intégrale :
   $$ = \varphi(0) \frac{1}{\sqrt{\pi}} \int_{-\infty}^{+\infty} e^{-u^2} du $$
   L'intégrale de Gauss vaut $\sqrt{\pi}$, donc :
   $$ = \varphi(0) \cdot \frac{1}{\sqrt{\pi}} \cdot \sqrt{\pi} = \varphi(0) = \langle \delta_0, \varphi \rangle $$
   La suite de distributions $T_n$ converge bien vers $\delta_0$.
