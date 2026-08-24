---
title: "Exercice 04 : Inégalité de Tchebychev via Markov"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 04 : Inégalité de Tchebychev via Markov

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace de probabilité. Soit $X$ une variable aléatoire réelle de carré intégrable (d'espérance $\mu = \mathbb{E}[X]$ et variance $\sigma^2 = \mathbb{E}[(X-\mu)^2]$). Démontrer l'inégalité de Tchebychev en utilisant l'inégalité de Markov pour une fonction positive appropriée.

---

## Correction détaillée

1. **Application de Markov :**
L'inégalité de Markov (démontrée dans le cours) s'énonce : pour toute fonction mesurable positive $f$ et $t>0$,
$$ \mathbb{P}(f \ge t) \le \frac{1}{t} \int_{\Omega} f \, d\mathbb{P} $$

2. **Choix de la fonction positive :**
Soit $a > 0$. On veut borner $\mathbb{P}(|X - \mu| \ge a)$.
Considérons la fonction $Y = (X - \mu)^2$. Puisque c'est un carré, $Y$ est une variable aléatoire (fonction mesurable) positive.

3. **Équivalence des événements :**
L'événement $\{|X - \mu| \ge a\}$ est équivalent à l'événement $\{(X - \mu)^2 \ge a^2\}$.
Ainsi, $\mathbb{P}(|X - \mu| \ge a) = \mathbb{P}(Y \ge a^2)$.

4. **Conclusion :**
On applique l'inégalité de Markov à $Y$ avec $t = a^2 > 0$ :
$$ \mathbb{P}(Y \ge a^2) \le \frac{1}{a^2} \int_{\Omega} Y \, d\mathbb{P} $$
Or $\int_{\Omega} Y \, d\mathbb{P} = \mathbb{E}[(X - \mu)^2] = \sigma^2$.
Donc $\mathbb{P}(|X - \mu| \ge a) \le \frac{\sigma^2}{a^2}$. La démonstration est achevée.
