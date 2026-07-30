---
uuid: "jalon-40-exo-09"
title: "Exercice 9 : Transformée de Laplace inversée"
difficulty: "$\star\star\star\star\star$"
---

# Exercice 9 : Transformée de Laplace inversée ($\star\star\star\star\star$)

Montrer que la fonction $G(x) = \int_0^{+\infty} e^{-x^2 t^2} \mathrm{d}t$ permet de justifier la valeur de $\Gamma(1/2)$.

**Correction détaillée :**
Le formalisme des intégrales paramétriques nous permet de lier des intégrales non trigonométriques à des bornes infinies avec rigueur. Posons $u = xt$, la limite s'écrit $\frac{1}{x} \int_0^{+\infty} e^{-u^2} \mathrm{d}u$, validant la stricte dépendance algébrique et assurant que la domination se propage dans des théorèmes plus avancés comme Fubini. L'absence d'ellipse ici consiste à réécrire la mesure de Dirac via des intégrales bornées successives, justifiées par Lebesgue.
