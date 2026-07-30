---
uuid: "jalon-40-exo-10"
title: "Exercice 10 : Application à l'IA : VAE et paramétrisation"
difficulty: "$\star\star\star\star\star$"
---

# Exercice 10 : Application à l'IA : VAE et paramétrisation ($\star\star\star\star\star$)

Montrer mathématiquement le passage du gradient sous l'espérance dans le cadre de la reparameterization trick pour les VAE :
$\nabla_\phi \mathbb{E}_{q_\phi(z|x)} [f(z)] = \mathbb{E}_{p(\epsilon)} [\nabla_\phi f(g_\phi(\epsilon, x))]$.

**Correction détaillée :**
1. L'espérance classique est $\int f(z) q_\phi(z|x) \mathrm{d}z$. Le gradient est $\nabla_\phi \int f(z) q_\phi(z|x) \mathrm{d}z$.
2. Sous des conditions strictes de régularité et domination (Leibniz), cela vaut $\int f(z) \nabla_\phi q_\phi(z|x) \mathrm{d}z$.
3. Avec le changement de variable déterministe et dérivable $z = g_\phi(\epsilon, x)$ où $\epsilon \sim p(\epsilon)$, le théorème de substitution des mesures garantit la validité de l'inversion et annule la nécessité de calculer la dérivée de la densité, transférant la dérivée aux poids du réseau $g_\phi$.
