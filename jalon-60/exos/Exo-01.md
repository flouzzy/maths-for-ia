---
title: "Exo 01 : Évaluation numérique d'une sigmoïde comme approximant"
difficulty: "$\bigstar\star\star\star\star$"
---

# Exo 01 : Évaluation numérique d'une sigmoïde comme approximant

## Énoncé formel
Considérons la fonction d'activation sigmoïde standard $\sigma(t) = \frac{1}{1 + e^{-t}}$. Montrer que la combinaison linéaire $g(x) = \sigma(\lambda x) - \sigma(\lambda(x - 1))$ s'approche de la fonction porte (échelon) définie sur l'intervalle $[0, 1]$ lorsque le scalaire $\lambda \to +\infty$. Calculer explicitement l'erreur absolue $\|g(x) - \mathbf{1}_{[0, 1]}(x)\|$ aux points $x = 0.5$ et $x = -0.5$ pour $\lambda = 10$.

---

## Démonstration et correction pas à pas
Pour analyser la convergence, nous étudions le comportement de $g(x) = \sigma(\lambda x) - \sigma(\lambda(x - 1))$ en fonction de $x$. \n\nCas 1 : $x \in (0, 1)$. Alors $x > 0$ et $x - 1 < 0$. Quand $\lambda \to +\infty$, on a $\lambda x \to +\infty$ et $\lambda(x-1) \to -\infty$. Or $\lim_{t \to +\infty} \sigma(t) = 1$ et $\lim_{t \to -\infty} \sigma(t) = 0$. Donc $g(x) \to 1 - 0 = 1$. \n\nCas 2 : $x < 0$. Alors $x < 0$ et $x - 1 < 0$. Donc $\lambda x \to -\infty$ et $\lambda(x-1) \to -\infty$. Il s'ensuit que $g(x) \to 0 - 0 = 0$. \n\nCas 3 : $x > 1$. Alors $x > 0$ et $x - 1 > 0$. Donc $\lambda x \to +\infty$ et $\lambda(x-1) \to +\infty$. Ainsi $g(x) \to 1 - 1 = 0$. \n\nCeci démontre que $g(x)$ converge ponctuellement vers la fonction porte $\mathbf{1}_{(0, 1)}(x)$ (aux bornes, $g(0) \to 0.5$ et $g(1) \to 0.5$). \n\nÉvaluations numériques pour $\lambda = 10$ :\nEn $x = 0.5$ : $g(0.5) = \sigma(5) - \sigma(-5)$. Or $\sigma(5) = \frac{1}{1+e^{-5}} \approx 0.9933$ et $\sigma(-5) = 1 - \sigma(5) \approx 0.0067$. Donc $g(0.5) \approx 0.9933 - 0.0067 = 0.9866$. L'erreur est $|1 - 0.9866| = 0.0134$.\nEn $x = -0.5$ : $g(-0.5) = \sigma(-5) - \sigma(-15)$. $\sigma(-5) \approx 0.0067$ et $\sigma(-15)$ est quasi-nul. Donc l'erreur est proche de $0.0067$. Le réseau approche donc très bien la fonction porte au centre des domaines.
