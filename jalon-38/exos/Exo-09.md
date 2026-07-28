---
uuid: "jalon-38-exo-09"
title: "Exercice 9 : Intégrales de Wallis (cas pair)"
tags:
  - math/analyse
  - ia/calcul-differentiel
---

# Exercice 9

**Difficulté :** ★★★★★

**Énoncé :**
Soit $I_n = \int_0^{\pi/2} \sin^n(x) \, dx$. Établir une relation de récurrence entre $I_n$ et $I_{n-2}$ pour $n \ge 2$, et en déduire l'expression explicite de $I_{2p}$ pour $p \in \mathbb{N}$.

**Correction détaillée :**
1. Soit $n \ge 2$. Séparons un sinus : $I_n = \int_0^{\pi/2} \sin^{n-1}(x) \sin(x) \, dx$.
2. Appliquons une intégration par parties. Posons $u(x) = \sin^{n-1}(x)$ et $v'(x) = \sin(x)$.
3. Les fonctions sont de classe $\mathcal{C}^1$. On a $u'(x) = (n-1)\cos(x)\sin^{n-2}(x)$ et $v(x) = -\cos(x)$.
4. La formule donne :
$$ I_n = [-\cos(x)\sin^{n-1}(x)]_0^{\pi/2} - \int_0^{\pi/2} (n-1)\cos(x)\sin^{n-2}(x)(-\cos(x)) \, dx $$
5. Évaluons le crochet : en $\pi/2$, $\cos(\pi/2)=0$. En $0$, $\sin(0)=0$ (car $n-1 \ge 1$). Le crochet est nul.
6. Il reste l'intégrale :
$$ I_n = (n-1) \int_0^{\pi/2} \cos^2(x)\sin^{n-2}(x) \, dx $$
7. Utilisons l'identité $\cos^2(x) = 1 - \sin^2(x)$ :
$$ I_n = (n-1) \int_0^{\pi/2} (1 - \sin^2(x))\sin^{n-2}(x) \, dx $$
$$ I_n = (n-1) \int_0^{\pi/2} (\sin^{n-2}(x) - \sin^n(x)) \, dx $$
8. Par linéarité, $I_n = (n-1)I_{n-2} - (n-1)I_n$.
9. Isolons $I_n$ en regroupant les termes : $I_n + (n-1)I_n = (n-1)I_{n-2}$, soit $n I_n = (n-1) I_{n-2}$.
10. La relation de récurrence est donc : $I_n = \frac{n-1}{n} I_{n-2}$.
11. Pour les termes pairs $n=2p$ : $I_{2p} = \frac{2p-1}{2p} I_{2p-2}$.
12. Par produit en cascade, $I_{2p} = \frac{2p-1}{2p} \times \frac{2p-3}{2p-2} \times \dots \times \frac{1}{2} I_0$.
13. On calcule $I_0 = \int_0^{\pi/2} \sin^0(x) \, dx = \int_0^{\pi/2} 1 \, dx = \frac{\pi}{2}$.
14. Pour unifier l'expression, multiplions le numérateur et le dénominateur par les entiers pairs manquant ($2p \times (2p-2) \times \dots \times 2$) :
$$ I_{2p} = \frac{(2p)!}{(2^p p!)^2} \frac{\pi}{2} = \frac{(2p)!}{4^p (p!)^2} \frac{\pi}{2} $$
$\blacksquare$
