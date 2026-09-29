\subsection*{Exercice 9 : Symétrie hermitienne pour les fonctions réelles \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$}

Soit $f \in L^1(\mathbb{R})$ une fonction à valeurs strictement réelles (i.e. $f(t) \in \mathbb{R}$ $\forall t$).
Montrer que sa transformée de Fourier possède une symétrie hermitienne, c'est-à-dire :
$$ \forall \xi \in \mathbb{R}, \quad \hat{f}(-\xi) = \overline{\hat{f}(\xi)} $$

---
**Correction :**

Partons de l'évaluation de la transformée de Fourier en $-\xi$ :
$$ \hat{f}(-\xi) = \int_{-\infty}^{+\infty} f(t) e^{-i(-\xi) t} \, dt = \int_{-\infty}^{+\infty} f(t) e^{i\xi t} \, dt $$
Par ailleurs, prenons le conjugué complexe de $\hat{f}(\xi)$ :
$$ \hat{f}(\xi) = \int_{-\infty}^{+\infty} f(t) e^{-i\xi t} \, dt $$
$$ \overline{\hat{f}(\xi)} = \overline{\int_{-\infty}^{+\infty} f(t) e^{-i\xi t} \, dt} $$
Les propriétés de l'intégrale sur $\mathbb{R}$ permettent de rentrer le conjugué sous le signe intégral :
$$ \overline{\hat{f}(\xi)} = \int_{-\infty}^{+\infty} \overline{f(t) e^{-i\xi t}} \, dt = \int_{-\infty}^{+\infty} \overline{f(t)} \overline{e^{-i\xi t}} \, dt $$
Puisque $f(t)$ est réelle par hypothèse, son conjugué est égal à elle-même : $\overline{f(t)} = f(t)$.
Le conjugué complexe de l'exponentielle imaginaire pure est : $\overline{e^{-i\xi t}} = e^{i\xi t}$.
Donc :
$$ \overline{\hat{f}(\xi)} = \int_{-\infty}^{+\infty} f(t) e^{i\xi t} \, dt $$
On constate que l'expression obtenue est rigoureusement identique à celle de $\hat{f}(-\xi)$.
Par conséquent, on a bien prouvé l'égalité fondamentale :
$$ \hat{f}(-\xi) = \overline{\hat{f}(\xi)} $$
Conséquence géométrique forte : le spectre d'amplitude $|\hat{f}(\xi)|$ d'un signal temporel réel est une fonction paire.
