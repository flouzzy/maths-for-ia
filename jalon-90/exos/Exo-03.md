---
uuid: "jalon-90-exo-03"
title: "Stabilité par composition continue"
---

# Exercice 3 : Stabilité par composition continue (Difficulté $\bigstar\bigstar\star\star\star$)

Soit $(X_n)_{n \ge 1}$ une suite convergeant en probabilité vers $X$. Soit $f : \mathbb{R} \to \mathbb{R}$ une fonction continue, non nécessairement bornée.
Démontrer que $f(X_n)$ converge en probabilité vers $f(X)$.

## Correction Pas-à-Pas

1. **Définition du cadre et des objectifs :**
   Nous voulons prouver que pour tout $\epsilon > 0$, $\lim_{n \to \infty} \mathbb{P}(|f(X_n) - f(X)| > \epsilon) = 0$.
   Fixons $\epsilon > 0$ et $\eta > 0$.

2. **Borner la variable limite :**
   La variable aléatoire limite $X$ prend ses valeurs dans $\mathbb{R}$. Il existe un compact $K = [-M, M]$ tel que :
   $$ \mathbb{P}(X \notin K) \leq \frac{\eta}{2} $$

3. **Utilisation de l'uniforme continuité :**
   La fonction $f$ est continue. Sur le segment fermé et borné $K$, par le théorème de Heine, $f$ est uniformément continue.
   Il existe donc $\delta > 0$ tel que pour tout $x \in K$ et $y \in \mathbb{R}$ vérifiant $|x - y| \leq \delta$, on a :
   $$ |f(x) - f(y)| \leq \epsilon $$

4. **Décomposition des événements :**
   L'événement indésirable est $A_n = \{ |f(X_n) - f(X)| > \epsilon \}$.
   Si $\omega \in A_n$, l'une des deux conditions suivantes doit être vraie (par contraposée de la continuité uniforme) :
   - Soit $X(\omega) \notin K$.
   - Soit $|X_n(\omega) - X(\omega)| > \delta$.

   Donc l'événement est inclus dans l'union :
   $$ \{ |f(X_n) - f(X)| > \epsilon \} \subset \{ X \notin K \} \cup \{ |X_n - X| > \delta \} $$

5. **Majoration et passage à la limite :**
   Par sous-additivité des probabilités :
   $$ \mathbb{P}(|f(X_n) - f(X)| > \epsilon) \leq \mathbb{P}(X \notin K) + \mathbb{P}(|X_n - X| > \delta) $$
   $$ \mathbb{P}(|f(X_n) - f(X)| > \epsilon) \leq \frac{\eta}{2} + \mathbb{P}(|X_n - X| > \delta) $$
   Par hypothèse, $X_n \xrightarrow{\mathbb{P}} X$, donc pour ce $\delta > 0$ fixé, il existe un entier $N$ tel que pour tout $n \geq N$ :
   $$ \mathbb{P}(|X_n - X| > \delta) \leq \frac{\eta}{2} $$
   Pour tout $n \geq N$, nous avons donc :
   $$ \mathbb{P}(|f(X_n) - f(X)| > \epsilon) \leq \frac{\eta}{2} + \frac{\eta}{2} = \eta $$
   Puisque $\eta$ est arbitraire, la limite est bien $0$.
   $$ f(X_n) \xrightarrow{\mathbb{P}} f(X) $$
   $\blacksquare$

