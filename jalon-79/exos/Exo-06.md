---
title: "Exercice 6 : Synthèse de signaux"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\star$"
---

# Exercice 6 : Le signal $t(\pi-|t|)$

**Niveau :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé

On considère $f$ la fonction $2\pi$-périodique, impaire, définie sur $[0, \pi]$ par $f(t) = t(\pi - t)$.
1. Calculer ses coefficients de Fourier trigonométriques.
2. Déduire de l'identité de Parseval la valeur de $\sum_{p=0}^\infty \frac{1}{(2p+1)^6}$.

## Correction Détaillée

1. **Calcul des coefficients de Fourier :**
La fonction est impaire, donc $a_n = 0$.
Pour $n \ge 1$, $b_n = \frac{2}{\pi} \int_0^\pi t(\pi-t) \sin(nt) dt$.
Réalisons une double intégration par parties :
$u = t(\pi-t) \implies u' = \pi - 2t$, et $v' = \sin(nt) \implies v = -\frac{\cos(nt)}{n}$.
$$ b_n = \frac{2}{\pi} \left[ -t(\pi-t)\frac{\cos(nt)}{n} \right]_0^\pi + \frac{2}{\pi n} \int_0^\pi (\pi-2t)\cos(nt) dt $$
Le premier crochet est nul.
Deuxième IPP : $u = \pi-2t \implies u' = -2$, $v' = \cos(nt) \implies v = \frac{\sin(nt)}{n}$.
$$ \int_0^\pi (\pi-2t)\cos(nt) dt = \left[ (\pi-2t)\frac{\sin(nt)}{n} \right]_0^\pi + \frac{2}{n} \int_0^\pi \sin(nt) dt $$
Le crochet est nul. Il reste :
$$ \frac{2}{n} \left[ -\frac{\cos(nt)}{n} \right]_0^\pi = \frac{-2}{n^2} ((-1)^n - 1) $$
Ainsi, $b_n = \frac{2}{\pi n} \frac{-2}{n^2} ((-1)^n - 1) = \frac{4(1 - (-1)^n)}{\pi n^3}$.
$b_{2p} = 0$, et $b_{2p+1} = \frac{8}{\pi (2p+1)^3}$.

2. **Parseval :**
Énergie totale :
$$ \|f\|_{L^2}^2 = \frac{1}{\pi} \int_0^\pi (t\pi - t^2)^2 dt = \frac{1}{\pi} \int_0^\pi (\pi^2 t^2 - 2\pi t^3 + t^4) dt = \frac{\pi^4}{30} $$
D'après Parseval :
$$ \frac{1}{2} \sum_{n=1}^\infty b_n^2 = \frac{\pi^4}{30} \implies \sum_{p=0}^\infty \left( \frac{8}{\pi (2p+1)^3} \right)^2 = \frac{\pi^4}{15} $$
$$ \frac{64}{\pi^2} \sum_{p=0}^\infty \frac{1}{(2p+1)^6} = \frac{\pi^4}{15} \implies \sum_{p=0}^\infty \frac{1}{(2p+1)^6} = \frac{\pi^6}{960} $$
