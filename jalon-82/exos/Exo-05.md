# Exercice 5 : Distribution associée au logarithme

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Montrer que la fonction $f(x) = \ln|x|$ définit une distribution régulière sur $\mathbb{R}$.

**Correction Détaillée :**
1. **Intégrabilité locale :**
   La fonction est continue sur $\mathbb{R}^*$, la seule singularité est en 0.
   Étudions l'intégrabilité de $\ln x$ sur $]0, 1]$.
   On connait une primitive de $\ln x$ : $x \ln x - x$.
   $\int_\epsilon^1 \ln x dx = [x \ln x - x]_\epsilon^1 = (1 \ln 1 - 1) - (\epsilon \ln \epsilon - \epsilon) = -1 - \epsilon \ln \epsilon + \epsilon$.
   Par croissance comparée, $\lim_{\epsilon \to 0^+} \epsilon \ln \epsilon = 0$.
   Donc $\lim_{\epsilon \to 0^+} \int_\epsilon^1 \ln x dx = -1$.
   L'intégrale converge, la fonction est intégrable au voisinage de 0.
   Par symétrie, $\ln|x|$ est intégrable sur $[-1, 0[$.
   Ainsi, $\ln|x|$ est localement intégrable sur $\mathbb{R}$.
2. **Conclusion :**
   $f(x) = \ln|x| \in L^1_{loc}(\mathbb{R})$, elle définit donc une distribution régulière sur $\mathbb{R}$.
